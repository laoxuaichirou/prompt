'use strict';
const $=s=>document.querySelector(s), M=CanvasModel, key='creator-desk-v1';
const titles={ecommerce:'一件商品，一套素材',film:'把一个镜头，先做对',longform:'长片，也从一个镜头开始',motion:'让口播，有画面可讲'};
const names={text:'TEXT / 需求',image:'IMAGE / 资产',video:'VIDEO / 镜头',motion:'MOTION / 动效'};
function template(kind){
 const shared={version:1,template:kind,title:{ecommerce:'我的商品素材',film:'山间气象站 · 镜头一',longform:'我的5分钟长视频',motion:'口播插入素材'}[kind]};
 const data={ecommerce:[['text','创作需求','为无品牌保温杯制作白底主图。\n1:1画幅，保留完整商品轮廓。\n先验证一张，再做场景套图。'],['image','商品定稿参考','本次真实生成样例 · IMG-EC-01\n正式商品任务需上传真实商品参考。','../artifacts/IMG-EC-01.png'],['image','场景图计划','保持商品外形与材质，加入自然光书桌场景。\n左侧留40%文案空间。\n待真实生成接口接入。']],film:[['text','单镜头分镜','成年女性维修员来到山间气象站。\n黎明冷光，窗内暖光。\n全景，向窗内看，一个动作。'],['image','影视关键帧','本次真实生成样例 · IMG-FILM-03\n角色、场景与光线在这里定稿。','../artifacts/IMG-FILM-03.png'],['video','5秒视频计划','引用关键帧，缓慢推近，人物保持姿态。\n声音后期补，禁止乱切。\n待视频供应商接入。']],longform:[['text','5分钟章节规划','目标300秒 · 30fps。\n60个5秒片段，按章节分组。\n先验收30秒试片，再批量生产。'],['image','场景与角色资产','每个场景复用同一套已批准资产。\n镜头表在 examples/longform-5min.json。','../artifacts/IMG-FILM-03.png'],['video','逐镜头生产计划','当前只展示一个代表镜头。\n队列、成本与连续性由生产服务管理。\n本原型没有生成5分钟影片。']],motion:[['text','口播内容','素材只准备一次，\n每个镜头都能引用。\n关键词：少搬运、先定稿、再生成。'],['image','口播插画资产','本次真实生成样例 · IMG-FILM-08\n真实文字由Remotion排版。','../artifacts/IMG-FILM-08.png'],['motion','Remotion动效','6秒关键词动效 · 已实际渲染MP4。\n在“口播动效”修改文案并本机重渲染。']]};
 return {...shared,nodes:data[kind].map((a,i)=>({id:'n'+(i+1),type:a[0],title:a[1],content:a[2],...(a[3]?{image:a[3]}:{}),...(kind==='motion'&&a[0]==='motion'?{media:'../artifacts/remotion-kinetic.mp4'}:{}),x:55+i*310,y:140})),edges:[{source:'n1',target:'n2'},{source:'n2',target:'n3'}]};
}
let graph=template('ecommerce'),selected='n1',past=[],future=[],pending=null,view={x:0,y:0,scale:1};
let storageWorks=true;
try{const s=localStorage.getItem(key);if(s)graph=M.validate(JSON.parse(s));}catch(e){storageWorks=false;}
selected=graph.nodes[0]?.id;
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function toast(s){$('#toast').textContent=s;$('#toast').style.display='block';clearTimeout(toast.timer);toast.timer=setTimeout(()=>$('#toast').style.display='none',3200);}
function save(){try{localStorage.setItem(key,JSON.stringify(graph));$('#save-state').textContent='已保存在本机';storageWorks=true;}catch(e){$('#save-state').textContent='保存失败，请导出备份';storageWorks=false;toast('本机存储不可用，请导出工程备份');}}
function checkpoint(){past.push(M.clone(graph));if(past.length>50)past.shift();future=[];}
function changed(){$('#plan-title').textContent='先锁定素材，再开始生产';$('#plan-detail').textContent='从素材库与提示词库加入卡片；在线生图尚未接入。';save();render();}
function edges(){const svg=$('#edges');svg.innerHTML='';for(const e of graph.edges){const a=graph.nodes.find(n=>n.id===e.source),b=graph.nodes.find(n=>n.id===e.target);if(!a||!b)continue;const p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('d',`M ${a.x+244} ${a.y+96} C ${a.x+285} ${a.y+96}, ${b.x-45} ${b.y+96}, ${b.x} ${b.y+96}`);p.setAttribute('stroke','#a2b6a2');p.setAttribute('stroke-width','2');p.setAttribute('fill','none');svg.append(p);}}
function transform(){$('#world').style.transform=`translate(${view.x}px,${view.y}px) scale(${view.scale})`;$('#zoom-value').textContent=Math.round(view.scale*100)+'%';}
function render(){
 $('#project-name').value=graph.title;$('#workflow-title').textContent=titles[graph.template];$('#node-count').textContent=`${graph.nodes.length}个节点 · ${graph.edges.length}条引用`;
 document.querySelectorAll('[data-template]').forEach(b=>b.classList.toggle('active',b.dataset.template===graph.template));
 $('#undo').disabled=!past.length;$('#redo').disabled=!future.length;
 $('#nodes').innerHTML=graph.nodes.map(n=>`<article class="node ${selected===n.id?'selected':''}" data-id="${n.id}" style="left:${n.x}px;top:${n.y}px"><div class="node-head"><div><span class="node-type">${names[n.type]}</span><strong>${esc(n.title)}</strong></div><span class="node-index">${esc(n.id.slice(-3))}</span></div><div class="node-body">${nodeMedia(n)}${esc(n.content)}<br><span class="status">${n.assetId?'● 本机上传素材':n.image||n.media?'● 已实测素材':'○ 可编辑计划'}</span></div>${n.type!=='text'?`<button class="port in" data-port="in" aria-label="${esc(n.title)} 输入端口"></button>`:''}<button class="port out ${pending===n.id?'pending':''}" data-port="out" aria-label="${esc(n.title)} 输出端口"></button></article>`).join('');
 document.querySelectorAll('.node').forEach(el=>{
  el.addEventListener('click',e=>{if(e.target.closest('.port,video,a'))return;selected=el.dataset.id;render();});
  el.querySelector('.node-head').addEventListener('pointerdown',e=>startNodeDrag(e,el));
  el.querySelectorAll('.port').forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();if(b.dataset.port==='out'){pending=el.dataset.id;toast('再点击下游卡片的输入端口');render();}else if(pending){const err=M.canConnect(graph,pending,el.dataset.id);if(err)toast(err);else{checkpoint();graph.edges.push({source:pending,target:el.dataset.id});pending=null;changed();toast('引用已连接');}}else toast('先点击上游卡片的输出端口');}));
 });
 edges();inspector();transform();
}
function inspector(){const n=graph.nodes.find(x=>x.id===selected);$('#selected-title').textContent=n?.title||'选择一张卡片';if(!n){$('#inspector').innerHTML='<p class="muted">点击卡片编辑；左侧可添加。</p>';return;}
 const refs=graph.nodes.filter(x=>x.id!==n.id&&(graph.edges.some(e=>e.source===x.id&&e.target===n.id)||!M.canConnect(graph,x.id,n.id)));
 $('#inspector').innerHTML=`<div><label for="node-title">卡片名称</label><input class="field" id="node-title" value="${esc(n.title)}" maxlength="100"></div><div><label for="node-content">需求 / 提示词 / 计划</label><textarea id="node-content" maxlength="10000">${esc(n.content)}</textarea></div><div><label>上游引用</label>${refs.length?refs.map(x=>`<label class="reference"><input type="checkbox" data-ref="${x.id}" ${graph.edges.some(e=>e.source===x.id&&e.target===n.id)?'checked':''}>${esc(x.title)}</label>`).join(''):'<p class="muted">此卡片不需要上游引用</p>'}</div><div class="inspector-actions"><button id="duplicate">复制卡片</button><button class="danger" id="delete">删除</button></div>`;
 $('#node-title').addEventListener('change',e=>{checkpoint();n.title=e.target.value||'未命名卡片';changed();});
 $('#node-content').addEventListener('change',e=>{checkpoint();n.content=e.target.value;changed();});
 document.querySelectorAll('[data-ref]').forEach(c=>c.addEventListener('change',()=>{if(c.checked){const err=M.canConnect(graph,c.dataset.ref,n.id);if(err){toast(err);c.checked=false;return;}}checkpoint();if(c.checked)graph.edges.push({source:c.dataset.ref,target:n.id});else graph.edges=graph.edges.filter(e=>!(e.source===c.dataset.ref&&e.target===n.id));changed();}));
 $('#delete').onclick=()=>{checkpoint();graph.nodes=graph.nodes.filter(x=>x.id!==n.id);graph.edges=graph.edges.filter(e=>e.source!==n.id&&e.target!==n.id);selected=graph.nodes[0]?.id;pending=null;changed();toast('卡片已删除，可撤销');};
 $('#duplicate').onclick=()=>{if(graph.nodes.length>=200){toast('原型最多200个节点');return;}checkpoint();const copy={...M.clone(n),id:uid(),title:n.title+' 副本',x:n.x+35,y:n.y+55};graph.nodes.push(copy);selected=copy.id;changed();};
}
function uid(){return 'n'+Date.now().toString(36)+Math.random().toString(36).slice(2,5);}
let drag=null;
function startNodeDrag(e,el){if(e.button!==0)return;e.preventDefault();e.stopPropagation();const n=graph.nodes.find(x=>x.id===el.dataset.id);selected=n.id;drag={node:n,startX:e.clientX,startY:e.clientY,x:n.x,y:n.y,moved:false,el,before:M.clone(graph)};}
window.addEventListener('pointermove',e=>{if(!drag)return;const dx=e.clientX-drag.startX,dy=e.clientY-drag.startY;if(Math.abs(dx)+Math.abs(dy)>3)drag.moved=true;if(drag.node){drag.node.x=drag.x+dx/view.scale;drag.node.y=drag.y+dy/view.scale;drag.el.style.left=drag.node.x+'px';drag.el.style.top=drag.node.y+'px';edges();}else{view.x=drag.x+dx;view.y=drag.y+dy;transform();}});
window.addEventListener('pointerup',()=>{if(!drag)return;if(drag.node&&drag.moved){past.push(drag.before);if(past.length>50)past.shift();future=[];save();}drag=null;render();});
$('#stage').addEventListener('pointerdown',e=>{if(e.button!==0||e.target.closest('.node,.zoom'))return;drag={startX:e.clientX,startY:e.clientY,x:view.x,y:view.y};});
function zoom(f,x,y){const next=Math.min(1.6,Math.max(.3,view.scale*f));view.x=x-(x-view.x)*next/view.scale;view.y=y-(y-view.y)*next/view.scale;view.scale=next;transform();}
$('#stage').addEventListener('wheel',e=>{e.preventDefault();const r=$('#stage').getBoundingClientRect();zoom(e.deltaY>0?.9:1.1,e.clientX-r.left,e.clientY-r.top);},{passive:false});
$('#zoom-in').onclick=()=>zoom(1.15,$('#stage').clientWidth/2,250);$('#zoom-out').onclick=()=>zoom(1/1.15,$('#stage').clientWidth/2,250);
function fit(){if(!graph.nodes.length){view={x:0,y:0,scale:1};transform();return;}const minX=Math.min(...graph.nodes.map(n=>n.x)),maxX=Math.max(...graph.nodes.map(n=>n.x+244)),minY=Math.min(...graph.nodes.map(n=>n.y)),maxY=Math.max(...graph.nodes.map(n=>n.y+360));const st=$('#stage');view.scale=Math.min(1.1,Math.max(.3,Math.min((st.clientWidth-75)/(maxX-minX),(st.clientHeight-95)/(maxY-minY))));view.x=(st.clientWidth-(maxX-minX)*view.scale)/2-minX*view.scale;view.y=55-minY*view.scale;transform();}
$('#fit').onclick=fit;
function undo(){if(!past.length)return;future.push(M.clone(graph));graph=past.pop();pending=null;selected=graph.nodes[0]?.id;changed();}
function redo(){if(!future.length)return;past.push(M.clone(graph));graph=future.pop();selected=graph.nodes[0]?.id;changed();}
$('#undo').onclick=undo;$('#redo').onclick=redo;
$('#arrange').onclick=()=>{checkpoint();graph.nodes.forEach((n,i)=>{n.x=55+(i%4)*310;n.y=100+Math.floor(i/4)*420;});changed();fit();};
$('#project-name').onchange=e=>{checkpoint();graph.title=e.target.value.slice(0,100)||'未命名工程';changed();};
document.querySelectorAll('[data-template]').forEach(b=>b.onclick=()=>{checkpoint();graph=template(b.dataset.template);selected='n1';pending=null;changed();fit();toast('模板已铺好；可撤销回到上一工程');});
document.querySelectorAll('[data-add]').forEach(b=>b.onclick=()=>{if(graph.nodes.length>=200){toast('原型最多200个节点');return;}checkpoint();const id=uid(),i=graph.nodes.length;graph.nodes.push({id,type:b.dataset.add,title:'新的'+names[b.dataset.add].split('/ ')[1],content:'写下需求，或连接上游素材。',x:55+(i%4)*310,y:100+Math.floor(i/4)*420});selected=id;changed();fit();});
$('#plan').onclick=()=>{const incoming=new Set(graph.edges.map(e=>e.target));const missing=graph.nodes.filter(n=>n.type!=='text'&&!incoming.has(n.id));$('#plan-title').textContent=missing.length?'有素材尚未连接':'引用结构检查完成 · 真实生成待接入';$('#plan-detail').textContent=missing.length?'请为这些卡片选择上游引用：'+missing.map(n=>n.title).join('、'):`${graph.nodes.length}个节点，${graph.edges.length}条引用，无循环。本原型只检查结构，尚未验证真实模型、参考资产或预算。`;toast(missing.length?'存在未连接卡片':'执行计划已检查，未提交生成任务');};
$('#export').onclick=async()=>{try{const data=window.CreatorStudio?await window.CreatorStudio.exportProject(graph):graph;downloadJSON(data,'creator-desk-project.json');toast('工程已导出；上传素材已打包');}catch(e){toast('导出失败：'+e.message);}};
$('#import').onclick=()=>$('#file').click();$('#file').onchange=async e=>{const file=e.target.files[0];if(!file)return;try{if(file.size>StudioModel.MAX_JSON)throw new Error('工程文件超过46MB');const data=JSON.parse(await file.text());const next=window.CreatorStudio?await window.CreatorStudio.importProject(data):M.validate(data);checkpoint();graph=next;selected=graph.nodes[0]?.id;pending=null;changed();fit();toast('工程已导入');}catch(err){toast('导入失败：'+err.message);}finally{e.target.value='';}};

window.addEventListener('keydown',e=>{if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)||document.querySelector('[data-panel="canvas"]').hidden)return;if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='z'){e.preventDefault();e.shiftKey?redo():undo();}if(e.key==='Escape'){pending=null;render();}});
window.addEventListener('resize',fit);render();fit();if(!storageWorks)toast('无法读取已保存工程，原记录未覆盖；请导出当前工作备份');


// Integration API: graph snapshots stay serializable; media bytes live in the workspace store.
function nodeMedia(n){
 const asset=n.assetId&&window.CreatorStudio?.getAsset(n.assetId);
 if(asset)return asset.mime==='video/mp4'?'<video src="'+esc(asset.dataURL)+'" controls preload="metadata" playsinline></video>':'<img src="'+esc(asset.dataURL)+'" alt="'+esc(n.title)+'">';
 if(n.assetId)return '<p class="editor-error">素材尚未载入或已缺失，请导入完整工作区备份。</p>';
 if(n.media)return '<video src="'+esc(n.media)+'" controls preload="metadata" playsinline></video>';
 return n.image?'<img src="'+esc(n.image)+'" alt="'+esc(n.title)+'">':'';
}
function downloadJSON(data,name){const url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),3000);}
window.CreatorCanvas={
 snapshot:()=>M.clone(graph),
 usesAsset:id=>[graph,...past,...future].some(g=>g.nodes.some(n=>n.assetId===id)),
 refresh:()=>render(),
 fit,
 add(spec){
  if(graph.nodes.length>=200)throw new Error('画布最多200个节点');
  const i=graph.nodes.length,node={id:uid(),type:spec.type,title:spec.title.slice(0,100),content:spec.content.slice(0,10000),x:55+(i%4)*310,y:100+Math.floor(i/4)*420,...spec};
  const trial=M.validate({...graph,nodes:[...graph.nodes,node]});
  checkpoint();graph=trial;selected=node.id;changed();fit();return node.id;
 }
};
