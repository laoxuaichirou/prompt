#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,json,datetime
B=Path(__file__).resolve().parents[1]
runs=[]
for name,script in [('mask-build','tools/make_mask.py'),('asset-check','tools/check_assets.py')]:
 r=subprocess.run([sys.executable,script],cwd=B,capture_output=True,text=True,timeout=60)
 (B/'results'/f'{name}.stdout.log').write_text(r.stdout)
 # Do not create an empty placeholder stderr artifact.
 if r.stderr:(B/'results'/f'{name}.stderr.log').write_text(r.stderr)
 runs.append({'command':['python3',script],'exitCode':r.returncode,'stdout':f'results/{name}.stdout.log','stderr':f'results/{name}.stderr.log' if r.stderr else None})
 if r.returncode:
  (B/'results/run-log.json').write_text(json.dumps({'executedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runs':runs,'status':'FAIL'},ensure_ascii=False,indent=2)+'\n')
  print(r.stdout);print(r.stderr,file=sys.stderr);sys.exit(r.returncode)
(B/'results/run-log.json').write_text(json.dumps({'executedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runs':runs,'status':'FILE_AND_MASK_CHECKS_PASS_WITH_RECORDED_EDIT_FAILURE'},ensure_ascii=False,indent=2)+'\n')
print(runs)
