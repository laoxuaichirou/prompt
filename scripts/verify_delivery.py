#!/usr/bin/env python3
"""Offline Hermes acceptance: stdlib + ffprobe. Fails on incomplete/mismatched evidence."""
from pathlib import Path
import argparse,csv,hashlib,json,re,struct,subprocess,sys,urllib.parse
R=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('--skip-checksums',action='store_true',help='Development only; default verifies every delivered file.');args=a.parse_args()
checks=[]
def check(label,condition):
 if not condition:raise AssertionError(label)
 checks.append(label)
def read(path):return json.loads((R/path).read_text())
try:
 rows=read('research/top30.json')['items'];check('30 ranked records',len(rows)==30)
 with (R/'research/top30.csv').open(encoding='utf-8-sig',newline='') as f: csvrows=list(csv.DictReader(f))
 check('CSV matches JSON ranking',len(csvrows)==30 and [(x['name'],int(x['stars'])) for x in csvrows]==[(x['name'],x['stars']) for x in rows])
 for cat in ['canvas','image','video']:
  group=[x for x in rows if x['category']==cat]
  check(cat+' has exactly 10 unique ranked repositories',len(group)==10 and len({x['name'] for x in group})==10 and [x['rank'] for x in group]==list(range(1,11)))
  check(cat+' sorted by star descending',[x['stars'] for x in group]==sorted([x['stars'] for x in group],reverse=True))
 for x in rows:
  d=read(x['star_evidence']);matches=[i for i in d['items'] if i['name']==x['name'] and i['stars']==x['stars']]
  check('star provenance '+x['name'],bool(matches) and d['retrieved_at']==x['stars_observed_at'])
  m=read(x['inspection_evidence']);check('commit provenance '+x['name'],m['commit']==x['commit'] and bool(re.fullmatch('[a-f0-9]{40}',x['commit'])))
 entry=read('research/evidence/entry-checks.json');check('30 pinned upstream file reads verified',len(entry)==30 and all(x['status']=='verified' for x in entry))
 check('upstream entry evidence covers ranking',{x['name'] for x in entry}=={x['name'] for x in rows})
 for x in rows:
  e=next(e for e in entry if e['name']==x['name']);check('entry path '+x['name'],e['path']==x['entry_path'] and x['commit'] in e['url'])
 items=read('prompts/catalog.json')['items'];check('50 unique original prompt templates',len(items)==50 and len({x['id'] for x in items})==50)
 for kind,count in [('image',24),('video',18),('remotion',8)]:check('prompt count '+kind,sum(x['kind']==kind for x in items)==count)
 for x in items:
  check('template schema '+x['id'],x['origin']=='original' and sorted(set(re.findall(r'{{(\w+)}}',x['prompt'])))==x['variables'] and bool(x['acceptance']) and (R/'prompts'/x['kind']/(x['id']+'.md')).is_file())
 skills=list((R/'skills').glob('*/SKILL.md'));check('8 original skills',len(skills)==8)
 for p in skills:check('skill frontmatter '+p.parent.name,p.read_text().startswith('---\nname: '+p.parent.name+'\n'))
 mirror=read('third_party/manifest.json')['files'];check('13 licensed mirrored text files',len(mirror)==13)
 for x in mirror:check('mirrored source hash '+x['local_path'],hashlib.sha256((R/x['local_path']).read_bytes()).hexdigest()==x['sha256'] and x['license']=='MIT')
 for minutes in [5,10]:
  d=read(f'examples/longform-{minutes}min.json');cursor=0
  for s in d['shots']:
   check(f'{minutes}min timeline '+s['id'],s['start_frame']==cursor and s['status']=='planned' and s['prompt_id'] in {x['id'] for x in items});cursor+=s['duration_frames']
  check(f'{minutes}min duration exact',cursor==d['fps']*d['target_duration_seconds']==minutes*60*30)
 for x in read('artifacts/image-test-results.json')['items']:
  p=R/x['artifact'];data=p.read_bytes();check('PNG signature '+x['id'],data[:8]==b'\x89PNG\r\n\x1a\n')
  w,h=struct.unpack('>II',data[16:24]);check('image metadata and hash '+x['id'],w==x['width'] and h==x['height'] and hashlib.sha256(data).hexdigest()==x['sha256'])
 videos=read('artifacts/media-probe.json')['items'];check('3 video samples',len(videos)==3)
 for x in videos:
  p=R/x['artifact'];q=subprocess.run(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)],capture_output=True,text=True,check=True);d=json.loads(q.stdout);v=next(s for s in d['streams'] if s['codec_type']=='video')
  check('actual video properties '+x['id'],v['width']==1080 and v['height']==1920 and v['codec_name']=='h264' and v['r_frame_rate']=='30/1' and int(v['nb_read_frames'])==x['frames'] and abs(float(d['format']['duration'])-x['duration_seconds'])<.05 and not any(s['codec_type']=='audio' for s in d['streams']))
  check('video hash '+x['id'],hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'])
 browser=read('artifacts/canvas-test-report.json');check('recorded 16 browser checks passed',browser['status']=='passed' and browser['count']==len(browser['checks'])==16)
 check('recorded frame review',read('artifacts/frame-review.json')['status']=='passed')
 pdf=(R/'artifacts/交付文档-创作画布研究与规划.pdf').read_bytes();check('downloadable PDF exists',pdf.startswith(b'%PDF') and len(pdf)>10000)
 # Verify our Markdown navigation without changing third-party source documents.
 for folder in ['docs','research','prompts','skills','prototype','remotion','artifacts']:
  for p in (R/folder).rglob('*.md'):
   if 'node_modules' in p.parts:continue
   for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith('#'):continue
    path=urllib.parse.unquote(link.split('#')[0].split('?')[0])
    if path:check('local link '+str(p.relative_to(R))+' -> '+path,(p.parent/path).exists())
 if not args.skip_checksums:
  sums=(R/'SHA256SUMS').read_text().splitlines();check('checksums cover delivered files',len(sums)>150)
  expected={line.split('  ',1)[1] for line in sums}
  actual={p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and not any(part in {'.git','node_modules','__pycache__','.cache','release'} for part in p.relative_to(R).parts) and p.name not in {'SHA256SUMS','verification-report.json'} and not p.name.endswith(('.pyc','.log'))}
  check('manifest covers every delivery file',expected==actual)
  for line in sums:
   digest,name=line.split('  ',1);p=R/name;check('sha256 '+name,p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest)
 result={'status':'passed','checks_passed':len(checks),'scope':'offline evidence, schemas, pinned references, actual media probing, mirrored-source hashes, local links'+('' if args.skip_checksums else ', full delivery checksums'),'live_github_stars':'not refreshed','browser_test':'saved evidence checked; rerun scripts/test_canvas.py for independent browser execution','long_video_generation':'not performed; supplied plans only','checksums':'skipped-development-only' if args.skip_checksums else 'verified'}
except Exception as e:
 result={'status':'failed','checks_passed':len(checks),'error':str(e),'exception':type(e).__name__}
(R/'artifacts/verification-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(result['status']!='passed')
