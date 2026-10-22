#!/usr/bin/env python3
"""Read-only offline integrity verification. Does not certify artistic quality."""
import argparse,csv,hashlib,json,sys
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(rel):return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--skip-manifest',action='store_true');ap.add_argument('--tool-originals',action='store_true');ap.add_argument('--source-A',type=Path);args=ap.parse_args();checks=[]
    def check(name,ok,detail=None):checks.append({'check':name,'passed':bool(ok),'detail':detail})
    req={x['asset_id']:x for x in read('brief/asset-requests.json')['items'] if x['priority']=='P0'};doc=read('asset-map.json');rows=doc['items'];baseline=read('provenance/baseline.json');old={x['asset_id']:x for x in read('provenance/A-asset-map.json')['items']}
    check('exact_27_unique_P0_ids',len(rows)==len({x['asset_id'] for x in rows})==27 and set(req)=={x['asset_id'] for x in rows}=={f'creative-preset-{i}' for i in range(27)})
    source=read('brief/MANIFEST.json');check('uploaded_brief_hashes',all(sha(ROOT/'brief'/x['path'])==x['sha256'] and (ROOT/'brief'/x['path']).stat().st_size==x['bytes'] for x in source['files']))
    inventory={x['id']:x for x in read('brief/existing-inventory.json')['image_presets']}
    picks=read('selection.json')['items'];pickmap={x['asset_id']:x for x in picks};check('selection_exact_27_ids',len(picks)==len(pickmap)==27 and set(pickmap)==set(req))
    counts=Counter();Brefs={};natives=[]
    for row in rows:
        aid=row['asset_id'];it=req[aid];n=int(aid.rsplit('-',1)[1]);choice=row['decision']['recommended_version'];counts[choice or 'neither']+=1
        check(aid+':exact_target_and_original_prompt',all(row[k]==it[k] for k in ['name','target','source_prompt','source_prompt_sha256','base_asset','preview_kind']) and sha_text(it['source_prompt'])==it['source_prompt_sha256'] and inventory[aid]['name']==it['name'] and inventory[aid]['prompt']==it['source_prompt'])
        check(aid+':pair_exists',(ROOT/row['pair_review']).is_file())
        for version,v in row['versions'].items():
            prefix=aid+':'+version
            check(prefix+':real_attribution',v['generated_by']=='ChatGPT' and v['preview_kind']==it['preview_kind'] and v['master'] is not None)
            for role,f in v['files'].items():
                p=ROOT/f['path'];check(prefix+':'+role+':nonempty',p.is_file() and p.stat().st_size>0)
                with Image.open(p) as im:im.load();size=list(im.size);fmt=im.format
                check(prefix+':'+role+':hash_size_decode',sha(p)==f['sha256'] and p.stat().st_size==f['bytes'] and size==f['dimensions'])
                check(prefix+':'+role+':format',fmt==('PNG' if role=='master' else 'WEBP'))
                if role=='thumbnail':check(prefix+':thumb_640x360',size==[640,360])
                if role=='card':check(prefix+':card_1536x864',size==[1536,864])
            natives.append(v['sha256']);check(prefix+':canonical_dimensions_hash',v['actual_dimensions']==v['files']['master']['dimensions'] and v['sha256']==v['files']['master']['sha256'])
            rec=read(v['generation_record']);check(prefix+':actual_prompt_provenance',v['actual_prompt']==rec['prompt'] and it['source_prompt'] in v['actual_prompt'] and (ROOT/v['actual_prompt_file']).read_text().rstrip('\n')==v['actual_prompt'])
            for i,ref in enumerate(v['reference_images']):check(prefix+':ref_'+str(i+1),sha(ROOT/ref['path'])==ref['sha256'])
            if version=='B':
                check(prefix+':correct_shared_base_first',not it['base_asset'] or (v['reference_images'][0]['path']==f"bases/{it['base_asset']}.png" and v['reference_images'][0]['sha256']==next(b['sha256'] for b in baseline['base_hashes'] if b['asset_id']==it['base_asset'])))
                check(prefix+':reference_order_actual',len(rec['reference_paths'])==len(v['reference_images']) and all(str(Path(ref).relative_to(ROOT))==v['reference_images'][i]['path'] for i,ref in enumerate(rec['reference_paths'])))
                Brefs[aid]=v['reference_images'][0]
            else:
                check(prefix+':unchanged_A_original',v['sha256']==old[aid]['sha256'])
                for role in ['master','thumbnail','card']:check(prefix+':unchanged_A_'+role,v['files'][role]['sha256']==old[aid]['files'][role]['sha256'])
            if args.tool_originals:check(prefix+':unchanged_tool_file',Path(rec['path']).is_file() and sha(Path(rec['path']))==v['sha256'])
            for co in v['comparisons']:check(prefix+':comparison_'+co['role'],sha(ROOT/co['path'])==co['sha256']==sha(ROOT/co['copy_of']))
        selected=pickmap[aid];check(aid+':selection_matches',selected==row['selected'] and selected['selected_version']==choice)
        if choice:
            v=row['versions'][choice];check(aid+':chosen_is_reviewed_candidate',v['status']=='reviewed_candidate')
            for role in ['master','thumbnail','card']:check(aid+':selected_copy_'+role,sha(ROOT/selected[role])==v['files'][role]['sha256'])
        else:
            check(aid+':neither_has_null_selection',all(selected[k] is None for k in ['master','thumbnail','card','sha256','source_master']) and selected['status']=='both_need_revision')
            check(aid+':both_statuses_need_revision',all(v['status']=='needs_revision' for v in row['versions'].values()))
        if n==17:
            for v in row['versions'].values():check(aid+':panorama_2_to_1_'+v['version'],v['actual_dimensions'][0]==2*v['actual_dimensions'][1])
    check('all_54_distinct_native_output_hashes',len(natives)==len(set(natives))==54)
    for b in doc['bases']:check(b['asset_id']+':unchanged_shared_base',sha(ROOT/b['path'])==b['sha256']==next(x['sha256'] for x in baseline['base_hashes'] if x['asset_id']==b['asset_id']) and (ROOT/b['generation_record']).is_file())
    check('same_action_base_for_24_and_25',Brefs['creative-preset-24']['sha256']==Brefs['creative-preset-25']['sha256'])
    check('same_portrait_base_for_all_six_skin_presets',len({Brefs[f'creative-preset-{i}']['sha256'] for i in range(11,17)})==1)
    check('all_recommendation_counts',counts['A']==doc['summary']['recommend_A'] and counts['B']==doc['summary']['recommend_B'] and counts['neither']==doc['summary']['both_need_revision'])
    for folder,role in [('masters','master'),('thumbs','thumbnail'),('cards','card')]:check('selected_'+folder+'_exact_set',{p.name for p in (ROOT/'selected'/folder).iterdir()}=={Path(x[role]).name for x in picks if x[role]})
    check('three_real_initial_attempts',len(list((ROOT/'attempts').glob('B-*-initial.png')))==3)
    for i in [16,18,19]:
        p=ROOT/'attempts'/f'B-creative-preset-{i}-initial.png';j=read(f'attempts/B-creative-preset-{i}-initial.json')
        if args.tool_originals:check('initial_'+str(i)+'_unchanged',sha(p)==sha(Path(j['path'])))
    with (ROOT/'selection.csv').open(encoding='utf-8-sig',newline='') as f:cr=list(csv.DictReader(f))
    check('CSV_has_all_27_mappings',len(cr)==27 and {x['asset_id'] for x in cr}==set(req))
    images=[]
    for p in sorted(ROOT.rglob('*')):
        if p.suffix.lower() in ['.png','.jpg','.webp']:
            with Image.open(p) as im:im.load()
            images.append(str(p.relative_to(ROOT)))
    check('all_package_images_decode',True,{'count':len(images)})
    check('no_zero_byte_payloads',all(p.stat().st_size>0 for p in ROOT.rglob('*') if p.is_file()))
    check('actual_browser_test_passed',read('results/browser-validation.json')['passed'])
    if args.source_A:
        original_manifest=read('provenance/A-MANIFEST.json')
        check('prior_A_manifest_unchanged',sha(args.source_A/'MANIFEST.json')==baseline['A_original_manifest_sha256'])
        check('all_prior_A_files_unchanged',all(sha(args.source_A/x['path'])==x['sha256'] for x in original_manifest['files']),{'count':len(original_manifest['files'])})
    if not args.skip_manifest:
        mf=read('MANIFEST.json');listed={x['path']:x for x in mf['files']};actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p!=ROOT/'MANIFEST.json'}
        check('manifest_exact_payload_set',set(listed)==actual)
        check('manifest_all_bytes_and_hashes',all((ROOT/rel).stat().st_size==x['bytes'] and sha(ROOT/rel)==x['sha256'] for rel,x in listed.items()),{'count':len(listed)})
    report={'executed_at_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version.split()[0],'pillow':Image.__version__,'visual_quality_certified':False,'manifest_checked':not args.skip_manifest,'tool_originals_checked':args.tool_originals,'source_A_checked':bool(args.source_A),'checks':checks,'passed':all(x['passed'] for x in checks)}
    print(json.dumps(report,ensure_ascii=False,indent=2));return 0 if report['passed'] else 1
def sha_text(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
if __name__=='__main__':raise SystemExit(main())
