#!/usr/bin/env python3
"""Optional online check for pinned source-file URLs; no credentials needed."""
import concurrent.futures,hashlib,json,datetime
from pathlib import Path
from github_research import ROOT,fetch
rows=json.loads((ROOT/'research/top30.json').read_text())['items']
def run(x):
 url=f'https://raw.githubusercontent.com/{x["name"]}/{x["commit"]}/{x["entry_path"]}'
 try:
  s=fetch(url);return {'name':x['name'],'path':x['entry_path'],'url':url,'status':'verified','bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest(),'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 except Exception as e:return {'name':x['name'],'path':x['entry_path'],'url':url,'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:out=list(p.map(run,rows))
(ROOT/'research/evidence/entry-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified':sum(x['status']=='verified' for x in out),'failed':[x for x in out if x['status']!='verified']},ensure_ascii=False,indent=2))
raise SystemExit(any(x['status']!='verified' for x in out))
