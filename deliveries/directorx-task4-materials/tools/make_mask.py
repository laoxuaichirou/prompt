"""Build technical masks from the actual finalized source; do not edit the photograph."""
from pathlib import Path
from PIL import Image, ImageFilter
from collections import deque
import hashlib,json
B=Path(__file__).resolve().parents[1]
src=B/'assets/masked-local-edit/source-living-room.png'
image=Image.open(src).convert('RGB');width,height=image.size
assert (width,height)==(1254,1254),'Source changed; inspect and redefine ROI before making a mask'
# ROI traced after viewing this exact source, not guessed for a future image.
roi=(450,390,820,710)
crop=image.crop(roi);w,h=crop.size
candidate=Image.new('L',(w,h),0)
pixels=zip(*(iter(crop.tobytes()),)*3)
candidate.putdata([255 if r>1.4*g and r>1.7*b and g>1.1*b and r-g>24 else 0 for r,g,b in pixels])
candidate=candidate.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
data=bytearray(candidate.tobytes());seed=(500-roi[1])*w+(620-roi[0]);assert data[seed]==255
# Retain just the connected cushion component containing the inspected center.
component=bytearray(w*h);component[seed]=255;queue=deque([seed])
while queue:
 i=queue.popleft();x=i%w;y=i//w
 for n in ([i-1] if x else [])+([i+1] if x+1<w else [])+([i-w] if y else [])+([i+w] if y+1<h else []):
  if data[n] and not component[n]:component[n]=255;queue.append(n)
# Fill holes inside the fabric area, preserving the external silhouette.
outside=bytearray(w*h);q=deque()
for i in range(w*h):
 if (i<w or i>=w*(h-1) or i%w in (0,w-1)) and component[i]==0:outside[i]=1;q.append(i)
while q:
 i=q.popleft();x=i%w;y=i//w
 for n in ([i-1] if x else [])+([i+1] if x+1<w else [])+([i-w] if y else [])+([i+w] if y+1<h else []):
  if not component[n] and not outside[n]:outside[n]=1;q.append(n)
filled=Image.frombytes('L',(w,h),bytes(255 if component[i] or not outside[i] else 0 for i in range(w*h)))
filled=filled.filter(ImageFilter.MaxFilter(3)) # one-pixel inclusion around the detected textile edge
mask=Image.new('L',image.size,0);mask.paste(filled,(roi[0],roi[1]))
out=B/'assets/masked-local-edit'
mask.save(out/'mask-edit-white.png')
inverse=mask.point(lambda x:255-x)
# White RGB everywhere: alpha=0 edit, alpha=255 preserve. Not a photo.
alpha=Image.new('RGBA',image.size,(255,255,255,255));alpha.putalpha(inverse);alpha.save(out/'mask-edit-alpha.png')
count=sum(v==255 for v in mask.tobytes())
metadata={'source':'assets/masked-local-edit/source-living-room.png','sourceSha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'width':width,'height':height,'coordinateSystem':'pixel origin top-left, x right, y down; bounds are [left, top, rightExclusive, bottomExclusive]',
 'inspectedROI':list(roi),'seedPixel':[620,500],'editBoundingBox':list(mask.getbbox()),'editPixels':count,'editFraction':count/(width*height),
 'binaryMask':{'path':'assets/masked-local-edit/mask-edit-white.png','mode':'L','editValue':255,'preserveValue':0,'featherPixels':0},
 'alphaMask':{'path':'assets/masked-local-edit/mask-edit-alpha.png','mode':'RGBA','editAlpha':0,'preserveAlpha':255,'rgb':'white constant'},
 'method':'Actual source RGB segmentation in visually inspected cushion ROI, connected component at seed, fill enclosed holes, one-pixel edge inclusion; no photograph was recolored or composited.',
 'toolContract':'GPT image editing used the binary mask as a reference image only; no native mask parameter was available, so hard pixel preservation is not claimed.'}
(B/'results/mask-metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(metadata,ensure_ascii=False,indent=2))
