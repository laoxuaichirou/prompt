#!/usr/bin/env python3
"""Offline structural verification. This cannot certify visual/physical quality."""
import argparse, csv, hashlib, json, sys, math
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--skip-manifest',action='store_true');ap.add_argument('--tool-originals',action='store_true');a=ap.parse_args()
    checks=[]
    def check(name,ok,detail=None):
        checks.append({'check':name,'passed':bool(ok),'detail':detail})
    req=load(ROOT/'brief/asset-requests.json'); doc=load(ROOT/'asset-map.json')
    source_manifest=load(ROOT/'brief/MANIFEST.json')
    check('uploaded_brief_hashes',all(sha(ROOT/'brief'/x['path'])==x['sha256'] and (ROOT/'brief'/x['path']).stat().st_size==x['bytes'] for x in source_manifest['files']))
    expected={x['asset_id']:x for x in req['items']};rows=doc['items'];got={x['asset_id']:x for x in rows}
    check('43_unique_ids_and_exact_request_set',len(rows)==len(got)==43 and set(got)==set(expected))
    check('27_exact_P0_ids',{x['asset_id'] for x in rows if x['priority']=='P0'}=={f'creative-preset-{i}' for i in range(27)})
    with (ROOT/'brief/production-list.csv').open(encoding='utf-8-sig',newline='') as f: csvrows=list(csv.DictReader(f))
    check('csv_and_json_id_sets',len(csvrows)==43 and {x['asset_id'] for x in csvrows}==set(got))
    inv=load(ROOT/'brief/existing-inventory.json'); old={x['id']:x for x in inv['image_presets']}
    for row in rows:
        aid=row['asset_id'];it=expected[aid]
        check(aid+':mapping',all(row[k]==it.get(k) for k in ['target','name','source_prompt','source_prompt_sha256','priority','preview_kind','base_asset']))
        if it['priority']=='P0':
            check(aid+':source_sha_and_inventory',hashlib.sha256(it['source_prompt'].encode()).hexdigest()==it['source_prompt_sha256'] and old[aid]['name']==it['name'] and old[aid]['prompt']==it['source_prompt'])
        if not row['master']:
            check(aid+':honest_missing',row['status']=='not_generated' and row['thumbnail'] is None and row['generated_by'] is None);continue
        check(aid+':attribution',row['generated_by']=='ChatGPT' and row['status'] in ['needs_revision','reviewed_candidate'])
        rec=load(ROOT/row['generation_record'])
        check(aid+':actual_prompt_record',row['actual_prompt']==rec['prompt'] and (ROOT/row['actual_prompt_file']).read_text().rstrip('\n')==rec['prompt'] and (it.get('source_prompt') is None or it['source_prompt'] in rec['prompt']))
        for role,fi in row['files'].items():
            p=ROOT/fi['path']
            ok=p.is_file() and p.stat().st_size>0
            check(aid+':'+role+':exists_nonempty',ok)
            if not ok:continue
            with Image.open(p) as im:
                im.load();size=list(im.size);fmt=im.format
            check(aid+':'+role+':hash_size_decode',sha(p)==fi['sha256'] and p.stat().st_size==fi['bytes'] and size==fi['dimensions'])
            check(aid+':'+role+':format',fmt==('PNG' if role=='master' else 'WEBP'))
            if role=='thumbnail':check(aid+':thumb_640x360',size==[640,360])
            if role=='card':check(aid+':card_1536x864',size==[1536,864])
        check(aid+':top_level_hash_dimensions',row['sha256']==row['files']['master']['sha256'] and row['actual_dimensions']==row['files']['master']['dimensions'])
        if row['base_asset']:
            check(aid+':exact_one_base_reference',len(row['reference_images'])==1 and row['reference_images'][0]['path']==f"bases/{row['base_asset']}.png" and sha(ROOT/row['reference_images'][0]['path'])==row['reference_images'][0]['sha256'])
        else:check(aid+':no_invented_reference',row['reference_images']==[])
        if a.tool_originals:check(aid+':unchanged_tool_original',Path(rec['path']).is_file() and sha(Path(rec['path']))==row['sha256'])
        for co in row['comparisons']:
            check(aid+':comparison:'+co['role'],sha(ROOT/co['path'])==co['sha256']==sha(ROOT/co['copy_of']))
    for b in doc['bases']:
        check(b['asset_id']+':base_hash_size',sha(ROOT/b['path'])==b['sha256'] and list(Image.open(ROOT/b['path']).size)==b['dimensions'])
        if a.tool_originals:
            rec=load(ROOT/b['generation_record']);check(b['asset_id']+':unchanged_tool_original',sha(Path(rec['path']))==b['sha256'])
    check('five_shared_bases',{b['asset_id'] for b in doc['bases']}=={b['asset_id'] for b in req['bases']})
    pano=Image.open(ROOT/got['creative-preset-17']['master'])
    check('panorama_exact_2_to_1_native',pano.width==2*pano.height,list(pano.size))
    check('all_43_generated',all(x['master'] for x in rows))
    check('no_duplicate_master_hashes',len({x['sha256'] for x in rows})==43)
    check('temporal_shared_base',got['creative-preset-24']['base_asset']==got['creative-preset-25']['base_asset']=='base-action')
    check('temporal_reference_hash_same',got['creative-preset-24']['reference_images']==got['creative-preset-25']['reference_images'])
    for role in ['master','thumbnail','card']:
        paths=[x[role] for x in rows if x[role]]
        check(role+':independent_unique_files',len(paths)==len(set(paths))==43)
    for d in ['P0','P1','P2']:
        check(d+':summary_consistent',doc['summary'][d]['generated']==sum(x['priority']==d and bool(x['master']) for x in rows) and doc['summary'][d]['needs_revision']==sum(x['priority']==d and x['status']=='needs_revision' for x in rows))
    images=[]
    for p in sorted(ROOT.rglob('*')):
        if p.suffix.lower() in ['.png','.jpg','.webp']:
            with Image.open(p) as im:im.load();images.append(str(p.relative_to(ROOT)))
    check('all_package_images_decode',True,{'count':len(images)})
    check('no_zero_byte_files',all(p.stat().st_size for p in ROOT.rglob('*') if p.is_file()))
    if not a.skip_manifest:
        mf=load(ROOT/'MANIFEST.json'); listed={x['path']:x for x in mf['files']}
        actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
        # Nested source MANIFEST is itself covered; only our root MANIFEST self-excludes.
        actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p!=ROOT/'MANIFEST.json'}
        check('manifest_exact_coverage',set(listed)==actual)
        check('manifest_all_bytes_hashes',all((ROOT/k).stat().st_size==v['bytes'] and sha(ROOT/k)==v['sha256'] for k,v in listed.items()),{'count':len(listed)})
    report={'executed_at_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version.split()[0],'pillow':Image.__version__,'manifest_checked':not a.skip_manifest,'tool_original_paths_checked':a.tool_originals,'visual_quality_certified':False,'checks':checks,'passed':all(c['passed'] for c in checks)}
    print(json.dumps(report,ensure_ascii=False,indent=2));return 0 if report['passed'] else 1
if __name__=='__main__': sys.exit(main())
