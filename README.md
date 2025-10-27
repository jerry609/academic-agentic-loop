# Academic Agentic Loop

> 🔬 **从种子论文到研究前沿的自动化探索系统**

基于 [Infinite Agentic Loop](https://github.com/IndyDevDan/infinite-agentic-loop) 改造的学术研究版本。使用 Claude Code 的并行代理协调能力，实现文献爬取和研究方向生成。

---

## ✨ 核心功能

### 🎯 两大系统

#### 1. 研究方向生成（✅ 已完成）
- **输入**: 种子论文或研究主题
- **处理**: 并行部署 AI 研究代理
- **输出**: 10-50+ 个独特的研究探索方向

#### 2. 文献爬取系统（✅ 命令已创建）
- **输入**: 种子论文（DOI/arXiv ID）或主题
- **处理**: 并行爬取引用网络，提取结构化知识
- **输出**: 知识库、引用图谱、文献分析报告

---

## 🚀 快速开始（5 分钟）

### 启动 Claude Code
```bash
cd academic-agentic-loop
claude
```

### 方式 1：生成研究方向
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md output 5
```

**输出**: 5 个完整的研究探索文档（每个包含 9 个章节）

### 方式 2：爬取文献网络
```bash
/literature_crawler "arXiv:1706.03762" 1 lit_output
```

**输出**: 知识库 JSON + 引用图谱 + 爬取报告

---

## 📖 使用场景

| 场景 | 命令示例 | 预期输出 |
|------|----------|----------|
| **快速试验** | `/research_deep_dive seed.md test 3` | 3 个研究方向 |
| **文献综述** | `/research_deep_dive topic.md review 15` | 15 个综述角度 |
| **提案构思** | `/research_deep_dive work.md ideas 10` | 10 个可行方向 |
| **博士规划** | `/research_deep_dive topic.md phd infinite` | 20-50+ 研究议程 |
| **文献调研** | `/literature_crawler "topic" 2 output` | 50-100 篇论文网络 |

---

## 🔄 整合工作流

```
研究主题
    ↓
文献爬取 → 知识库 + 引用图谱
    ↓
识别关键论文
    ↓
研究方向生成 → 10-50+ 个探索方向
    ↓
质量评估 → 深度探索
```

**示例**:
```bash
# 1. 爬取文献
/literature_crawler "Graph Neural Networks" 2 gnn_lit

# 2. 查看推荐论文
cat gnn_lit/crawl_summary.md

# 3. 生成研究方向
/research_deep_dive gnn_lit/papers/paper_5.md research 10
```

---

## 📊 性能指标

### 研究方向生成
- **3 个方向**: 2-4 分钟
- **10 个方向**: 8-15 分钟（2 批并行）
- **无限模式**: 20-60 分钟（20-50+ 方向）

### 文献爬取
- **深度 1**: 10-30 篇，5-10 分钟
- **深度 2**: 50-100 篇，15-30 分钟
- **深度 3**: 100-300 篇，30-60 分钟

---

## 🎯 核心价值

### 为研究人员节省时间
- **文献调研**: 2-3 周 → 1-2 小时
- **研究构思**: 1-2 周 → 30 分钟
- **综述准备**: 1-2 月 → 1 天

### 输出质量保证
- ✅ 学术严谨性（适合发表水平）
- ✅ 具体可行性（1-3 年可完成）
- ✅ 唯一创新性（自动去重）
- ✅ 完整研究计划（9 个章节）

---

## 📚 完整文档

| 文档 | 用途 | 阅读时间 |
|------|------|----------|
| [QUICKSTART.md](QUICKSTART.md) | 5 分钟快速上手 | 3 分钟 |
| [QUICK_START_V2.md](QUICK_START_V2.md) | 文献爬取快速指南 | 5 分钟 |
| [RESEARCH_USAGE_GUIDE.md](RESEARCH_USAGE_GUIDE.md) | 研究探索详细指南 | 10 分钟 |
| [COMMAND_REVIEW.md](COMMAND_REVIEW.md) | 文献爬取命令审查 | 10 分钟 |
| [ARCHITECTURE.md](ARCHITECTURE.md) | 系统架构详解 | 15 分钟 |
| [TESTING_GUIDE.md](TESTING_GUIDE.md) | 测试验证指南 | 8 分钟 |

**建议阅读顺序**: QUICKSTART → QUICK_START_V2 → RESEARCH_USAGE_GUIDE

---

## 🛠️ 高级功能

### 工具套件
```bash
# arXiv 检索
python tools/arxiv_search.py "attention mechanism" 10

# 原创性评分
python tools/novelty_scorer.py research_1.md research_output/

# LaTeX 转换
python tools/latex_converter.py research_1.md paper.tex

# 可视化
python tools/research_visualizer.py research_output/ report.md
```

### 协作研究模式
```bash
/research_collaborative seed.md collab 5 critique
```
让 AI 代理相互评审、优化和综合研究提案。

---

## 📂 项目结构

```
academic-agentic-loop/
├── .claude/commands/              # Claude Code 命令
│   ├── research_deep_dive.md     # 研究探索
│   ├── research_collaborative.md  # 协作研究
│   └── literature_crawler.md      # 文献爬取
├── seed_papers/                   # 种子论文
├── research_output/               # 研究输出
└── literature_output/             # 文献输出
```

---

## 🎯 开发状态

### ✅ 已完成
- [x] 研究方向生成系统
- [x] 文献爬取命令
- [x] 并行代理协调
- [x] 工具套件

### 🧪 待测试
- [ ] 文献爬取基础功能
- [ ] 并行处理验证
- [ ] 多层爬取测试

### 📋 计划中
- [ ] 系统整合命令
- [ ] 可视化工具
- [ ] 增量更新

---

## 🙏 致谢

- **原始项目**: [IndyDevDan/infinite-agentic-loop](https://github.com/IndyDevDan/infinite-agentic-loop)
- **核心技术**: [Claude Code](https://docs.anthropic.com/claude-code)
- **教程视频**: [Infinite Agentic Loop Tutorial](https://youtu.be/9ipM_vDwflI)

---

<div align="center">

**🚀 开始你的研究之旅！**

[![Claude Code](https://img.shields.io/badge/Claude-Code-blue)](https://docs.anthropic.com/claude-code)
[![Research](https://img.shields.io/badge/Academic-Research-green)](https://github.com/IndyDevDan/infinite-agentic-loop)

[快速开始](QUICKSTART.md) • [使用指南](RESEARCH_USAGE_GUIDE.md) • [命令审查](COMMAND_REVIEW.md)

</div>
