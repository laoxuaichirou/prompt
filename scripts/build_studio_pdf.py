#!/usr/bin/env python3
"""Standalone Chinese handoff for the integrated workspace; original PDFs unchanged."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Image
from reportlab.lib.pagesizes import A4
R=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
styles={
 'body':ParagraphStyle('body',fontName='STSong-Light',fontSize=10,leading=16,wordWrap='CJK',spaceAfter=7,textColor=colors.HexColor('#203c48')),
 'h1':ParagraphStyle('h1',fontName='STSong-Light',fontSize=21,leading=29,spaceBefore=12,spaceAfter=16,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='STSong-Light',fontSize=14,leading=21,spaceBefore=13,spaceAfter=10,keepWithNext=True,textColor=colors.HexColor('#b86c4d')),
 'code':ParagraphStyle('code',fontName='STSong-Light',fontSize=8,leading=13,wordWrap='CJK',backColor=colors.HexColor('#f1f2ec'),spaceAfter=4)
}
story=[]
def paragraph(text,style='body'):
 text=escape(text.replace('**','').replace(chr(96),''))
 text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1（\2）',text)
 return Paragraph(text,styles[style])
story+=[Spacer(1,35),paragraph('创作桌：素材与动效工作台','h1'),paragraph('追加交付 / 2026-10-23（北京时间）'),paragraph('GitHub: https://github.com/laoxuaichirou/prompt'),Spacer(1,12)]
story.append(Image(str(R/'artifacts/studio/motion-custom.png'),width=510,height=340,kind='proportional'))
story+=[Spacer(1,16),paragraph('已跑通：素材上传 → 提示词与Skill → A/B评审 → 画布 → 自定义Remotion渲染 → MP4 → 带素材工程迁移。'),paragraph('启动：python scripts/studio_server.py；浏览器打开 http://127.0.0.1:8765/prototype/index.html。在线生图、AI视频供应商和完整长片尚未接入。'),PageBreak()]
code=False
for line in (R/'docs/06-创作桌工作台与Hermes验收.md').read_text().splitlines():
 if line.startswith(chr(96)*3):code=not code;continue
 if not line.strip():story.append(Spacer(1,5));continue
 if code:story.append(paragraph(line,'code'));continue
 if line.startswith('#'):
  level=len(line)-len(line.lstrip('#'));story.append(paragraph(line.lstrip('#').strip(),'h1' if level==1 else 'h2'));continue
 if re.fullmatch(r'\|[-:| ]+\|',line):continue
 if line.startswith('|'):line=' / '.join(x.strip() for x in line.strip('|').split('|'))
 story.append(paragraph(line))
def footer(canvas,doc):
 canvas.setFont('STSong-Light',8);canvas.setFillColor(colors.HexColor('#81908e'));canvas.drawString(40,25,'创作桌 / 工作台追加交付 / 2026-10-23');canvas.drawRightString(A4[0]-40,25,str(doc.page))
target=R/'artifacts/studio/工作台交付与Hermes验收.pdf'
doc=SimpleDocTemplate(str(target),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=42,bottomMargin=45,title='创作桌工作台与Hermes验收',author='laoxuaichirou/prompt')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(target)
