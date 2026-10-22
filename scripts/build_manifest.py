#!/usr/bin/env python3
"""Deterministic delivery SHA256 manifest. Rerun only after intentional changes."""
from pathlib import Path
import hashlib
R=Path(__file__).resolve().parents[1]
def included(p):
 parts=p.relative_to(R).parts
 return not any(x in {'.git','node_modules','__pycache__','.cache','release'} for x in parts) and p.name not in {'SHA256SUMS','verification-report.json'} and not p.name.endswith(('.pyc','.log'))
rows=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and included(p):rows.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(R).as_posix())
(R/'SHA256SUMS').write_text('\n'.join(rows)+'\n')
print(f'Manifest: {len(rows)} files')
