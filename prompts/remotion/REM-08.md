# REM-08 透明叠加说明层

原创模板 · overlay

## 使用输入

`duration_seconds`, `host_bbox`, `point`

## 提示词

```text
为 {{point}} 设计透明背景Remotion说明层，使用真实字体、箭头和形状；位置避开 {{host_bbox}} 与字幕区，持续 {{duration_seconds}}秒。先交付普通MP4示例；透明交付另用支持alpha的编解码器并用ffprobe与alpha测试确认，不能把普通H264称为透明视频。
```

## 验收

- 帧驱动且确定性
- 真实字体与安全区
- 渲染后ffprobe确认时长分辨率
- 引用的素材文件存在


