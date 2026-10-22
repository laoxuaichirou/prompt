# 中文口播 / 字幕体检台 · 实测交付报告

## 1. 交付

独立四文件，应用无外部资源、无依赖、无构建。未访问用户本机，只在云端交付目录写入新文件；没有运行 Node/Python。

| 文件 | 字节数 |
|---|---:|
| srt-checker.html | 55292 |
| README.md | 8170 |
| TEST_REPORT.md | 13607 |
| UNVERIFIED.md | 2923 |


新仓库创建已实际尝试：`gh repo create laoxuaichirou/srt-checker-web-2026-10-23` 在GitHub账户查询阶段返回 `Forbidden`，退出1，没有创建成功。没有索要凭证或规避访问限制。改用此前已授权的现有仓库 `laoxuaichirou/prompt` 的独立交付分支提供四个文件的完整内容下载；不称作新仓库，不覆盖main或其他交付。发布后的真实固定提交URL由最终消息提供，不在此预填不存在的链接。

所有字幕规则、自测期望比较、压力统计都在普通浏览器页面内执行，点击“自测”“规则边界检查”“2000条压测”获得结果。自动化仅使用系统 Perl 标准组件启动本地静态服务、驱动浏览器真实鼠标点击、捕获页面结果与下载文件；没有在外部脚本实现或计算字幕规则。用户运行应用或自测不需要该驱动或任何终端。

## 2. 原始八项自测

原样例与期望ID集合未修改，阈值未调整。实际集合比较错误/警告；L2-CJK-LATIN-SPACE、L4-TYPO 为提示，另列、不计入错误集合。A合计硬检查包含所有级别。

| 测试项 | 期望ID集合 | 实际ID集合（错误/警告） | 提示ID | 结果 |
|---|---|---|---|---|
| 样例A 第1条 | ∅ | ∅ | ∅ | PASS |
| 样例A 第2条 | ∅ | ∅ | ∅ | PASS |
| 样例B 第1条 | L2-LONG-LINE、L3-YEAR | L2-LONG-LINE、L3-YEAR | L2-CJK-LATIN-SPACE | PASS |
| 样例B 第2条 | L2-END-PUNCT、L3-ACRONYM | L1-OVERLAP、L2-END-PUNCT、L3-ACRONYM | ∅ | FAIL |
| 样例B 第3条 | L1-TOO-SHORT、L4-DUPWORD | L1-TOO-SHORT、L2-END-PUNCT、L4-DUPWORD | ∅ | FAIL |
| 样例B 第4条 | L1-TOO-LONG、L2-HALFWIDTH-PUNCT、L3-DECIMAL、L3-PERCENT | L1-TOO-LONG、L2-END-PUNCT、L2-HALFWIDTH-PUNCT、L2-LONG-LINE、L3-DECIMAL、L3-PERCENT | L2-CJK-LATIN-SPACE | FAIL |
| 样例C 第1条 | ∅ | L2-END-PUNCT | ∅ | FAIL |
| 样例C 第2条 | L3-DIGITS | L2-END-PUNCT、L3-DIGITS | ∅ | FAIL |

**3 PASS / 5 FAIL；误报ID 6；漏报ID 0。没有合成准确率。**

样例A：第1条零命中、第2条零命中、合计 0 命中：PASS。

“误报ID”在这里严格表示相对给定基线的集合差集，并非主观证明检测无效。六个额外ID均可由通用规则复现：

- B2：开始3.5秒 < B1结束4秒，按规则必须报 L1-OVERLAP。
- B3：行尾是“强”，按规则必须报 L2-END-PUNCT。
- B4：行尾是“倍”且折算宽度20.5，必须额外报 L2-END-PUNCT、L2-LONG-LINE。
- C1：行尾是“了”，必须报 L2-END-PUNCT；未报 RANGE，1秒整未报过短。
- C2：行尾是“6”，必须额外报 L2-END-PUNCT；7秒整未报过长，12306正确报五位数字。

此外，A原文各15全角单位，不是说明中的13；B1原文35.5，不是说明中的26。这里保持字面全角/半角折算，没有改字符或排除标点来凑说明数值。

以上两组“通用规则 / 期望集合”不能同时全部满足，故**不宣称全部基线验收通过**。页面用红色FAIL原样显示，导出自测JSON保留期望、实际、额外及缺失ID。

### 额外页面边界检查

以下是独立标注的合成片段，不替代原八项；有些只验证指定规则存在/不存在，表中不将其夸称为全量语义正确性验证。

| 项 | 实际ID（所有级别） | 结果 |
|---|---|---|
| 1秒与18全角整不报 | ∅ | PASS |
| 7秒整不报过长 | ∅ | PASS |
| 零时长仅报过短不报倒置 | L1-TOO-SHORT | PASS |
| 0.999秒报过短 | L1-TOO-SHORT | PASS |
| 7.001秒报过长 | L1-TOO-LONG | PASS |
| 非三位毫秒报时间码 | L1-TIMECODE | PASS |
| 缺失序号 | L1-INDEX | PASS |
| 缺时间码仍保留正文 | L1-TIMECODE | PASS |
| 空正文 | L1-EMPTY | PASS |
| 三行正文 | L1-LINES | PASS |
| 中文数字不报朗读数字风险 | ∅ | PASS |
| 千位数字范围单位货币 | L2-CJK-LATIN-SPACE、L2-LONG-LINE、L3-ACRONYM、L3-CURRENCY、L3-DECIMAL、L3-RANGE、L3-THOUSANDS、L3-UNIT | PASS |
| 独立缩写边界与三位数字 | L2-CJK-LATIN-SPACE | PASS |
| 空白与中文半角句读 | L2-END-PUNCT、L2-HALFWIDTH-PUNCT、L2-SPACE、L3-ACRONYM | PASS |
| 重复词与三次啊 | L4-DUPWORD、L4-FILLER | PASS |
| 词表错字仅提示且有理由 | L4-TYPO | PASS |
| 口播按句号与空行切段 | ∅ | PASS |
| 5001字正文不执行正文规则 | ∅ | PASS |
| 5001条强制建议分批 | ∅ | PASS |

额外边界：19 PASS / 0 FAIL。5001字正文按要求提示并跳过，unprocessed明确记录L2–L4未执行；5001条明确显示建议分批。

## 3. 2000条压测与让出证据

**合成压力数据，不是用户真实库。** 用样例B正文循环500次，序号重编为1–2000，开始时间间隔10秒，保留3秒、1.5秒、0.6秒、8.5秒四种时长。没有改样例B原文作为基线；这里只生成独立压力数据。生成的数据无重复序号、非法时间码或重叠。

页面加载后浏览器被设为离线，两次压力测试均通过点击页面同一按钮运行。第二次显式设置DevTools六倍CPU降速，目的是实际覆盖160ms中途让出分支，不把降速结果冒充普通设备性能。最后已恢复为1倍。

| 模式 | 处理数 | 总耗时/ms | 让出次数 | 独立0ms计时器实际回调 | 最大工作片/ms |
|---|---:|---:|---:|---:|---:|
| 正常CPU | 2000 / 2000 | 74.60 | 2 | 2 | 52.70 |
| 显式六倍CPU降速 | 2000 / 2000 | 491.90 | 4 | 4 | 160.70 |

六倍降速的逐次让出记录（计时来自页面performance.now，不是编写的预估）：

```json
{
   "budget_ms" : 160,
   "heartbeat_count" : 4,
   "heartbeat_max_gap_ms" : 175.300000000745,
   "heartbeat_timer_ms" : 0,
   "max_work_slice_ms" : 160.70000000298,
   "max_yield_latency_ms" : 31.9000000022352,
   "yield_count" : 4,
   "yields" : [
      {
         "at_ms" : 57.2000000029802,
         "processed" : 0,
         "stage" : "体检",
         "total" : 2000,
         "wait_ms" : 31.9000000022352,
         "work_ms" : 21.3999999985099
      },
      {
         "at_ms" : 232.5,
         "processed" : 741,
         "stage" : "体检",
         "total" : 2000,
         "wait_ms" : 15,
         "work_ms" : 160.29999999702
      },
      {
         "at_ms" : 410.10000000149,
         "processed" : 1705,
         "stage" : "体检",
         "total" : 2000,
         "wait_ms" : 16.8999999985099,
         "work_ms" : 160.70000000298
      },
      {
         "at_ms" : 491.900000002235,
         "processed" : 2000,
         "stage" : "完成",
         "total" : 2000,
         "wait_ms" : 15.3000000007451,
         "work_ms" : 66.5
      }
   ]
}
```

单条完成后检查160ms预算，触达预算就await零延时计时器，并更新已处理/总数；解析前和完成后也有明确让出。单条不可被抢占，故最大工作片略超160ms，不虚报严格零误差。表中的独立计时器确有机会运行，进一步证明主线程任务之间实际让出，而非只更新数字。

首轮测量保留：2000条已处理完成，但当时使用25ms计时器作必要判据，运行结束前回调未发生，页面压力测试显示FAIL。随后改为独立零延时心跳并在完成时也明确让出，再实际重跑；没有手改日志中的FAIL，原八项的5个FAIL也始终保留。首轮摘录：

```json
{
   "elapsed_ms" : 88.7999999970198,
   "evidence" : {
      "budget_ms" : 160,
      "heartbeat_count" : 0,
      "heartbeat_max_gap_ms" : 0,
      "max_work_slice_ms" : 76.6999999992549,
      "max_yield_latency_ms" : 3.30000000074506,
      "yield_count" : 1,
      "yields" : [
         {
            "at_ms" : 12.0999999977648,
            "processed" : 0,
            "stage" : "体检",
            "total" : 2000,
            "wait_ms" : 3.30000000074506,
            "work_ms" : 8.29999999701977
         }
      ]
   },
   "passed" : false
}
```

## 4. file://、导入及实际下载

**file:// 双击、file页面导入/下载和断网刷新：未能验证。** 云端 Chromium 返回 `net::ERR_BLOCKED_BY_ADMINISTRATOR`；没有禁用或绕过管理员策略。以下通过仅绑定127.0.0.1的测试静态页面验证，加载后浏览器设为离线。localhost通过不能代替file通过。

```json
{
   "browser" : {
      "jsVersion" : "15.4.80.11",
      "product" : "Chrome/154.0.8037.57",
      "protocolVersion" : "1.3",
      "revision" : "@73c14f6228d7cd537c855007e8f88678969cc0eb",
      "userAgent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/154.0.0.0 Safari/537.36"
   },
   "browser_offline_during_buttons" : true,
   "external_requests" : [],
   "file_protocol" : {
      "navigation" : {
         "errorText" : "net::ERR_BLOCKED_BY_ADMINISTRATOR",
         "frameId" : "7BE89E2659AAB64CACEA761810D69B1B",
         "isDownload" : false,
         "loaderId" : "64285636D1807960D6EB4AB469F6FC81"
      },
      "opened" : false,
      "status" : "未能验证"
   },
   "uncaught_exceptions" : []
}
```

已通过真实文件输入验证：UTF-8 BOM样例A与内嵌原文一致；已知GBK片段“你好，字幕。”从UTF-8严格失败后回退正确；单个坏字节严格失败并显示中文错误；失败导入后旧结果导出按钮保持禁用。没有索要用户文件或访问用户本机。

页面实际点击并下载了三件套，自测JSON和测试记录Markdown也实际下载。文件名、字节数、SHA256如下，供区分真实下载与仅准备Blob：

| 页面下载文件 | 字节数 | SHA256 |
|---|---:|---|
| 样例B-issues.json | 10608 | f87aca25d53bec92e32863fbf7d04c599b51f5114d38ac6b72a0af3701ce8238 |
| 样例B-issues.csv | 3618 | 480047b784ebf901aaa162c0983a4de4c5e13b6261a450075e3db4ee36db5ccd |
| 样例B-report.md | 5291 | 6e88da65d1c0ea29bdd1f278d01c4e192536513eb2ff36ad820b43d95e77c9a1 |
| downloaded-selftest.json | 43811 | 4cb9650a22c2a59a01ca2900c4f4cfcc42bfe8d7af18abdc23cef269349b8d88 |
| downloaded-test-report.md | 2947 | db406f49b9be67e721d48a2d53d915020df38ba134c3f248ae34e98296c4e783 |

CSV实际BOM：PASS；下载后原编辑框仍等于样例B：PASS；390px窄屏无页面横向溢出：PASS。未实际使用桌面Excel打开。复制清单权限未实际验证。

## 5. 已知缺陷及验收缺口

| 级别 | 位置 | 复现 | 实际结果 | 最小修复或补验范围 |
|---|---|---|---|---|
| P0 | 当前已执行范围 | A合计硬检查及只读导出 | 未发现已知未修复的数据覆盖或干净样例误报；不等于证明所有输入无P0 | 真实库与不同浏览器另行验证，不扩大当前结论 |
| P1 规格冲突 | HTML：EXPECTED、checkStructure、checkText | 点击自测，查看B2/B3/B4/C1/C2 | 通用规则要求的6个额外ID导致5项FAIL | 规格维护时补齐期望集合，或明确修改规则范围；本次原断言、原规则均保留，不擅自改成PASS |
| P1 验收缺口 | 整个HTML的file协议入口 | 当前云端打开file URL | 管理员策略阻止，未能验证 | 在允许本地网页的独立浏览器补验，不绕过策略，不用localhost冒充 |
| P2 编码判别 | loadFile | 同一字节流对多种编码均有效 | 严格解码成功仍不能推断语义是否正确；完整歧义矩阵未验证 | 保留实际编码提示及手动选择；补充标注编码的边界语料 |
| P2 字符宽度 | lineWidth | 罕见Unicode、不同字体或无Intl.Segmenter环境 | 当前字符簇折算不是字体像素测量，相关边界未验证 | 补充明确的Unicode宽度规则和跨浏览器语料，保持18阈值 |
| P2 超大输入 | loadFile、analyzeText初始字符串处理 | 远超已测5001字的巨型文件 | 解码/分配仍同步，未做峰值上界验证；5001字会安全跳过正文 | 文件体积预警和分块解码/解析；未检查正文继续明确列入未处理 |

## 6. 未验证清单

详见UNVERIFIED.md：file入口与断网刷新、Safari/Firefox、GBK扩展/歧义、10万字以上单条及超大文件、真实字幕库和音频、Emoji复杂字形、桌面Excel、剪贴板权限、非标准SRT变体。已测5001字为跳过正文，不写成全部检查通过。

## 7. 红线逐条核对

- [x] 不访问用户电脑、不询问本机路径、不索要其他数据；只用内嵌样例和明确标注的合成数据。
- [x] 没有运行Node/Python；规则与自测均在页面按钮中执行，无终端自测要求。
- [x] 应用无网络调用、无同目录读取、无外链/CDN/字体/图片、无模块脚本、无eval、无凭证输入；普通内嵌script，系统字体。
- [x] 无依赖、无后端、无构建；单文件小于300KB。
- [x] 未写回源文件，实际下载的是新JSON/CSV/Markdown；不导出改好的SRT。
- [x] 固定24个规则ID；阈值不变，样例原文不变，错误/警告/提示分开。
- [x] A合计零命中实际通过；5项原基线FAIL照实保留，没有改为PASS。
- [x] 误报与漏报分开；没有合成准确率，没有把压力数据称作真实库。
- [x] 测试只访问回环静态服务；浏览器离线期间实际检查和下载，外部请求为零。GitHub发布是用户另行授权的交付操作，不属于应用运行。
- [x] 未验证项、跳过范围和环境受阻项全部明确披露。
