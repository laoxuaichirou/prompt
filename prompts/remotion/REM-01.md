# REM-01 口播关键词动效

原创模板 · kinetic

## 使用输入

`duration_seconds`, `script`, `timings`

## 提示词

```text
根据口播 {{script}} 与时间码 {{timings}}，设计一段 {{duration_seconds}} 秒Remotion动效：短词分段进入，最多两行，每行不超过12个汉字；动画绑定useCurrentFrame，真实字体渲染，9:16，底部20%字幕安全区。交付可编译的组件与帧区间，不使用CSS时间动画或Math.random。
```

## 验收

- 帧驱动且确定性
- 真实字体与安全区
- 渲染后ffprobe确认时长分辨率
- 引用的素材文件存在
