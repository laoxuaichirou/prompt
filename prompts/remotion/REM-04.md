# REM-04 章节标题

原创模板 · chapter

## 使用输入

`duration_seconds`, `series`, `subtitle`, `title`

## 提示词

```text
制作系列 {{series}} 的Remotion章节过渡：章节名 {{title}}，副标题 {{subtitle}}，时长 {{duration_seconds}}秒；背景图从资产清单读取，缓慢缩放，标题在安全区，淡入淡出共不超过总长30%。
```

## 验收

- 帧驱动且确定性
- 真实字体与安全区
- 渲染后ffprobe确认时长分辨率
- 引用的素材文件存在


