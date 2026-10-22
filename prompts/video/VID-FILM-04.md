# VID-FILM-04 动作衔接镜头

原创模板 · film

## 使用输入

`action`, `audio_plan`, `camera`, `character_ref`, `duration_seconds`, `end_pose_ref`, `previous_shot_id`, `screen_direction`

## 提示词

```text
【参考锚定】沿用镜头 {{previous_shot_id}} 的角色资产 {{character_ref}} 和结束姿态 {{end_pose_ref}}。
【分镜动作】从该姿态开始，角色 {{action}}，运动方向 {{screen_direction}}，时长 {{duration_seconds}}秒，机位 {{camera}}。
【声音】{{audio_plan}}。
【禁止项】不反转方向、不改变持物手、不跨越轴线、无跳切字幕。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
