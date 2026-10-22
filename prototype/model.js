/* Original canvas data model: browser + Node, no external dependencies. */
(function(root,factory){const m=factory();if(typeof module==='object'&&module.exports)module.exports=m;else root.CanvasModel=m;})(typeof globalThis!=='undefined'?globalThis:this,()=>{
 const kinds=['text','image','video','motion'];
 const clone=x=>JSON.parse(JSON.stringify(x));
 function canConnect(g,source,target){
  if(source===target)return '不能引用自身';
  const a=g.nodes.find(n=>n.id===source),b=g.nodes.find(n=>n.id===target);
  if(!a||!b)return '缺少节点';
  if(b.type==='text'||(a.type==='video'&&b.type!=='motion')||(a.type==='motion'&&b.type!=='motion'))return '节点输入类型不兼容';
  if(g.edges.some(e=>e.source===source&&e.target===target))return '已有这条引用';
  const seen=new Set();function reaches(id){if(id===source)return true;if(seen.has(id))return false;seen.add(id);return g.edges.filter(e=>e.source===id).some(e=>reaches(e.target));}
  if(reaches(target))return '引用会形成循环';return null;
 }
 function validate(g){
  if(!g||g.version!==1||typeof g.title!=='string'||g.title.length>100||!Array.isArray(g.nodes)||!Array.isArray(g.edges)||g.nodes.length>200||g.edges.length>1000)throw new Error('工程格式或大小不符合要求');
  const ids=new Set();
  const clean={version:1,title:g.title,template:['ecommerce','film','longform','motion'].includes(g.template)?g.template:'ecommerce',nodes:[],edges:[]};
  for(const n of g.nodes){
   if(!n||typeof n.id!=='string'||!/^[A-Za-z0-9_-]{1,80}$/.test(n.id)||ids.has(n.id)||!kinds.includes(n.type)||typeof n.title!=='string'||n.title.length>100||typeof n.content!=='string'||n.content.length>10000||!Number.isFinite(n.x)||!Number.isFinite(n.y)||Math.abs(n.x)>10000||Math.abs(n.y)>10000)throw new Error('节点内容无效或ID重复');
   if(n.image&&!/^\.\.\/artifacts\/IMG-[A-Z0-9-]+\.png$/.test(n.image))throw new Error('原型只允许本地样例图片');
   ids.add(n.id);clean.nodes.push({id:n.id,type:n.type,title:n.title,content:n.content,x:n.x,y:n.y,...(n.image?{image:n.image}:{})});
  }
  for(const e of g.edges){if(!e||typeof e.source!=='string'||typeof e.target!=='string')throw new Error('连线格式无效');const err=canConnect(clean,e.source,e.target);if(err)throw new Error(err);clean.edges.push({source:e.source,target:e.target});}
  return clean;
 }
 return {clone,canConnect,validate,kinds};
});
