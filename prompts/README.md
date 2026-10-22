# 提示词库

50条原创模板：24条生图、18条视频/导演生产、8条Remotion。机器可读总表：[catalog.json](catalog.json)。每条也有独立Markdown，按 `image/`、`video/`、`remotion/` 分开。`origin: original` 表示本次编写，不冒充上游原文。

| 用途 | 从哪里开始 |
|---|---|
| 电商 | IMG-EC-01至08；VID-EC-01至04 |
| 影视资产/分镜 | IMG-FILM-01至07；VID-FILM-01至08 |
| 口播/自媒体 | IMG-FILM-08（口播插画）、IMG-SOC-01至08；VID-SOC-01至06 |
| Remotion动效 | REM-01至08 |

IMG-FILM-08按历史ID保留在image目录，但 `category` 为social；VID-SOC-06是长片/成片质检，`category` 为longform。查询以结构化字段为准。

```bash
python scripts/prompt_cli.py list --kind image --category ecommerce
python scripts/prompt_cli.py show IMG-EC-01
python scripts/prompt_cli.py render IMG-EC-02 --vars '{"product":"保温杯"}'
```

所有 `{{变量}}` 必须填完。模板中写“参考图”不代表图片已传入模型，需实际附加资产。提示词不是API参数；比例、透明输出、音频、参考数量和时长要按真实工具能力映射。缺素材时输出计划，不声称完成生成。

文字、价格、数据与字幕优先后期用真实字体排版。透明背景必须检查alpha；普通MP4不支持透明交付。实测范围只覆盖 [生图检查记录](../docs/03-生图与动效测试记录.md) 所列3条原创生图模板，其他模板尚未逐条生成验证。

上游资源、Skill与选定MIT原文镜像见 [资源索引](../research/04-upstream-resources.md)。
