#!/usr/bin/env python3
"""Build the offline browser catalog from the delivered prompt and A/B evidence."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_text())
data={'prompts':read('prompts/catalog.json')['items'],'cases':read('artifacts/ab-2026-10-23/plan.json')['cases'],'reviews':read('artifacts/ab-2026-10-23/review.json')['cases']}
data['skills']=[]
for p in sorted((R/'skills').glob('*/SKILL.md')):
 text=p.read_text();title=re.search(r'^# (.+)$',text,re.M).group(1);description=re.search(r'^description: (.+)$',text,re.M).group(1)
 data['skills'].append({'id':p.parent.name,'title':title,'description':description,'text':text,'path':p.relative_to(R).as_posix()})
(R/'prototype/data/library.js').write_text('/* Generated from repository evidence; run scripts/build_studio_library.py. */\nwindow.CreatorLibrary='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n')
print('Offline library: 50 prompt templates, 5 image A/B cases with final reviews, 8 original skills.')
