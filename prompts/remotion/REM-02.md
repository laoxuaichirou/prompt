# REM-02 三步流程卡片

原创模板 · steps

## 使用输入

`duration_seconds`, `palette`, `steps`, `timings`

## 提示词

```text
将 {{steps}} 制作为三步卡片动效，步骤分别按 {{timings}} 入场，颜色 {{palette}}，字体大于48px（1080竖屏），总时长 {{duration_seconds}}秒，30fps。使用Sequence、interpolate和spring，所有值可由输入props替换。
```

## 验收

- 帧驱动且确定性
- 真实字体与安全区
- 渲染后ffprobe确认时长分辨率
- 引用的素材文件存在


