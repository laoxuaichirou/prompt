#!/usr/bin/env python3
"""Create a SHA256 manifest and an actual ZIP; never generate image contents."""
import hashlib, json, zipfile
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
def main():
    files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and p!=ROOT/'MANIFEST.json']
    manifest={'schema':'directorx-file-manifest/1','hash':'sha256','excluded':['MANIFEST.json (self)'],'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
    (ROOT/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    dest=ROOT.parent/(ROOT.name+'.zip')
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file():z.write(p,str(Path(ROOT.name)/p.relative_to(ROOT)))
    with zipfile.ZipFile(dest) as z:
        bad=z.testzip()
        report={'executed_at_utc':datetime.now(timezone.utc).isoformat(),'zip':dest.name,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'files':len(z.infolist()),'crc_first_bad_file':bad,'all_crc_passed':bad is None,'no_empty_files':all(x.file_size>0 for x in z.infolist())}
    (dest.parent/(dest.name+'.report.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False));return 0 if report['all_crc_passed'] and report['no_empty_files'] else 1
if __name__=='__main__':raise SystemExit(main())
