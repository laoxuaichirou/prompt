#!/usr/bin/env python3
"""Verify a frozen delivery. No third-party packages, writes or network."""
import hashlib
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
expected = {item['path']: item for item in manifest['files']}
actual = {p.relative_to(root).as_posix(): p for p in root.rglob('*') if p.is_file() and p.name != 'MANIFEST.json'}
errors = []
if set(actual) != set(expected):
    errors.append({'missing': sorted(set(expected) - set(actual)), 'extra': sorted(set(actual) - set(expected))})
for name in sorted(set(actual) & set(expected)):
    data = actual[name].read_bytes()
    if len(data) != expected[name]['bytes'] or hashlib.sha256(data).hexdigest() != expected[name]['sha256']:
        errors.append({'mismatch': name})
    if not data:
        errors.append({'empty': name})
html = actual.get('promptdedup.html')
if html is None or html.stat().st_size > 350 * 1024:
    errors.append({'html_size': 'missing or exceeds 350KB'})
print(json.dumps({'passed': not errors, 'files': len(actual), 'errors': errors}, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
