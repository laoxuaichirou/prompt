"""Offline file/mask checks and pixel diagnostics; never calls a generation service."""
from pathlib import Path
from PIL import Image,ImageChops,ImageStat
import hashlib,json,sys,datetime
B=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def mask_diff():
 src=Image.open(B/'assets/masked-local-edit/source-living-room.png').convert('RGB')
 out=Image.open(B/'assets/masked-local-edit/gpt-effect-reference-attempt-01.png').convert('RGB')
 mask=Image.open(B/'assets/masked-local-edit/mask-edit-white.png').convert('L')
 assert src.size==out.size==mask.size
 outside=ImageChops.invert(mask);diff=ImageChops.difference(src,out)
 r,g,b=diff.split();maximum=ImageChops.lighter(ImageChops.lighter(r,g),b)
 pixels=outside.histogram()[255]
 changed=lambda threshold:sum(n for value,n in enumerate(maximum.histogram(mask=outside)) if value>threshold)
 result={'scope':'GPT效果参考；逐像素差异诊断，不是Qwen/Krea/H3测试或感知质量评分',
  'inputSha256':digest(B/'assets/masked-local-edit/source-living-room.png'),
  'outputSha256':digest(B/'assets/masked-local-edit/gpt-effect-reference-attempt-01.png'),
  'dimensions':list(src.size),'nativeMaskParameterUsed':False,'maskAsImageReference':True,
  'insidePixels':mask.histogram()[255],'outsidePixels':pixels,
  'outsidePixelsAnyChange':changed(0),'outsideFractionAnyChange':changed(0)/pixels,
  'outsidePixelsMaxChannelDiffAbove16':changed(16),'outsideFractionMaxChannelDiffAbove16':changed(16)/pixels,
  'outsideMeanAbsoluteRGBDifference':ImageStat.Stat(diff,mask=outside).mean,
  'insideMeanAbsoluteRGBDifference':ImageStat.Stat(diff,mask=mask).mean,
  'strictOutsidePixelPreservation':'FAIL' if changed(0)>0 else 'PASS',
  'interpretation':'中心抱枕变蓝，但非蒙版区域也被重绘；保留第一次结果作为局部硬约束不理想样例，不作后期贴回掩饰。'}
 (B/'results/masked-edit-diff.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 return result

def check():
 index=json.loads((B/'asset-index.json').read_text());calls=json.loads((B/'results/tool-calls.json').read_text())
 assets={a['id']:a for a in index['assets']};by_path={a['path']:a for a in index['assets']}
 assert len(assets)==len(by_path)==10
 checks=[]
 def ok(value,message):
  assert value,message
  checks.append(message)
 for a in assets.values():
  p=B/a['path'];ok(p.is_file() and p.stat().st_size>0,a['id']+' real nonempty file')
  ok(digest(p)==a['sha256'],a['id']+' SHA256 matches index')
  with Image.open(p) as im:
   im.load();ok(list(im.size)==[a['width'],a['height']],a['id']+' pixel dimensions')
   ok(im.format=='PNG' and im.mode==a['mode'],a['id']+' PNG format/mode')
 ok(len(calls)==8 and sum(c['operation']=='generate' for c in calls)==5 and sum(c['operation']=='edit' for c in calls)==3,'8 recorded actual builtin generation/edit calls')
 for c in calls:
  ok(c['asset'] in by_path,c['id']+' output included')
  ok((B/c['prompt']).is_file() and (B/c['prompt']).stat().st_size>0,c['id']+' exact prompt included')
  for ref in c['references']:ok(ref in by_path,c['id']+' actual reference file included')
  if c['operation']=='edit':ok(c['label']=='GPT效果参考',c['id']+' correctly labeled GPT reference only')
 # No unlisted photograph or mask, no hidden successful replacement for failed attempt.
 actual={str(p.relative_to(B)) for p in (B/'assets').rglob('*.png')}
 ok(actual==set(by_path),'every independent PNG indexed')
 for scenario in index['scenarios']:
  c=next(c for c in calls if c['id']==scenario['editCallId'])
  ok(c['references']==[assets[x]['path'] for x in scenario['actualToolInputOrder']],'fixed input order '+scenario['id'])
  ok(c['asset']==assets[scenario['gptEffectReference']]['path'],'output binding '+scenario['id'])
  ok(assets[scenario['source']]['width']==assets[scenario['gptEffectReference']]['width'] and assets[scenario['source']]['height']==assets[scenario['gptEffectReference']]['height'],'source/output canvas '+scenario['id'])
 meta=json.loads((B/'results/mask-metadata.json').read_text())
 source=B/meta['source'];mask=Image.open(B/'assets/masked-local-edit/mask-edit-white.png')
 alpha=Image.open(B/'assets/masked-local-edit/mask-edit-alpha.png')
 ok(digest(source)==meta['sourceSha256'],'mask bound to finalized source hash')
 ok(mask.size==alpha.size==Image.open(source).size==(1254,1254),'both masks exactly match source canvas')
 ok(mask.mode=='L' and set(mask.tobytes())=={0,255},'binary mask white edit/black preserve')
 ok(alpha.mode=='RGBA' and set(alpha.getchannel('A').tobytes())=={0,255},'alpha mask supports two alpha values')
 ok(all(c.getextrema()==(255,255) for c in alpha.split()[:3]),'alpha mask RGB white everywhere')
 ok(alpha.getchannel('A').tobytes()==ImageChops.invert(mask).tobytes(),'alpha zero edit and 255 preserve exactly invert binary mask')
 ok(list(mask.getbbox())==meta['editBoundingBox']==[466,409,787,673],'mask actual pixel bounding box')
 ok(mask.histogram()[255]==meta['editPixels']==63073,'mask exact area')
 for point,value in [((620,500),255),((200,550),0),((1000,550),0),((620,750),0),((0,0),0)]:ok(mask.getpixel(point)==value,'mask position check '+str(point))
 ok(index['unavailableGeneratedImages']==[],'no generated photos missing from ZIP candidate')
 ok(index['discardedAttempts']==[],'all actual attempts preserved')
 diff=mask_diff()
 # File/mask checks pass while the edit's hard-preservation quality check FAILS.
 ok(diff['strictOutsidePixelPreservation']=='FAIL','unideal hard-mask result explicitly recorded rather than hidden')
 summary={'status':'FILES_VERIFIED_WITH_RECORDED_EDIT_LIMITATIONS','executedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'python':sys.version.split()[0],'independentPNGFiles':len(assets),'realBuiltinImageCalls':8,'photoOutputs':8,'technicalMasks':2,
  'fileAndMaskChecks':'PASS','assertions':len(checks),'checks':checks,
  'strictMaskedEditOutsidePreservation':diff['strictOutsidePixelPreservation'],
  'nativeMaskAPIValidated':False,'QwenTested':False,'KreaTested':False,'H3Tested':False,
  'unavailableGeneratedImages':[],'discardedAttempts':[]}
 (B/'results/checks.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k!='checks'},ensure_ascii=False,indent=2))

if __name__=='__main__':check()
