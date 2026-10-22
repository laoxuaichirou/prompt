# VID-SOC-01 口播插入B-roll

原创模板 · social

## 使用输入

`duration_seconds`, `visual_action`, `voiceover_sentence`

## 提示词

```text
围绕口播句 {{voiceover_sentence}}，生成一个 {{duration_seconds}}秒无对白B-roll镜头：{{visual_action}}。画面表达一个概念，9:16，主体置中，底部20%不放关键内容，镜头缓慢稳定。字幕、配音和图表都在后期完成，不生成伪文字。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
