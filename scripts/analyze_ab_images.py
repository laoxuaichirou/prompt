#!/usr/bin/env python3
"""Analyze existing image-generation outputs without changing any image pixels."""
from pathlib import Path
import hashlib,json
from PIL import Image,ImageStat
R=Path(__file__).resolve().parents[1];D=R/'artifacts/ab-2026-10-23'
def measure(path):
 with Image.open(path) as im:
  im.load();rgb=im.convert('RGB');w,h=im.size
  def mean(box):return [round(x,3) for x in ImageStat.Stat(rgb.crop(box)).mean]
  k=max(4,min(w,h)//30);corners=[mean(b) for b in [(0,0,k,k),(w-k,0,w,k),(0,h-k,k,h),(w-k,h-k,w,h)]]
  a=im.convert('RGBA').getchannel('A');hist=a.histogram();total=w*h
  return {'width':w,'height':h,'mode':im.mode,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'corner_mean_rgb':corners,'alpha':{'minimum':min(i for i,c in enumerate(hist) if c),'maximum':max(i for i,c in enumerate(hist) if c),'fully_transparent_fraction':round(hist[0]/total,6),'semitransparent_fraction':round(sum(hist[1:255])/total,6),'fully_opaque_fraction':round(hist[255]/total,6),'has_real_transparency':sum(hist[:255])>0,'visible_bbox_alpha_gt8':a.point(lambda x:255 if x>8 else 0).getbbox()},'sky_probe_mean_rgb':mean((0,0,int(w*.25),int(h*.2))),'accent_probe_rgb':list(rgb.getpixel((int(w*.54),int(h*.395))))}
plan=json.loads((D/'plan.json').read_text());calls={x['id']:x for x in json.loads((D/'invocations.json').read_text())['records']}
items=[]
for case in plan['cases']:
 for variant in case['variants']:
  path=R/variant['expected_output'];m=measure(path)
  items.append({'id':variant['id'],'case_id':case['id'],'artifact':variant['expected_output'],'invocation':calls[variant['id']],**m})
(D/'image-metrics.json').write_text(json.dumps({'method':'Pillow metadata, PNG alpha histogram and explicitly located pixel probes; no image editing','note':'Pixel probes do not establish identity, physical Kelvin, product fidelity, or perceptual quality.','items':items},ensure_ascii=False,indent=2)+'\n')
for x in items:print(x['id'],x['width'],x['height'],x['mode'],'alpha0',x['alpha']['fully_transparent_fraction'],'corner',x['corner_mean_rgb'][0],'accent',x['accent_probe_rgb'])
