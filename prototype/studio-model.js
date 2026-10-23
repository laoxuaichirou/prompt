/* Portable workspace validation. No network or executable content in project files. */
(function(root,factory){if(typeof module==='object'&&module.exports)module.exports=factory(require('./model.js'));else root.StudioModel=factory(root.CanvasModel);})(globalThis,function(M){
 'use strict';
 const MAX_FILE=20*1024*1024,MAX_TOTAL=32*1024*1024,MAX_JSON=46*1024*1024;
 const allowed=['image/png','image/jpeg','image/webp','video/mp4'];
 function assert(ok,message){if(!ok)throw new Error(message);}
 function validateAsset(a){
  assert(a&&typeof a.id==='string'&&/^asset-[a-f0-9]{24}$/.test(a.id),'素材ID无效');
  assert(typeof a.name==='string'&&a.name.length>0&&a.name.length<=180,'素材名称无效');
  assert(allowed.includes(a.mime)&&Number.isInteger(a.bytes)&&a.bytes>0&&a.bytes<=MAX_FILE,'素材类型或大小无效');
  assert(a.mime==='video/mp4'||a.bytes<=8*1024*1024,'图片不能超过8MB');
  assert(typeof a.sha256==='string'&&/^[a-f0-9]{64}$/.test(a.sha256)&&a.id==='asset-'+a.sha256.slice(0,24),'素材校验信息无效');
  assert(typeof a.dataURL==='string'&&a.dataURL.startsWith('data:'+a.mime+';base64,'),'素材必须内嵌，不能引用外部地址');
  const data=a.dataURL.slice(a.dataURL.indexOf(',')+1);
  assert(data.length===4*Math.ceil(a.bytes/3)&&/^[A-Za-z0-9+/]+={0,2}$/.test(data),'素材编码或长度无效');
  return {id:a.id,name:a.name,mime:a.mime,bytes:a.bytes,sha256:a.sha256,dataURL:a.dataURL};
 }
 function validateState(s){
  assert(s&&Array.isArray(s.assets)&&s.assets.length<=50,'素材数量不能超过50');
  const assets=s.assets.map(validateAsset),ids=new Set(assets.map(a=>a.id));
  assert(ids.size===assets.length,'素材ID重复');
  assert(assets.reduce((n,a)=>n+a.bytes,0)<=MAX_TOTAL,'素材总大小不能超过32MB');
  const decisions={};
  assert(s.decisions&&typeof s.decisions==='object'&&!Array.isArray(s.decisions),'评审记录无效');
  assert(Object.keys(s.decisions).length<=5,'评审记录数量无效');
  for(const [id,d] of Object.entries(s.decisions)){
   assert(/^AB0[1-5]$/.test(id)&&d&&['A','B','neither','pending'].includes(d.choice)&&typeof d.note==='string'&&d.note.length<=2000,'评审选择或备注无效');
   decisions[id]={choice:d.choice,note:d.note};
  }
  const promptDrafts={},motionDrafts={};
  for(const [id,vars] of Object.entries(s.promptDrafts||{})){
   assert(/^(IMG|VID|REM)-[A-Z0-9-]+$/.test(id)&&vars&&typeof vars==='object'&&!Array.isArray(vars),'提示词草稿格式无效');
   assert(Object.keys(vars).length<=20,'提示词变量过多');promptDrafts[id]={};
   for(const [key,value] of Object.entries(vars)){assert(/^[a-zA-Z_][a-zA-Z0-9_]{0,60}$/.test(key)&&typeof value==='string'&&value.length<=1000,'提示词草稿变量无效');promptDrafts[id][key]=value;}
  }
  assert(Object.keys(promptDrafts).length<=50,'提示词草稿过多');
  for(const [id,props] of Object.entries(s.motionDrafts||{})){
   assert(['KineticWords','ProcessSteps','DataComparison'].includes(id)&&props&&typeof props==='object'&&!Array.isArray(props),'动效草稿格式无效');
   assert(Object.keys(props).length<=8,'动效草稿字段过多');motionDrafts[id]={};
   for(const [key,v] of Object.entries(props)){
    assert(['title','words','footer','steps','descriptions','labels','values','unit','source'].includes(key),'未知动效草稿字段');
    assert(typeof v==='string'&&v.length<=1000||Array.isArray(v)&&v.length<=10&&v.every(x=>typeof x==='string'&&x.length<=1000||typeof x==='number'&&Number.isFinite(x)),'动效草稿值无效');motionDrafts[id][key]=v;
   }
  }
  let customCompare={left:'sample:IMG-EC-01',right:'sample:IMG-FILM-03',choice:'pending',note:''};
  if(s.customCompare){
   const d=s.customCompare;const refs=new Set(['sample:IMG-EC-01','sample:IMG-FILM-03','sample:IMG-FILM-08',...assets.filter(a=>a.mime!=='video/mp4').map(a=>a.id)]);
   assert(refs.has(d.left)&&refs.has(d.right)&&['A','B','neither','pending'].includes(d.choice)&&typeof d.note==='string'&&d.note.length<=2000,'自定义对比引用或评审无效');
   customCompare={left:d.left,right:d.right,choice:d.choice,note:d.note};
  }
  return {assets,decisions,promptDrafts,motionDrafts,customCompare};
 }
 function validateBundle(b){
  assert(b&&b.format==='creator-desk-studio'&&b.version===2,'不支持的工作区格式');
  const graph=M.validate(b.graph),state=validateState(b.workspace);
  const ids=new Set(state.assets.map(a=>a.id));
  for(const n of graph.nodes)assert(!n.assetId||ids.has(n.assetId),'工程引用的素材缺失');
  return {format:b.format,version:2,graph,workspace:state};
 }
 function renderPrompt(item,vars){
  let text=item.prompt;
  for(const name of item.variables){assert(typeof vars[name]==='string'&&vars[name].trim()&&vars[name].length<=1000,'请填写变量：'+name);text=text.split('{{'+name+'}}').join(vars[name].trim());text=text.replace(new RegExp('{{\\s*'+name+'\\s*}}','g'),()=>vars[name].trim());}
  assert(!/{{[^}]+}}/.test(text),'提示词还有未填写变量');
  return text+'\n\n'+item.negative_guidance;
 }
 function mimeFromBytes(bytes){
  if(bytes[0]===137&&String.fromCharCode(...bytes.slice(1,4))==='PNG')return 'image/png';
  if(bytes[0]===255&&bytes[1]===216&&bytes[2]===255)return 'image/jpeg';
  if(String.fromCharCode(...bytes.slice(0,4))==='RIFF'&&String.fromCharCode(...bytes.slice(8,12))==='WEBP')return 'image/webp';
  if(String.fromCharCode(...bytes.slice(4,8))==='ftyp')return 'video/mp4';
  throw new Error('只接受实际PNG、JPEG、WebP或MP4文件，不接受SVG/网页');
 }
 return {validateAsset,validateState,validateBundle,renderPrompt,mimeFromBytes,MAX_FILE,MAX_TOTAL,MAX_JSON};
});
