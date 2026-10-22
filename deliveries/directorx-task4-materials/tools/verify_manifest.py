#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1]
m=json.loads((B/'MANIFEST.json').read_text())
actual={str(p.relative_to(B)) for p in B.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
declared={x['path'] for x in m['files']}
assert actual==declared,{'missing':sorted(declared-actual),'extra':sorted(actual-declared)}
for x in m['files']:
 p=B/x['path'];assert p.resolve().is_relative_to(B)
 raw=p.read_bytes();assert len(raw)==x['bytes'] and hashlib.sha256(raw).hexdigest()==x['sha256'],x['path']
print(f'PASS: {len(declared)} files verified; MANIFEST excludes its own checksum.')
