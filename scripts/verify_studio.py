#!/usr/bin/env python3
"""Read-only evidence verification for the integrated workspace. stdlib + ffprobe."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
R=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)
def read(name):return json.loads((R/name).read_text())
def digest(name):return hashlib.sha256((R/name).read_bytes()).hexdigest()
try:
 source=(R/'prototype/data/library.js').read_text()
 payload=source.split('window.CreatorLibrary=',1)[1].rsplit(';',1)[0]
 library=json.loads(payload)
 check('browser library matches all 50 source prompts',library['prompts']==read('prompts/catalog.json')['items'] and len(library['prompts'])==50)
 check('browser A/B plan matches actual invocations',library['cases']==read('artifacts/ab-2026-10-23/plan.json')['cases'])
 check('browser A/B reviews match final corrected evidence',library['reviews']==read('artifacts/ab-2026-10-23/review.json')['cases'])
 skills=library['skills']
 check('eight unique original skills',len(skills)==8 and len({x['id'] for x in skills})==8)
 for skill in skills:
  check('skill exact source '+skill['id'],skill['path']=='skills/'+skill['id']+'/SKILL.md' and skill['text']==(R/skill['path']).read_text())
 report=read('artifacts/studio/workspace-test-report.json')
 check('real browser workflow checks passed',report['status']=='passed' and report['count']==len(report['checks']) and report['count']>=55)
 check('browser checked full portable roundtrip','portable import works in a clean browser' in report['checks'])
 check('browser checked byte tampering refusal','tampered bytes rejected before graph mutation' in report['checks'])
 check('browser checked actual custom render',report['render']['status']=='passed' and 'real local render completes' in report['checks'])
 files={p.relative_to(R).as_posix() for p in [*(R/'prototype').rglob('*'),R/'scripts/studio_server.py',R/'scripts/local_media_server.py'] if p.is_file() and p.suffix in {'.html','.css','.js'}}
 check('browser evidence covers current frontend files',set(report['source_sha256'])==files)
 for path,sha in report['source_sha256'].items():check('tested source hash '+path,digest(path)==sha)
 evidence=read('artifacts/studio/custom-kinetic-evidence.json')
 check('render component hash unchanged',evidence['component_sha256']==digest('remotion/src/Root.tsx'))
 check('render dependency lock hash unchanged',evidence['lock_sha256']==digest('remotion/package-lock.json'))
 render=evidence['render']
 check('render evidence matches browser roundtrip',render==report['render'])
 check('actual custom MP4 hash matches',digest(render['artifact'])==render['sha256'])
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(R/render['artifact'])]))
 v=next(s for s in probe['streams'] if s['codec_type']=='video')
 check('actual MP4 resolution codec and frame count',v['width']==1080 and v['height']==1920 and v['codec_name']=='h264' and v['r_frame_rate']=='30/1' and int(v['nb_read_frames'])==180)
 check('actual MP4 duration and no audio',abs(float(probe['format']['duration'])-6)<.05 and not any(s['codec_type']=='audio' for s in probe['streams']))
 for name in ['asset-library.png','ab-review.png','motion-custom.png','mobile-workspace.png','custom-kinetic-middle.png']:
  check('browser/frame PNG exists '+name,(R/'artifacts/studio'/name).read_bytes().startswith(b'\x89PNG\r\n\x1a\n'))
 ab04=next(x for x in library['reviews'] if x['id']=='AB04')
 check('AB04 remains human review, not overwritten by user picks',ab04['status']=='needs-human-review')
 result={'status':'passed','checks_passed':len(checks),'scope':'current offline library, original skills, corrected A/B evidence, recorded real-browser checks, current frontend hashes, actual custom MP4 ffprobe','checks':checks,'limits':['No connected image/video model provider','Only KineticWords custom rendering was exercised this round','Evidence integrity does not imply real-product fidelity or all prompt templates passing']}
except Exception as e:result={'status':'failed','checks_passed':len(checks),'error':str(e)}
# Deterministic report; successful reruns do not change the checksum baseline.
(R/'artifacts/studio/workspace-validation-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(result['status']!='passed')
