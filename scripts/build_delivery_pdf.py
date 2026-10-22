#!/usr/bin/env python3
"""Build a standalone Chinese delivery document; optional dependency: reportlab."""
from pathlib import Path
import json,re
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Image,KeepTogether
from reportlab.lib.pagesizes import A4
R=Path(__file__).resolve().parents[1];pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
ink=colors.HexColor('#173345');accent=colors.HexColor('#d77451')
styles={'body':ParagraphStyle('Body',fontName='STSong-Light',fontSize=10,leading=16,textColor=ink,spaceAfter=7,wordWrap='CJK'), 'small':ParagraphStyle('Small',fontName='STSong-Light',fontSize=8,leading=12,textColor=ink,wordWrap='CJK'), 'h1':ParagraphStyle('H1',fontName='STSong-Light',fontSize=21,leading=29,textColor=ink,spaceAfter=16,spaceBefore=12,keepWithNext=True), 'h2':ParagraphStyle('H2',fontName='STSong-Light',fontSize=14,leading=20,textColor=accent,spaceBefore=15,spaceAfter=10,keepWithNext=True)}
story=[]
def para(t,style='body'):
 t=escape(t.replace('**','').replace('`',''))
 t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<link href="\2" color="#a1583c">\1</link>',t)
 t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1（仓库内：\2）',t)
 return Paragraph(t,styles[style])
def emit_md(path):
 lines=path.read_text().splitlines();code=False;buffer=[]
 def flush():
  if buffer:story.append(para(' '.join(buffer)));buffer.clear()
 for line in lines:
  if line.startswith('```'):
   flush();code=not code
   if code:story.append(para('命令、源码与交互图请结合仓库原文件使用。','small'))
   continue
  if code:continue
  if not line.strip():flush();continue
  if line.startswith('#'):
   flush();level=len(line)-len(line.lstrip('#'));story.append(para(line.lstrip('#').strip(),'h1' if level==1 else 'h2'));continue
  if line.startswith('|'):
   flush()
   if re.match(r'^\|[-:| ]+\|$',line):continue
   cells=[x.strip() for x in line.strip('|').split('|')];story.append(para(' / '.join(cells),'small'));continue
  if line.startswith('- ') or re.match(r'^\d+\. ',line):flush();story.append(para('• '+line.lstrip('- ')));continue
  buffer.append(line)
 flush()
def footer(canvas,doc):
 canvas.setFont('STSong-Light',8);canvas.setFillColor(colors.HexColor('#81908e'));canvas.drawString(40,25,'创作桌 / AI画布研究与规划 / 2026-10-23');canvas.drawRightString(A4[0]-40,25,str(doc.page))
story.extend([Spacer(1,50),para('创作桌','h1'),para('AI画布研究、提示词与视频素材规划','h1'),para('面向电商、影视素材、5–10分钟长视频与自媒体口播动效'),para('交付日期：2026-10-23（北京时间）'),para('GitHub仓库：https://github.com/laoxuaichirou/prompt'),Spacer(1,20)])
story.append(Image(str(R/'artifacts/canvas-prototype.png'),width=515,height=335))
story.extend([Spacer(1,20),para('交付：PDF课程整理、三类各10项已核验候选star榜单、50条原创模板、8个原创技能、选定MIT上游原文、交互原型、三张生图样例、三个真实Remotion MP4，以及Hermes验收脚本。'),para('范围：研究、规划与可运行样例，不是已接入付费供应商的生产系统。榜单不是全站穷尽排名；5/10分钟文件是镜头计划，不是已生成长片。'),PageBreak()])
emit_md(R/'docs/01-PDF课程整理.md');story.append(PageBreak())
emit_md(R/'docs/02-画布工具产品规划.md');story.append(PageBreak())
rows=json.loads((R/'research/top30.json').read_text())['items']
for cat,title in [('canvas','画布项目Top10'),('image','生图提示词 / Skill Top10'),('video','视频生成提示词 / Skill Top10')]:
 story.append(para(title,'h1'));story.append(para('按本次检索并核验的相关候选star降序；采集于2026-10-23北京时间，非GitHub全站穷尽排名。完整来源、commit与文件入口请查看仓库research目录。'))
 data=[[para(t,'small') for t in ['排名','项目','Stars','用途与许可']]]
 for x in [x for x in rows if x['category']==cat]:data.append([para(str(x['rank']),'small'),para(x['name'],'small'),para(f'{x["stars"]:,}','small'),para(x['use_case']+'；'+x['license'],'small')])
 t=Table(data,colWidths=[26,170,55,264],repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eee9de')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor('#dedfd8'))]));story.append(t);story.append(PageBreak())
emit_md(R/'docs/03-生图与动效测试记录.md');story.append(PageBreak());emit_md(R/'docs/交付文档-Hermes验收.md')
path=R/'artifacts/交付文档-创作画布研究与规划.pdf';doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=40,leftMargin=40,topMargin=42,bottomMargin=45,title='创作桌：AI画布研究与规划交付',author='laoxuaichirou/prompt');doc.build(story,onFirstPage=footer,onLaterPages=footer);print(path)
