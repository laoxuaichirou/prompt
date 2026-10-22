#!/usr/bin/env python3
"""Inspect public repo metadata and pin source references. No third-party source vendoring."""
import concurrent.futures, datetime, hashlib, json, re, sys
from pathlib import Path
from github_research import fetch, ROOT
CACHE=Path('/tmp/canvas-upstream-readmes');CACHE.mkdir(exist_ok=True)
def inspect(name):
 s=fetch('https://github.com/'+name)
 found=re.findall(r'<script[^>]*data-target="react-app.embeddedData"[^>]*>(.*?)</script>',s,re.S)
 route=next((json.loads(m)['payload']['codeViewRepoRoute'] for m in found if 'codeViewRepoRoute' in json.loads(m).get('payload',{})),None)
 if not route:raise ValueError('Missing code metadata '+name)
 ref=route['refInfo'];tree=route['tree']['items'];oid=ref['currentOid']
 paths=[x['path'] for x in tree];readme=next((p for p in paths if p.lower()=='readme.md'),None) or next((p for p in paths if p.lower().startswith('readme')),None)
 text=fetch(f'https://raw.githubusercontent.com/{name}/{oid}/{readme}') if readme else ''
 (CACHE/(name.replace('/','__')+'.md')).write_text(text)
 licenses=[p for p in paths if p.lower().startswith(('license','licence','copying'))]
 license_evidence=[]
 for p in licenses[:2]:
  try:
   ls=fetch(f'https://raw.githubusercontent.com/{name}/{oid}/{p}');(CACHE/(name.replace('/','__')+'__'+p.replace('/','_'))).write_text(ls)
   license_evidence.append({'path':p,'url':f'https://github.com/{name}/blob/{oid}/{p}','first_lines':ls.strip().splitlines()[:4],'sha256':hashlib.sha256(ls.encode()).hexdigest()})
  except Exception as e:license_evidence.append({'path':p,'error':str(e)})
 links=re.findall(r'\]\(([^)]+)\)',text)
 resource_links=[x for x in links if any(w in x.lower() for w in ['prompt','skill','workflow','example','template','agent'])][:50]
 data={'name':name,'url':'https://github.com/'+name,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'default_branch':ref['name'],'commit':oid,'readme_path':readme,'readme_url':f'https://github.com/{name}/blob/{oid}/{readme}' if readme else None,'readme_sha256':hashlib.sha256(text.encode()).hexdigest(),'root_paths':paths,'readme_headings':re.findall(r'^#{1,4}\s+(.+)',text,re.M)[:50],'resource_links':resource_links,'license_evidence':license_evidence}
 (ROOT/'research/evidence/repos'/(name.replace('/','__')+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 return {'name':name,'commit':oid[:12],'license':[x.get('first_lines') for x in license_evidence],'headings':data['readme_headings'][:8]}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
  fs={p.submit(inspect,n):n for n in sys.argv[1:]}
  for f in concurrent.futures.as_completed(fs):
   try:print(json.dumps(f.result(),ensure_ascii=False),flush=True)
   except Exception as e: print(json.dumps({'name':fs[f],'error':str(e)}),flush=True)
