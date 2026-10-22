#!/usr/bin/env python3
"""Build an honest Chinese acceptance report from the actual test outputs."""
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

root = Path(__file__).resolve().parent.parent
read = lambda name: json.loads((root / 'results' / name).read_text(encoding='utf-8'))
core = read('core-validation.json')
browser = read('browser-validation.json')
core_cmd = read('core-command.json')
browser_cmd = read('browser-command.json')
functional = sum(x['passed'] for x in core['tests'])
ui_pass = sum(x['passed'] for x in browser['checks'])
blocked = [x for x in browser['checks'] if x.get('blocked')]
assert core['passed'] and not core['acceptancePassed']
assert all(x['passed'] or x.get('blocked') for x in browser['checks'])
assert core_cmd['exit_code'] == 2 and browser_cmd['exit_code'] == 2
size = (root / 'promptdedup.html').stat().st_size
now = datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')
rows = '\n'.join(f"| {x['entries']} | {x['totalPairs']:,} | {x['elapsedSeconds']:.3f} | {x['maxProgressGapMs']:.2f} | {x['intervalCallbacks']} |" for x in core['performance'])
text = f'''# 提示词去重合并器 · 实测交付报告

报告生成：{now}（北京时间）。原始日志保留 UTC 时间。

完成：`promptdedup.html`（{size} 字节，{size/1024:.2f} KiB）＋ README＋审查指令＋原始规格＋真实测试与导出样例。运行应用只需 HTML，不需要测试目录。

**总体不是全绿验收：** {functional}/{len(core['tests'])} 项核心功能检查通过；{ui_pass}/{len(browser['checks'])} 项浏览器检查通过，另有 {len(blocked)} 项被管理员策略阻止；附件的 2 项数值断言未通过。没有修改样例、阈值或公式，也没有把受阻测试改写成通过。

## 附件九项自查

| 项 | 有/无 | 实测证据与范围 |
|---|---|---|
| 1 双击打开、内置 8 条正常 | 无（未完成完整验证） | file 导航被管理员阻止；localhost 页面实际显示 8 条、3 簇，真实文件输入已验证 |
| 2 默认参数抓出三组重复 | 有 | S1+S2、S3+S4、S5+S6；与期望簇完全相同 |
| 3 S7、S8 未被并入 | 有 | 两条均未进入任何候选簇；未确认时 8 条全部保留 |
| 4 S5/S6 的 default 冲突进入 CSV | 有 | 实际下载并解析的 CSV 包含发色“棕黑 / 黑茶”冲突 |
| 5 手动改主条后导出 provenance 改变 | 有 | 浏览器选 S1 为主条并确认，下载 JSON 的 merged_from 为 S2，merge_sim 对应实分 |
| 6 勾补片段后 prompt 增加原文 | 有 | 浏览器勾选、确认后检查 JSON 末尾；核心另核对反向勾选顺序 |
| 7 刷新后裁定仍在 | 有（localhost） | 实际刷新保留 S1 主条、确认状态及一条补片段；另实际恢复裁定备份 |
| 8 三件套可打开、字段完整、含参数快照 | 有 | 浏览器实际下载三文件；JSON 解析、CSV 六列解析、Markdown 参数快照及逐簇台账检查 |
| 9 断网刷新不报错 | 无（未完成完整验证） | file 导航受策略阻止，不能声称断网刷新通过；已加载页面在浏览器离线状态重算通过 |

对应简写：**1无 2有 3有 4有 5有 6有 7有（localhost） 8有 9无**。

## 分数与独立复算

| 对 | 实际 | 附件断言 | 结论 |
|---|---:|---|---|
| S1/S2 | 0.649530455 | 0.63±0.03 | 通过 |
| S3/S4 | 0.789853501 | 0.78±0.03 | 通过 |
| S5/S6 | 0.736442358 | 0.78±0.03 | 未通过 |
| S1/S3 | 0.121518987 | <0.10 | 未通过 |
| S7/S8 | 0.100035808 | <0.25 | 通过 |

本实现把中文标点统一成 ASCII 标点，保留折叠后的单个空格，仅去噪声前后缀。所有 28 对与独立逐格 DP＋独立 2-gram 词频余弦实现一致，另外 180 对合成 Unicode 字符串的位并行 LCS 与 DP 一致。

反例可手算：S1/S3 长度 43/36、LCS 8、2-gram 余弦 0，故 `0.6×16/79=0.121518987`；按此明确归一化不可能同时满足 `<0.10`。S5/S6 长度 48/48、LCS 38、余弦 0.653605896，最终为 0.736442358。原归一化字符串保存在 `calibration-details.json`。这两项偏差作为未解决的规格数值差异交付，没有宣称附件验收全部通过。

## 架构与安全检查

- 单文件小于 350KB；vanilla JavaScript、零运行时依赖，无构建。
- 静态扫描确认无 fetch、XHR、远程脚本、样式外链、脚本模块或凭证输入；CSP 禁止网络连接。
- 浏览器没有外部 HTTP 请求、没有未捕获应用异常。测试用 localhost 服务与 CDP 只属于测试脚本，不属于应用。
- 用户输入作为文本/JSON 处理；不打开 `source`、`image_ref`；不改写导入对象或原文件。
- 人工确认前不合并；改选或改补片段后回到待确认状态。槽位冲突阻止并入并保留原条目。
- 模板默认排除但输出保留；片段禁止作主条；CSV 公式前缀已转义。
- 配额错误实际注入后红色错误常驻，实际导出备份成功。
- file 兼容性采用内嵌常量、文件输入、本地存储设计，但在本环境没有完成 file 的实际运行证明。

## 参数默认

阈值 0.50；权重 0.6/0.4；短串护栏少于 12 字；噪声词 13 条，默认开启，版本 `boundary-noise-v1-词表指纹`；标点/全半角、空白、英文小写默认开启；模板默认排除；分桶默认关闭。

## 实际性能

Node {core['runtime']}，将附件样例复制为合成压力条目，保持原提示词、改成唯一 ID。**不是真实 403 条库或真实 22 主题实测。**

| 条目数 | 候选比较对 | 实际耗时/秒 | 最大进度回调间隔/ms | 计时器回调次数 |
|---:|---:|---:|---:|---:|
{rows}

分片预算 160ms，再调用零延时计时器让出线程；上述计时器实际有机会运行。浏览器另外导入 1201 条合成短串验证强制提示与按 topic 分桶按钮。预估时间不保证在用户设备上相同，JSON 解析与极长单条的预处理未单独做性能上界验证。

单次缓存超过 600 万对明确拒绝并提示分桶/分批，差异超过 3000 万格不计算，均不静默删数据。

## 实际命令和退出码

| 命令 | 退出码 | 含义 |
|---|---:|---|
| `node tests/core-test.cjs` | {core_cmd['exit_code']} | 功能检查通过；两项附件数值断言未通过 |
| `node tests/browser-test.cjs` | {browser_cmd['exit_code']} | 可执行功能通过；两个 file 检查被策略阻止 |

日志：`results/core-test.log`、`core-validation.json`、`core-command.json`；浏览器对应 `browser-*`、`file-protocol.json`、桌面及手机截图。实际下载文件为 `browser-prompts.dedup.json`、`browser-merge_report.md`、`browser-conflicts.csv`。额外核心样例为 `example-*`，不是用户真实库导出。

## 已知限制及 schema 建议

详见 `UNVERIFIED.md`。不做同义词理解、简繁统一；并查集有传递链；分桶漏跨主题。localStorage 配额不固定，file 存储隔离依浏览器。tags 按并集后可能把来源的“片段”标签带到完整主条，建议上游未来区分条目类型和来源标签，本次不改 schema。
'''
(root / 'TEST_REPORT.md').write_text(text, encoding='utf-8')
unverified = '''# 未验证与未通过清单

- **未通过：** 按明确归一化及指定公式，S5/S6=0.736442358，未落在 0.78±0.03 内；S1/S3=0.121518987，不满足 <0.10。三簇检出仍正确，独立 DP 复算一致。未调阈值、样例或公式。
- **环境受阻 / 未验证：** 云端 Chromium 对 file 导航返回 net::ERR_BLOCKED_BY_ADMINISTRATOR，双击启动和 file 页面断网刷新没有执行成功。没有绕过策略，也没有把 localhost 验证当作 file 验证。
- **未提供 / 未验证：** 用户真实 403 条、22 主题的库；所有压力数据来自内嵌样例复制或明确标记的合成短串。
- **未验证：** 用户设备、Safari、Firefox、不同浏览器 file 存储隔离与实际配额、系统文件关联和批量下载设置。
- **未验证：** 极长单条的预处理性能上界、任意规模 JSON 解析时间。大库有显式候选对内存护栏；部分超长差异面板会明确不计算差异。
- **算法限制：** 非语义算法，不理解同义词；不统一简繁；并查集会形成传递簇；分桶无法查跨主题。
- **数据契约限制：** tags 并集可能给完整主条带入来源的“片段”标签，再导入仍按该标签处理；没有擅自修改 schema。
- **未做：** 没有接入项目、没有修改画布、没有访问用户本机、没有任何真实生成服务调用。
'''
(root / 'UNVERIFIED.md').write_text(unverified, encoding='utf-8')
print(json.dumps({'core_functional': [functional, len(core['tests'])], 'browser_passed': [ui_pass, len(browser['checks'])], 'blocked': len(blocked), 'full_acceptance_passed': False, 'html_bytes': size}, ensure_ascii=False))
