#!/usr/bin/env python3
"""List, show, and render original templates; exits nonzero for unresolved inputs."""
import argparse,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();s=a.add_subparsers(dest='cmd',required=True)
l=s.add_parser('list');l.add_argument('--kind',choices=['image','video','remotion']);l.add_argument('--category')
v=s.add_parser('show');v.add_argument('id')
v=s.add_parser('render');v.add_argument('id');v.add_argument('--vars',default='{}',help='JSON object or @path/to/variables.json')
args=a.parse_args();items=json.loads((R/'prompts/catalog.json').read_text())['items']
if args.cmd=='list':
 for x in items:
  if (not args.kind or args.kind==x['kind']) and (not args.category or args.category==x['category']):print(x['id'],x['title'],x['category'])
else:
 x=next((x for x in items if x['id']==args.id),None)
 if not x:a.error('Unknown template ID')
 if args.cmd=='show':print(json.dumps(x,ensure_ascii=False,indent=2))
 else:
  try:data=json.loads(Path(args.vars[1:]).read_text() if args.vars.startswith('@') else args.vars)
  except (ValueError,OSError) as e:a.error(str(e))
  if not isinstance(data,dict):a.error('--vars must be a JSON object')
  missing=[v for v in x['variables'] if v not in data or not isinstance(data[v],str) or not data[v].strip()]
  if missing:a.error('Missing non-empty variables: '+', '.join(missing))
  result=re.sub(r'{{(\w+)}}',lambda m:data[m[1]],x['prompt'])
  if re.search(r'{{\w+}}',result):a.error('Variables contain unresolved placeholders')
  print(result)
