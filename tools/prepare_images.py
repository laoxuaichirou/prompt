#!/usr/bin/env python3
"""Size/layout derivatives only. Never retouch, recolor, or create artwork."""
import json,shutil,math
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
def fit(im,size=(1536,864)):
    inner=(size[0]-2*math.ceil(size[0]*.08),size[1]-2*math.ceil(size[1]*.08))
    small=ImageOps.contain(im.convert('RGB'),inner,Image.Resampling.LANCZOS)
    out=Image.new('RGB',size,(28,30,34));out.paste(small,((size[0]-small.width)//2,(size[1]-small.height)//2));return out
def main():
    for p in sorted((ROOT/'B/results').glob('creative-preset-*.json')):
        j=json.loads(p.read_text())
        if not j.get('path') or j.get('version')!='B':continue
        aid=j['id'];dst=ROOT/'B/masters'/f'{aid}.png';shutil.copy2(j['path'],dst)
        with Image.open(dst) as im:
            card=fit(im);card.save(ROOT/'B/cards'/f'{aid}.webp',quality=94,method=6)
            card.resize((640,360),Image.Resampling.LANCZOS).save(ROOT/'B/thumbs'/f'{aid}.webp',quality=88,method=6)
    available=[]
    for i in range(27):
        aid=f'creative-preset-{i}';bp=ROOT/'B/thumbs'/f'{aid}.webp'
        if not bp.exists():continue
        available.append(i)
        pair=Image.new('RGB',(1280,400),'#202226');d=ImageDraw.Draw(pair)
        for n,v in enumerate(['A','B']):
            pair.paste(Image.open(ROOT/v/'thumbs'/f'{aid}.webp').convert('RGB'),(n*640,40));d.text((n*640+16,14),f'{aid} | {v}',fill='white')
        pair.save(ROOT/'reviews/pairs'/f'{aid}.jpg',quality=94)
    groups={'first-six':[0,12,19,18,23,26],'filters':list(range(11)),'skin':list(range(11,17)),'functions':list(range(17,27))}
    for name,nums in groups.items():
        nums=[i for i in nums if i in available]
        if not nums:continue
        sheet=Image.new('RGB',(1280,len(nums)*400),'#202226')
        for n,i in enumerate(nums):sheet.paste(Image.open(ROOT/'reviews/pairs'/f'creative-preset-{i}.jpg'),(0,n*400))
        sheet.save(ROOT/'reviews'/f'{name}-ab.jpg',quality=93)
    print(json.dumps({'B_masters':len(available),'AB_pairs':len(available)}))
if __name__=='__main__':main()
