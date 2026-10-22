#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    data=json.loads((ROOT/'asset-map.json').read_text())['items']
    encoded=json.dumps(data,ensure_ascii=False).replace('<','\\u003c')
    html='''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DirectorX · A/B 素材选择</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#11151c;color:#e9edf5;font:16px/1.65 system-ui,"Noto Sans CJK SC","Microsoft Yahei",sans-serif}header{position:sticky;top:0;z-index:2;background:#171e2bf5;border-bottom:1px solid #34415a;padding:18px max(20px,calc((100vw - 1360px)/2));backdrop-filter:blur(8px)}h1{font-size:25px;margin:0 0 7px}header p{margin:5px 0;font-size:14px}.actions{display:flex;gap:10px;flex-wrap:wrap;align-items:center}button{font:inherit;border-radius:7px;padding:8px 18px;border:1px solid #6c85a5;color:#eef4ff;background:#24344d;cursor:pointer}button:first-child{background:#96dfc7;color:#112c25;border-color:#96dfc7}button:focus-visible,a:focus-visible,input:focus-visible{outline:3px solid #e9cb7c;outline-offset:4px}main{max-width:1360px;padding:20px;margin:auto}article{background:#1a2130;border:1px solid #34415a;border-radius:12px;margin:0 0 24px;padding:22px}h2{font-size:23px;margin:0}p{margin:8px 0}.muted{color:#adbbce;font-size:14px}.recommendation{background:#222e42;padding:12px;border-radius:6px}.options{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}.option{border:2px solid #45536b;border-radius:8px;cursor:pointer;display:block;padding:10px}.option.chosen{border-color:#96dfc7;background:#20353a}.option input{margin-right:9px;accent-color:#96dfc7}.option img{display:block;width:100%;height:auto;margin-top:8px;aspect-ratio:16/9;object-fit:contain}.reject{display:inline-block;margin:15px 0 0;padding:5px 10px;border:1px solid #45536b;border-radius:5px;cursor:pointer}.reject.chosen{border-color:#edc88a;color:#edc88a}.reject input{accent-color:#edc88a;margin-right:9px}a{color:#a5e3db}.links{display:flex;gap:24px}details{color:#c7d0df;font-size:14px}summary{cursor:pointer}footer{max-width:1360px;margin:auto;padding:0 20px 30px;color:#a7b7cb;font-size:14px}@media(max-width:700px){header{position:static;padding:16px}main{padding:12px}article{padding:14px}.options{grid-template-columns:1fr}h1{font-size:21px}.actions button{padding:8px 12px}}
</style><script src="review.js" defer></script></head><body>
<header><h1>DirectorX · P0 素材 A/B 选择</h1><p>同一底图与真实ID，逐项选A、选B，或两版返修。点击下方独立原图链接可查看细节。</p><div class="actions"><button id="export" type="button">导出我的选择</button><button id="reset" type="button">恢复推荐</button><span id="summary" aria-live="polite"></span></div><p id="notice" aria-live="polite">选择仅保留在当前页面，关闭前请导出。此页可离线使用。</p></header>
<main id="pairs"></main><footer>图片均为ChatGPT创意候选。选择不会修改现有画布，也不代表Qwen/Krea/H3/RH工作流实测通过。<a href="README.md">交付说明</a></footer>
<script id="review-data" type="application/json">@@DATA@@</script></body></html>'''
    (ROOT/'review.html').write_text(html.replace('@@DATA@@',encoded),encoding='utf-8')
    print('Built offline review for '+str(len(data))+' pairs')
if __name__=='__main__':main()
