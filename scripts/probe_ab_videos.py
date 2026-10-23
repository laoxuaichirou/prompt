#!/usr/bin/env python3
"""Record actual A/B Remotion outputs; this command never invokes a generation API."""
from pathlib import Path
import hashlib,json,subprocess
R=Path(__file__).resolve().parents[1];D=R/'artifacts/ab-2026-10-23'
items=[]
for label in ['A','B']:
 p=D/f'remotion-{label}.mp4';q=subprocess.run(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)],capture_output=True,text=True,check=True);d=json.loads(q.stdout);v=next(x for x in d['streams'] if x['codec_type']=='video')
 assert (v['width'],v['height'],v['r_frame_rate'],v['codec_name'],int(v['nb_read_frames']))==(1080,1920,'30/1','h264',180)
 assert abs(float(d['format']['duration'])-6)<.05 and not any(x['codec_type']=='audio' for x in d['streams'])
 props=R/f'remotion/props/ab-{label}.json';image=R/'remotion/public'/('ab-coral.png' if label=='A' else 'ab-teal.png')
 assert image.read_bytes()==(D/f'AB03-{label}.png').read_bytes()
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','3','-i',str(p),'-frames:v','1',str(D/f'remotion-{label}-middle.png')],check=True)
 items.append({'id':'AB06-'+label,'artifact':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'props_file':str(props.relative_to(R)),'props':json.loads(props.read_text()),'image_file':str(image.relative_to(R)),'image_sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'frame_file':f'artifacts/ab-2026-10-23/remotion-{label}-middle.png','width':1080,'height':1920,'fps':'30/1','frames':180,'duration_seconds':6,'audio':'none','codec':'h264','probe':d})
a,b=[x['props'] for x in items];assert {k for k in a if a[k]!=b[k]}=={'illustration'}
(D/'video-results.json').write_text(json.dumps({'component_sha256':hashlib.sha256((R/'remotion/src/Root.tsx').read_bytes()).hexdigest(),'package_lock_sha256':hashlib.sha256((R/'remotion/package-lock.json').read_bytes()).hexdigest(),'case_id':'AB06','variable':'illustration local asset only; same component, text, timing and render settings','items':items},ensure_ascii=False,indent=2)+'\n')
print('AB06: both actual 6s/180-frame 1080x1920 silent H264 videos verified')
