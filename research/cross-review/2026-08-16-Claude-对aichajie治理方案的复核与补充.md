# Claude｜对 aichajie 治理方案的复核与补充

> 日期：2026-08-16
> 治理工单：GOV-2026-08-16-AICHAJIE
> 来源：杨转交的 Claude 复核意见；本文件用于保留交叉复核原始判断与 Codex 本轮最小核验记录。
> 外部来源：无。
> 凭证边界：本轮不展示、不转录、不二次核验凭证内容；凭证类风险按“第一个发现者核实并记录，其他 Agent 不为交叉验证重复读取”的纪律处理。

## 90 秒版本

Claude 接受“不并仓、原地冻结、P0 安全优先、aichajie 只作为 L2 邻近自有样本”的主方案，但补充了六处需要改严的地方：

1. 凭证风险应按账号级处理，立即撤销或轮换，不等审计结果；
2. 任何 diff 或 git 操作前，先做仓外冷拷贝；
3. 理论文档先判断是“旧版本快照”还是“两套编号体系撞号”，再决定冻结或改编号；
4. README 顶部必须直说“不要按 Step 1 配置 Claude Project”；
5. DR01 自有先验应登记两条，而不是只登记 C 端转 B 端；
6. “杨回答三问”应提前，因为它低成本且可能改变后续审计优先级。

Codex 本轮最小核验确认：`DOC-S036` 编号冲突成立。`aichajie` 的 `DOC-S036` 是《规则制定者》，而 `sanxiangwendao` 的 `DOC-S036` 对应《精益创业：用科学实验代替赌博》；`sanxiangwendao` 中《规则制定者》另映射为 `DOC-S038`。这更像编号体系冲突或历史分叉，不应直接预设为“母版旧快照”。

## 一、Claude 独立复核的两条

### 1. S036 编号冲突：成立

Claude 核对了两边：

- `aichajie/01-knowledge-base/theory/DOC-S036-规则制定者.md` 正文讲的是主权与规则制定，包括赵长鹏、Starlink 等案例；
- `sanxiangwendao/rag-index/indexes/DOC-S036.yaml` 的标题是“精益创业：用科学实验代替赌博”。

同一编号对应两个无关文档，因此 S036 冲突成立。

Codex 本轮补充核验：

- `D:\aichajie\01-knowledge-base\theory\DOC-S036-规则制定者.md` 标题为《规则制定者：从改写规则到制定规则》；
- `D:\sanxiangwendao\02-shu\innovation\精益创业.md` 标题为《精益创业：用科学实验代替赌博》；
- `D:\sanxiangwendao\rag-index\doc-mapping.md` 将 `DOC-S036` 映射到 `精益创业.md`；
- `D:\sanxiangwendao\rag-index\doc-mapping.md` 将 `规则制定者.md` 映射到 `DOC-S038`。

证据标签：`F-P`。
能证明：存在跨仓编号冲突。
不能证明：aichajie 理论文档一定是 sanxiangwendao 的旧快照，也不能证明应批量改号。
反证条件：若后续发现 aichajie 有独立编号规范，需按独立体系处理，而不是按 sanxiangwendao 旧版快照处理。

### 2. 凭证风险：接受，但不复验内容

Claude 接受 Codex 关于凭证风险的判断，但没有再次读取 `.git/config`。理由是：如果为了“独立核实”再读一次同一份凭证，就会把凭证内容拉进第二个上下文，扩大暴露面。

建议写入后续治理规则：

> 凭证类风险由第一个发现者核实并记录，其他 Agent 不得为验证而重复读取。

这与普通交叉复核不同。普通事实需要多方核验；凭证风险则应避免重复暴露。

## 二、Claude 接受的纠正

### 1. “aichajie 就是 EarnPath 第一版”定级过高

Claude 接受将 aichajie 定级为 `L2 邻近自有样本`，而不是 EarnPath 第一版。

理由：两者用户阶段不同。aichajie 面向“已有项目去评估”，EarnPath 当前讨论的是“还没有方向时去选择或验证一条个人赚钱路线”。按 DR01 购买证据分级，aichajie 只能作为邻近自有样本。

### 2. 不新建 `VentureLab/cases/`

Claude 接受“不为 aichajie 新建 `cases/` 目录”的纠正。

理由：VentureLab 当前没有 `cases/` 治理定义。自有样本应留在 `research/claude/` 或 `research/cross-review/` 报告层，并明确标注“自有样本，不计入外部分母”。

### 3. 整体方案接受

Claude 接受以下整体方向：

- 不并仓；
- 四类资产分别路由；
- P0 安全优先；
- S00 不占预算、不计入外部分母；
- DCC 回溯先于盲案例；
- DR01 先验标为 `F-P`，不可外推。

## 三、Claude 的六条补充

### 1. 这不是 aichajie 一个仓的问题，而是账号级问题

git log 中出现过类似“remove hardcoded GitHub token from COMPLETED-PUSH.bat”和“filter-branch rewrite”的记录，意味着 token 曾经进入提交历史。

Claude 判断：

- `filter-branch` 只重写本地历史。如果相关提交曾经推送过，GitHub 上的旧对象仍可能通过 commit SHA 访问一段时间；
- 如果 PAT 带有 repo 级权限，风险边界可能覆盖同账号下的 VentureLab、EarnPath、aichajie 等多个仓。

建议：P0 第一步措辞改成“立即撤销或轮换，不等审计结果”，并检查同账号其他仓是否有同类残留，例如 `.bat`、`.ps1`、CI 配置、`.git/config`。

证据标签：`F-P` 指向风险线索，权限范围仍为 `H`。
禁止外推：不能从 commit message 推断 token 当前仍有效或权限范围具体为何；但安全处理上应按已泄露处理。

### 2. 在任何 diff 之前，先冷拷贝一份

Claude 建议先把 `D:\aichajie` 整目录做一次纯文件复制，再开始分析未提交改动。

理由：三十多个未提交改动时间久、来源不明。冷拷贝是现场保护，优先级应高于 diff、提交或归档。

约束：备份位置必须符合 privacy 约定，不能进入任何 git 跟踪范围，也不能随手放进会同步或公开的位置。

### 3. “理论 Snapshot”定性可能是错的

Claude 指出，P2 若直接要求逐篇比对 8 篇、全仓扫描编号引用、登记 `_cross_refs.yaml` 冻结告警，实际预设了“这 8 篇是母版旧副本”。

S036 的证据也可能指向另一种性质：两套独立编号体系撞号。

| 实际情况 | 正确处理 |
|---|---|
| 同一文档的旧版本 | Snapshot 冻结、登记告警 |
| 两套独立编号体系 | 给 aichajie 编号加前缀或去编号；登记 Snapshot 反而会制造“这是母版旧版”的错误印象 |

建议：P2 第一步改成“先比对 2—3 篇判断性质”，确认是版本差异还是体系撞号，再决定冻结、改编号或保留双编号说明。

### 4. 验收标准缺少“不得重新作为 Claude Project 当前知识包”

Claude 指出，`aichajie/README.md` 的快速开始 Step 1 教用户复制 `00-system/claude-project-instructions.md` 到 Custom Instructions，并上传 `01-knowledge-base/`。

如果未来有人照着 README 操作，撞号理论、旧评分体系和历史知识包会重新进入活跃使用。

建议 README 顶部状态声明第一句应明确写：

> 请勿按本文档 Step 1 配置 Claude Project。

中性措辞如“历史源仓/暂停维护”不足以阻止误用。

### 5. DR01 的自有先验应登记两条

Claude 建议 DR01 登记两条自有先验：

1. DCC 或相邻产品曾出现 C 端转 B 端方向；
2. `aichajie/README.md` 的三个使用场景中，“创业者自查”被设计成免费体检，而付费预期主要放在投资人筛选和大赛评审等机构侧。

两条都只能标记为：

- `F-P`；
- 邻近品类；
- 不可外推；
- 不参与外部市场分母；
- DR01 仍需独立验证。

反向诚实：README 中“免费”也可能只是获客漏斗设计，不能直接证明个人不愿付费。

### 6. 执行顺序应把“杨回答三问”提到第 2 位

Claude 建议顺序调整为：

1. token 撤销或轮换；
2. 冷拷贝；
3. 杨回答三问；
4. 其余审计。

三问是：

- aichajie 为什么停止？
- 是否有外部人真实使用或付款？
- DCC 真实结果如何？

理由：这些问题成本低，但可能改变后续动作优先级。如果答案显示项目停止原因与需求不成立有关，P2/P3 审计优先级会下降；如果存在外部付款，DR01 核心假设需要重排；如果只是转向 DCC，则 aichajie 更像暂停或路径迁移，而不是终止。

## 四、Claude 认为自己可能错在哪

1. 账号级 token 风险基于 git log 字面记录，没有查看 token 内容和权限范围。它可能早已过期或权限很低，但安全判断上宁可说重；
2. 冷拷贝会产生仓外完整副本。如果未提交改动里有敏感内容，备份本身可能扩大暴露面，因此备份位置必须先定；
3. S036 初始对照使用的是 aichajie 正文与 sanxiangwendao 索引 YAML，不是 sanxiangwendao 正文。Codex 本轮已补充用 sanxiangwendao 正文与 doc-mapping 复核。

## 五、Codex 本轮执行记录

### 已完成

- 保存本交叉复核文件；
- 用 sanxiangwendao 正文与索引映射补核 S036 编号冲突；
- 在 DR01 中登记两条自有先验；
- 在 DR02 中登记 `DR02-S00｜aichajie 历史源仓`，并明确不占外部样本预算、不计入外部分母。

### 未完成 / 暂停

- 未修改 `D:\aichajie\README.md`：工单要求先完成冷拷贝与未提交改动审计，且该路径不在当前可写根；
- 未做冷拷贝：需要杨指定仓外、非同步、非 git 跟踪的备份位置；
- 未修改 EarnPath 的 E000：`D:\EarnPath` 不在当前可写根，且需要先确认是否授权跨仓写入；
- 未保存 Claude 原始 aichajie 报告：本轮只收到交叉复核与治理工单，没有收到该“原始报告”全文；不可编造原文。

## 六、建议给杨的决策问题

1. 是否已经撤销或轮换 GitHub PAT？如果没有，应先做，不等待仓库审计；
2. `D:\aichajie` 冷拷贝放在哪里？建议使用一个不在任何 git 仓库、不同步云盘、权限本地可控的位置；
3. 是否授权 Codex 后续跨仓修改：
   - `D:\aichajie\README.md` 顶部禁用提示；
   - `D:\EarnPath\experiments\E000-判断能力校准.md` 中加入 DCC2026 候选案例。
