# REM-03 数据对比动效

原创模板 · comparison

## 使用输入

`data`, `source`, `timings`

## 提示词

```text
为 {{data}} 设计Remotion对比图表，明确单位、来源 {{source}} 和是否示例数据，不夸大截断坐标轴；按 {{timings}} 动画，数据与图形长度一致，支持9:16与16:9，文本由React渲染。
```

## 验收

- 帧驱动且确定性
- 真实字体与安全区
- 渲染后ffprobe确认时长分辨率
- 引用的素材文件存在
