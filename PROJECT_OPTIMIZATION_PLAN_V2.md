# 项目优化方案 V2 - 基于 Claude Code 命令系统

## 🎯 核心理念调整

### ❌ 错误理解（V1）
- 需要写 Python 代码实现文献爬取系统
- 需要实现复杂的类和模块
- 需要 17 个编程任务

### ✅ 正确理解（V2）
- **完全基于 Claude Code 的并行代理能力**
- **通过自定义命令编排多个 Sub Agent**
- **每个 Agent 负责特定的文献处理任务**
- **不需要写传统的 Python 代码**

## 🧠 原项目模式分析

### Infinite Agentic Loop 的核心
```
用户命令 → 主协调器 → 并行 Sub Agents → 生成多个输出
```

**关键文件**：`.claude/commands/infinite.md`
- 定义命令参数解析
- 编排并行代理任务
- 管理输出和迭代

**不需要**：
- ❌ Python 类和模块
- ❌ 复杂的代码架构
- ❌ 传统的软件工程实现

**只需要**：
- ✅ 一个 Markdown 命令文件
- ✅ 清晰的 Agent 任务规范
- ✅ 并行协调逻辑

## 🚀 调整后的实施方案

### 阶段 1：创建文献爬取命令（1-2 天）

**目标**：创建 `.claude/commands/literature_crawler.md`

**命令结构**：
```markdown
**LITERATURE CRAWLER COMMAND**

**ARGUMENTS:**
1. seed_papers - 种子文献（DOI/arXiv ID/主题）
2. crawl_depth - 爬取深度（1-3）
3. output_dir - 输出目录

**PHASE 1: SEED PAPER VALIDATION**
- 验证种子文献的可访问性
- 从 Semantic Scholar/arXiv 获取元数据
- 创建初始知识库文件

**PHASE 2: CITATION EXTRACTION**
- 提取种子文献的引用列表
- 构建待爬取队列
- 计算优先级

**PHASE 3: PARALLEL CRAWLING**
- 根据队列大小部署 Sub Agents
- 每个 Agent 处理特定文献集合
- 并行获取元数据和引用关系

**PHASE 4: KNOWLEDGE EXTRACTION**
- 部署知识提取 Agents
- 从文献中提取结构化信息
- 更新知识库

**PHASE 5: ITERATION & REGRESSION**
- 分析爬取质量
- 调整下一波次优先级
- 继续迭代直到达到深度限制
```

### 阶段 2：整合两个命令系统（1 天）

**创建整合命令**：`.claude/commands/research_workflow.md`

```markdown
**RESEARCH WORKFLOW COMMAND**

**执行流程**：
1. 调用 literature_crawler 爬取文献
2. 从知识库选择 Top N 论文
3. 调用 research_deep_dive 生成研究方向
4. 生成整合报告
```

### 阶段 3：优化现有系统（2-3 天）

**增强 research_deep_dive 命令**：
- 支持从知识库读取种子论文
- 添加文献引用上下文
- 生成与文献网络的关联

## 📂 调整后的项目结构

```
academic-agentic-loop/
├── .claude/
│   └── commands/
│       ├── research_deep_dive.md        # ✅ 已存在
│       ├── research_collaborative.md     # ✅ 已存在
│       ├── literature_crawler.md         # 📋 待创建（核心）
│       └── research_workflow.md          # 📋 待创建（整合）
│
├── .kiro/
│   └── specs/
│       └── literature-crawler/
│           ├── requirements.md           # ✅ 保留（作为参考）
│           ├── design.md                # ✅ 简化（命令设计）
│           └── tasks.md                 # ✅ 调整（命令任务）
│
├── seed_papers/                          # 种子论文
├── research_output/                      # 研究探索输出
├── literature_output/                    # 文献爬取输出
│   ├── knowledge_base.json              # 知识库
│   ├── citation_graph.json              # 引用图谱
│   └── papers/                          # 文献详情
│       ├── paper_1.md
│       └── paper_2.md
│
└── tools/                                # 辅助工具（可选）
    └── visualize_graph.py               # 可视化脚本
```

## 🎯 核心任务调整

### ❌ 删除的任务（不需要编程实现）
- ~~创建 Python 类和模块~~
- ~~实现 API 客户端~~
- ~~实现队列管理器~~
- ~~实现回归引擎~~
- ~~创建 CLI~~

### ✅ 保留的任务（命令编排）
1. **创建 literature_crawler.md 命令**
   - 定义参数解析
   - 设计 5 个执行阶段
   - 编排并行 Agent 任务

2. **设计 Sub Agent 任务规范**
   - 文献获取 Agent
   - 引用提取 Agent
   - 知识提取 Agent
   - 质量评估 Agent

3. **实现波次管理逻辑**
   - 1-5 个文献：全部并行
   - 6-20 个文献：分批处理
   - >20 个文献：波次迭代

4. **创建整合命令**
   - research_workflow.md
   - 串联两个系统

5. **优化输出格式**
   - 知识库 JSON 结构
   - 文献详情 Markdown 模板
   - 引用图谱数据格式

## 💡 关键实现细节

### 1. 文献获取（通过 Claude Code 的网络能力）

```markdown
**Sub Agent Task: Fetch Paper Metadata**

Given paper identifier: {paper_id}

1. Determine identifier type (DOI/arXiv/Title)
2. Use appropriate API:
   - Semantic Scholar: https://api.semanticscholar.org/v1/paper/{id}
   - arXiv: http://export.arxiv.org/api/query?id={id}
3. Extract metadata: title, authors, abstract, year, citations
4. Save to: literature_output/papers/paper_{n}.md
5. Return: paper_id, metadata_summary, citation_count
```

### 2. 并行协调（类似 research_deep_dive）

```markdown
**PARALLEL CRAWLING COORDINATION**

If queue_size <= 5:
  Deploy all agents simultaneously
  
If 6 <= queue_size <= 20:
  Deploy in batches of 5
  Wait for batch completion before next batch
  
If queue_size > 20:
  Use wave strategy:
  - Wave 1: Process top 5 priority papers
  - Analyze results and update priorities
  - Wave 2: Process next 5 papers
  - Continue until depth limit reached
```

### 3. 知识库管理（JSON 文件）

```json
{
  "papers": {
    "paper_1": {
      "id": "DOI:10.1234/example",
      "title": "...",
      "authors": [...],
      "abstract": "...",
      "year": 2023,
      "citations": [...],
      "cited_by": [...],
      "knowledge": {
        "research_questions": [...],
        "methods": [...],
        "contributions": [...]
      }
    }
  },
  "citation_graph": {
    "nodes": [...],
    "edges": [...]
  },
  "metadata": {
    "seed_papers": [...],
    "crawl_depth": 2,
    "total_papers": 50,
    "last_updated": "2024-01-01"
  }
}
```

## 🚀 立即可执行的行动

### 今天（1-2 小时）

1. **创建 literature_crawler.md 命令骨架**
   ```bash
   # 创建文件
   touch .claude/commands/literature_crawler.md
   
   # 定义基本结构
   # - 参数解析
   # - 5 个执行阶段
   # - Sub Agent 任务模板
   ```

2. **测试基础功能**
   ```bash
   # 在 Claude Code 中测试
   /literature_crawler "10.48550/arXiv.1706.03762" 1 test_output
   
   # 预期输出：
   # - test_output/knowledge_base.json
   # - test_output/papers/paper_1.md
   ```

### 本周（3-5 天）

1. **完善 literature_crawler 命令**
   - 实现所有 5 个阶段
   - 添加错误处理
   - 优化并行协调

2. **创建 research_workflow 整合命令**
   - 串联两个系统
   - 测试端到端流程

3. **更新文档**
   - 简化 design.md（移除编程实现部分）
   - 更新 tasks.md（改为命令任务）
   - 更新 README

## 📊 效果对比

### V1 方案（错误）
- ❌ 需要 2-3 周编程实现
- ❌ 17 个复杂的编程任务
- ❌ 需要维护大量代码
- ❌ 偏离原项目理念

### V2 方案（正确）
- ✅ 只需 3-5 天创建命令
- ✅ 5 个命令编排任务
- ✅ 零代码维护（纯命令）
- ✅ 完全符合原项目模式

## 🎯 成功标准

### 短期（今天）
- [ ] 创建 literature_crawler.md 骨架
- [ ] 定义参数解析逻辑
- [ ] 设计 Sub Agent 任务模板

### 中期（本周）
- [ ] 完成 literature_crawler 命令
- [ ] 能够爬取 1 层引用网络
- [ ] 生成知识库 JSON 文件
- [ ] 创建整合命令

### 长期（下周）
- [ ] 支持多层爬取
- [ ] 实现回归优化
- [ ] 完整的端到端测试
- [ ] 更新所有文档

## 💡 关键洞察

**原项目的精髓**：
> 不是写代码，而是**编排 AI 代理**

**Claude Code 的能力**：
- 并行执行多个 Sub Agent
- 每个 Agent 可以访问网络、读写文件
- 主协调器管理 Agent 的任务分配
- 自动处理上下文和结果收集

**我们要做的**：
- 设计清晰的 Agent 任务规范
- 编排合理的并行策略
- 定义标准的输出格式
- 实现智能的迭代逻辑

## 🚀 立即开始

**你想要我帮你：**

1. **创建 literature_crawler.md 命令骨架**
   - 我会创建完整的命令文件
   - 包含 5 个执行阶段
   - 定义 Sub Agent 任务规范

2. **简化现有的 spec 文档**
   - 移除编程实现部分
   - 改为命令设计文档
   - 更新任务列表

3. **更新项目文档**
   - 修正 README
   - 更新优化方案
   - 创建快速开始指南

**选择一个，我们立即开始！** 🚀
