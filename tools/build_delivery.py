#!/usr/bin/env python3
"""Build A/B metadata and byte-identical selected copies. No image retouching/API."""
import json,hashlib,shutil,csv
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def info(rel):
    p=ROOT/rel
    with Image.open(p) as im:size=list(im.size)
    return {'path':rel,'dimensions':size,'bytes':p.stat().st_size,'sha256':digest(p)}
def main():
    req=json.loads((ROOT/'brief/asset-requests.json').read_text());original=json.loads((ROOT/'provenance/A-asset-map.json').read_text())
    A={x['asset_id']:x for x in original['items']};dec=json.loads((ROOT/'results/decisions.json').read_text());rows=[];selection=[]
    for folder in ['masters','thumbs','cards']:
        for p in (ROOT/'selected'/folder).iterdir():
            if p.is_file():p.unlink() # Only previously compiled mixed selections, never originals.
    for src in req['items']:
        if src['priority']!='P0':continue
        aid=src['asset_id'];n=int(aid.rsplit('-',1)[1]);d=dec['items'][str(n)]
        row={k:src.get(k) for k in ['asset_id','priority','name','target','source_prompt','source_prompt_sha256','art_direction','base_asset','preview_kind']}
        row.update(generated_by='ChatGPT',versions={},decision={'recommended_version':d['recommended_version'],'reason':d['reason'],'method':'assistant_visual_review','provider_verified':False},pair_review=f'reviews/pairs/{aid}.jpg')
        for version in ['A','B']:
            old=A[aid] if version=='A' else None
            rp=ROOT/version/'results'/f'{aid}.json';rec=json.loads(rp.read_text()) if rp.exists() else None
            master=f'{version}/masters/{aid}.png';thumbnail=f'{version}/thumbs/{aid}.webp';card=f'{version}/cards/{aid}.webp'
            if not rec or not (ROOT/master).exists():
                row['versions'][version]={'version':version,'status':'not_generated','master':None,'thumbnail':None,'card':None,'generated_by':None,'preview_kind':src['preview_kind'],'visual_notes':['未生成，不提供空图片或假路径。']};continue
            prompt=old['actual_prompt'] if old else rec['prompt'];promptfile=f'{version}/prompts/{aid}-actual.txt';(ROOT/promptfile).write_text(prompt+'\n',encoding='utf-8')
            v={'version':version,'status':old['status'] if old else d['B_status'],'generated_by':'ChatGPT','preview_kind':src['preview_kind'],'master':master,'thumbnail':thumbnail,'card':card,'actual_prompt':prompt,'actual_prompt_file':promptfile,'generation_record':f'{version}/results/{aid}.json','visual_notes':old['visual_notes'] if old else [d['B_notes']],'reference_images':[],'files':{key:info(rel) for key,rel in [('master',master),('thumbnail',thumbnail),('card',card)]},'comparisons':[]}
            v.update(actual_dimensions=v['files']['master']['dimensions'],sha256=v['files']['master']['sha256'])
            if old:
                v['reference_images']=old['reference_images'];v['source_commit']='a220b7bab57a493e6ce8a4354fd30f0695207843'
            else:
                for i,path in enumerate(rec['reference_paths']):
                    rel=str(Path(path).relative_to(ROOT));v['reference_images'].append(info(rel)|{'input_order':i+1})
                v['derivative_method']='Whole native PNG contained inside >=8% outer margin on 1536x864 dark WebP canvas, then 640x360 WebP. No stretch, crop or artistic filters.'
                if n==17:v['usage_limit']='panorama composition illustration only; not seamless 360'
            row['versions'][version]=v
        for version in ['A','B']:
            v=row['versions'][version]
            if not v['master'] or n not in [24,25,26]:continue
            if n==24:files=[('before','bases/base-action.png'),('after',v['master'])]
            elif n==25:files=[('before',v['master']),('after','bases/base-action.png')]
            else:files=[('before','bases/base-scene.png'),('after',v['master'])]
            out=ROOT/'comparisons'/version/aid;out.mkdir(parents=True,exist_ok=True)
            for role,source in files:
                rel=f'comparisons/{version}/{aid}/{role}.png';shutil.copy2(ROOT/source,ROOT/rel);v['comparisons'].append(info(rel)|{'role':role,'copy_of':source})
        chosen=d['recommended_version'];v=row['versions'].get(chosen) if chosen else None
        row['status']='selected_candidate' if chosen else 'both_need_revision'
        pick={k:row[k] for k in ['asset_id','name','target','preview_kind']};pick.update(selected_version=chosen,status=row['status'],reason=d['reason'],generated_by='ChatGPT' if chosen else None,master=None,thumbnail=None,card=None,sha256=None,source_master=None)
        if v and v['master']:
            for role,folder,suffix in [('master','masters','png'),('thumbnail','thumbs','webp'),('card','cards','webp')]:
                rel=f'selected/{folder}/{aid}.{suffix}';shutil.copy2(ROOT/v[role],ROOT/rel);pick[role]=rel
            pick['sha256']=v['sha256'];pick['source_master']=v['master']
        row['selected']=pick;selection.append(pick);rows.append(row)
    counts=Counter(x['decision']['recommended_version'] or 'neither' for x in rows)
    summary={'P0_requested':27,'A_generated':sum(bool(x['versions']['A']['master']) for x in rows),'B_generated':sum(bool(x['versions']['B']['master']) for x in rows),'recommend_A':counts['A'],'recommend_B':counts['B'],'both_need_revision':counts['neither'],'mixed_selected':counts['A']+counts['B'],'this_run_B_image_calls':30,'retained_B_initial_attempts':3,'quota_error_observed':False}
    bases=[{**b,'path':'bases/'+Path(b['path']).name,'generation_record':'provenance/base-results/'+Path(b['generation_record']).name} for b in original['bases']]
    write(ROOT/'asset-map.json',{'schema':'directorx-preset-ab-delivery/1','scope':'P0 only; preserve original preset IDs','built_at_utc':datetime.now(timezone.utc).isoformat(),'generated_by':'ChatGPT','summary':summary,'source_A_commit':'a220b7bab57a493e6ce8a4354fd30f0695207843','status_definitions':{'reviewed_candidate':'actual visually reviewed creative candidate, not production/provider certification','needs_revision':'actual image retained with unresolved issues','both_need_revision':'neither version selected; original files remain under versions','selected_candidate':'qualitative assistant recommendation only'},'bases':bases,'items':rows})
    write(ROOT/'selection.json',{'schema':'directorx-assistant-ab-selection/1','selection_is_not_canvas_integration':True,'items':selection})
    write(ROOT/'results/visual-review.json',{'review_method':dec['review_method'],'criteria':dec['criteria'],'summary':summary,'first_six_record':'results/first-six-review.json','all_pairs_reviewed':True,'native_skin_review':'reviews/details/skin-native-crops.jpg','panorama_join_review':'reviews/panorama-seams-ab.jpg','decisions':[{k:x[k] for k in ['asset_id','name','decision']} for x in rows]})
    lines=['# A/B 推荐与理由','','推荐仅针对GPT创意候选。原图、缩略图和实际提示词均独立保存；选择页允许你覆盖推荐。','','| ID / 名称 | 推荐 | 理由 | 对照 | A原图 | B原图 |','|---|---|---|---|---|---|']
    for x in rows:
        d=x['decision'];choice=d['recommended_version'] or '两版返修'
        lines.append(f"| {x['asset_id']} / {x['name']} | {choice} | {d['reason']} | [A/B]({x['pair_review']}) | [PNG]({x['versions']['A']['master']}) | [PNG]({x['versions']['B']['master']}) |")
    (ROOT/'RECOMMENDATIONS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    with (ROOT/'selection.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['asset_id','name','selected_version','status','master','thumbnail','sha256','reason']);w.writeheader();w.writerows({k:x.get(k) for k in w.fieldnames} for x in selection)
    missing=[x for x in rows if not x['versions']['B']['master']]
    unfinished=['# 缺项与不理想结果','','B生成缺项：'+str(len(missing))+'。本轮只重做P0；P1/P2沿用此前独立交付，不计作本轮缺项。','','## 两版均待返修','']
    unfinished += [f"- {x['asset_id']} / {x['name']}：{x['decision']['reason']}" for x in rows if not x['decision']['recommended_version']]
    unfinished += ['','## B不如A、仍保留原图','']+[f"- {x['asset_id']} / {x['name']}：{x['decision']['reason']}" for x in rows if x['versions']['B']['status']=='needs_revision' and x['decision']['recommended_version']=='A']
    unfinished += ['','## 保留的定向修正初版','','- B-creative-preset-16-initial：控油特征不足；定向重试仍未达到小图可辨要求。','- B-creative-preset-18-initial：首排中间是斜侧面，最终通过GPT改成严格侧视。','- B-creative-preset-19-initial：整体留白仍不足，最终通过GPT后移取景扩大上下留白。','','三张PNG及对应JSON均在attempts/，没有被悄悄丢弃。']
    (ROOT/'UNFINISHED.md').write_text('\n'.join(unfinished)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__':main()
