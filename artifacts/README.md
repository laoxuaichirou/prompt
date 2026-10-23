# 样例与验收证据

- `IMG-EC-01.png`：电商白底主图，1254×1254。
- `IMG-FILM-03.png`：影视关键帧，1672×941。
- `IMG-FILM-08.png`：口播插画底图，941×1672。
- `image-test-results.json`：三次实际生图调用与观察；属于本次测试记录，不应在未重新生成时随意改写。
- `remotion-kinetic.mp4`、`remotion-steps.mp4`、`remotion-comparison.mp4`：6/8/6秒静音竖屏动效。
- `media-probe.json`：实际视频的ffprobe完整结果与哈希。
- `frames/`、`frame-review.json`：首帧/中帧/末帧抽取及底色、非静态检查记录。
- `canvas-prototype.png`、`canvas-test-report.json`：真实浏览器截图与16项交互检查。
- `verification-report.json`：最近一次离线验收结果，重复验收会更新此文件。
- `交付文档-创作画布研究与规划.pdf`：12页中文交付报告，可独立下载。

PNG与MP4为本次实际输出；长片计划放在 `examples/`，没有冒充5–10分钟成片。技术探测不等同完整人工审片。完整范围见 [交付文档](../docs/交付文档-Hermes验收.md)。

追加原图、视频、alpha指标、对照PDF与画廊见 [ab-2026-10-23](ab-2026-10-23/README.md)。原12页交付PDF为初版快照；新增实验以独立A/B报告为准。
