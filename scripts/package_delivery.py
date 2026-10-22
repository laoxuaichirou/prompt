#!/usr/bin/env python3
"""Verify and create a portable ZIP from the immutable delivery manifest."""
from pathlib import Path
import subprocess,sys,zipfile
R=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(R/'scripts/verify_delivery.py')],cwd=R,check=True)
files=[line.split('  ',1)[1] for line in (R/'SHA256SUMS').read_text().splitlines()]+['SHA256SUMS','artifacts/verification-report.json']
dest=R/'release';dest.mkdir(exist_ok=True);path=dest/'canvas-creator-delivery-2026-10-23.zip'
with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for name in sorted(files):z.write(R/name,'creator-desk-delivery/'+name)
with zipfile.ZipFile(path) as z:
 assert z.testzip() is None
 assert not any('/node_modules/' in x or '/.git/' in x or x.endswith('.env') for x in z.namelist())
print(f'ZIP: {path} ({path.stat().st_size:,} bytes; {len(files)} files)')
