# 快速开始 - 文献爬取系统

## ✅ 已完成

**核心命令已创建**：`.claude/commands/literature_crawler.md`

这个命令实现了完整的文献爬取功能，**无需编写任何 Python 代码**！

## 🚀 立即测试

### 1. 启动 Claude Code

```bash
cd academic-agentic-loop
claude
```

### 2. 运行第一个测试

在 Claude Code 对话中输入：

```bash
/literature_crawler "arXiv:1706.03762" 1 test_output
```

**这个命令会**：
1. 获取 "Attention is All You Need" 论文的元数据
2. 提取它引用的所有论文
3. 并行爬取这些引用论文的信息
4. 提取结构化知识
5. 生成知识库和报告

### 3. 查看输出

```bash
ls test_output/
# 应该看到：
# - knowledge_base.json      # 完整知识库
# - citation_graph.json      # 引用图谱数据
# - crawl_summary.md         # 爬取总结报告
# - papers/                  # 各个论文的详细信息
#   ├── seed_paper_1.md
#   ├── paper_1.md
#   ├── paper_2.md
#   └── ...
```

### 4. 查看知识库

```bash
cat test_output/knowledge_base.json
# 查看完整的知识库结构

cat test_output/crawl_summary.md
# 查看爬取总结报告
```

## 📖 使用示例

### 示例 1：单篇论文，浅层爬取
```bash
/literature_crawler "arXiv:1706.03762" 1 attention_papers
```
- 爬取深度：1 层
- 预期论文数：30-50 篇
- 预期时间：5-10 分钟

### 示例 2：多篇种子论文
```bash
/literature_crawler "arXiv:1706.03762,arXiv:1810.04805" 2 transformer_network
```
- 种子论文：Transformer + BERT
- 爬取深度：2 层
- 预期论文数：80-150 篇
- 预期时间：15-30 分钟

### 示例 3：主题搜索
```bash
/literature_crawler "Graph Neural Networks" 2 gnn_literature
```
- 自动搜索 GNN 相关的顶级论文作为种子
- 爬取深度：2 层
- 预期论文数：100-200 篇
- 预期时间：20-40 分钟

### 示例 4：深度爬取
```bash
/literature_crawler "10.1145/3292500.3330989" 3 deep_crawl
```
- 爬取深度：3 层（最深）
- 预期论文数：150-300 篇
- 预期时间：30-60 分钟

## 🔄 与研究探索系统整合

### 工作流 1：从文献到研究方向

```bash
# 步骤 1：爬取文献网络
/literature_crawler "Multimodal Learning" 2 multimodal_lit

# 步骤 2：查看爬取总结，识别关键论文
cat multimodal_lit/crawl_summary.md

# 步骤 3：选择 Top 3 论文，生成研究方向
/research_deep_dive multimodal_lit/papers/paper_5.md research_output 10
```

### 工作流 2：深度研究规划

```bash
# 步骤 1：从已有研究方向出发
existing_research="research_output/research_3.md"

# 步骤 2：爬取该方向的相关文献
# （需要从 research_3.md 中提取关键论文）
/literature_crawler "extracted_paper_id" 2 deep_lit

# 步骤 3：生成深度变体
/research_deep_dive deep_lit/papers/paper_X.md deep_variants 8
```

## 📊 输出结构

```
test_output/
├── knowledge_base.json          # 完整知识库
│   ├── papers: {}              # 所有论文的元数据和知识
│   ├── citation_graph: {}      # 引用关系图
│   ├── metadata: {}            # 爬取元信息
│   └── queue: {}               # 队列状态
│
├── citation_graph.json          # 可视化用的图数据
│   ├── nodes: []               # 论文节点
│   └── edges: []               # 引用边
│
├── crawl_summary.md             # 爬取总结报告
│   ├── 统计信息
│   ├── 高影响力论文 Top 10
│   ├── 研究领域分布
│   └── 推荐论文
│
├── papers/                      # 论文详情
│   ├── seed_paper_1.md         # 种子论文
│   ├── paper_1.md              # 爬取的论文
│   ├── paper_2.md
│   └── ...
│
└── checkpoints/                 # 检查点（用于恢复）
    ├── wave_1.json
    └── wave_2.json
```

## 🎯 下一步

### 今天可以做的
1. ✅ 测试基础爬取功能（示例 1）
2. ✅ 验证输出格式
3. ✅ 检查知识提取质量

### 本周可以做的
1. 测试并行爬取（示例 2）
2. 测试多层爬取（示例 3）
3. 优化命令参数和输出
4. 创建整合命令

### 下周可以做的
1. 实现增量更新功能
2. 添加可视化工具
3. 完善文档
4. 端到端测试

## 💡 Pro Tips

### 1. 控制爬取规模
- 从 depth=1 开始测试
- 逐步增加到 depth=2, depth=3
- 注意 API 速率限制

### 2. 选择好的种子论文
- 使用高引用的经典论文
- 选择综述论文可以获得更广的覆盖
- 多个种子论文可以覆盖不同角度

### 3. 利用爬取结果
- 查看 crawl_summary.md 找到关键论文
- 使用高影响力论文作为研究探索的种子
- 分析研究领域分布找到热点方向

### 4. 整合工作流
- 文献爬取 → 识别关键论文 → 研究方向生成
- 形成完整的研究规划流程

## 🐛 故障排查

### 问题 1：命令未找到
```bash
# 确认命令文件存在
ls .claude/commands/literature_crawler.md

# 重启 Claude Code
exit
claude
```

### 问题 2：API 速率限制
- Semantic Scholar: 等待 5 分钟后重试
- arXiv: 等待 3 秒后重试
- 命令会自动处理，耐心等待

### 问题 3：论文未找到
- 检查 DOI/arXiv ID 是否正确
- 尝试使用论文标题搜索
- 查看错误日志了解详情

### 问题 4：输出不完整
- 检查是否达到上下文限制
- 减少爬取深度或种子论文数量
- 使用检查点恢复功能

## 📚 参考资源

- **命令文件**: `.claude/commands/literature_crawler.md`
- **需求文档**: `.kiro/specs/literature-crawler/requirements.md`
- **设计文档**: `.kiro/specs/literature-crawler/design.md`
- **任务列表**: `.kiro/specs/literature-crawler/tasks.md`
- **原项目**: https://github.com/disler/infinite-agentic-loop

---

**准备好开始爬取文献了吗？** 🚀

```bash
claude
/literature_crawler "your_paper_id" 1 output
```
