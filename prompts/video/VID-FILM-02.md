# VID-FILM-02 空镜建立

原创模板 · film

## 使用输入

`ambience`, `duration_seconds`, `environment_motion`, `scene_ref`

## 提示词

```text
【参考锚定】使用 {{scene_ref}} 的建筑与光线。
【分镜动作】{{duration_seconds}}秒广角建立镜头，缓慢推进，只有 {{environment_motion}} 运动；无人物。
【声音】{{ambience}}，若模型不支持音频则后期添加。
【禁止项】不新增建筑、文字、天气突变或镜头跳切。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
