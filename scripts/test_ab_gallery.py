#!/usr/bin/env python3
"""Exercise the offline A/B gallery in real Chromium and print its comparison PDF."""
from pathlib import Path
import json,os,shutil,threading
from http.server import ThreadingHTTPServer
from local_media_server import RangeHandler
from functools import partial
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];D=R/'artifacts/ab-2026-10-23';checks=[]
def check(name,condition):
 if not condition:raise AssertionError(name)
 checks.append(name)
class Quiet(RangeHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)))
threading.Thread(target=server.serve_forever,daemon=True).start()
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path=os.environ.get('CANVAS_BROWSER_EXECUTABLE') or shutil.which('chromium') or '/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(f'http://127.0.0.1:{server.server_port}/artifacts/ab-2026-10-23/index.html');page.wait_for_function("Array.from(document.querySelectorAll('.frame img')).every(i=>i.complete&&i.naturalWidth>100)")
  check('ten full-size image outputs load',page.locator('.frame img').count()==10)
  check('six comparison sections',page.locator('main section').count()==6)
  page.locator('[data-bg="dark"]').click();check('dark backdrop switch',page.locator('body').get_attribute('data-alpha')=='dark')
  page.locator('#AB04').screenshot(path=str(D/'alpha-dark-review.png'))
  page.locator('[data-zoom]').click();check('native-pixel view stays within page',page.evaluate('document.documentElement.scrollWidth<=innerWidth'));check('native-pixel alpha inspection',page.locator('#AB04 .frame img').first.evaluate('(i)=>Math.abs(i.getBoundingClientRect().width-i.naturalWidth)<1'))
  page.locator('#AB04 .grid').screenshot(path=str(D/'alpha-edge-100pct.png'));page.locator('[data-zoom]').click()
  check('native-pixel mode resets to fit',page.locator('#AB04 .frame img').first.evaluate('(i)=>i.getBoundingClientRect().width<i.naturalWidth'))
  page.locator('[data-bg="white"]').click();check('white backdrop switch',page.locator('body').get_attribute('data-alpha')=='white')
  page.locator('[data-bg="checker"]').click();check('checker backdrop switch',page.locator('body').get_attribute('data-alpha')=='checker')
  page.wait_for_function("Array.from(document.querySelectorAll('video')).every(v=>v.readyState>=1)")
  check('both actual MP4 metadata load',page.locator('video').evaluate_all('(vs)=>vs.length===2&&vs.every(v=>Math.abs(v.duration-6)<.05&&v.videoWidth===1080&&v.videoHeight===1920)'))
  page.locator('#seek').click();page.wait_for_function("Array.from(document.querySelectorAll('video')).every(v=>Math.abs(v.currentTime-3)<.1 && v.readyState>=2)");check('both seek to same 3-second point',True)
  page.locator('#play').click();page.wait_for_function("Array.from(document.querySelectorAll('video')).every(v=>v.currentTime>.2&&!v.paused)")
  page.locator('#pause').click();check('both videos pause',page.locator('video').evaluate_all('(vs)=>vs.every(v=>v.paused)'))
  check('play starts are approximately aligned (not frame-locked)',page.locator('video').evaluate_all('(vs)=>Math.abs(vs[0].currentTime-vs[1].currentTime)<.5'))
  page.locator('#seek').click();page.locator('#AB06').screenshot(path=str(D/'remotion-comparison.png'))
  page.set_viewport_size({'width':390,'height':844});check('mobile layout has no horizontal overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
  page.set_viewport_size({'width':1440,'height':1000});page.emulate_media(media='print');page.pdf(path=str(D/'AB对照报告.pdf'),format='A4',print_background=True,margin={'top':'12mm','bottom':'12mm','left':'10mm','right':'10mm'})
  check('no browser exceptions',not errors);browser.close()
 result={'status':'passed','checks':checks,'count':len(checks),'scope':'offline gallery file loading, background switching, video controls, responsive layout and PDF print; not a quality-pass verdict'}
 (D/'gallery-test-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
finally:
 server.shutdown();server.server_close()
