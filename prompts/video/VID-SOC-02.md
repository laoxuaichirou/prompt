# VID-SOC-02 轻运动静物

原创模板 · social

## 使用输入

`duration_seconds`, `image_ref`, `subtle_motion`

## 提示词

```text
使用 {{image_ref}} 为首帧，{{duration_seconds}}秒轻微推近约5%，保留原图构图和主体，不增添物体，仅 {{subtle_motion}} 缓慢运动，静音，无文字。用于口播视频短暂视觉切换。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
