#!/usr/bin/env python3
"""Supplement search with named candidates; record exact public repository star metadata."""
import datetime,json,re,sys
from pathlib import Path
from github_research import ROOT,fetch
out=ROOT/'research/evidence/direct';out.mkdir(exist_ok=True)
for name in sys.argv[1:]:
 s=fetch('https://github.com/'+name);counts=set(re.findall(r'"stargazerCount":(\d+)',s))
 if len(counts)!=1:raise ValueError('Ambiguous star metadata: '+name)
 meta={'query':'named repository inspection: '+name,'kind':'repository-page metadata (not a search result)','url':'https://github.com/'+name,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'items':[{'name':name,'stars':int(next(iter(counts))),'url':'https://github.com/'+name}],'raw_field':'stargazerCount'}
 p=out/(name.replace('/','__')+'.json')
 if p.exists(): p=p.with_name(p.stem+'__'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')
 p.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');print(name,meta['items'][0]['stars'])
