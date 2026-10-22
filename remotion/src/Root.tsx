import React from 'react';
import {AbsoluteFill, Composition, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
const C={paper:'#f5f1e9',navy:'#142b42',muted:'#71818b',orange:'#ef795a',line:'#d9ddd8',white:'#ffffff'};
const font='"Noto Sans CJK SC", "PingFang SC", "Microsoft YaHei", sans-serif';
const clamp={extrapolateLeft:'clamp' as const,extrapolateRight:'clamp' as const};
function text(v:unknown,max=30):string {if(typeof v!=='string'||!v.trim()||v.length>max)throw new Error(`Expected non-empty string <= ${max} chars`);return v;}
function Base({label,children}: {label:string;children:React.ReactNode}){
 const f=useCurrentFrame(),{durationInFrames,width,height}=useVideoConfig();
 const opacity=interpolate(f,[0,10,durationInFrames-12,durationInFrames-1],[0,1,1,0],clamp);
 return <AbsoluteFill style={{backgroundColor:C.paper}}><AbsoluteFill style={{backgroundColor:C.paper,fontFamily:font,color:C.navy,opacity,padding:width>height?'70px 110px':'130px 90px',boxSizing:'border-box'}}>
  <div style={{fontSize:22,letterSpacing:5,fontWeight:700,color:C.muted}}>CREATOR / MOTION NOTES</div>
  <div style={{display:'flex',alignItems:'center',gap:15,marginTop:24,fontSize:28,color:C.orange}}><span style={{height:10,width:10,borderRadius:'50%',background:C.orange}}/>{label}</div>
  {children}
  <div style={{position:'absolute',left:width>height?110:90,right:width>height?110:90,bottom:height*.21,height:3,background:C.line}}><div style={{height:'100%',background:C.orange,width:`${interpolate(f,[0,durationInFrames-1],[0,100],clamp)}%`}}/></div>
  <div style={{position:'absolute',bottom:height*.17,fontSize:22,color:C.muted}}>口播插入素材 / 静音画面</div>
 </AbsoluteFill></AbsoluteFill>
}
type KineticProps={title:string;words:string[];footer:string};
export const KineticWords:React.FC<KineticProps>=({title,words,footer})=>{
 text(title,16);text(footer,24);if(!Array.isArray(words)||words.length!==3)throw new Error('Provide exactly 3 words');words.forEach(v=>text(v,8));
 const f=useCurrentFrame(),{fps}=useVideoConfig();
 return <Base label="01 — 从想法到素材">
  <h1 style={{fontSize:68,fontWeight:500,margin:'86px 0 56px',lineHeight:1.35}}>{title}</h1>
  <div style={{position:'relative',zIndex:1}}>{words.map((w,i)=>{
   const p=spring({frame:f-16-i*26,fps,config:{damping:18,stiffness:110}});
   return <div key={i} style={{display:'flex',alignItems:'baseline',gap:30,opacity:Math.min(1,p),transform:`translateY(${(1-p)*48}px)`,marginBottom:23}}><span style={{fontSize:24,color:C.muted,fontWeight:500}}>0{i+1}</span><span style={{fontSize:104,fontWeight:800,letterSpacing:-3,color:i===1?C.orange:C.navy}}>{w}</span></div>
  })}</div>
  <Img src={staticFile('folder-illustration.png')} style={{position:'absolute',right:48,top:800,width:510,height:660,objectFit:'cover',objectPosition:'center 62%',mixBlendMode:'multiply',maskImage:'radial-gradient(ellipse at 50% 55%, black 42%, transparent 75%)',opacity:interpolate(f,[74,96],[0,.95],clamp),transform:`translateY(${interpolate(f,[74,110],[30,0],clamp)}px)`}}/>
  <p style={{position:'absolute',left:90,top:1250,fontSize:27,lineHeight:1.7,maxWidth:450,whiteSpace:'pre-line'}}>{footer}</p>
 </Base>
};
type StepsProps={title:string;steps:string[];descriptions:string[]};
export const ProcessSteps:React.FC<StepsProps>=({title,steps,descriptions})=>{
 text(title,16);if(steps.length!==3||descriptions.length!==3)throw new Error('Exactly three steps and descriptions required');steps.forEach(x=>text(x,10));descriptions.forEach(x=>text(x,22));
 const f=useCurrentFrame(),{fps,width,height}=useVideoConfig(),wide=width>height;
 return <Base label="02 — 一条可复用的工作流">
  <h1 style={{fontSize:wide?78:76,lineHeight:1.3,margin:wide?'50px 0 55px':'100px 0 80px'}}>{title}</h1>
  <div style={{display:'flex',flexDirection:wide?'row':'column',gap:wide?28:30}}>{steps.map((s,i)=>{
   const p=spring({frame:f-18-i*37,fps,config:{damping:20}});
   return <div key={i} style={{background:C.white,border:`1px solid ${C.line}`,borderRadius:22,padding:wide?'32px 38px':'36px 40px',flex:wide?1:undefined,opacity:Math.min(1,p),transform:`translateY(${(1-p)*45}px)`}}>
    <div style={{fontSize:26,color:C.orange,marginBottom:16}}>STEP / 0{i+1}</div><div style={{fontSize:wide?49:57,fontWeight:750,marginBottom:16}}>{s}</div><div style={{fontSize:wide?25:28,color:C.muted,lineHeight:1.6}}>{descriptions[i]}</div>
   </div>
  })}</div>
 </Base>
};
type ComparisonProps={title:string;labels:string[];values:number[];unit:string;source:string};
export const DataComparison:React.FC<ComparisonProps>=({title,labels,values,unit,source})=>{
 text(title,16);text(unit,6);text(source,40);if(values.length!==2||labels.length!==2||values.some(x=>!Number.isFinite(x)||x<0))throw new Error('Two non-negative finite values required');labels.forEach(x=>text(x,12));
 const f=useCurrentFrame(),{fps}=useVideoConfig(),max=Math.max(...values,1);
 return <Base label="03 — 让信息一眼可见">
  <h1 style={{fontSize:76,lineHeight:1.3,margin:'100px 0 70px'}}>{title}</h1>
  <div style={{display:'inline-flex',fontSize:24,color:C.muted,border:`1px solid ${C.line}`,padding:'12px 20px',borderRadius:100}}>示例数据 · 非实测 · 零基线</div>
  <div style={{marginTop:80}}>{values.map((v,i)=>{
   const p=Math.min(1,spring({frame:f-25-i*35,fps,config:{damping:22}}));
   return <div key={i} style={{marginBottom:70}}><div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',marginBottom:25}}><span style={{fontSize:34}}>{labels[i]}</span><span style={{fontSize:72,fontWeight:800}}>{Math.round(v*p)}<span style={{fontSize:24,fontWeight:400,marginLeft:12}}>{unit}</span></span></div><div style={{height:55,borderRadius:12,background:C.line,overflow:'hidden'}}><div style={{height:'100%',width:`${v/max*p*100}%`,background:i?C.orange:C.navy,borderRadius:12}}/></div></div>
  })}</div>
  <p style={{fontSize:25,color:C.muted,lineHeight:1.6,marginTop:60}}>来源：{source}</p>
 </Base>
};
const kinetic={title:'把创作留在一张桌上',words:['少搬运','先定稿','再生成'],footer:'素材只准备一次，\n每个镜头都能复用。'};
const steps={title:'先跑通，再加量',steps:['写清需求','锁定素材','逐镜生产'],descriptions:['明确任务、比例和时长','角色、商品、场景先定稿','只改一个变量，确认后批量']};
const comparison={title:'少一次搬运，多一点创作',labels:['手动往返示意','引用复用示意'],values:[8,3],unit:'步',source:'用于说明图表组件的虚构示例'};
export const Root=()=> <>
 <Composition id="KineticWords" component={KineticWords} width={1080} height={1920} fps={30} durationInFrames={180} defaultProps={kinetic}/>
 <Composition id="ProcessSteps" component={ProcessSteps} width={1080} height={1920} fps={30} durationInFrames={240} defaultProps={steps}/>
 <Composition id="DataComparison" component={DataComparison} width={1080} height={1920} fps={30} durationInFrames={180} defaultProps={comparison}/>
 <Composition id="ProcessStepsLandscape" component={ProcessSteps} width={1920} height={1080} fps={30} durationInFrames={240} defaultProps={steps}/>
</>;
