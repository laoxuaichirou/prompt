#!/usr/bin/env python3
"""Loopback-only read-only static server with HTTP byte ranges for MP4 seeking."""
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from functools import partial
import argparse,re
class RangeHandler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
 def end_headers(self):
  self.send_header('Accept-Ranges','bytes');super().end_headers()
 def send_head(self):
  self._range_left=None
  target=Path(self.translate_path(self.path)).resolve();root=Path(self.directory).resolve()
  try:relative=target.relative_to(root)
  except ValueError:self.send_error(403);return None
  if any(p.startswith('.') for p in relative.parts):self.send_error(403);return None
  value=self.headers.get('Range')
  if not value or not target.is_file():return super().send_head()
  m=re.fullmatch(r'bytes=(\d*)-(\d*)',value.strip());size=target.stat().st_size
  if not m or not size:self.send_error(416);return None
  first,last=m.groups()
  if first:start=int(first);end=min(int(last) if last else size-1,size-1)
  elif last:start=max(0,size-int(last));end=size-1
  else:self.send_error(416);return None
  if start>=size or start>end:self.send_error(416);return None
  f=target.open('rb');f.seek(start);self._range_left=end-start+1
  self.send_response(206);self.send_header('Content-Type',self.guess_type(str(target)));self.send_header('Content-Length',str(self._range_left));self.send_header('Content-Range',f'bytes {start}-{end}/{size}');self.end_headers();return f
 def copyfile(self,source,outputfile):
  if self._range_left is None:return super().copyfile(source,outputfile)
  remaining=self._range_left
  while remaining:
   chunk=source.read(min(65536,remaining))
   if not chunk:break
   outputfile.write(chunk);remaining-=len(chunk)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--port',type=int,default=8765);args=a.parse_args();root=Path(__file__).resolve().parents[1]
 server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(RangeHandler,directory=str(root)))
 print(f'Local media server on port {server.server_port}; open artifacts/ab-2026-10-23/index.html through this server. Ctrl+C stops it.')
 try:server.serve_forever()
 except KeyboardInterrupt:pass
 finally:server.server_close()
