# VID-FILM-03 反应近景

原创模板 · film

## 使用输入

`character_ref`, `duration_seconds`, `emotion`, `eyeline`, `scene_ref`

## 提示词

```text
【参考锚定】成年角色 {{character_ref}} 和场景 {{scene_ref}}。
【分镜动作】{{duration_seconds}}秒近景，角色看向 {{eyeline}}，先保持平静，再出现轻微 {{emotion}}，动作克制，固定机位。
【声音】不说话，环境声后期补。
【禁止项】不换脸、不换衣、不夸张表演、不突然转头、无字幕。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
