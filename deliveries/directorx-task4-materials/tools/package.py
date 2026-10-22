#!/usr/bin/env python3
from pathlib import Path
import zipfile,hashlib,json
B=Path(__file__).resolve().parents[1]
def purpose(rel):
 s=str(rel)
 if s.startswith('assets/') and 'gpt-effect-reference' in s:return '真实GPT编辑首轮结果；仅GPT效果参考，包含未达到严格保留条件的结果'
 if s.startswith('assets/') and 'mask-edit' in s:return '由最终原图实际尺寸和轮廓产生的独立技术蒙版，约定见metadata'
 if s.startswith('assets/'):return '真实ChatGPT生成的独立原图或参考图，未重编码、未拼图替代'
 if s.startswith('prompts/'):return '真实调用提示词或中文复用说明，参考顺序与索引对应'
 if s.startswith('results/'):return '本次实际调用记录、文件/蒙版检查、失败差异或日志'
 if s.startswith('tools/'):return '技术蒙版/只读诊断/哈希检查或打包脚本，不调用生成服务'
 if s.startswith('asset-index'):return '独立素材ID、来源、尺寸、SHA256、提示词及引用顺序索引'
 return '使用说明、真实效果审阅或未验证边界'
files=[]
for p in sorted(B.rglob('*')):
 if not p.is_file() or p.name=='MANIFEST.json':continue
 assert '__pycache__' not in p.parts and p.suffix!='.pyc','remove generated cache before packaging'
 raw=p.read_bytes();assert len(raw)>0,'Refuse an empty placeholder: '+str(p)
 rel=p.relative_to(B);files.append({'path':str(rel),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'purpose':purpose(rel)})
(B/'MANIFEST.json').write_text(json.dumps({'schema':1,'scope':'Task four: actual GPT image assets and GPT effect references, not Qwen/Krea/H3 tests',
 'selfHash':'MANIFEST.json excludes itself to avoid circular hashing; all other ZIP entries are listed','files':files},ensure_ascii=False,indent=2)+'\n')
out=B.parent/'directorx-task4-materials.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(B/f['path'],f['path'])
 z.write(B/'MANIFEST.json','MANIFEST.json')
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 for f in files:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
 assert set(z.namelist())=={f['path'] for f in files}|{'MANIFEST.json'}
print(json.dumps({'file':str(out),'bytes':out.stat().st_size,'files':len(files)+1,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'integrity':'PASS'}))
