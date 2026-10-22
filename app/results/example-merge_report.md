# 提示词合并台账

生成时间：2026-10-22T18:52:02.010Z（UTC）

## 参数快照

```json
{
  "normalization": "width-punctuation/whitespace/lower/boundary-noise-v1",
  "threshold": 0.5,
  "lcs_weight": 0.6,
  "bigram_weight": 0.4,
  "short_guard": true,
  "short_limit": 12,
  "length_ratio": [
    0.4,
    2.5
  ],
  "width": true,
  "space": true,
  "lower": true,
  "noise_enabled": true,
  "noise_version": "boundary-noise-v1-f7fdf0fc9b1a6f04",
  "noise_words": [
    "输出前检查",
    "生成一张",
    "请基于",
    "请生成",
    "一张",
    "图片",
    "尽量",
    "必须",
    "检查",
    "注意",
    "画面",
    "确保",
    "要求"
  ],
  "exclude_templates": true,
  "topic_bucket": false,
  "totalEntries": 8,
  "eligible": 8,
  "excluded": 0,
  "totalPairs": 28,
  "processed": 28,
  "compared": 28,
  "pruned": 0,
  "shortCount": 0,
  "elapsed": 0.0037654960000000058,
  "dataset_fingerprint": "5fab7d64d67b7df0",
  "parameter_fingerprint": "38c47d3ea95936b4"
}
```

条目总数 8；排除模板 0（仍保留导出）；比较次数 28；长度剪枝 0；候选对 28；输出 7。

本次全库比较；跨主题达到阈值的对均列入冲突清单。

推荐不是裁定。未确认和不合并簇保留所有条目。槽位冲突阻止对应条目并入；没有自动覆盖 default。

## 簇 1：S3 / S4

状态：未裁定；最高相似度 0.789853501。

主条 ID：S4

实际并入 / 丢弃的条目及原因：
- 无；未删除条目。

勾选补入片段（依勾选顺序，保留原文）：
- 无。

未合并簇及原因：尚未人工确认。

## 簇 2：S5 / S6

状态：未裁定；最高相似度 0.736442358。

主条 ID：S5

实际并入 / 丢弃的条目及原因：
- 无；未删除条目。

勾选补入片段（依勾选顺序，保留原文）：
- 无。

未合并簇及原因：尚未人工确认。

## 簇 3：S1 / S2

状态：已确认合并；最高相似度 0.649530455。

主条 ID：S1

实际并入 / 丢弃的条目及原因：
- S2 → S1；相似度 0.649530455；原因：人工确认并入。

勾选补入片段（依勾选顺序，保留原文）：
- S2："景深较浅"（已追加）
- S2："35 毫米镜头拍摄"（已追加）

