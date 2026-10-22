#!/usr/bin/env python3
"""Reproducible public GitHub HTML research; never reads or exports credentials."""
import argparse, concurrent.futures, datetime, html, json, re, time, urllib.parse, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ResearchError(RuntimeError): pass

def fetch(url):
    for attempt in range(4):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; repository-research/1.0)'})
            with urllib.request.urlopen(req,timeout=60) as r:
                return r.read().decode('utf-8','replace')
        except urllib.error.HTTPError as e:
            if e.code not in (429,502,503) or attempt==3: raise
            time.sleep(min(15*(attempt+1),45))
    raise ResearchError(url)

def search(query,page=1):
    url='https://github.com/search?'+urllib.parse.urlencode({'q':query,'type':'repositories','s':'stars','o':'desc','p':page})
    s=fetch(url)
    m=re.search(r'<script[^>]*data-target="react-app.embeddedData"[^>]*>(.*?)</script>',s,re.S)
    if not m: raise ResearchError('No structured search payload: '+url)
    p=json.loads(m.group(1))['payload'];p=p.get('blackbirdSearchRoute',p)
    if p.get('errors'): raise ResearchError(str(p['errors']))
    items=[]
    for x in p.get('results',[]):
        r=x['repo']['repository'];name=r['owner_login']+'/'+r['name']
        items.append({'name':name,'stars':x['followers'],'description':html.unescape(re.sub('<[^>]+>','',x.get('hl_trunc_description') or '')),'topics':x.get('topics',[]),'archived':x['archived'],'language':x.get('language'),'updated_at':r.get('updated_at'),'url':'https://github.com/'+name})
    out={'query':query,'page':page,'url':url,'sort':'stars descending','retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result_count':p.get('result_count'),'items':items}
    key=re.sub(r'[^a-zA-Z0-9_-]+','_',query).strip('_')+f'__p{page}'
    path=ROOT/'research/evidence/search'/f'{key}.json'
    if path.exists(): path=path.with_name(path.stem+'__'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    return out

def main():
    a=argparse.ArgumentParser();a.add_argument('queries',nargs='+');a.add_argument('--pages',type=int,default=1);args=a.parse_args()
    tasks=[(q,p) for q in args.queries for p in range(1,args.pages+1)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        fs={pool.submit(search,q,p):(q,p) for q,p in tasks}
        for f in concurrent.futures.as_completed(fs):
            q,p=fs[f]
            try:
                d=f.result();print(json.dumps({'query':q,'page':p,'total':d['result_count'],'items':[(x['name'],x['stars']) for x in d['items']]},ensure_ascii=False),flush=True)
            except Exception as e: print(json.dumps({'query':q,'page':p,'error':str(e)}),flush=True)
if __name__=='__main__':main()
