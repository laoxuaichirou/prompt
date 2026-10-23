#!/usr/bin/env python3
"""Independently verify A/B evidence, actual alpha and actual MP4 properties.
A passed evidence check does not override the recorded failed/partial quality reviews.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,subprocess,sys
from PIL import Image
R=Path(__file__).resolve().parents[1];D=R/'artifacts/ab-2026-10-23';checks=[]
def check(label,ok):
 if not ok:raise AssertionError(label)
 checks.append(label)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
try:
 plan=json.loads((D/'plan.json').read_text());metrics=json.loads((D/'image-metrics.json').read_text())['items'];reviews=json.loads((D/'review.json').read_text())['cases'];coverage=json.loads((D/'coverage.json').read_text());calls=json.loads((D/'invocations.json').read_text())['records']
 check('5 cases, 10 outputs and 10 independent call records',len(plan['cases'])==5 and len(metrics)==10 and len(calls)==10 and len({x['id'] for x in calls})==10)
 for c in plan['cases']:
  a,b=c['variants'];check(c['id']+' paired labels',[a['label'],b['label']]==['A','B'])
  if c['id']!='AB05':
   check(c['id']+' prompt differs only in designated variable',a['prompt'].replace(a['variable_value'],b['variable_value'])==b['prompt'])
   check(c['id']+' identical reference paths',a['referenced_image_paths']==b['referenced_image_paths'])
  else:
   check('AB05 same prompt, reference presence only',a['prompt']==b['prompt'] and a['referenced_image_paths']==[] and len(b['referenced_image_paths'])==1)
  check(c['id']+' same transparency flag',a['transparent_background']==b['transparent_background'])
  for source in c['reference_assets']:check(c['id']+' reference file hash',sha(R/source['repository_path'])==source['sha256'])
  for v in c['variants']:
   m=next(x for x in metrics if x['id']==v['id']);p=R/v['expected_output'];check(v['id']+' original PNG hash',sha(p)==m['sha256'])
   with Image.open(p) as im:
    check(v['id']+' PNG dimensions and mode',im.format=='PNG' and im.size==(m['width'],m['height']) and im.mode==m['mode'])
    hist=im.convert('RGBA').getchannel('A').histogram();total=im.width*im.height
    check(v['id']+' actual alpha matches recorded evidence',abs(hist[0]/total-m['alpha']['fully_transparent_fraction'])<1e-6)
    if c['id']=='AB04':check(v['id']+' real transparent and opaque pixels',im.mode=='RGBA' and hist[0]/total>.1 and hist[255]>0 and v['transparent_background'] is True)
   call=next(x for x in calls if x['id']==v['id']);check(v['id']+' successful tool-return record',call['status']=='generated' and call['started_at']<=call['finished_at'])
 revision=json.loads((D/'review-revision.json').read_text())
 check('alpha review correction preserved',revision['previous_status']=='failed-production-gate' and revision['current_status']=='needs-human-review' and revision['original_pngs_modified'] is False and (D/revision['previous_review']).is_file())
 for sample in revision['observed_pixels']:
  with Image.open(D/sample['artifact']) as im:check('actual low-alpha review pixel '+sample['artifact'],list(im.convert('RGBA').getpixel((sample['x'],sample['y'])))==sample['rgba'])
 video=json.loads((D/'video-results.json').read_text());check('Remotion source recorded',sha(R/'remotion/src/Root.tsx')==video['component_sha256'] and sha(R/'remotion/package-lock.json')==video['package_lock_sha256'])
 for v in video['items']:
  p=R/v['artifact'];check(v['id']+' original MP4 hash',sha(p)==v['sha256'])
  q=subprocess.run(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)],check=True,capture_output=True,text=True);probe=json.loads(q.stdout);s=next(s for s in probe['streams'] if s['codec_type']=='video')
  check(v['id']+' actual technical properties',s['width']==1080 and s['height']==1920 and s['codec_name']=='h264' and s['r_frame_rate']=='30/1' and int(s['nb_read_frames'])==180 and abs(float(probe['format']['duration'])-6)<.05 and not any(s['codec_type']=='audio' for s in probe['streams']))
  check(v['id']+' actual image input hash',sha(R/v['image_file'])==v['image_sha256'])
  check(v['id']+' actual props file',json.loads((R/v['props_file']).read_text())==v['props'])
 a,b=[x['props'] for x in video['items']];check('only illustration prop changed',{k for k in set(a)|set(b) if a.get(k)!=b.get(k)}=={'illustration'})
 check('50 prompt and 8 skill coverage states explicit',len(coverage['prompts'])==50 and len(coverage['skills'])==8 and sum(x['status']=='not-run-in-this-round' for x in coverage['prompts'])==44)
 check('5 visual review outcomes preserved',len(reviews)==5 and {x['id'] for x in reviews}=={c['id'] for c in plan['cases']})
 gallery=json.loads((D/'gallery-test-report.json').read_text());check('gallery real browser evidence',gallery['status']=='passed' and gallery['count']==len(gallery['checks']))
 check('downloadable comparison PDF',(D/'AB对照报告.pdf').read_bytes().startswith(b'%PDF'))
 result={'evidence_validation':'passed','checks_passed':len(checks),'visual_quality_outcomes':dict(Counter(x['status'] for x in reviews)),'quality_warning':'AB04 needs target-background review after alpha-compositing recheck; AB02 strict lighting-only output control failed; AB05 identity needs review. Evidence validation does not turn them into passes.','scope':'10 original image outputs + 2 actual Remotion videos; not all 50 prompts or 8 skills end-to-end'}
except Exception as ex:result={'evidence_validation':'failed','checks_passed':len(checks),'error':str(ex)}
(D/'ab-validation-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(result['evidence_validation']!='passed')
