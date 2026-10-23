#!/usr/bin/env python3
"""Real Chromium interaction test; serves only on loopback and shuts down after run."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import threading, json, tempfile, os, shutil
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)))
threading.Thread(target=server.serve_forever,daemon=True).start()
checks=[]
def check(name,condition):
 if not condition:raise AssertionError(name)
 checks.append(name)
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path=os.environ.get('CANVAS_BROWSER_EXECUTABLE') or shutil.which('chromium') or shutil.which('google-chrome') or '/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':1536,'height':1000},device_scale_factor=1)
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(f'http://127.0.0.1:{server.server_port}/prototype/index.html');page.wait_for_selector('.node')
  check('default graph contains three nodes',page.locator('.node').count()==3)
  check('sample image actually loaded',page.locator('.node img').evaluate('(e)=>e.complete && e.naturalWidth>100'))
  page.locator('#node-content').fill('验收测试：编辑保温杯主图需求。');page.locator('#node-title').click()
  page.reload();check('edits persist after reload','验收测试' in page.locator('#node-content').input_value())
  before=page.locator('.node').first.evaluate('(e)=>[e.offsetLeft,e.offsetTop]')
  h=page.locator('.node-head').first.bounding_box();page.mouse.move(h['x']+60,h['y']+20);page.mouse.down();page.mouse.move(h['x']+120,h['y']+75,steps=10);page.mouse.up()
  after=page.locator('.node').first.evaluate('(e)=>[e.offsetLeft,e.offsetTop]');check('drag updates graph coordinates',after!=before)
  page.locator('#undo').click();check('undo restores node position',page.locator('.node').first.evaluate('(e)=>[e.offsetLeft,e.offsetTop]')==before)
  page.locator('[data-add="video"]').click();check('can add node',page.locator('.node').count()==4)
  new_id=page.locator('.node.selected').get_attribute('data-id')
  page.locator('[data-id="n2"] .out').click();page.locator(f'[data-id="{new_id}"] .in').click()
  check('port connection changes graph',page.locator('#edges path').count()==3)
  page.locator('[data-id="n2"] .node-head').click()
  page.locator(f'[data-ref="{new_id}"]').count() # video to image must not be offered
  check('incompatible input not offered',page.locator(f'[data-ref="{new_id}"]').count()==0)
  page.locator('#plan').click();check('execution plan explicitly says no provider task','未提交生成任务' in page.locator('#toast').inner_text())
  page.locator('#zoom-in').click();check('zoom changes viewport',page.locator('#zoom-value').inner_text()!='100%')
  with page.expect_download() as d:page.locator('#export').click()
  exported=Path(tempfile.mkdtemp())/'project.json';d.value.save_as(str(exported));data=json.loads(exported.read_text());data=data.get('graph',data);check('export contains current graph',len(data['nodes'])==4 and len(data['edges'])==3)
  bad=exported.parent/'bad.json';bad.write_text('{"version":1,"title":"bad","nodes":[],"edges":[{"source":"no","target":"no"}]}')
  page.locator('#file').set_input_files(str(bad));page.wait_for_function("document.querySelector('#toast').textContent.includes('导入失败')");check('invalid import preserves project',page.locator('.node').count()==4)
  page.locator('[data-template="film"]').click();check('template changes workflow',page.locator('.node img').get_attribute('src').endswith('IMG-FILM-03.png'))
  page.locator('#file').set_input_files(str(exported));page.wait_for_function("document.querySelectorAll('.node').length===4");check('import restores exported content','验收测试' in page.locator('.node-body').first.inner_text())
  page.locator('[data-template="ecommerce"]').click();page.locator('#fit').click();page.locator('#toast').evaluate('(e)=>e.style.display="none"');page.screenshot(path=str(R/'artifacts/canvas-prototype.png'),full_page=True)
  page.set_viewport_size({'width':390,'height':844});page.reload();check('mobile layout stays within viewport',page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
  check('no browser exceptions',not errors)
  browser.close()
 result={'status':'passed','checks':checks,'count':len(checks),'browser':'system Chromium; Playwright','note':'Checks prototype workflow only; no image/video provider call.'}
 (R/'artifacts/canvas-test-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
finally:server.shutdown();server.server_close()
