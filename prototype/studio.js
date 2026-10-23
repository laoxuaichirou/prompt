'use strict';
(function(){
 const q=s=>document.querySelector(s),SM=StudioModel,L=CreatorLibrary,C=CreatorCanvas;
 const html=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const status=(s,error=false)=>{q('#workspace-status').textContent=s;q('#workspace-status').classList.toggle('error',error);};
 let state=SM.validateState({assets:[],decisions:{}}),db=null,volatile=false,writeQueue=Promise.resolve(),activeTab='canvas';
 const samples=[
  {id:'IMG-EC-01',name:'电商 · 保温杯白底主图',image:'../artifacts/IMG-EC-01.png'},
  {id:'IMG-FILM-03',name:'影视 · 气象站关键帧',image:'../artifacts/IMG-FILM-03.png'},
  {id:'IMG-FILM-08',name:'自媒体 · 文件夹插画',image:'../artifacts/IMG-FILM-08.png'}
 ];
 const clone=x=>JSON.parse(JSON.stringify(x));
 async function openStore(){
  return new Promise((resolve,reject)=>{
   const req=indexedDB.open('creator-desk-studio-v2',1);
   req.onupgradeneeded=()=>req.result.createObjectStore('workspace');
   req.onerror=()=>reject(req.error);req.onblocked=()=>reject(new Error('请关闭其他旧版本工作台页面后刷新'));
   req.onsuccess=()=>resolve(req.result);
  });
 }
 async function readStore(){return new Promise((resolve,reject)=>{const t=db.transaction('workspace');const r=t.objectStore('workspace').get('current');r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);});}
 async function persist(){
  if(!db){volatile=true;status('本机素材存储不可用，当前修改只在内存中；关闭前请导出工程。',true);return;}
  const snapshot=clone(state);
  const job=writeQueue.catch(()=>{}).then(()=>new Promise((resolve,reject)=>{
   const t=db.transaction('workspace','readwrite');t.objectStore('workspace').put(snapshot,'current');
   t.oncomplete=resolve;t.onerror=()=>reject(t.error);t.onabort=()=>reject(t.error||new Error('存储事务中断'));
  }));
  writeQueue=job;
  try{await job;volatile=false;status('工作区已保存在本机 · 上传素材不离开浏览器 · 生图服务尚未接入');}
  catch(e){volatile=true;status('本机保存失败，当前修改仅在内存中；请立即导出工程备份。',true);}
 }
 const ready=(async()=>{
  try{db=await openStore();const stored=await readStore();if(stored)state=SM.validateState(stored);status('工作区已保存在本机 · 上传素材不离开浏览器 · 生图服务尚未接入');}
  catch(e){db?.close();db=null;volatile=true;status('本机素材存储不可用或旧数据异常；原数据未覆盖，请导出当前工程备份。',true);}
  promptVars=state.promptDrafts;for(const m of motions){if(state.motionDrafts[m.id])drafts[m.id]={...clone(m.props),...state.motionDrafts[m.id]};}renderAssets();promptList();compare();motionEditor();C.refresh();
 })();
 function showTab(name){
  activeTab=name;
  document.querySelectorAll('[data-panel]').forEach(p=>p.hidden=p.dataset.panel!==name);
  document.querySelectorAll('[data-tab]').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.tab===name)));
  if(name==='canvas')C.fit();
  if(name==='compare')compare();
  document.querySelectorAll('[data-panel] video').forEach(v=>{if(v.closest('[data-panel]').dataset.panel!==name)v.pause();});
  if(name!=='motion')q('#motion-preview').pause();
 }
 document.querySelectorAll('[data-tab]').forEach(b=>b.onclick=()=>showTab(b.dataset.tab));
 function addToCanvas(spec){C.add(spec);showTab('canvas');toast('已加入画布，可连接上游引用');}
 async function hash(bytes){const d=await crypto.subtle.digest('SHA-256',bytes);return Array.from(new Uint8Array(d),v=>v.toString(16).padStart(2,'0')).join('');}
 async function verifyBytes(a){
  const res=await fetch(a.dataURL),bytes=new Uint8Array(await res.arrayBuffer());
  if(bytes.length!==a.bytes||SM.mimeFromBytes(bytes)!==a.mime||await hash(bytes)!==a.sha256)throw new Error('素材内容与校验信息不符：'+a.name);
 }
 function dataURL(file){return new Promise((resolve,reject)=>{const f=new FileReader();f.onload=()=>resolve(f.result);f.onerror=()=>reject(f.error);f.readAsDataURL(file);});}
 async function upload(files){
  await ready;
  q('#upload-assets').disabled=true;
  let added=0;const failures=[];
  for(const file of files){
   try{
    if(file.size>SM.MAX_FILE||!file.size)throw new Error('文件为空或超过20MB');
    const bytes=new Uint8Array(await file.arrayBuffer()),mime=SM.mimeFromBytes(bytes),sha256=await hash(bytes);
    const a=SM.validateAsset({id:'asset-'+sha256.slice(0,24),name:file.name.slice(0,180),mime,bytes:file.size,sha256,dataURL:await dataURL(file)});
    if(state.assets.some(x=>x.sha256===sha256))continue;
    const next=SM.validateState({...state,assets:[...state.assets,a]});state=next;added++;
   }catch(e){failures.push(file.name+'：'+e.message);}
  }
  if(added)await persist();
  renderAssets();q('#upload-assets').disabled=false;
  toast(failures.length?'已加入'+added+'份；'+failures.join('；'):'已加入'+added+'份素材，重复文件已跳过');
 }
 q('#upload-assets').onclick=()=>q('#asset-file').click();
 q('#asset-file').onchange=async e=>{try{await upload(Array.from(e.target.files));}catch(err){toast(err.message);}finally{e.target.value='';}};
 const drop=q('#drop-zone');drop.onclick=()=>q('#asset-file').click();drop.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();q('#asset-file').click();}};
 drop.ondragover=e=>{e.preventDefault();drop.classList.add('dragover');};drop.ondragleave=()=>drop.classList.remove('dragover');
 drop.ondrop=async e=>{e.preventDefault();drop.classList.remove('dragover');try{await upload(Array.from(e.dataTransfer.files));}catch(err){toast(err.message);}};
 function renderAssets(){
  q('#asset-badge').textContent=state.assets.length+samples.length;
  q('#asset-list').innerHTML=samples.map(s=>'<article class="asset-card"><img src="'+s.image+'" alt="'+s.name+'"><span class="asset-tag">已实际生图 / 虚构素材</span><h3>'+s.name+'</h3><p>'+s.id+' · 真实商品需另上传实拍</p><div class="row-actions"><button data-sample="'+s.id+'">加入画布</button><a href="'+s.image+'" download>下载原图</a></div></article>').join('')+
   state.assets.map(a=>'<article class="asset-card" data-asset="'+a.id+'">'+(a.mime==='video/mp4'?'<video controls preload="metadata" playsinline src="'+a.dataURL+'"></video>':'<img src="'+a.dataURL+'" alt="'+html(a.name)+'">')+'<span class="asset-tag">本机上传</span><h3>'+html(a.name)+'</h3><p>'+a.mime+' · '+(a.bytes/1024/1024).toFixed(2)+' MB<br>SHA256 '+a.sha256.slice(0,16)+'…</p><div class="row-actions"><button data-asset-add="'+a.id+'">加入画布</button><a download="'+html(a.name)+'" href="'+a.dataURL+'">下载</a><button class="danger" data-asset-delete="'+a.id+'">移除</button></div></article>').join('');
  document.querySelectorAll('[data-sample]').forEach(b=>b.onclick=()=>{const s=samples.find(x=>x.id===b.dataset.sample);addToCanvas({type:'image',title:s.name,content:'已实际生成样例：'+s.id+'。正式商品与人物需人工验收。',image:s.image});});
  document.querySelectorAll('[data-asset-add]').forEach(b=>b.onclick=()=>{const a=state.assets.find(x=>x.id===b.dataset.assetAdd);try{addToCanvas({type:a.mime==='video/mp4'?'video':'image',title:a.name,content:'本机素材 · SHA256 '+a.sha256,assetId:a.id});}catch(e){toast(e.message);}});
  document.querySelectorAll('[data-asset-delete]').forEach(b=>b.onclick=async()=>{
   if(C.usesAsset(b.dataset.assetDelete)){toast('画布或撤销历史仍引用这份素材，暂不能移除；可先切换模板并重新载入页面清除历史。');return;}if([state.customCompare.left,state.customCompare.right].includes(b.dataset.assetDelete)){toast('自定义对比仍引用这份素材，请先换成其他图片。');return;}state.assets=state.assets.filter(a=>a.id!==b.dataset.assetDelete);await persist();renderAssets();toast('素材已移除');
  });
 }
 // Prompt library
 q('#skill-list').innerHTML=L.skills.map(s=>'<article class="asset-card"><h3>'+html(s.title)+'</h3><p>'+html(s.description)+'</p><div class="row-actions"><a href="../'+s.path+'" target="_blank">阅读Skill原文</a><button data-skill="'+s.id+'">加入画布</button></div></article>').join('');
 document.querySelectorAll('[data-skill]').forEach(b=>b.onclick=()=>{const s=L.skills.find(x=>x.id===b.dataset.skill);try{addToCanvas({type:'text',title:'Skill · '+s.title,content:s.text});}catch(e){toast(e.message);}});
 const categories={ecommerce:'电商',film:'影视',social:'自媒体',longform:'长视频',motion:'动效',production:'制作',remotion:'Remotion',chapter:'章节卡',comparison:'数据对照',contrast:'前后对照',kinetic:'关键词动效',overlay:'口播叠加',product:'商品展示',steps:'步骤流程',timeline:'时间线'};
 const allCategories=[...new Set(L.prompts.map(p=>p.category))];
 q('#prompt-category').innerHTML+=[...allCategories].map(c=>'<option value="'+html(c)+'">'+html(categories[c]||c)+'</option>').join('');
 const variableNames={"action":"动作","adult_age":"成年角色年龄","adult_character":"成年角色描述","after":"变化后","ambience":"环境氛围","asset_manifest":"素材清单","audio_plan":"声音计划","background":"背景","beat":"节奏节点","before":"变化前","bible":"资产设定规范","brief":"创作需求","camera":"运镜","chapter":"章节","character":"角色描述","character_ref":"角色参考图说明","clip_ref":"片段参考说明","concept":"创意概念","constraints":"固定约束","data":"示例数据","detail":"工艺细节","duration_seconds":"时长（秒）","elements":"画面元素","emotion":"情绪","end_pose_ref":"结束姿态参考","end_state":"结束状态","environment_motion":"环境运动","expected":"预期结果","eyeline":"视线方向","feature":"展示特征","festival":"节日主题","host_bbox":"口播人物占位区域","image_ref":"图片参考说明","last_frame_ref":"上一镜尾帧参考","layout":"版式","lens":"镜头焦段","lighting":"光线","location":"地点","materials":"材质","metaphor":"视觉比喻","motion":"运动方式","object":"物体","observations":"观察记录","observed":"实际结果","one_action":"唯一动作","one_variable":"唯一变化项","ongoing_action":"连续动作","palette":"配色","point":"核心观点","position":"位置","previous_shot_id":"上一镜头编号","product":"商品描述","product_ref":"商品参考图说明","prop":"道具","prop_ref":"道具参考图说明","reverse_shot":"反打镜头","scene":"场景","scene_ref":"场景参考说明","screen_direction":"画面运动方向","script":"脚本","series":"系列主题","series_style":"系列风格","shot_id":"镜头编号","shot_manifest":"镜头素材清单","shotlist":"分镜表","single_variable":"唯一变化项","sku":"商品规格","source":"数据来源","state":"当前状态","steps":"步骤","style":"风格","style_bible":"风格设定规范","subject":"主体","subtitle":"字幕文案","subtle_motion":"细微动作","time_weather":"时间与天气","timings":"时间节点","title":"标题","topic":"主题","verified_claim":"已核实卖点","verified_feature":"已核实特征","verified_specs":"已核实规格","visual_action":"画面动作","visual_style":"画面风格","voiceover_sentence":"口播原句"};
 let promptId=L.prompts[0].id,promptVars={};
 let draftTimer;function saveDrafts(){clearTimeout(draftTimer);draftTimer=setTimeout(()=>persist(),350);}
 function promptList(){
  const search=q('#prompt-search').value.trim().toLowerCase(),kind=q('#prompt-kind').value,category=q('#prompt-category').value;
  const items=L.prompts.filter(p=>(!kind||p.kind===kind)&&(!category||p.category===category)&&(!search||(p.id+' '+p.title+' '+p.prompt).toLowerCase().includes(search)));
  q('#prompt-count').textContent=items.length+'条模板';
  if(items.length&&!items.some(p=>p.id===promptId))promptId=items[0].id;
  q('#prompt-list').innerHTML=items.length?items.map(p=>'<button data-prompt="'+p.id+'" class="'+(p.id===promptId?'active':'')+'"><small>'+p.id+' · '+html(categories[p.category]||p.category)+'</small><strong>'+html(p.title)+'</strong></button>').join(''):'<p class="empty-state">没有匹配模板，试试清空筛选。</p>';
  document.querySelectorAll('[data-prompt]').forEach(b=>b.onclick=()=>{promptId=b.dataset.prompt;promptList();});
  promptEditor(items.length>0);
 }
 function promptEditor(hasItems){
  if(!hasItems){q('#prompt-editor').innerHTML='<p class="empty-state">请选择其他筛选条件。</p>';return;}
  const p=L.prompts.find(x=>x.id===promptId),vars=promptVars[p.id]||(promptVars[p.id]={});
  q('#prompt-editor').innerHTML='<p class="eyebrow">'+p.id+'</p><h2>'+html(p.title)+'</h2><p class="editor-note">'+html(p.reference_policy)+'</p>'+p.variables.map(v=>'<label>'+html(variableNames[v]||v)+'<input class="field" data-variable="'+v+'" maxlength="1000" placeholder="填写 '+html(variableNames[v]||v)+'" value="'+html(vars[v]||'')+'"></label>').join('')+'<label for="prompt-output">完整提示词</label><textarea id="prompt-output" class="prompt-output" readonly></textarea><p id="prompt-error" class="editor-error"></p><div class="row-actions"><button id="prompt-copy">复制提示词</button><button id="prompt-download">下载文本</button><button id="prompt-add" class="primary">加入画布</button></div><p class="editor-note">验收：'+p.acceptance.map(html).join('；')+'</p><p class="editor-note">'+html(p.model_notes)+'</p>';
  document.querySelectorAll('[data-variable]').forEach(input=>input.oninput=()=>{vars[input.dataset.variable]=input.value;state.promptDrafts=promptVars;saveDrafts();updateOutput();});
  function updateOutput(){try{q('#prompt-output').value=SM.renderPrompt(p,vars);q('#prompt-error').textContent='';}catch(e){q('#prompt-output').value=p.prompt;q('#prompt-error').textContent=e.message;}for(const id of ['#prompt-copy','#prompt-download','#prompt-add'])q(id).disabled=!!q('#prompt-error').textContent;}
  updateOutput();
  q('#prompt-copy').onclick=async()=>{try{await navigator.clipboard.writeText(q('#prompt-output').value);toast('提示词已复制');}catch(e){q('#prompt-output').select();toast('浏览器未开放剪贴板，请手动复制已选文本');}};
  q('#prompt-download').onclick=()=>downloadBlob(new Blob([q('#prompt-output').value],{type:'text/plain;charset=utf-8'}),p.id+'.txt');
  q('#prompt-add').onclick=()=>{try{addToCanvas({type:'text',title:p.id+' · '+p.title,content:SM.renderPrompt(p,vars),promptId:p.id});}catch(e){toast(e.message);}};
 }
 ['#prompt-search','#prompt-kind','#prompt-category'].forEach(s=>q(s).addEventListener(s==='#prompt-search'?'input':'change',promptList));
 // A/B review: reviewer choices never rewrite the original evidence.
 q('#compare-case').innerHTML='<option value="custom">我的素材 · 自定义对比</option>'+L.cases.map(c=>'<option value="'+c.id+'">'+html(c.title)+'</option>').join('');
 q('#compare-case').value='AB01';
 let native=false;
 function imageOptions(){return [...samples.map(s=>({id:'sample:'+s.id,name:s.name,src:s.image})),...state.assets.filter(a=>a.mime!=='video/mp4').map(a=>({id:a.id,name:a.name,src:a.dataURL}))];}
 function customCompare(){
  const d=state.customCompare,options=imageOptions(),labels={A:'选A',B:'选B',neither:'两者都不采用',pending:'待评审'};
  const optionHTML=current=>options.map(o=>'<option value="'+o.id+'" '+(o.id===current?'selected':'')+'>'+html(o.name)+'</option>').join('');
  q('#compare-content').className='backdrop-'+q('#compare-backdrop').value+(native?' native':'');
  q('#compare-content').innerHTML='<div class="compare-grid">'+['left','right'].map((side,i)=>{const o=options.find(x=>x.id===d[side]);return '<article class="compare-variant"><label>版本 '+(i?'B':'A')+'<select class="field" data-custom-side="'+side+'">'+optionHTML(d[side])+'</select></label><div class="image-viewport"><img src="'+o.src+'" alt="自定义版本 '+(i?'B':'A')+'"></div></article>';}).join('')+'</div><div class="review-card"><h2>我的素材版本对比</h2><p>选择任意两份图片；此处记录个人判断，不会新增或覆盖原始生图实测结论。换素材后选择会重置为待评审。</p><div class="review-controls">'+Object.entries(labels).map(([id,label])=>'<button data-custom-choice="'+id+'" aria-pressed="'+(d.choice===id)+'">'+label+'</button>').join('')+'</div><label>评审备注<textarea id="custom-note" maxlength="2000">'+html(d.note)+'</textarea></label><button id="custom-apply" '+(!['A','B'].includes(d.choice)?'disabled':'')+'>将选中版本加入画布</button></div>';
  document.querySelectorAll('[data-custom-side]').forEach(el=>el.onchange=async()=>{state.customCompare={...state.customCompare,[el.dataset.customSide]:el.value,choice:'pending',note:''};await persist();customCompare();});
  document.querySelectorAll('[data-custom-choice]').forEach(b=>b.onclick=async()=>{state.customCompare={...state.customCompare,choice:b.dataset.customChoice};await persist();customCompare();});
  q('#custom-note').oninput=()=>{state.customCompare.note=q('#custom-note').value;saveDrafts();};
  q('#custom-apply').onclick=()=>{const ref=d.choice==='A'?d.left:d.right,o=options.find(x=>x.id===ref);try{addToCanvas({type:'image',title:'我的版本 '+d.choice+' · '+o.name,content:d.note||'自定义素材评审选择',...(ref.startsWith('sample:')?{image:o.src}:{assetId:ref})});}catch(e){toast(e.message);}};
 }
 function compare(){
  if(q('#compare-case').value==='custom'){customCompare();return;}
  const c=L.cases.find(x=>x.id===q('#compare-case').value),r=L.reviews.find(x=>x.id===c.id),decision=state.decisions[c.id]||{choice:'pending',note:''};
  const labels={A:'选A',B:'选B',neither:'两者都不采用',pending:'待评审'};
  q('#compare-content').className='backdrop-'+q('#compare-backdrop').value+(native?' native':'');
  q('#compare-content').innerHTML='<div class="compare-grid">'+c.variants.map(v=>'<article class="compare-variant"><h3>'+v.label+' / '+html(v.variable_value)+'</h3><div class="image-viewport"><img src="../'+v.expected_output+'" alt="'+html(c.title+' '+v.label)+'"></div><div class="row-actions"><a href="../'+v.expected_output+'" download>下载原图</a><button data-compare-add="'+v.label+'">加入画布</button></div></article>').join('')+'</div><div class="review-card"><p class="eyebrow">原始实测评审 / '+html(r.status)+'</p><h2>'+html(r.summary)+'</h2><ul>'+r.limitations.map(s=>'<li>'+html(s)+'</li>').join('')+'<p>'+html(r.recommendation)+'</p><div class="decision-detail"><strong>我的选择</strong><div class="review-controls">'+Object.entries(labels).map(([id,label])=>'<button data-choice="'+id+'" aria-pressed="'+(decision.choice===id)+'">'+label+'</button>').join('')+'</div><label for="review-note">评审备注（自动保存，随工程导出）</label><textarea id="review-note" maxlength="2000" placeholder="如：白底用于主图；暖灰用于广告">'+html(decision.note)+'</textarea><p id="review-save" role="status">'+(state.decisions[c.id]?'已记录 · '+labels[decision.choice]:'尚未记录选择')+'</p><button id="apply-choice" '+(!['A','B'].includes(decision.choice)?'disabled':'')+'>将选中版本加入画布</button></div></div>';
  document.querySelectorAll('[data-choice]').forEach(b=>b.onclick=async()=>{state.decisions[c.id]={choice:b.dataset.choice,note:q('#review-note').value};await persist();compare();});
  q('#review-note').oninput=()=>{const d=state.decisions[c.id]||{choice:'pending',note:''};state.decisions[c.id]={...d,note:q('#review-note').value};q('#review-save').textContent='正在保存…';clearTimeout(compare.timer);compare.timer=setTimeout(async()=>{await persist();if(q('#compare-case').value===c.id)q('#review-save').textContent=volatile?'仅保留内存，请导出备份':'已保存在本机';},250);};
  const apply=label=>{const v=c.variants.find(x=>x.label===label);try{addToCanvas({type:'image',title:c.id+'-'+label+' · '+c.title,content:r.summary+'\n人工选择不等于原始实验通过。',image:'../'+v.expected_output});}catch(e){toast(e.message);}};
  document.querySelectorAll('[data-compare-add]').forEach(b=>b.onclick=()=>apply(b.dataset.compareAdd));q('#apply-choice').onclick=()=>apply(state.decisions[c.id].choice);
 }
 q('#compare-case').onchange=compare;q('#compare-backdrop').onchange=()=>{q('#compare-content').className='backdrop-'+q('#compare-backdrop').value+(native?' native':'');};
 q('#compare-native').onclick=()=>{native=!native;q('#compare-native').setAttribute('aria-pressed',String(native));q('#compare-content').classList.toggle('native',native);};
 // Actual rendered videos and editable, Remotion-compatible props.
 const motions=[
  {id:'KineticWords',name:'关键词动效',seconds:6,file:'../artifacts/remotion-kinetic.mp4',props:{title:'把创作留在一张桌上',words:['少搬运','先定稿','再生成'],footer:'素材只准备一次，\n每个镜头都能复用。'}},
  {id:'ProcessSteps',name:'三步流程',seconds:8,file:'../artifacts/remotion-steps.mp4',props:{title:'先跑通，再加量',steps:['写清需求','锁定素材','逐镜生产'],descriptions:['明确任务、比例和时长','角色、商品、场景先定稿','只改一个变量，确认后批量']}},
  {id:'DataComparison',name:'数据对照',seconds:6,file:'../artifacts/remotion-comparison.mp4',props:{title:'少一次搬运，多一点创作',labels:['手动往返示意','引用复用示意'],values:[8,3],unit:'步',source:'用于说明图表组件的虚构示例'}}
 ];
 let motion=motions[0],service=false,rendering=false,renderedAsset=null,renderedProps=null;
 const drafts=Object.fromEntries(motions.map(m=>[m.id,clone(m.props)]));
 function motionEditor(){
  q('#motion-templates').innerHTML=motions.map(m=>'<button data-motion="'+m.id+'" class="'+(m.id===motion.id?'active':'')+'">'+m.name+'</button>').join('');
  q('#motion-preview').poster='../artifacts/frames/'+({KineticWords:'kinetic',ProcessSteps:'steps',DataComparison:'comparison'})[motion.id]+'-middle.png';q('#motion-preview').src=motion.file;q('#motion-download').href=motion.file;q('#motion-download').download=motion.id+'.mp4';renderedAsset=null;
  q('#motion-caption').textContent=motion.seconds+'秒 · 1080×1920 · 30fps · H.264 · 静音 · 原始已渲染样片';
  q('#render-status').textContent='';
  const props=drafts[motion.id];
  q('#motion-fields').innerHTML='<h2>'+motion.name+'文案</h2>'+Object.entries(props).map(([k,v])=>'<label>'+html(({title:'标题',words:'三个关键词（每行一个）',footer:'补充文案',steps:'三个步骤（每行一个）',descriptions:'三条说明（每行一条）',labels:'两个数据标签（每行一个）',values:'两个示例数值（每行一个）',unit:'单位',source:'数据来源'})[k])+'<textarea data-motion-field="'+k+'" maxlength="1000">'+html(Array.isArray(v)?v.join('\n'):v)+'</textarea></label>').join('');
  document.querySelectorAll('[data-motion]').forEach(b=>b.onclick=()=>{if(rendering){toast('请等待当前渲染完成');return;}motion=motions.find(m=>m.id===b.dataset.motion);motionEditor();});
  document.querySelectorAll('[data-motion-field]').forEach(el=>el.oninput=()=>{const original=motion.props[el.dataset.motionField];const value=el.value.trim();drafts[motion.id][el.dataset.motionField]=Array.isArray(original)?value.split('\n').map(x=>el.dataset.motionField==='values'?Number(x):x.trim()):value;state.motionDrafts=clone(drafts);saveDrafts();q('#render-status').textContent='文案已修改，上方视频仍是上次渲染结果。';});
 }
 function currentProps(){
  const p=clone(drafts[motion.id]);const string=(v,n)=>{if(typeof v!=='string'||!v.trim()||v.length>n)throw new Error('文案不能为空，且需符合长度限制（'+n+'字）');};
  const list=(xs,n,max)=>{if(!Array.isArray(xs)||xs.length!==n)throw new Error('请提供'+n+'行');xs.forEach(x=>string(x,max));};
  string(p.title,16);
  if(motion.id==='KineticWords'){list(p.words,3,8);string(p.footer,24);}
  if(motion.id==='ProcessSteps'){list(p.steps,3,10);list(p.descriptions,3,22);}
  if(motion.id==='DataComparison'){list(p.labels,2,12);string(p.unit,6);string(p.source,40);if(p.values.length!==2||p.values.some(v=>!Number.isFinite(v)||v<0||v>1000000))throw new Error('请填写两个0到1000000之间的数值');}
  return p;
 }
 q('#motion-props').onclick=()=>{try{downloadJSON(currentProps(),motion.id+'-props.json');toast('参数已导出，在Remotion工程中重新渲染即可');}catch(e){toast(e.message);}};
 q('#motion-add').onclick=async()=>{try{
  if(renderedAsset)addToCanvas({type:'motion',title:motion.name+' · 自定义渲染',content:JSON.stringify(renderedProps,null,2),assetId:renderedAsset.id});
  else addToCanvas({type:'motion',title:motion.name+' · 已渲染样片',content:motion.seconds+'秒 · 1080×1920 · 静音。\n此卡片引用原始样片，修改文案需重新渲染。',media:motion.file});
 }catch(e){toast(e.message);}};
 async function detectService(){
  try{const r=await fetch('/api/status',{signal:AbortSignal.timeout(3000)});if(!r.ok)throw new Error();const s=await r.json();service=s.service==='creator-desk-local'&&s.render_ready;q('#render-service').textContent=service?'本机Remotion服务已连接':'本机服务已连接，需先安装Remotion依赖';}
  catch(e){q('#render-service').textContent='静态预览 · 下载参数可交给Hermes渲染';}
  q('#motion-render').disabled=!service;
 }
 q('#motion-render').onclick=async()=>{
  if(rendering)return;
  let props;try{props=currentProps();}catch(e){toast(e.message);return;}
  rendering=true;q('#motion-render').disabled=true;
  const captured=motion;
  try{
   q('#render-status').textContent='正在提交本机渲染任务…';
   const response=await fetch('/api/render',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({composition:captured.id,props})});
   const job=await response.json();if(!response.ok)throw new Error(job.error||'渲染提交失败');
   let result;
   for(let attempt=0;attempt<180;attempt++){
    await new Promise(resolve=>setTimeout(resolve,1000));
    const r=await fetch('/api/jobs/'+job.id);result=await r.json();if(!r.ok)throw new Error(result.error||'无法读取渲染状态');
    q('#render-status').textContent='本机渲染中 · '+(attempt+1)+'秒';
    if(result.status==='failed')throw new Error(result.error||'渲染失败');
    if(result.status==='completed')break;
   }
   if(result.status!=='completed')throw new Error('等待超时；本机任务可能仍在执行，可检查服务日志');
   q('#motion-preview').removeAttribute('poster');q('#motion-preview').src=result.url;q('#motion-download').href=result.url;
   q('#motion-caption').textContent='自定义文案已实际渲染 · '+captured.seconds+'秒 · 1080×1920 · 30fps · H.264 · 静音';
   const responseVideo=await fetch(result.url);if(!responseVideo.ok)throw new Error('MP4读取失败');
   const blob=await responseVideo.blob(),bytes=new Uint8Array(await blob.arrayBuffer()),sha256=await hash(bytes);
   const a=SM.validateAsset({id:'asset-'+sha256.slice(0,24),name:captured.id+'-custom.mp4',mime:'video/mp4',bytes:bytes.length,sha256,dataURL:await dataURL(blob)});
   if(!state.assets.some(x=>x.id===a.id)){state=SM.validateState({...state,assets:[...state.assets,a]});await persist();}
   renderedAsset=a;renderedProps=props;renderAssets();q('#render-status').textContent='渲染完成，MP4已加入本机素材库，可下载或加入画布。';
  }catch(e){q('#render-status').textContent='未完成：'+e.message+'。可下载参数后本机重试。';}
  finally{rendering=false;q('#motion-render').disabled=!service;}
 };
 function downloadBlob(blob,name){const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),3000);}
 window.CreatorStudio={
  ready,
  getAsset:id=>state.assets.find(a=>a.id===id),
  async exportProject(graph){
   await ready;
   // Pending note edits are already in memory; no debounce can lose them in this snapshot.
   return SM.validateBundle({format:'creator-desk-studio',version:2,graph,workspace:clone(state)});
  },
  async importProject(input){
   await ready;
   if(input.format!=='creator-desk-studio'){
    const graph=CanvasModel.validate(input);
    if(graph.nodes.some(n=>n.assetId))throw new Error('带上传素材的工程必须使用完整工作区格式');
    return graph;
   }
   const bundle=SM.validateBundle(input);
   for(const a of bundle.workspace.assets)await verifyBytes(a);
   // Merge previous assets so undo/redo keeps media available; reject before mutation on overflow.
   const merged=new Map(state.assets.map(a=>[a.id,a]));
   for(const a of bundle.workspace.assets)merged.set(a.id,a);
   const next=SM.validateState({...bundle.workspace,assets:[...merged.values()]});
   state=next;promptVars=state.promptDrafts;for(const m of motions)drafts[m.id]={...clone(m.props),...state.motionDrafts[m.id]};await persist();renderAssets();promptList();compare();motionEditor();return bundle.graph;
  },
  showTab,
  snapshot:()=>clone(state)
 };
 promptList();compare();motionEditor();detectService();
})();
