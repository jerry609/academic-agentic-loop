# Tools Quick Reference Card

## 🚀 快速命令参考

### 📚 arXiv 文献搜索
```bash
python tools/arxiv_search.py "<关键词>" [数量]
```
**示例：**
```bash
python tools/arxiv_search.py "graph neural networks" 15
```

---

### 🎯 原创性评分
```bash
python tools/novelty_scorer.py <提案文件> [对比目录]
```
**示例：**
```bash
python tools/novelty_scorer.py research_1.md research_output/
```

---

### 📝 LaTeX 转换
```bash
python tools/latex_converter.py <markdown文件> [输出文件]
```
**示例：**
```bash
python tools/latex_converter.py research_1.md paper.tex
pdflatex paper.tex
```

---

### 📊 研究可视化
```bash
python tools/research_visualizer.py <研究目录> [输出文件]
```
**示例：**
```bash
python tools/research_visualizer.py research_output/ report.md
```

---

### 🤝 代理协作（Claude Code 内）
```bash
/research_collaborative <种子论文> <输出目录> <数量> <模式>
```
**模式：** `critique` | `refine` | `synthesize`

**示例：**
```bash
/research_collaborative seed_papers/transformer.md collab 5 critique
```

---

## 📋 完整工作流

```bash
# 1. 文献搜索
python tools/arxiv_search.py "attention mechanism" 20 > lit.json

# 2. 生成研究方向（Claude Code 内）
claude
/research_deep_dive seed_papers/paper.md phase1 10

# 3. 评分筛选
python tools/novelty_scorer.py phase1/research_1.md phase1/ > scores.json

# 4. 协作优化（Claude Code 内）
/research_collaborative phase1/research_3.md phase2 1 refine

# 5. LaTeX 转换
python tools/latex_converter.py phase2/round3/research_3_v3.md final.tex
pdflatex final.tex

# 6. 生成可视化
python tools/research_visualizer.py phase1/ evolution.md
```

---

## 🎯 快速决策

### 何时使用哪个工具？

| 需求 | 使用工具 |
|------|---------|
| 了解研究现状 | arXiv Search |
| 筛选最佳方向 | Novelty Scorer |
| 准备投稿 | LaTeX Converter |
| 展示研究规划 | Research Visualizer |
| 提升提案质量 | Collaborative Mode |

---

## ⚡ 性能参考

| 工具 | 典型耗时 |
|------|---------|
| arXiv Search (10篇) | 2-5 秒 |
| Novelty Scorer | <1 秒 |
| LaTeX Converter | <1 秒 |
| Visualizer (10文件) | 1-3 秒 |
| Collaborative (5提案) | 10-30 分钟 |

---

## 🔗 相关文档

- [ADVANCED_TOOLS_GUIDE.md](ADVANCED_TOOLS_GUIDE.md) - 详细使用指南
- [README.md](README.md) - 项目概览
- [QUICKSTART.md](QUICKSTART.md) - 快速开始
