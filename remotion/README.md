# 可复用口播动效：Remotion工程

3个原创模板已实际渲染，均为1080×1920、30fps、H.264 MP4、静音。适合作为口播B-roll/叠加设计的素材起点，配音、音乐与完整口播剪辑未包含。另有横版流程组件入口，但不把未渲染的横版视频写成已测试。

| Composition ID | 模板 | 时长 | 已交付文件 |
|---|---|---:|---|
| KineticWords | 关键词逐项进入 + 本次生成插画 | 6秒 | ../artifacts/remotion-kinetic.mp4 |
| ProcessSteps | 三步流程卡片 | 8秒 | ../artifacts/remotion-steps.mp4 |
| DataComparison | 数据对照条形图 | 6秒 | ../artifacts/remotion-comparison.mp4 |
| ProcessStepsLandscape | 横版流程组件 | 8秒 | 已定义，未输出样片 |

数据对照中的8步/3步是**虚构示例**，画面明确标注“示例数据·非实测”，没有宣称真实效率提升。三个竖屏模板把底部约17%区域留给外部字幕/平台UI；用于具体平台前仍需检查平台安全区。

## 重现

前提：Node.js 22或更新版本、npm、Chrome/Chromium、ffmpeg/ffprobe；中文需Noto Sans CJK SC、苹方或微软雅黑之一。本次机器使用Node24.19.0、Remotion4.0.538、React19.3.1和系统Chromium。依赖锁定在package-lock.json，不运行上游第三方Skill安装脚本。

```bash
cd remotion
npm ci --ignore-scripts
npm run typecheck
# Linux已有/usr/bin/chromium时：
npm run render:all
```

如果Chrome在其他位置，设置 `REMOTION_BROWSER_EXECUTABLE` 为真实浏览器路径，再运行上述渲染命令。例如macOS可指向 `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`。PowerShell请使用 `$env:REMOTION_BROWSER_EXECUTABLE=...`；npm脚本内的POSIX变量表达式推荐在Bash/WSL使用。也可直接用跨平台CLI：

```bash
npx --no-install remotion render src/index.ts KineticWords ../artifacts/remotion-kinetic.mp4 --browser-executable="你的Chrome完整路径" --concurrency=2 --crf=20
```

`npm ci --ignore-scripts`安装已锁定包；渲染本身只执行本地原创组件。仓库 `.npmrc` 把缓存放到 `/tmp/prompt-npm-cache`，适合Linux/macOS；Windows原生可用命令参数 `--cache` 指向本机可写目录。受限网络环境直接使用已安装浏览器，避免自动下载浏览器。

修改props的示例文件在 `props/`：

```bash
npx --no-install remotion render src/index.ts KineticWords ../artifacts/my-kinetic.mp4 --props=props/kinetic.json --browser-executable=/usr/bin/chromium --concurrency=2
npm run studio
```

文字长度和数据有运行时检查。动画全部由帧数驱动；同样props没有时间随机性。使用本地生图素材，不依赖在线CDN。要把素材接入长片，用Sequence编排整数帧，单独加入旁白音轨。

当前导出的H.264视频不透明。若需要透明叠加，应另实现ProRes 4444或其他支持alpha的格式并验证alpha通道，不能仅改扩展名。Remotion本身采用自定义许可，商用部署、团队规模与授权条件请查看 [官方LICENSE](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)。本仓库原创组件的MIT许可不覆盖Remotion依赖。
