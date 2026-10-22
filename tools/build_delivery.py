#!/usr/bin/env python3
"""Build portable metadata from saved, actual image-tool results. No generation/API."""
import json, hashlib, shutil, csv
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p, data): p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def info(rel):
    p=ROOT/rel
    with Image.open(p) as im: size=list(im.size)
    return {'path':rel,'dimensions':size,'bytes':p.stat().st_size,'sha256':sha(p)}

NOTES={
0:'暖色、高光过渡和细颗粒可见；脸、衣服、杯子、红本与植物位置保持。品牌名称仅代表色彩意图。',
1:'绿蓝较清新，阴影略冷；同一咖啡馆物件和姿势。',
2:'黑白与灰阶层次明确，缩略图易辨认；颗粒未经物理测量。',
3:'饱和度受控、阴影加深；主体构图保持。',
4:'暖色褪色与柔和反差可见，没有额外宝丽来边框。',
5:'窗侧主光与亮边增强，背景实景灯保持；与柯达暖调仍相近，作为灯光候选。',
6:'暗部可读，但相对自然光底图改变较弱，640缩略图中不易辨识HDR意图，待返修。',
7:'高光扩散明显，五官与主体轮廓仍可读；窗边高光略强。',
8:'原图可见细颗粒，缩略图不应期待颗粒显著；未用代码添加噪声。',
9:'青红夜间霓虹、雨窗和湿桌反射明确；人物与固定物件保持，新增湿润表面属于预设要求。',
10:'暖黄褪色和低饱和阴影可见，缩略图与其他暖色胶片仍有相近之处。',
11:'同一脸、发型、表情、灰衣和取景；清透与其他肤质在缩略图中区别不足，待返修。',
12:'局部瑕疵有柔化，身份保持；缩略图与底图及其他肤质区别不足，待返修。',
13:'原图毛孔细节有所增强；在640缩略图仍难与其他肤质快速区分，待返修。',
14:'肤色略均匀柔润，未换脸；奶油肌视觉识别度仍弱，待返修。',
15:'高频细节略柔化，眼睛与头发清晰；缩略图区别弱，待返修。',
16:'额头和鼻部油光有所控制，身份保持；缩略图与柔肤仍相近，待返修。',
17:'实际原图1774×887，严格2:1；横向空间可读。左右柱、家具和亮度不能证明接缝连续，仅为全景构图示意，待返修/专门全景验证。',
18:'实际3×3等格，九种景别/机位可分辨。原图顶行头脚靠近格线；小图面部细节有限，部分背包/肩带形状不完全一致，待返修。',
19:'正侧背全身齐全，等高；原图上下安全留白不足，肩带/包形跨视角有偏差，待返修。',
20:'2×2包含正侧背全身与面部特写；侧面肩带/包位置仍需核对，原图外边距偏小，待返修。',
21:'全身主视图及衣服、包、鞋细节齐全；部件拼接关系未工程验证，原图边距紧，缩略图细节偏密，衣领有细小伪标签，待返修。',
22:'原创湖畔小咖啡馆概念页，外观、室内和材质细节可辨。模型自行加入湖山环境；剖视与外观未严格几何对应，作为概念意图候选。',
23:'正侧背、拆解与材质细节齐全；表冠/铰链方向大体对应，但机芯拆解为生成想象，部分形状与底图不同，原图边距紧，待返修。',
24:'从伸手未持杯推进到举杯，人物服装与咖啡馆连续；手指接触未做逐像素或物理验证。3秒为叙事情境。',
25:'初版几乎重复底图，已保留。重试后双手下垂远离杯，白杯仍在原桌面，形成伸手前状态；5秒为叙事情境。',
26:'同一取景、身份与物件，窗光和明暗比校正可见；不是目标工作流实测，也不是光度学正确性结论。'
}
REVISE={6,11,12,13,14,15,16,17,18,19,20,21,23}
CAMERA_NOTES={
'camera-preview-01':'成年虚构人物浅景深人像，冷暖实景光与电影感可读；不是ARRI/Cooke实拍或镜头标定。',
'camera-preview-02':'河岸人物与周围环境同时可见，环境纪实意图清楚；未测视场角与真实景深。',
'camera-preview-03':'建筑主立面与空间透视可读，广角建筑意图明确；垂线未做像素级标定或移轴光学验证。',
'camera-preview-04':'原创无品牌腕表机芯微距，金属细节可读；机芯出现细小伪刻字，需清除；外缘与表带为细节裁切，机械结构未验证，待返修。'
}
LIGHT_NOTES={
'lighting-preview-01':'左侧窗光、背景窗影可读，人物姿势服装保持。',
'lighting-preview-02':'斜向可见光束与漂浮微粒形成丁达尔意图，人物保持；没有物理散射测量。',
'lighting-preview-03':'低角度暖金光明显，脸与服装保持。',
'lighting-preview-04':'冷蓝月光与暗背景明显，脸与服装保持。',
'lighting-preview-05':'米白柔光过渡与低反差意图，暖白背景与灰底其他光线可区分；没有改变衣服与脸。',
'lighting-preview-06':'青红混合照明意图，脸与服装保持。',
'lighting-preview-07':'背后边缘亮光形成轮廓，主体保留。',
'lighting-preview-08':'左上聚光束与明暗区隔可见，面部保留补光；舞台聚光意图示例，无实际灯具测量。',
'lighting-preview-09':'阴天散射、柔和低反差，取景与人物保持；与米白柔光差异需复核。',
'lighting-preview-10':'硬光与阴影边界明确，人物身份保持。',
'lighting-preview-11':'低照度暖光与肤色反射意图，人物保持；不是烛光色温实测。',
'lighting-preview-12':'自然正向光，明亮均匀，人物保持；与柔光类缩略图区分需复核。'
}

def main():
    req=json.loads((ROOT/'brief/asset-requests.json').read_text())
    entries=[]
    for it in req['items']:
        aid=it['asset_id']; result=ROOT/'results'/f'{aid}.json'
        row={k:it.get(k) for k in ['asset_id','priority','name','target','source_prompt','source_prompt_sha256','art_direction','base_asset','preview_kind']}
        row.update(status='not_generated',master=None,thumbnail=None,card=None,generated_by=None,actual_prompt=None,actual_dimensions=None,sha256=None,reference_images=[],visual_notes=[],comparisons=[])
        if not result.exists():
            row['visual_notes']=['尚未生成；不提供假路径。']; entries.append(row); continue
        j=json.loads(result.read_text())
        m=info(f'masters/{aid}.png'); t=info(f'thumbs/{aid}.webp'); c=info(f'cards/{aid}.webp')
        row.update(status='reviewed_candidate',master=m['path'],thumbnail=t['path'],card=c['path'],generated_by='ChatGPT',actual_prompt=j['prompt'],actual_dimensions=m['dimensions'],sha256=m['sha256'],files={'master':m,'thumbnail':t,'card':c},generation_record=f'results/{aid}.json')
        (ROOT/'prompts'/f'{aid}-actual.txt').write_text(j['prompt']+'\n',encoding='utf-8')
        row['actual_prompt_file']=f'prompts/{aid}-actual.txt'
        if it['base_asset']:
            row['reference_images']=[info(f"bases/{it['base_asset']}.png")]
        if it['priority']=='P0':
            n=int(aid.rsplit('-',1)[1]); row['visual_notes']=[NOTES[n]]
            if n in REVISE: row['status']='needs_revision'
        elif it['priority']=='P1':
            row['visual_notes']=[CAMERA_NOTES[aid]]
            if aid=='camera-preview-04': row['status']='needs_revision'
        else:
            row['visual_notes']=[LIGHT_NOTES[aid]]
            if aid in {'lighting-preview-09','lighting-preview-12'}: row['status']='needs_revision'
        row['visual_review_method']='assistant visual inspection of actual image-tool output and review contact sheet; subjective, no face-recognition/physical proof'
        row['derivative_method']='contain whole original without stretch/crop inside a 1536x864 dark canvas with >=8% outer margin; quality94 WebP card, quality88 640x360 WebP thumbnail; originals unchanged. Does not fix already clipped contents or internal panel defects.'
        entries.append(row)
    for aid,before,after in [
        ('creative-preset-24','bases/base-action.png','masters/creative-preset-24.png'),
        ('creative-preset-25','masters/creative-preset-25.png','bases/base-action.png'),
        ('creative-preset-26','bases/base-scene.png','masters/creative-preset-26.png')]:
        dest=ROOT/'comparisons'/aid;dest.mkdir(exist_ok=True)
        for label,src in [('before',before),('after',after)]:
            shutil.copy2(ROOT/src,dest/f'{label}.png')
        row=next(x for x in entries if x['asset_id']==aid)
        row['comparisons']=[info(f'comparisons/{aid}/{label}.png')|{'role':label,'copy_of':src} for label,src in [('before',before),('after',after)]]
        row['comparison_time_order']='before is chronologically earlier; 25: generated minus5s -> shared t0; 24: shared t0 -> generated plus3s' if aid!='creative-preset-26' else 'lighting base -> GPT relighting'
    base_rows=[]
    for b in req['bases']:
        aid=b['asset_id']; j=json.loads((ROOT/'results'/f'{aid}.json').read_text())
        rec=f'results/{aid}.json'; prompt=j['prompt']
        if aid=='base-portrait':
            rec='results/base-portrait-reframe.json';j=json.loads((ROOT/rec).read_text());prompt=j['prompt']
        base_rows.append({'asset_id':aid,'description':b['description'],'generated_by':'ChatGPT',**info(f'bases/{aid}.png'),'actual_prompt':prompt,'generation_record':rec,'notes':'Portrait first output clipped crown; retained in attempts and reframed by image tool.' if aid=='base-portrait' else 'Actual generated base. Full-body/prop raw margins tighter than requested; inspect before production.'})
    summary={p:{'requested':sum(x['priority']==p for x in entries),'generated':sum(x['priority']==p and bool(x['master']) for x in entries),'needs_revision':sum(x['priority']==p and x['status']=='needs_revision' for x in entries)} for p in ['P0','P1','P2']}
    doc={'schema':'directorx-preset-art-delivery/1','generated_by':'ChatGPT','built_at_utc':datetime.now(timezone.utc).isoformat(),'summary':summary,'status_definitions':{'reviewed_candidate':'Actual generated, visually inspected creative candidate; not a target-provider or production approval.','needs_revision':'Actual files delivered; unresolved visual issues listed.','not_generated':'No image produced; file paths null.'},'bases':base_rows,'items':entries}
    write(ROOT/'asset-map.json',doc)
    write(ROOT/'results/visual-review.json',{'method':'assistant_visual_review','structural_tests_are_separate':True,'first_six_inspected_before_remaining':[f'creative-preset-{n}' for n in [0,12,19,18,23,26]],'notes_by_asset':[{k:x[k] for k in ['asset_id','status','visual_notes']} for x in entries]})
    missing=[x for x in entries if not x['master']]
    revision=[x for x in entries if x['status']=='needs_revision']
    lines=['# 未完成与返修清单','','生成缺项：'+str(len(missing))+'。','没有收到额度不足错误；不把优先级安排或视觉返修写成额度耗尽。','','## 已生成但待返修','']
    lines += [f"- {x['asset_id']} / {x['name']}：{x['visual_notes'][0]}" for x in revision]
    lines += ['','## 未生成项','']+[f"- {x['asset_id']} / {x['name']}" for x in missing]
    if not missing:lines+=['无。P0 27项、P1 4项、P2 12项均已有实际图片；生成完成不等同于视觉验收通过。']
    (ROOT/'UNFINISHED.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__': main()
