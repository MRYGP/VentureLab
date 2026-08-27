# 产品卡字段规范

> 版本：v1.1 · 2026-08-27
> 目标：让每张产品卡既适合杨浏览，也适合关键词检索和未来 RAG 切片。

## 一、文件头

每张 `product.md` 使用以下 YAML 元数据。数组使用短语，不写长段结论。

```yaml
---
id: VL-P0000
name: Product Name
aliases: []
legacy_ids: []
entity_type: product
categories: []
user_tasks: []
mechanisms: []
innovation_patterns: []
outcomes: []
markets: []
source_platforms: []
learning_status: 待观察
yang_status: 未开口
evidence_ceiling: Ø
source_verification: Agent转述未回源
rag_status: canonical
last_updated: YYYY-MM-DD
recall_triggers: []
---
```

字段约束：

- `id`、`name`、`learning_status`、`yang_status`、`source_verification`、`rag_status`、`last_updated` 必填；
- `legacy_ids` 保存 `Cxx`、`KS-Pxxx` 等旧编号；
- `outcomes` 只写已核状态或明确的待观察状态；
- `learning_status` 只描述仓库对产品的理解进度，取 `待观察`、`观察中`、`已理解`、`已暂停`、`待结果回看`；不得用它表达是否已建正式案例；
- `yang_status` 只描述杨本人是否形成过观察，取 `未开口`、`已给第一印象`、`已完成观察`、`已判断暂停`；不得用 Agent 分析代替杨开口；
- `evidence_ceiling` 表示当前最高可用证据，不替代正文分项标记；
- `source_verification` 取 `原页已核`、`Agent转述未回源`、`混合`。它描述整张卡的来源核验天花板，不替代正文逐条来源属性；`混合` 卡中的高负重陈述仍须说明哪些已回原页、哪些只是转述；
- `rag_status` 取 `canonical`、`provisional`、`excluded`；默认检索只读 `canonical`；
- `recall_triggers` 使用杨可能产生的任务或灵感语言，不写空泛品类词。

## 二、固定正文

```markdown
# VL-P0000｜产品名

## 1. 一句话看懂

## 2. 为什么以后要召回它

## 3. 用户、任务与旧方案

## 4. 承重机制与创新结构

## 5. 用户选择与结果证据

## 6. 失败边界与不可照搬条件

## 7. 可迁移方向

## 8. 杨的观察与修正

## 9. 关联产品

## 10. 原始材料入口

## 11. 更新记录
```

章节可以写 `Ø`，不得删除关键未知。产品卡保持紧凑；详细证据表继续保留在正式案例或证据文件中。

## 三、陈述纪律

1. 每条高负重陈述继续使用 `F-M`、`F-P`、`I`、`H`、`Ø`。
2. 平台支持金额、榜单、评论数和项目方自述不得改写为利润或长期成功。
3. “为什么以后要召回它”写学习价值，不写创业推荐。
4. “可迁移方向”写机制和条件，不自动生成方案假设。
5. “杨的观察”链接原始观察文件，并区分原始判断与后续修正。
6. 产品卡更新只追加日期记录；发生重大结论变化时说明旧判断为何被修正。
7. 从 Agent 学习卡转录的平台数字、项目方说法或用户原句，在没有回到原页前不得只写成裸 `F-P`；至少保留 `Agent转述未回源` 的卡级或逐条标记。

## 四、关联关系

关联产品至少说明一种关系：

- `同任务不同机制`；
- `同机制不同场景`；
- `成功／失败对照`；
- `原品／改良品`；
- `品牌品／白牌`；
- `前代／后代`；
- `替代品／近零成本做法`。

关系必须有一句解释，不能只堆链接。

## 五、完成标准

一张产品卡至少满足：

- 能在 90 秒内看懂产品、任务和承重机制；
- 能知道它为什么被纳入；
- 能分辨事实、推断与未知；
- 能找到原始材料；
- 能回答以后什么灵感应召回它；
- 不需要阅读 Agent 原始报告才能判断是否继续深挖。
