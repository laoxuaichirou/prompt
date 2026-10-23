# 提示词去重合并器 · 独立返工交付

执行时间：2026/10/23 20:36:02（北京时间）。仅处理返工单的片段簇、默认勾选、比较串口径三项。

完成: promptdedup.html（75937 B，74.16 KiB，sha256 20003b968f7ab94226e2592b2b515d20b702ab2b28d2870133f573f37595464d）。新包SHA256在归档外的SHA256SUMS及最终交付消息给出；包内报告不自引用ZIP哈希。

修复1 片段簇: 夹具F1最大簇=0（要求≤5）| 片段作主条=0 | F1-09/F1-10保留=是 | 折叠护栏25条→默认渲染0张成员卡、5条摘要代表，展开后25张。

修复2 默认勾选: 不变量断言通过（检查29项默认勾选）| 传递链C默认勾选=否 | 人工勾回后台账“低于阈值”标注=有。

修复3 归一化: 自检五项=0.615425164439 / 0.753562475387 / 0.780910144740 / 0.058064516129 / 0.036401436564 | 偏差≤0.002=是 | core-test exit=0。

三簇: S1+S2 / S3+S4 / S5+S6 | S7、S8未并入 | 发色槽位冲突出现在浏览器实际下载的conflicts.csv。

旧包SHA256: 57dbe1e0b488ff21bb46921212be70711a44902820b346b6c0364ee80988b3a7，改动前后均复算一致。原8条样例脚本区逐字节不变；F1与返工单JSON对象逐字段相同。

## 修复1 · 片段簇与大簇展示

- F1共10条：8条片段不进入配对/union；完整条目只比较1对。结果无重复候选簇，最大簇记为0，不是漏掉夹具。10条全部原样保留；F1-09、F1-10没有删除或并入片段。
- 25条同主题高度相似完整条目仍形成25成员簇；默认不创建.member卡片（0张），只显示簇头、大簇标记和5条代表，没有确认按钮。点击“展开全部”后真实DOM为25张，并出现逐条裁定控件。没有强拆或静默丢成员。
- 片段池可在已有完整提示词候选簇中手动补入，支持搜索和分批展示。实际勾选补入原文后，主条prompt追加、片段来源保留，主条不带入片段tag。仅补文字不会伪造删除来源的merged_from。

“单簇>20折叠”按返工单§1的展示护栏实现。它不等同于强制所有数据集聚类成员≤20；§7真实403条的最大簇约束留给Hermes实际验收，不在未拿到真实库时承诺结果。

## 修复2 · 默认勾选与传递链

合成链实算：A/B=0.725038402458，B/C=0.669524308325，A/C=0.302714819573。A与B同为最长、按原顺序推荐A；B默认勾选，C默认不勾。卡片显示“传递链并入（与主条0.303）”。

浏览器实际人工勾回C并确认、下载台账，记录真实分数0.302714820及“低于阈值，人工勾选”。导出merge_sim保存完整精度0.3027148195733541，不是取传递边分数。改选C为主条后，B默认勾选，低分A不自动勾回。reason和原台账结构未改，只增加低分标记。

## 修复3 · 五项实际数值

| 对 | 本轮实算 | 靶值 | 绝对偏差 | ±0.002 | 原SPEC条件 |
|---|---:|---:|---:|---|---|
| S1/S2 | 0.615425164439 | 0.615425 | 1.644385e-7 | 通过 | 通过 |
| S3/S4 | 0.753562475387 | 0.753562 | 4.753870e-7 | 通过 | 通过 |
| S5/S6 | 0.780910144740 | 0.780910 | 1.447400e-7 | 通过 | 通过 |
| S1/S3 | 0.058064516129 | 0.058065 | 4.838710e-7 | 通过 | 通过 |
| S7/S8 | 0.036401436564 | 0.036401 | 4.365645e-7 | 通过 | 通过 |

比较串明确删除空白及Unicode P*、Sm、Sk、So，`+`属于Sm所以删除；未指定的Sc货币类别不额外删除。前置全半角、小写、噪声前后缀逻辑保留。阈值0.50、权重0.6/0.4、短串12字和13个噪声词均未改。原文本、展示和字符diff不删标点；矩阵对应原条目、分数采用比较串。

按新口径得到五项正确实算，说明先前差异来自未明确的比较串口径；本次不修改原§6期望值或放宽容差。28对分数与独立字符DP及词频余弦复算的最大差为2.7755575615628914e-17。

## 实际执行记录

- `node core-test.cjs`：退出0，12项核心检查通过。包装器读取本HTML的dedup-core与rework-tests两个普通脚本区，不安装依赖。下列断言全部内嵌HTML，可由“运行内置算法自检”重跑；不是仅报告声称。
- `node browser-test.cjs`：退出0，15项本轮交互检查通过。真实浏览器加载HTML并执行自检按钮、F1导入、大簇展开、人工勾回、主条切换、片段池补入、刷新和三件套下载。
- 按“只发指定文件”要求，独立执行包装器和临时下载证据不加入新包；HTML内保留实际测试函数，报告保留逐条结果。没有截图、真实库、依赖目录或凭证。

### 内嵌核心断言

| 检查 | 实际结果 |
|---|---|
| 固定样例与默认参数边界 | 通过 |
| 比较串移除指定Unicode类别；原文不改 | 通过 |
| 五组校准实算值与原SPEC宽容差均通过 | 通过 |
| 28对与独立字符DP及词频余弦一致 | 通过 |
| 三簇、孤立项、发色冲突与未确认零删除 | 通过 |
| F1片段不建union、不能作主条、完整条保留 | 通过 |
| 所有夹具默认勾选均直接达到主条阈值 | 通过 |
| 传递链A~B~C：C默认不勾，更换主条重新推荐 | 通过 |
| 人工勾回低分C：真实分数与低于阈值台账 | 通过 |
| 来源池补入只追加原文，片段保留且不污染tags | 通过 |
| 25条完整合成簇保留全部成员，交给展示层折叠 | 通过 |
| 新比较语义与旧裁定上下文隔离 | 通过 |

### 浏览器交互断言

| 检查 | 实际结果 |
|---|---|
| page core assertions and isolated DOM guard | 通过 |
| isolated DOM guard default 0, expand 25 | 通过 |
| running selftest preserves user dataset and member controls | 通过 |
| F1 visible source pool and no fragment masters or deletions | 通过 |
| visible large cluster only summary before expansion | 通过 |
| visible expand-all renders every one of 25 members | 通过 |
| chain C is not checked and has transitive badge | 通过 |
| manual below-threshold C is really downloaded with true score | 通过 |
| changing master does not default-check former low-score main | 通过 |
| source-pool checkbox really appends original without deleting fragment | 通过 |
| source-pool selection survives actual reload | 通过 |
| three actual downloads exist | 通过 |
| downloaded sample preserves schema, all entries and hair-color conflict | 通过 |
| downloaded snapshot records new normalization and fragment policy | 通过 |
| no external page requests or uncaught app exceptions | 通过 |

浏览器环境：Chrome/154.0.8037.57。HTML无外部页面请求、无未捕获异常。三件套实际下载后的记录：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| prompts.dedup.json | 3526 | 3fa2ef1d114323875d29cd6faa0daf350151b17f51a29961967660de22a1bb19 |
| merge_report.md | 2365 | 34885aa1cf430cb5d797d5f174bebc0c6c3a4b994b9e3223a3bf4a935ec099ef |
| conflicts.csv | 824 | ae2473e74bfd94f588b8e64d04b1ad9c1a01933b67ce419d24017363cddb5f7a |

### 核心复跑方式

浏览器打开成品后点击内置自检即可运行核心与25条DOM断言。若Hermes用自己的Node包装器，可从HTML读取`dedup-core`、`rework-tests`脚本区，在Node执行后调用：

```js
await PromptDedupReworkTests.runCore(sample, fixtureF1);
// returned.passed必须为true，失败必须给非0退出码；不能修改断言。
```

25条DOM断言由页面内`PromptDedupReworkTests.runDOM()`执行；页面自检按钮会实际调用它，不把Node中的簇成员计数冒充渲染检查。

## 改动行

- promptdedup.html:165 — 算法口径纳入参数指纹，避免自动套用旧裁定。
- promptdedup.html:174 — 比较串末尾删除空白及P/Sm/Sk/So，样例和相似度公式不变。
- promptdedup.html:206 — 默认仅勾选与当前主条直接达到阈值的成员。
- promptdedup.html:226 — 片段进入独立来源池，不进入比较或union。
- promptdedup.html:269 — 保留完整条目补片段，并接入独立片段来源池。
- promptdedup.html:285 — 保留人工低分选择；限制并入仅为簇内完整条目，允许来源池补文字。
- promptdedup.html:304 — 低分人工并入记录真实相似度，台账明确低于阈值。
- promptdedup.html:304 — 补入来源片段时不删除来源、不污染主条tags。
- promptdedup.html:314 — 嵌入可复算传递链及其他合成夹具。
- promptdedup.html:327 — 内嵌F1、五组数值、默认勾选不变量和低分台账等可执行断言。
- promptdedup.html:399 — 内嵌25条大簇默认摘要、展开后25卡的真实DOM断言。
- promptdedup.html:424 — 大簇懒渲染；自测使用独立DOM容器避免改动用户数据。
- promptdedup.html:463 — 更换主条时重新按直接相似度推荐，避免自动勾回低分旧主条。
- promptdedup.html:481 — 片段池按需打开、搜索和每批50项展示，来源不参与删除合并。
- promptdedup.html:504 — 大于20条默认摘要及前5代表，展开后才创建全量成员卡与裁定控件。
- promptdedup.html:519 — 自检按钮执行内嵌核心断言与DOM护栏，显示五组实际分数。
- SPEC.md:3 — 仅补充比较串口径与§3.3三个新校准值，原§6容差不改。
- README.md:25 — 同步比较串口径、五组实算与复算方法。
- README.md:75 — 同步片段来源池、低分默认不勾及大簇折叠。

## 没做的 / 做不了的

1. 未取得或内嵌真实403条库；未声称跑过真实库，也未声称真实库最大簇一定≤20。Hermes报告的真实库结果作为问题来源，不当成本轮已复测证据。
2. file://双击与断网刷新未能验证：当前云端Chromium返回`net::ERR_BLOCKED_BY_ADMINISTRATOR`。未绕过策略；本轮交互验证使用仅绑定127.0.0.1的临时静态服务，不能代替file验收。
3. 未重新运行旧版1200/2000条性能测试，未验证Safari/Firefox或用户本机；不将旧性能数字冒充新口径结果。
4. 没有强制拆分完整提示词的大簇；>20仅默认折叠，保留全部成员，符合25条展开验收。
5. 本轮只发HTML、SPEC增补、README、TEST_REPORT、MANIFEST五个文件；不附截图、独立测试目录或真实数据。新包ZIP哈希在包外提供，MANIFEST不自哈希，避免循环引用。
