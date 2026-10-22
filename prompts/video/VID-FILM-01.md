# VID-FILM-01 单镜头角色动作

原创模板 · film

## 使用输入

`adult_character`, `audio_plan`, `camera`, `character_ref`, `duration_seconds`, `one_action`, `position`, `prop_ref`, `scene_ref`

## 提示词

```text
【参考锚定】角色 {{character_ref}}、场景 {{scene_ref}}、道具 {{prop_ref}}，保持脸、服饰与空间一致。
【分镜动作】{{adult_character}} 在 {{position}} 完成 {{one_action}}，{{camera}}，{{duration_seconds}}秒，单镜头。
【声音】{{audio_plan}}；对白如需配音则单独交由TTS，不假定模型口型同步。
【禁止项】无字幕、水印、Logo、额外人物、跳切、脸部漂移和道具变形。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
