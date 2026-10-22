#!/usr/bin/env python3
"""Copy actual tool outputs unchanged; make only size/layout derivatives."""
import json, shutil, math
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
ROOT = Path(__file__).resolve().parents[1]

def contain(im, size):
    # The entire native image fits inside an 8% outer safety margin.
    # This is a layout derivative; it does not repair internal grid/cropping defects.
    inner=(size[0]-2*math.ceil(size[0]*.08),size[1]-2*math.ceil(size[1]*.08))
    fitted = ImageOps.contain(im.convert('RGB'), inner, Image.Resampling.LANCZOS)
    out = Image.new('RGB', size, (28, 30, 34))
    out.paste(fitted, ((size[0]-fitted.width)//2, (size[1]-fitted.height)//2))
    return out

def main():
    for p in sorted((ROOT/'results').glob('*.json')):
        j = json.loads(p.read_text())
        if j.get('kind') != 'preset' or not j.get('path'): continue
        aid = j['id']
        master = ROOT/'masters'/f'{aid}.png'
        shutil.copy2(j['path'], master)
        with Image.open(master) as im:
            card = contain(im, (1536, 864))
            card.save(ROOT/'cards'/f'{aid}.webp', quality=94, method=6)
            card.resize((640,360), Image.Resampling.LANCZOS).save(ROOT/'thumbs'/f'{aid}.webp', quality=88, method=6)
    groups = {'representative': [0,12,19,18,23,26], 'filters': list(range(17)), 'functions': list(range(17,27))}
    groups={name:[f'creative-preset-{i}' for i in nums] for name,nums in groups.items()}
    groups['camera']=[f'camera-preview-{i:02d}' for i in range(1,5)]
    groups['lighting']=[f'lighting-preview-{i:02d}' for i in range(1,13)]
    for name, candidates in groups.items():
        ids = [aid for aid in candidates if (ROOT/'thumbs'/f'{aid}.webp').exists()]
        if not ids: continue
        cols=3; w=400; h=254
        sheet=Image.new('RGB', (cols*w, ((len(ids)+cols-1)//cols)*h), '#202226')
        draw=ImageDraw.Draw(sheet)
        for n,aid in enumerate(ids):
            x=(n%cols)*w; y=(n//cols)*h
            im=Image.open(ROOT/'thumbs'/f'{aid}.webp').convert('RGB').resize((384,216),Image.Resampling.LANCZOS)
            sheet.paste(im,(x+8,y+8)); draw.text((x+10,y+230),aid,fill='white')
        sheet.save(ROOT/'reviews'/f'{name}.jpg',quality=92)
    print(json.dumps({'copied_masters': len(list((ROOT/'masters').glob('*.png'))), 'thumbs':len(list((ROOT/'thumbs').glob('*.webp')))}))

if __name__ == '__main__': main()
