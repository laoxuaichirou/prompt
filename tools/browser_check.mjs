// Actual offline Chromium smoke test using only Node built-ins and Chrome CDP.
import {spawn} from 'node:child_process';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {createServer} from 'node:http';
const root=path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const temporary=await fs.mkdtemp('/tmp/directorx-ab-browser-');
const downloadDir=path.join(temporary,'downloads');await fs.mkdir(downloadDir);
const server=createServer(async(req,res)=>{
  try{const u=new URL(req.url,'http://127.0.0.1');const pathname=decodeURIComponent(u.pathname);const file=path.resolve(root,'.'+(pathname==='/'?'/review.html':pathname));
    if(!file.startsWith(root+path.sep)){res.writeHead(403);res.end();return;}
    if(pathname==='/favicon.ico'){res.writeHead(204);res.end();return;}
    const data=await fs.readFile(file);const mime={'.html':'text/html; charset=utf-8','.js':'application/javascript; charset=utf-8','.json':'application/json','.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp'}[path.extname(file)]||'application/octet-stream';res.writeHead(200,{'Content-Type':mime});res.end(data);
  }catch{res.writeHead(404);res.end('Not found');}
});
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
const origin='http://127.0.0.1:'+server.address().port;
const chrome=spawn('/usr/bin/chromium',['--headless','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--disable-background-networking','--disable-component-update','--no-first-run','--disable-sync','--disable-default-apps','--remote-debugging-address=127.0.0.1','--remote-debugging-port=0','--user-data-dir='+path.join(temporary,'profile'),'about:blank'],{stdio:['ignore','ignore','pipe']});
const wait=ms=>new Promise(r=>setTimeout(r,ms));
let endpoint='';chrome.stderr.on('data',b=>{const m=b.toString().match(/DevTools listening on (ws:\/\/[^\s]+)/);if(m)endpoint=m[1];});
class CDP{
  static async connect(url){const x=new CDP();x.socket=new WebSocket(url);x.pending=new Map();x.events=[];x.handlers=[];x.id=0;await new Promise((res,rej)=>{x.socket.addEventListener('open',res,{once:true});x.socket.addEventListener('error',rej,{once:true});});x.socket.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id){const p=x.pending.get(m.id);if(p){clearTimeout(p.timer);x.pending.delete(m.id);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result);}}else{x.events.push(m);for(const h of x.handlers)Promise.resolve(h(m)).catch(error=>x.events.push({method:'test.handlerError',params:{error:String(error)}}));}});return x;}
  send(method,params={}){const id=++this.id;return new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('CDP timeout '+method)),20000);this.pending.set(id,{resolve,reject,timer});this.socket.send(JSON.stringify({id,method,params}));});}
  close(){this.socket.close();}
}
let browser,page;
const checks=[];function check(name,ok,detail){checks.push({check:name,passed:!!ok,detail});if(!ok)throw Error('Failed '+name);}
try{
  for(let i=0;i<150&&!endpoint;i++)await wait(100);
  if(!endpoint)throw Error('Chromium did not expose a debugging endpoint');
  browser=await CDP.connect(endpoint);const version=await browser.send('Browser.getVersion');
  const {targetId}=await browser.send('Target.createTarget',{url:'about:blank'});
  const port=new URL(endpoint).port;const targets=await(await fetch('http://127.0.0.1:'+port+'/json/list')).json();
  page=await CDP.connect(targets.find(t=>t.id===targetId).webSocketDebuggerUrl);
  await page.send('Page.enable');await page.send('Runtime.enable');await page.send('Network.enable');
  page.handlers.push(async e=>{if(e.method==='Fetch.requestPaused'){const local=new URL(e.params.request.url).origin===origin;await page.send(local?'Fetch.continueRequest':'Fetch.failRequest',local?{requestId:e.params.requestId}:{requestId:e.params.requestId,errorReason:'BlockedByClient'});}});
  await page.send('Fetch.enable',{patterns:[{urlPattern:'http://*',requestStage:'Request'},{urlPattern:'https://*',requestStage:'Request'}]});
  await browser.send('Browser.setDownloadBehavior',{behavior:'allow',downloadPath:downloadDir});
  await page.send('Emulation.setDeviceMetricsOverride',{width:1440,height:1100,deviceScaleFactor:1,mobile:false});
  const navigation=await page.send('Page.navigate',{url:origin+'/review.html'});
  async function evaluate(expression){const r=await page.send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;}
  let loaded=false;
  for(let i=0;i<150;i++){loaded=await evaluate("document.querySelectorAll('article').length===27&&[...document.images].every(i=>i.complete&&i.naturalWidth>0)");if(loaded)break;await wait(100);}
  if(!loaded){const debug={navigation,state:await evaluate('({url:location.href,title:document.title,articles:document.querySelectorAll("article").length,images:document.images.length,body:document.body.innerText.slice(0,1800)})'),errors:page.events.filter(e=>e.method==='Runtime.exceptionThrown'||e.method==='Network.loadingFailed')};await fs.writeFile(path.join(root,'results/browser-debug.json'),JSON.stringify(debug,null,2)+'\n');}
  check('offline_page_and_54_thumbnails_load',loaded,await evaluate('({articles:document.querySelectorAll("article").length,images:document.images.length})'));
  const original=await evaluate('window.buildExport()');
  check('initial_27_ids_and_recommendations',original.items.length===27&&new Set(original.items.map(x=>x.asset_id)).size===27);
  await evaluate('document.querySelector(\'input[name="creative-preset-0"][value="B"]\').click()');
  const changed=await evaluate('window.buildExport().items[0]');
  const map=JSON.parse(await fs.readFile(path.join(root,'asset-map.json'),'utf8'));
  check('select_B_exports_corresponding_original_and_hash',changed.selected_version==='B'&&changed.master===map.items[0].versions.B.master&&changed.sha256===map.items[0].versions.B.sha256);
  await evaluate('document.querySelector(\'input[name="creative-preset-0"][value="neither"]\').click()');
  const rejected=await evaluate('window.buildExport().items[0]');
  check('reject_both_exports_null_paths_and_hash',rejected.selected_version===null&&rejected.master===null&&rejected.sha256===null);
  await evaluate('document.querySelector(\'input[name="creative-preset-0"][value="B"]\').click();document.getElementById("export").click()');
  const exported=path.join(downloadDir,'directorx-my-ab-selection.json');let bytes;
  for(let i=0;i<100;i++){try{bytes=await fs.readFile(exported);break;}catch{await wait(100);}}
  if(!bytes)throw Error('Browser export download missing');
  const downloaded=JSON.parse(bytes.toString());
  check('actual_browser_download_contains_27_selections',downloaded.items.length===27&&downloaded.items[0].selected_version==='B');
  for(const x of downloaded.items){if(x.master){const b=await fs.readFile(path.join(root,x.master));check('exported_hash_'+x.asset_id,createHash('sha256').update(b).digest('hex')===x.sha256);}else check('exported_missing_is_null_'+x.asset_id,x.selected_version===null&&x.sha256===null);}
  await evaluate('document.getElementById("reset").click()');
  const reset=await evaluate('window.buildExport()');
  check('reset_restores_every_original_recommendation',reset.items.every((x,i)=>x.selected_version===original.items[i].selected_version));
  const desktop=await page.send('Page.captureScreenshot',{format:'png'});await fs.writeFile(path.join(root,'reviews/review-desktop.png'),Buffer.from(desktop.data,'base64'));
  check('desktop_has_no_horizontal_overflow',await evaluate('document.documentElement.scrollWidth<=innerWidth'));
  await page.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await evaluate('window.scrollTo(0,0)');await wait(150);
  check('mobile_has_no_horizontal_overflow',await evaluate('document.documentElement.scrollWidth<=innerWidth'),await evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth})'));
  const mobile=await page.send('Page.captureScreenshot',{format:'png'});await fs.writeFile(path.join(root,'reviews/review-mobile.png'),Buffer.from(mobile.data,'base64'));
  const errors=page.events.filter(x=>x.method==='Runtime.exceptionThrown');
  check('no_javascript_exceptions',errors.length===0,errors);
  const external=page.events.filter(x=>x.method==='Network.requestWillBeSent'&&/^https?:/.test(x.params.request.url)&&new URL(x.params.request.url).origin!==origin);
  check('no_external_page_network_requests',external.length===0,external.map(x=>x.params.request.url));
  const report={executed_at_utc:new Date().toISOString(),browser:version.product,network_mode:'Temporary localhost static server; all non-origin HTTP(S) blocked by CDP',direct_file_url_test:'Blocked by managed Chromium administrator policy, retained in browser-file-url-block.json; no policy changes attempted',checks,passed:checks.every(x=>x.passed),export_download_sha256:createHash('sha256').update(bytes).digest('hex'),export_download_bytes:bytes.length};
  await fs.writeFile(path.join(root,'results/browser-validation.json'),JSON.stringify(report,null,2)+'\n');
  process.stdout.write(JSON.stringify({passed:report.passed,checks:checks.length,browser:version.product})+'\n');
}catch(error){const report={executed_at_utc:new Date().toISOString(),passed:false,error:String(error),checks};await fs.writeFile(path.join(root,'results/browser-validation.json'),JSON.stringify(report,null,2)+'\n');process.stderr.write(String(error)+'\n');process.exitCode=1;
}finally{page?.close();browser?.close();chrome.kill('SIGTERM');server.close();}
