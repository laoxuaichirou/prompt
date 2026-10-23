#!/usr/bin/env python3
"""Loopback Creator Desk server: static media + constrained local Remotion jobs."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer
from concurrent.futures import ThreadPoolExecutor
import argparse,json,os,re,shutil,subprocess,threading,uuid
from urllib.parse import urlsplit
from local_media_server import RangeHandler

ROOT=Path(__file__).resolve().parents[1]
COMPOSITIONS={'KineticWords','ProcessSteps','DataComparison'}
JOBS={};LOCK=threading.Lock();POOL=ThreadPoolExecutor(max_workers=1)
BROWSER=os.environ.get('REMOTION_BROWSER_EXECUTABLE') or shutil.which('chromium') or shutil.which('google-chrome')
CLI=ROOT/'remotion/node_modules/@remotion/cli/remotion-cli.js'
CACHE=ROOT/'.cache/studio-renders'

def validate_props(composition,p):
 if composition not in COMPOSITIONS or not isinstance(p,dict):raise ValueError('只支持三个内置Remotion组件')
 def text(v,n):
  if not isinstance(v,str) or not v.strip() or len(v.encode('utf-16-le'))//2>n:raise ValueError(f'文案应为1到{n}字符')
  return v
 def array(v,n,max_chars):
  if not isinstance(v,list) or len(v)!=n:raise ValueError(f'需要{n}行内容')
  return [text(x,max_chars) for x in v]
 clean={'title':text(p.get('title'),16)}
 if composition=='KineticWords':
  clean.update(words=array(p.get('words'),3,8),footer=text(p.get('footer'),24))
 elif composition=='ProcessSteps':
  clean.update(steps=array(p.get('steps'),3,10),descriptions=array(p.get('descriptions'),3,22))
 else:
  values=p.get('values')
  if not isinstance(values,list) or len(values)!=2 or any(type(x) not in {int,float} or not 0<=x<=1000000 for x in values):raise ValueError('需提供两个0到1000000的示例数值')
  clean.update(labels=array(p.get('labels'),2,12),values=values,unit=text(p.get('unit'),6),source=text(p.get('source'),40))
 if set(p)!=set(clean):raise ValueError('包含不支持的参数；图片路径固定为内置素材')
 return clean

def render_ready():return bool(BROWSER and CLI.is_file() and shutil.which('node'))
def execute_job(job_id,composition,props):
 try:
  CACHE.mkdir(parents=True,exist_ok=True)
  prop_file=CACHE/(job_id+'.json');output=CACHE/(job_id+'.mp4')
  prop_file.write_text(json.dumps(props,ensure_ascii=False),encoding='utf-8')
  command=['node',str(CLI),'render','src/index.ts',composition,str(output),'--props='+str(prop_file),'--browser-executable='+BROWSER,'--concurrency=2','--crf=20']
  completed=subprocess.run(command,cwd=ROOT/'remotion',capture_output=True,text=True,timeout=180)
  if completed.returncode or not output.is_file():raise RuntimeError('Remotion执行失败，请检查本机依赖、Chrome与中文字体')
  probe=subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(output)],capture_output=True,text=True,check=True,timeout=20)
  info=json.loads(probe.stdout);v=next(s for s in info['streams'] if s['codec_type']=='video')
  duration=8 if composition=='ProcessSteps' else 6
  if v['codec_name']!='h264' or v['width']!=1080 or v['height']!=1920 or v['r_frame_rate']!='30/1' or abs(float(info['format']['duration'])-duration)>.05:raise RuntimeError('渲染输出参数不符合预期')
  with LOCK:JOBS[job_id].update(status='completed',url='/api/renders/'+job_id+'.mp4')
 except Exception as e:
  with LOCK:JOBS[job_id].update(status='failed',error=str(e)[:300])
  (CACHE/(job_id+'.mp4')).unlink(missing_ok=True)

class StudioHandler(RangeHandler):
 def json_response(self,status,data):
  b=json.dumps(data,ensure_ascii=False).encode()
  self.send_response(status);self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Content-Length',str(len(b)));self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(b)
 def trusted_host(self):return self.headers.get('Host') in {f'127.0.0.1:{self.server.server_port}',f'localhost:{self.server.server_port}'}
 def do_GET(self):
  if not self.trusted_host():return self.json_response(403,{'error':'仅允许本机访问'})
  path=urlsplit(self.path).path
  if path=='/api/status':return self.json_response(200,{'service':'creator-desk-local','render_ready':render_ready() and bool(shutil.which('ffprobe'))})
  if path.startswith('/api/jobs/'):
   job_id=path.rsplit('/',1)[-1]
   with LOCK:job=dict(JOBS[job_id]) if job_id in JOBS else None
   return self.json_response(200,job) if job else self.json_response(404,{'error':'任务不存在或服务已重启'})
  if path.startswith('/api/renders/'):
   match=re.fullmatch(r'/api/renders/([a-f0-9]{32})\.mp4',path)
   with LOCK:allowed=bool(match and JOBS.get(match[1],{}).get('status')=='completed')
   if not allowed:return self.json_response(404,{'error':'已完成视频不存在'})
  elif path.startswith('/api/'):return self.json_response(404,{'error':'接口不存在'})
  return super().do_GET()
 def do_HEAD(self):
  if not self.trusted_host():return self.send_error(403)
  path=urlsplit(self.path).path
  if path.startswith('/api/'):
   match=re.fullmatch(r'/api/renders/([a-f0-9]{32})\.mp4',path)
   with LOCK:allowed=bool(match and JOBS.get(match[1],{}).get('status')=='completed')
   if not allowed:return self.send_error(404)
  return super().do_HEAD()
 def translate_path(self,path):
  match=re.fullmatch(r'/api/renders/([a-f0-9]{32})\.mp4',urlsplit(path).path)
  if match:return str(CACHE/(match[1]+'.mp4'))
  return super().translate_path(path)
 def send_head(self):
  path=urlsplit(self.path).path
  if re.fullmatch(r'/api/renders/[a-f0-9]{32}\.mp4',path):
   original=self.directory;self.directory=str(CACHE)
   try:return super().send_head()
   finally:self.directory=original
  return super().send_head()
 def do_POST(self):
  if not self.trusted_host():return self.json_response(403,{'error':'仅允许本机访问'})
  origin=self.headers.get('Origin')
  if origin and origin!='http://'+self.headers['Host']:return self.json_response(403,{'error':'只接受工作台同源请求'})
  if self.headers.get('Sec-Fetch-Site')=='cross-site':return self.json_response(403,{'error':'拒绝跨站请求'})
  if urlsplit(self.path).path!='/api/render':return self.json_response(404,{'error':'接口不存在'})
  if self.headers.get_content_type()!='application/json':return self.json_response(415,{'error':'只接受JSON'})
  if not render_ready() or not shutil.which('ffprobe'):return self.json_response(503,{'error':'需安装锁定的Remotion依赖、Chrome与ffprobe'})
  try:
   length=int(self.headers.get('Content-Length','0'))
   if not 0<length<=16384:raise ValueError('请求大小无效')
   data=json.loads(self.rfile.read(length));composition=data.get('composition');props=validate_props(composition,data.get('props'))
  except (ValueError,AttributeError,UnicodeError) as e:return self.json_response(400,{'error':str(e)})
  with LOCK:
   if any(j['status']=='running' for j in JOBS.values()):return self.json_response(409,{'error':'已有渲染进行中，请等待完成'})
   if len(JOBS)>=100:return self.json_response(429,{'error':'本次服务任务数已达100，请重启服务'})
   job_id=uuid.uuid4().hex;JOBS[job_id]={'id':job_id,'status':'running','composition':composition}
  POOL.submit(execute_job,job_id,composition,props)
  self.json_response(202,{'id':job_id,'status':'running'})

def make_server(port=8765):return ThreadingHTTPServer(('127.0.0.1',port),partial(StudioHandler,directory=str(ROOT)))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8765);args=parser.parse_args()
 server=make_server(args.port)
 print(f'创作桌：http://127.0.0.1:{server.server_port}/prototype/index.html',flush=True)
 print('本机Remotion可用' if render_ready() else '静态功能可用；渲染需先在remotion目录 npm ci --ignore-scripts',flush=True)
 try:server.serve_forever()
 except KeyboardInterrupt:pass
 finally:server.server_close();POOL.shutdown(wait=True)
