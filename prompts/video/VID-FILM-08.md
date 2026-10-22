# VID-FILM-08 片段延长

原创模板 · longform

## 使用输入

`clip_ref`, `duration_seconds`, `end_state`, `last_frame_ref`, `ongoing_action`

## 提示词

```text
以 {{clip_ref}} 的最后一帧 {{last_frame_ref}} 为起点，延长 {{duration_seconds}}秒，继续 {{ongoing_action}}，保持角色、道具、镜头速度和光照；结尾停在 {{end_state}}。先确认供应商支持延长与输入片段长度，否则改用末帧图生视频并安排剪辑遮挡衔接。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
