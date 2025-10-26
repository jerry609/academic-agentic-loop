# Academic Agentic Loop

> 🔬 **从种子论文到研究前沿的自动化探索系统**

基于 [Infinite Agentic Loop](https://github.com/IndyDevDan/infinite-agentic-loop) 改造的学术研究版本，使用 Claude Code 的并行代理协调能力，自动从种子论文生成多样化的研究探索方向。

---

## ✨ 核心功能

### 🎯 智能研究探索
- 📄 **输入**: 一篇种子论文（PDF/摘要/主题描述）
- 🤖 **处理**: 并行部署多个 AI 研究代理
- 📊 **输出**: 10-50+ 个独特的研究探索文档

### 🚀 并行代理系统
- **3 个探索** → 1 批并行生成（2-4 分钟）
- **10 个探索** → 2 批并行生成（6-12 分钟）
- **无限模式** → 持续波次生成直到上下文耗尽（20-60 分钟，生成 20-50+ 方向）

### 📚 研究维度覆盖
每个代理探索不同维度：
1. **理论扩展** - 应用到新的理论框架
2. **方法变体** - 改进或替代算法
3. **应用迁移** - 跨领域应用
4. **局限解决** - 针对性改进
5. **批判分析** - 挑战核心假设
6. **跨学科综合** - 融合其他领域见解

---

## 🎬 快速开始

### 安装前提
- [Claude Code](https://docs.anthropic.com/claude-code) 已安装
- 本仓库克隆到本地

### 5 分钟上手

```bash
# 1. 进入项目目录
cd academic-agentic-loop

# 2. 启动 Claude Code
claude

# 3. 在 Claude Code 中运行命令（生成 3 个研究方向）
/research_deep_dive seed_papers/transformer_attention_summary.md research_output 3
```

**输出示例：**
```
research_output/
├── research_1.md  # 理论扩展：Transformers 在强化学习中的应用
├── research_2.md  # 方法变体：线性复杂度的稀疏注意力机制
└── research_3.md  # 应用迁移：图神经网络的自注意力
```

---

## 📖 使用场景

### 1️⃣ 文献综述准备
```bash
/research_deep_dive "Self-supervised learning in NLP" lit_review 15
```
生成 15 个不同角度的文献综述框架。

### 2️⃣ 研究提案构思
```bash
/research_deep_dive seed_papers/your_preliminary_work.md grant_ideas 10
```
为基金申请生成 10 个可行的研究方向。

### 3️⃣ 博士论文规划
```bash
/research_deep_dive seed_papers/thesis_topic.md phd_plan infinite
```
生成全面的 3-5 年博士研究议程（20-50+ 方向）。

### 4️⃣ 跨学科探索
```bash
/research_deep_dive "Combining neuroscience and RL for interpretable AI" interdisciplinary 12
```

---

## 📂 项目结构

```
academic-agentic-loop/
├── .claude/
│   └── commands/
│       ├── infinite.md              # 原始 UI 生成命令
│       └── research_deep_dive.md    # ⭐ 研究探索命令
│
├── seed_papers/                     # 📥 输入：种子论文
│   └── transformer_attention_summary.md
│
├── research_output/                 # 📤 输出：研究探索
│   ├── research_1.md
│   └── ...
│
├── QUICKSTART.md                    # ⚡ 5 分钟快速开始
├── RESEARCH_USAGE_GUIDE.md          # 📘 完整使用指南
├── ARCHITECTURE.md                  # 🏗️ 系统架构文档
└── README.md                        # 本文件
```

---

## 🎨 命令参数详解

### 基本语法
```bash
/research_deep_dive <seed_paper_path> <output_dir> <count>
```

### 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| `seed_paper_path` | 种子论文路径或主题描述 | `seed_papers/paper.md` 或 `"Graph Neural Networks"` |
| `output_dir` | 输出目录 | `research_output` |
| `count` | 生成数量 | `1`, `5`, `10`, `infinite` |

### 生成数量建议

- **1-3**: 快速试验，了解系统输出
- **5-10**: 获得多样化的研究角度
- **15-20**: 全面覆盖研究空间
- **infinite**: 穷尽探索，生成 20-50+ 方向

---

## 📊 输出文件格式

每个生成的 `research_N.md` 包含完整的研究计划：

```markdown
# Research Exploration N: [创新标题]

## 1. 与种子论文的联系
## 2. 核心研究问题
## 3. 动机与创新性
## 4. 提议方法
## 5. 期望贡献
## 6. 评估策略
## 7. 挑战与局限
## 8. 种子论文之外的相关工作
## 9. 未来方向
```

**质量保证：**
- ✅ 学术严谨性（适合发表的水平）
- ✅ 具体可行性（1-3 年内可完成）
- ✅ 唯一创新性（避免重复）
- ✅ 完整评估计划（指标、基准、数据集）

---

## 🔬 工作流程示例

### 完整研究探索流程

```bash
# Step 1: 广度探索（10 个不同方向）
/research_deep_dive seed_papers/transformer.md phase1_broad 10

# Step 2: 人工审阅，选出最有前景的 3 个
# 假设选中了 research_3.md（视觉Transformer）
#            research_7.md（高效注意力）
#            research_9.md（理论分析）

# Step 3: 对选中方向进行深度探索（每个方向 8 个变体）
/research_deep_dive phase1_broad/research_3.md phase2_vision 8
/research_deep_dive phase1_broad/research_7.md phase2_efficient 8
/research_deep_dive phase1_broad/research_9.md phase2_theory 8

# 结果：
# - 10 个广度探索
# - 24 个深度探索（3 × 8）
# - 总计 34 个研究方向可供选择
```

---

## 🧠 系统工作原理

### 并行代理协调

```
种子论文
    ↓
深度分析（贡献、方法、局限）
    ↓
生成 6 个探索维度
    ↓
┌─────────────────────────────────┐
│  并行部署研究代理                │
│                                 │
│  Agent 1 → 理论扩展              │
│  Agent 2 → 方法变体              │
│  Agent 3 → 应用迁移       [并行] │
│  Agent 4 → 局限解决              │
│  Agent 5 → 批判分析              │
└─────────────────────────────────┘
    ↓
5 个独特的研究探索文档
```

### 批次管理策略

- **1-5 个**: 单批并行
- **6-20 个**: 每批 5 个，分批执行
- **infinite**: 波次生成，渐进复杂度
  - Wave 1-2: 直接扩展
  - Wave 3-4: 跨领域应用
  - Wave 5+: 范式转换

详见 [ARCHITECTURE.md](ARCHITECTURE.md) 📐

---

## 🛠️ 创建自己的种子论文

### 方式 1: 使用现有论文摘要

创建 `seed_papers/your_paper.md`：

```markdown
# Your Paper Title

**Authors:** Author et al., Year
**Venue:** Conference/Journal

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

### 方式 2: 直接使用研究主题

无需创建文件，直接在命令中描述：

```bash
/research_deep_dive "Causal inference in deep learning" causal_dl_research 8
```

---

## 📚 示例种子论文主题

项目包含示例：
- ✅ `transformer_attention_summary.md` - Attention Is All You Need

推荐尝试的主题：

**AI/ML:**
- Diffusion Models for Image Generation
- Proximal Policy Optimization (PPO)
- Chain-of-Thought Prompting
- Retrieval-Augmented Generation (RAG)

**跨学科:**
- Graph Neural Networks for Drug Discovery
- Neuroscience-Inspired Attention Mechanisms
- Causal Machine Learning
- Quantum-Inspired Algorithms for Optimization

---

## 🎯 特色功能

### ✅ 自动去重
系统分析已有输出，确保每个新方向都是独特的。

### ✅ 学术质量保证
每个输出都包含：
- 具体研究问题（非泛泛而谈）
- 可行的方法论
- 明确的评估计划
- 诚实的局限性讨论

### ✅ 渐进复杂度（无限模式）
后期波次探索更激进的范式转换和跨学科融合。

### ✅ 上下文优化
高效管理并行代理，在上下文限制内最大化输出。

---

## 📖 完整文档

- **⚡ [QUICKSTART.md](QUICKSTART.md)** - 5 分钟上手指南
- **📘 [RESEARCH_USAGE_GUIDE.md](RESEARCH_USAGE_GUIDE.md)** - 详细使用说明
- **🏗️ [ARCHITECTURE.md](ARCHITECTURE.md)** - 系统架构与技术细节

---

## 🚀 进阶用法

### 组合工作流

```bash
# 1. 广度探索
/research_deep_dive seed_papers/topic.md broad 10

# 2. 选择 Top 3

# 3. 深度探索
/research_deep_dive broad/research_3.md deep1 8
/research_deep_dive broad/research_7.md deep2 8
/research_deep_dive broad/research_9.md deep3 8

# 4. 综合成文献综述或研究提案
```

### 与文献数据库结合（未来）

```bash
# 计划中：集成 arXiv/Semantic Scholar
/research_deep_dive seed.md output 10 --with-literature-search
```

---

## 🤝 贡献与反馈

### 改进方向

- [ ] 集成 MCP Server 用于真实文献检索
- [ ] 添加原创性评分算法
- [ ] 实现代理间协作模式
- [ ] 支持 LaTeX 输出格式
- [ ] 构建研究演化可视化

欢迎提交 Issue 和 Pull Request！

---

## 📜 许可证

本项目基于 [Infinite Agentic Loop POC](https://github.com/IndyDevDan/infinite-agentic-loop) 改造。

---

## 🙏 致谢

- **原始项目**: [IndyDevDan/infinite-agentic-loop](https://github.com/IndyDevDan/infinite-agentic-loop)
- **Claude Code**: [Anthropic](https://docs.anthropic.com/claude-code)
- **教程视频**: [Infinite Agentic Loop Tutorial](https://youtu.be/9ipM_vDwflI)

---

## 🎓 引用

如果在学术工作中使用本工具，建议引用：

```bibtex
@software{academic_agentic_loop,
  title = {Academic Agentic Loop: Automated Research Exploration from Seed Papers},
  author = {Your Name},
  year = {2025},
  url = {https://github.com/yourusername/academic-agentic-loop},
  note = {Based on Infinite Agentic Loop by IndyDevDan}
}
```

---

<div align="center">

**🚀 开始探索研究前沿！**

[![Claude Code](https://img.shields.io/badge/Claude-Code-blue)](https://docs.anthropic.com/claude-code)
[![Agentic](https://img.shields.io/badge/Agentic-Loop-green)](https://github.com/IndyDevDan/infinite-agentic-loop)

[快速开始](QUICKSTART.md) • [使用指南](RESEARCH_USAGE_GUIDE.md) • [系统架构](ARCHITECTURE.md)

</div>
