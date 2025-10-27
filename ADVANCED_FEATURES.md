# 高级功能与扩展指南

本文档包含系统的详细功能说明、高级用法和扩展方向。

---

## 📖 目录

1. [研究方向生成系统详解](#研究方向生成系统详解)
2. [文献爬取系统详解](#文献爬取系统详解)
3. [推荐工作流](#推荐工作流)
4. [高级工具套件](#高级工具套件)
5. [性能优化](#性能优化)
6. [扩展开发](#扩展开发)

---

## 研究方向生成系统详解

### 核心特性

#### 1. 并行代理协调
- **3-5 个代理同时工作**
- 每个代理探索不同的研究维度
- 自动去重和唯一性保证

#### 2. 六个探索维度
1. **理论扩展** - 应用到新的理论框架
2. **方法变体** - 改进或替代算法
3. **应用迁移** - 跨领域应用
4. **局限解决** - 针对性改进
5. **批判分析** - 挑战核心假设
6. **跨学科综合** - 融合其他领域见解

#### 3. 无限模式
- 持续生成 20-50+ 个研究方向
- 渐进式复杂度提升
- 自动上下文管理

#### 4. 输出格式
每个 `research_N.md` 包含完整的 9 章节：
1. 与种子论文的联系
2. 核心研究问题（2-4 个）
3. 动机与创新性
4. 提议方法
5. 期望贡献
6. 评估策略
7. 挑战与局限
8. 相关工作
9. 未来方向

### 使用场景详解

#### 场景 1: 文献综述准备
```bash
/research_deep_dive "Self-supervised learning in NLP" lit_review 15
```
**输出**: 15 个不同角度的综述框架
**用途**: 快速构建文献综述的结构

#### 场景 2: 研究提案构思
```bash
/research_deep_dive seed_papers/prelim_work.md grant_ideas 10
```
**输出**: 10 个可行的研究方向
**用途**: 为基金申请准备多个提案方向

#### 场景 3: 博士论文规划
```bash
/research_deep_dive seed_papers/thesis_topic.md phd_plan infinite
```
**输出**: 20-50+ 个研究议程
**用途**: 构建 3-5 年的研究路线图

#### 场景 4: 讨论准备
```bash
/research_deep_dive seed_papers/seminar_paper.md discussion 5
```
**输出**: 5 个讨论角度
**用途**: 为研讨会准备多样化讨论点

### 高级用法

#### 两阶段探索策略
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

## 文献爬取系统详解

### 核心特性

#### 1. 并行文献爬取
- **智能批次管理**
  - ≤5 篇：全部并行
  - 6-20 篇：分批处理（每批 5 个）
  - >20 篇：波次策略（每波 3-5 个）

#### 2. 智能引用网络构建
- 自动提取引用关系
- 构建有向引用图
- 识别关键节点（高引用论文）

#### 3. 结构化知识提取
从每篇论文提取：
- 研究问题（2-4 个）
- 方法论描述
- 关键贡献（3-5 点）
- 数据集和基准
- 结果总结
- 局限性
- 研究方向标签

#### 4. 迭代回归优化
- 相关性评分
- 质量指标计算
- 优先级权重动态调整
- 下一波次智能规划

#### 5. 输出格式

**knowledge_base.json**:
```json
{
  "papers": {
    "paper_1": {
      "metadata": {...},
      "knowledge": {...},
      "citations": [...]
    }
  },
  "citation_graph": {
    "nodes": [...],
    "edges": [...]
  },
  "metadata": {
    "seed_papers": [...],
    "crawl_depth": 2,
    "total_papers": 50
  }
}
```

**crawl_summary.md**:
- 统计信息
- 高影响力论文 Top 10
- 研究领域分布
- 推荐论文列表

### 数据源支持

#### 1. Semantic Scholar
- **用途**: 元数据、引用关系
- **API**: `https://api.semanticscholar.org/v1/paper/`
- **速率限制**: 100 请求/5分钟
- **优点**: 免费，数据全面

#### 2. arXiv
- **用途**: 预印本全文
- **API**: `http://export.arxiv.org/api/query`
- **速率限制**: 1 请求/3秒
- **优点**: 免费，全文访问

#### 3. CrossRef（计划中）
- **用途**: DOI 解析
- **API**: `https://api.crossref.org/works/`
- **速率限制**: 50 请求/秒
- **优点**: 权威的 DOI 数据库

#### 4. PubMed（计划中）
- **用途**: 生物医学文献
- **API**: `https://eutils.ncbi.nlm.nih.gov/entrez/`
- **优点**: 医学领域专业

### 使用场景详解

#### 场景 1: 单篇论文快速调研
```bash
/literature_crawler "arXiv:1706.03762" 1 attention_papers
```
- **爬取深度**: 1 层
- **预期论文数**: 30-50 篇
- **预期时间**: 5-10 分钟
- **用途**: 快速了解一篇论文的引用网络

#### 场景 2: 多篇种子论文
```bash
/literature_crawler "arXiv:1706.03762,arXiv:1810.04805" 2 transformer_network
```
- **种子论文**: Transformer + BERT
- **爬取深度**: 2 层
- **预期论文数**: 80-150 篇
- **预期时间**: 15-30 分钟
- **用途**: 构建特定主题的文献网络

#### 场景 3: 主题搜索
```bash
/literature_crawler "Graph Neural Networks" 2 gnn_literature
```
- **自动推荐**: 3-5 篇顶级 GNN 论文作为种子
- **爬取深度**: 2 层
- **预期论文数**: 100-200 篇
- **预期时间**: 20-40 分钟
- **用途**: 新领域的全面调研

#### 场景 4: 深度爬取
```bash
/literature_crawler "10.1145/3292500.3330989" 3 deep_crawl
```
- **爬取深度**: 3 层（最深）
- **预期论文数**: 150-300 篇
- **预期时间**: 30-60 分钟
- **用途**: 构建完整的研究图谱

---

## 推荐工作流

### 工作流 1: 新领域探索

```bash
# 步骤 1: 广度探索（10 个方向）
/research_deep_dive "Multimodal LLMs" broad 10

# 步骤 2: 人工审阅，选出 Top 3
# 假设选中 research_3.md, research_7.md, research_9.md

# 步骤 3: 深度探索（每个 8 个变体）
/research_deep_dive broad/research_3.md deep1 8
/research_deep_dive broad/research_7.md deep2 8
/research_deep_dive broad/research_9.md deep3 8

# 结果: 10 + 24 = 34 个研究方向
```

### 工作流 2: 文献驱动的研究规划

```bash
# 步骤 1: 爬取文献网络
/literature_crawler "Multimodal Learning" 2 multimodal_lit

# 步骤 2: 查看爬取总结
cat multimodal_lit/crawl_summary.md

# 步骤 3: 选择关键论文
# 从 Top 10 高影响力论文中选择 3 篇

# 步骤 4: 为每篇论文生成研究方向
/research_deep_dive multimodal_lit/papers/paper_5.md research1 10
/research_deep_dive multimodal_lit/papers/paper_12.md research2 10
/research_deep_dive multimodal_lit/papers/paper_23.md research3 10

# 结果: 100-200 篇文献 + 30 个研究方向
```

### 工作流 3: 深度研究规划

```bash
# 步骤 1: 从已有研究方向出发
existing_research="research_output/research_3.md"

# 步骤 2: 提取该方向提到的关键论文
# （手动或使用工具）

# 步骤 3: 爬取相关文献
/literature_crawler "extracted_paper_id" 2 deep_lit

# 步骤 4: 生成深度变体
/research_deep_dive deep_lit/papers/paper_X.md deep_variants 8

# 结果: 50-100 篇相关文献 + 8 个深度变体
```

### 工作流 4: 文献综述准备（未来整合命令）

```bash
# 整合命令（待实现）
/research_workflow "Attention Mechanisms" crawl_depth=3 explore_count=20

# 自动执行：
# 1. 推荐 5 篇种子论文
# 2. 爬取 3 层引用网络（100-200 篇文献）
# 3. 生成 20 个研究角度
# 4. 创建综述框架
# 5. 生成可视化报告

# 输出：
# - literature_output/knowledge_base.json
# - literature_output/citation_graph.html
# - research_output/research_1-20.md
# - reports/literature_review_framework.md
```

---

## 高级工具套件

### 1. arXiv 文献检索

**功能**: 实时搜索 arXiv 上的相关论文

**使用**:
```bash
python tools/arxiv_search.py "attention mechanism" 10
```

**输出**:
```
Found 10 papers:
1. Attention Is All You Need (2017) - 15234 citations
2. BERT: Pre-training of Deep Bidirectional Transformers (2018) - 12456 citations
...
```

**用途**:
- 快速找到相关论文
- 获取最新研究动态
- 作为文献爬取的种子

### 2. 原创性评分器

**功能**: 自动评估研究提案的创新性

**使用**:
```bash
python tools/novelty_scorer.py research_1.md research_output/
```

**输出**:
```
Novelty Score: 85/100

Breakdown:
- Uniqueness: 90/100 (highly unique approach)
- Feasibility: 80/100 (realistic within 2-3 years)
- Impact: 85/100 (significant potential contribution)

Comparison with existing research:
- Similar to research_3.md (similarity: 35%)
- Different from research_7.md (similarity: 12%)
```

**用途**:
- 评估研究方向的原创性
- 识别重复或相似的想法
- 排名多个研究提案

### 3. LaTeX 转换器

**功能**: 将 Markdown 研究提案转换为 LaTeX 文档

**使用**:
```bash
python tools/latex_converter.py research_1.md paper.tex
pdflatex paper.tex
```

**输出**: 可发表的 LaTeX 文档

**用途**:
- 快速生成论文草稿
- 准备会议投稿
- 创建研究提案文档

### 4. 研究可视化

**功能**: 生成研究演化图和维度分布

**使用**:
```bash
python tools/research_visualizer.py research_output/ report.md
```

**输出**:
- 维度分布饼图
- 研究演化时间线
- 相似度热力图
- 综合分析报告

**用途**:
- 可视化研究方向的多样性
- 识别研究热点
- 生成演示材料

### 5. 协作研究模式

**功能**: AI 代理相互评审和优化研究提案

**使用**:
```bash
/research_collaborative seed_papers/paper.md collab 5 critique
```

**模式**:
- **critique**: 代理相互批评和改进
- **synthesize**: 代理综合多个想法
- **debate**: 代理辩论不同方法
- **refine**: 代理迭代精化提案

**用途**:
- 提高研究提案质量
- 发现潜在问题
- 综合多个视角

---

## 性能优化

### 研究方向生成优化

#### 1. 批次大小调整
```bash
# 小批次（更快，但可能不够多样）
/research_deep_dive seed.md output 3

# 大批次（更多样，但更慢）
/research_deep_dive seed.md output 15
```

#### 2. 无限模式控制
- 默认生成 20-50+ 个方向
- 可以通过上下文监控提前终止
- 使用检查点恢复

#### 3. 种子论文质量
- 使用详细的种子论文摘要
- 包含关键贡献和局限性
- 提供潜在研究方向提示

### 文献爬取优化

#### 1. 爬取深度选择
- **深度 1**: 快速调研（5-10 分钟）
- **深度 2**: 平衡选择（15-30 分钟）
- **深度 3**: 深度调研（30-60 分钟）

#### 2. 种子论文选择
- 使用高引用的经典论文
- 选择综述论文获得更广覆盖
- 多个种子论文覆盖不同角度

#### 3. API 速率限制管理
- 系统自动处理速率限制
- 使用检查点避免重复请求
- 缓存已获取的元数据

#### 4. 上下文管理
- 大规模爬取时使用波次策略
- 定期保存检查点
- 渐进式摘要策略

---

## 扩展开发

### 1. 添加新数据源

**示例**: 添加 Google Scholar 支持

```markdown
# 在 .claude/commands/literature_crawler.md 中添加

**Google Scholar Client:**
- Endpoint: https://scholar.google.com/scholar?q={query}
- Parse HTML response
- Extract: title, authors, citations, year
```

### 2. 自定义知识提取

**示例**: 为机器学习论文添加特定提取

```markdown
**ML-Specific Knowledge Extraction:**
- Model architecture
- Training datasets
- Performance metrics (accuracy, F1, etc.)
- Hyperparameters
- Computational requirements
```

### 3. 创建整合命令

**示例**: 端到端研究工作流命令

```markdown
**RESEARCH WORKFLOW COMMAND**

Arguments:
1. topic - 研究主题
2. crawl_depth - 文献爬取深度
3. explore_count - 研究方向数量

Execution:
1. Call /literature_crawler
2. Analyze knowledge_base.json
3. Select top N papers
4. Call /research_deep_dive for each
5. Generate integrated report
```

### 4. 可视化工具开发

**示例**: 交互式引用图谱

```python
# tools/visualize_citation_graph.py
import json
import networkx as nx
from pyvis.network import Network

def visualize_graph(knowledge_base_path, output_html):
    # Load knowledge base
    with open(knowledge_base_path) as f:
        kb = json.load(f)
    
    # Create network graph
    G = nx.DiGraph()
    for paper_id, paper in kb['papers'].items():
        G.add_node(paper_id, 
                   title=paper['title'],
                   citations=paper['citation_count'])
    
    for edge in kb['citation_graph']['edges']:
        G.add_edge(edge['source'], edge['target'])
    
    # Generate interactive HTML
    net = Network(height='800px', width='100%')
    net.from_nx(G)
    net.save_graph(output_html)
```

### 5. MCP Server 封装

**目标**: 将系统封装为 MCP Server，供其他工具使用

**功能**:
- `crawl_literature(seed_papers, depth)` - 文献爬取
- `generate_research(seed_paper, count)` - 研究方向生成
- `evaluate_novelty(research_file)` - 原创性评估
- `visualize_network(knowledge_base)` - 网络可视化

---

## 总结

本文档涵盖了系统的高级功能和扩展方向。更多详细信息请参考：

- [QUICKSTART.md](QUICKSTART.md) - 快速上手
- [RESEARCH_USAGE_GUIDE.md](RESEARCH_USAGE_GUIDE.md) - 研究探索指南
- [COMMAND_REVIEW.md](COMMAND_REVIEW.md) - 命令审查
- [ARCHITECTURE.md](ARCHITECTURE.md) - 系统架构

**有问题或建议？** 欢迎提交 Issue 或贡献代码！
