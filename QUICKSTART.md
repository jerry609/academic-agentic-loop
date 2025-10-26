# Quick Start Demo

## 🎯 立即试用研究调研系统

### 1️⃣ 启动 Claude Code
```bash
cd /Users/jerry/Sec4AI/academic-agentic-loop
claude
```

### 2️⃣ 运行示例命令

#### 基础示例：生成 3 个研究探索
在 Claude Code 对话中输入：
```
/research_deep_dive seed_papers/transformer_attention_summary.md research_output 3
```

**期望输出：**
- `research_output/research_1.md` - 理论扩展方向
- `research_output/research_2.md` - 方法论变体
- `research_output/research_3.md` - 应用迁移

---

## 📝 使用你自己的种子论文

### 方式 1: 创建论文摘要文件

创建 `seed_papers/your_paper.md`：

```markdown
# Your Paper Title

**Authors:** Author et al., Year

## Key Contributions
- Contribution 1
- Contribution 2

## Methods
- Method description

## Limitations
- Limitation 1
- Limitation 2

## Potential Research Directions
- Direction 1
- Direction 2
```

然后运行：
```
/research_deep_dive seed_papers/your_paper.md output 5
```

### 方式 2: 直接使用研究主题

```
/research_deep_dive "Graph Neural Networks for drug discovery" gnn_research 5
```

---

## 🚀 进阶使用

### 大规模探索（10个方向）
```
/research_deep_dive seed_papers/transformer_attention_summary.md large_exploration 10
```

### 无限模式（持续生成直到上下文耗尽）
```
/research_deep_dive seed_papers/transformer_attention_summary.md infinite_output infinite
```

预期生成 **20-50+** 个研究方向，涵盖：
- 理论扩展
- 方法变体
- 跨领域应用
- 局限性解决
- 批判性分析
- 范式转换

---

## 📊 输出文件结构

每个生成的 `research_N.md` 包含：

```markdown
# Research Exploration N: [标题]

## 1. 与种子论文的联系
[如何基于/扩展/挑战原论文]

## 2. 核心研究问题
- 问题 1
- 问题 2

## 3. 动机与创新性
[为何重要，填补什么空白]

## 4. 提议方法
[高层方法论，关键技术]

## 5. 期望贡献
[预期新见解，对领域的影响]

## 6. 评估策略
[如何验证，指标，基��]

## 7. 挑战与局限
[技术困难，资源需求]

## 8. 种子论文之外的相关工作
[需要调研的其他论文/理论]

## 9. 未来方向
[后续问题，长期轨迹]
```

---

## 🔍 工作流程示例

### 完整研究探索流程

```bash
# Step 1: 广度探索（10个方向）
/research_deep_dive seed_papers/transformer_attention_summary.md phase1_broad 10

# Step 2: 人工审阅，选出最有前景的 3 个
# 假设选中了 research_3.md, research_7.md, research_9.md

# Step 3: 对选中方向进行深度探索
/research_deep_dive phase1_broad/research_3.md phase2_vision_deep 8
/research_deep_dive phase1_broad/research_7.md phase2_efficient_deep 8
/research_deep_dive phase1_broad/research_9.md phase2_theory_deep 8

# 现在你有：
# - 10 个广度探索
# - 24 个深度探索（3 × 8）
# - 总计 34 个研究方向
```

---

## 💡 实际应用场景

### 1. 文献综述准备
```
/research_deep_dive "Self-supervised learning in computer vision" lit_review 15
```
生成 15 个不同角度的文献综述方向。

### 2. 研究提案构思
```
/research_deep_dive seed_papers/your_preliminary_work.md proposal_ideas 10
```
为基金申请生成 10 个研究方向。

### 3. 博士论文规划
```
/research_deep_dive seed_papers/thesis_topic.md phd_plan infinite
```
生成全面的 3-5 年博士研究议程。

### 4. 跨学科探索
```
/research_deep_dive "Combining neuroscience and machine learning for interpretability" interdisciplinary 12
```

---

## ⚡ 关键特性

### ✅ 自动去重
系统会分析已有输出，确保每个新方向都是独特的。

### ✅ 并行生成
多个研究代理同时工作，快速生成多样化方向：
- 1-5 个：全部并行
- 6-15 个：分批并行（每批 5 个）
- infinite：波次生成

### ✅ 渐进复杂度
无限模式下，后期波次会探索更激进的范式转换。

### ✅ 学术质量保证
每个输出都包含完整的研究计划要素（问题、方法、评估、局限）。

---

## 🛠️ 故障排查

### 命令未找到？
确保文件存在：
```bash
ls .claude/commands/research_deep_dive.md
```

### 输出目录为空？
检查命令是否完成，或查看错误信息。

### 生成质量不高？
- 使用更详细的种子论文摘要
- 减少并发数量（3-5 个质量更高）
- 提供更具体的研究领域描述

---

## 📚 示例种子论文主题

创建这些摘要文件并尝试：

1. **AI 安全**
   - "Constitutional AI: Harmlessness from AI Feedback"
   - "Scalable Oversight for AI Alignment"

2. **深度学习**
   - "Diffusion Models for Image Generation"
   - "Vision Transformers"

3. **强化学习**
   - "Proximal Policy Optimization (PPO)"
   - "Offline Reinforcement Learning"

4. **NLP**
   - "Chain-of-Thought Prompting"
   - "Retrieval-Augmented Generation (RAG)"

5. **跨学科**
   - "Graph Neural Networks for Biology"
   - "Causal Inference in Machine Learning"

---

## 🎓 下一步

1. **试运行**：
   ```
   /research_deep_dive seed_papers/transformer_attention_summary.md test 3
   ```

2. **创建自己的种子论文**

3. **构建研究流水线**：
   - 种子论文 → 广度探索 → 深度探索 → 综合

4. **集成到你的工作流**：
   - 文献综述
   - 提案写作
   - 论文构思

---

**开始探索研究前沿！🚀**

需要帮助？查看 `RESEARCH_USAGE_GUIDE.md` 了解更多详情。
