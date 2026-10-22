# DirectorX RH 任务三独立交付

[下载 directorx-rh-recovery-candidate.zip](directorx-rh-recovery-candidate.zip?raw=true)

若未直接下载，请在 ZIP 文件页点击 **Download raw file**。

这是与 UI 无关的 JavaScript 状态机候选，零 npm 运行时依赖，仅使用模拟服务。包含状态转换表、实现、模拟服务、具体故障测试、脱敏持久化样例、README、未验证清单和真实测试日志。

19 个具体故障场景实际通过，失败/跳过/取消均为 0。未接收密钥、未调用真实 API、未生成媒体、未修改或接入现有画布。

下载后解压，先运行 `node tools/verify.mjs` 核对哈希，再运行 `node tools/run-tests.mjs`。用 `node examples/offline-demo.mjs` 复现模拟状态样例。

提交未知时不会自动重发；有 taskId 只恢复原任务查询；下载重试不重新生成。421 无已知在途 ID 时保持等待，不能推断 RH 支持幂等键或本地 ID 查询。费用账本按 taskId 去重，null 保留未知，RH_COIN/CNY 分开。真实集成边界详见 ZIP 内文档。

任务一的 `directorx-web-review-delivery.zip` 保留原文件与哈希；本包是独立任务三候选，不覆盖任务一。
