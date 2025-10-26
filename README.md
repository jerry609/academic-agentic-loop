# Academic Agentic Loop

> 🔬 **从种子论文到研究前沿的自动化探索系统**

基于 [Infinite Agentic Loop](https://github.com/IndyDevDan/infinite-agentic-loop) 改造的学术研究版本。使用 Claude Code 的并行代理协调能力，自动从种子论文生成多样化的研究探索方向。

---

## ✨ 核心功能

### 🎯 智能研究探索
- 📄 **输入**: 一篇种子论文（PDF摘要/Markdown/主题描述）
- 🤖 **处理**: 并行部署多个 AI 研究代理
- 📊 **输出**: 10-50+ 个独特的研究探索文档

### 🚀 并行代理系统
- **3 个探索** → 1 批并行生成（2-4 分钟）
- **10 个探索** → 2 批并行生成（6-12 分钟）
- **无限模式** → 持续波次生成（20-60 分钟，生成 20-50+ 方向）

### 📚 研究维度覆盖
1. **理论扩展** - 应用到新的理论框架
2. **方法变体** - 改进或替代算法
3. **应用迁移** - 跨领域应用
4. **局限解决** - 针对性改进
5. **批判分析** - 挑战核心假设
6. **跨学科综合** - 融合其他领域见解

---

## 🎬 快速开始（5 分钟）

### 第一步：启动 Claude Code
```bash
cd academic-agentic-loop
claude
```

### 第二步：运行命令（在 Claude Code 对话中）

#### 基础测试 - 生成 3 个研究方向
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md test_output 3
```

**输出示例：**
```
test_output/
├── research_1.md  # 理论扩展：Transformers 在强化学习中的应用
├── research_2.md  # 方法变体：线性复杂度的稀疏注意力机制
└── research_3.md  # 应用迁移：图神经网络的自注意力
```

---

## 📖 命令格式

### 基本语法
```bash
/research_deep_dive <seed_paper_path> <output_dir> <count>
```

### 4 种使用模式

#### 1. 单次生成（快速试验）
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md single 1
```

#### 2. 小批量（5 个方向）
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md batch_5 5
```
并行部署 5 个代理，每个探索不同维度。

#### 3. 中批量（10 个方向）
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md batch_10 10
```
分 2 批执行，每批 5 个代理。

#### 4. 无限模式（持续生成）
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md infinite_research infinite
```
持续生成 20-50+ 个研究方向，直到上下文耗尽。

---

## 📊 输出文件结构

每个 `research_N.md` 包含完整的 9 章节研究计划：

```markdown
# Research Exploration N: [创新标题]

## 1. 与种子论文的联系
## 2. 核心研究问题（2-4 个具体问题）
## 3. 动机与创新性
## 4. 提议方法
## 5. 期望贡献
## 6. 评估策略（指标、基准、数据集）
## 7. 挑战与局限
## 8. 相关工作
## 9. 未来方向
```

---

## 🎯 实际应用场景

| 场景 | 命令示例 | 预期输出 |
|------|----------|----------|
| **文献综述准备** | `/research_deep_dive "Self-supervised learning in NLP" lit_review 15` | 15 个综述角度 |
| **研究提案构思** | `/research_deep_dive seed_papers/prelim_work.md grant_ideas 10` | 10 个可行方向 |
| **博士论文规划** | `/research_deep_dive seed_papers/thesis_topic.md phd_plan infinite` | 20-50+ 研究议程 |
| **讨论准备** | `/research_deep_dive seed_papers/seminar_paper.md discussion 5` | 5 个讨论角度 |

---

## 🛠️ 使用自己的论文

### 方式 1: 创建论文摘要文件

创建 `seed_papers/your_paper.md`:

```markdown
# Your Paper Title

**Authors:** Author et al., Year

## Key Contributions
- Contribution 1
- Contribution 2

## Methods
Brief method description

## Limitations
- Limitation 1
- Limitation 2

## Potential Research Directions
- Direction 1
- Direction 2
```

运行：
```bash
/research_deep_dive seed_papers/your_paper.md output 5
```

### 方式 2: 直接使用研究主题

无需创建文件：
```bash
/research_deep_dive "Graph Neural Networks for drug discovery" gnn_research 5
```

---

## 💡 推荐工作流程

### 两阶段探索策略

```bash
# 阶段 1: 广度探索（10 个不同方向）
/research_deep_dive seed_papers/transformer.md phase1_broad 10

# 人工审阅，选出最有前景的 3 个
# 假设选中了 research_3.md, research_7.md, research_9.md

# 阶段 2: 深度探索（每个方向 8 个变体）
/research_deep_dive phase1_broad/research_3.md phase2_vision 8
/research_deep_dive phase1_broad/research_7.md phase2_efficient 8
/research_deep_dive phase1_broad/research_9.md phase2_theory 8

# 最终结果：
# - 10 个广度探索
# - 24 个深度探索（3 × 8）
# - 总计 34 个研究方向可供选择
```

---

## 🧠 系统工作原理

```
种子论文
    ↓
深度分析（贡献、方法、局限）
    ↓
生成 6 个探索维度
    ↓
┌──────────────────────────────┐
│  并行部署研究代理              │
│                              │
│  Agent 1 → 理论扩展           │
│  Agent 2 → 方法变体           │
│  Agent 3 → 应用迁移    [并行] │
│  Agent 4 → 局限解决           │
│  Agent 5 → 批判分析           │
└──────────────────────────────┘
    ↓
N 个完整研究探索文档
```

**详细架构**: 查看 [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 📚 完整文档

| 文档 | 用途 | 阅读时间 |
|------|------|----------|
| [QUICKSTART.md](QUICKSTART.md) | 5 分钟快速上手 | 3 分钟 |
| [RESEARCH_USAGE_GUIDE.md](RESEARCH_USAGE_GUIDE.md) | 详细使用指南 | 10 分钟 |
| [ARCHITECTURE.md](ARCHITECTURE.md) | 系统架构详解 | 15 分钟 |
| [TESTING_GUIDE.md](TESTING_GUIDE.md) | 测试验证指南 | 8 分钟 |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | 项目总结 | 5 分钟 |

**建议阅读顺序**: QUICKSTART → RESEARCH_USAGE_GUIDE → TESTING_GUIDE → ARCHITECTURE

---

## 📊 性能指标

| 生成数量 | 批次 | 预期时间 | 输出质量 |
|----------|------|----------|----------|
| 1 个 | 1 | 2-4 分钟 | 单一深度探索 |
| 5 个 | 1 | 3-6 分钟 | 多样化角度 |
| 10 个 | 2 | 8-15 分钟 | 全面覆盖 |
| infinite | 5-10 | 20-60 分钟 | 20-50+ 方向 |

---

## ✅ 快速验证

运行以下命令验证系统：

```bash
# 1. 检查命令文件
ls .claude/commands/research_deep_dive.md

# 2. 启动 Claude Code
claude

# 3. 运行测试（在 Claude Code 中）
/research_deep_dive seed_papers/transformer_attention_summary.md test 3

# 4. 查看结果
ls test/
cat test/research_1.md
```

---

## 🎓 核心价值

### 为学术研究者节省时间：
- **文献综述**: 5-10 小时 → 10 分钟
- **提案构思**: 2-3 天 → 30 分钟
- **博士规划**: 数周 → 1 小时

### 输出质量保证：
- ✅ 学术严谨性（适合发表水平）
- ✅ 具体可行性（1-3 年可完成）
- ✅ 唯一创新性（自动去重）
- ✅ 完整研究计划（9 个章节）

---

## 🔍 与原项目对比

| 维度 | 原版 Infinite Agentic Loop | Academic Agentic Loop |
|------|---------------------------|----------------------|
| **目标** | UI 组件生成 | 研究探索生成 |
| **输入** | UI 规范文件 | 种子论文/主题 |
| **输出** | HTML 文件 | Markdown 研究计划 |
| **命令** | `/project:infinite` | `/research_deep_dive` |
| **应用** | 前端开发 | 学术研究 |

**原项目仍然保留**: 可以继续使用 `/project:infinite` 生成 UI 组件。

---

## 🚧 未来增强计划

- [ ] 集成 arXiv API 进行真实文献检索
- [ ] 添加原创性评分算法
- [ ] 实现代理间协作模式
- [ ] 支持 LaTeX 输出格式
- [ ] 构建研究演化可视化

---

## 🙏 致谢

- **原始项目**: [IndyDevDan/infinite-agentic-loop](https://github.com/IndyDevDan/infinite-agentic-loop)
- **教程视频**: [Infinite Agentic Loop Tutorial](https://youtu.be/9ipM_vDwflI)
- **核心技术**: [Claude Code](https://docs.anthropic.com/claude-code)

---

## 📜 许可证

基于原项目改造，遵循相同的开源协议。

---

<div align="center">

**🚀 开始探索研究前沿！**

[![Claude Code](https://img.shields.io/badge/Claude-Code-blue)](https://docs.anthropic.com/claude-code)
[![Research](https://img.shields.io/badge/Academic-Research-green)](https://github.com/IndyDevDan/infinite-agentic-loop)

[快速开始](QUICKSTART.md) • [使用指南](RESEARCH_USAGE_GUIDE.md) • [系统架构](ARCHITECTURE.md)

</div>