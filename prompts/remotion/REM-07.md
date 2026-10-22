# REM-07 时间线素材插入

原创模板 · timeline

## 使用输入

`asset_manifest`, `shotlist`

## 提示词

```text
根据 {{shotlist}} 和 {{asset_manifest}} 输出Remotion时间线组件：以帧为唯一时间单位，用Sequence拼接素材，保留旁白轨，统一音量；缺文件要报错而不是静默跳过，不用视频生成模型画字幕。
```

## 验收

- 帧驱动且确定性
- 真实字体与安全区
- 渲染后ffprobe确认时长分辨率
- 引用的素材文件存在
