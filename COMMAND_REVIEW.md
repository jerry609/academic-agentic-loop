# Literature Crawler 命令审查

## 📋 命令文件概览

**文件位置**: `.claude/commands/literature_crawler.md`

**命令格式**: `/literature_crawler <seed_papers> <crawl_depth> <output_dir>`

## ✅ 已实现的功能

### 1. 参数解析
- ✅ seed_papers: 支持 DOI/arXiv ID/标题/主题
- ✅ crawl_depth: 1-3 层爬取深度
- ✅ output_dir: 自定义输出目录

### 2. 六个执行阶段

#### Phase 1: 种子论文验证与初始化
- ✅ 识别论文标识符类型
- ✅ 从 Semantic Scholar/arXiv 获取元数据
- ✅ 创建知识库 JSON 结构
- ✅ 保存种子论文详情

#### Phase 2: 爬取队列准备
- ✅ 提取引用关系
- ✅ 优先级计算（引用数 + 时效性 + 相关性）
- ✅ 去重机制
- ✅ 按深度组织队列

#### Phase 3: 并行爬取协调
- ✅ 智能批次分配
  - ≤5 篇：全部并行
  - 6-20 篇：分批处理（每批 5 个）
  - >20 篇：波次策略
- ✅ Sub Agent 任务规范
- ✅ 错误处理和重试

#### Phase 4: 知识提取
- ✅ 结构化知识提取
  - 研究问题
  - 方法论
  - 关键贡献
  - 数据集和基准
  - 结果总结
  - 局限性
  - 研究方向标签

#### Phase 5: 回归分析与迭代
- ✅ 相关性评分
- ✅ 质量指标计算
- ✅ 优先级权重调整
- ✅ 下一波次准备
- ✅ 检查点保存

#### Phase 6: 输出生成
- ✅ 知识库 JSON
- ✅ 引用图谱数据
- ✅ 爬取总结报告
- ✅ 可视化数据准备

### 3. 数据源支持
- ✅ Semantic Scholar API
- ✅ arXiv API
- 📋 CrossRef API（已规划）
- 📋 PubMed API（已规划）

### 4. 输出格式
- ✅ knowledge_base.json（完整知识库）
- ✅ citation_graph.json（图数据）
- ✅ crawl_summary.md（总结报告）
- ✅ papers/*.md（论文详情）
- ✅ checkpoints/*.json（恢复点）

## 🎯 命令特点

### 优势
1. **完全无代码** - 纯命令驱动，无需编程
2. **并行高效** - 智能批次管理
3. **容错性强** - 完善的错误处理和重试
4. **可恢复** - 检查点机制
5. **结构化输出** - 标准 JSON 和 Markdown 格式

### 创新点
1. **动态优先级** - 基于回归分析调整
2. **波次管理** - 渐进式爬取策略
3. **知识提取** - 不仅是元数据，还有结构化知识
4. **质量控制** - 相关性评分和过滤

## 🔍 需要审查的关键点

### 1. API 调用逻辑

**当前设计**:
```markdown
1. Fetch metadata from Semantic Scholar API:
   - Endpoint: https://api.semanticscholar.org/v1/paper/{paper_id}
   
2. If Semantic Scholar fails, try arXiv API:
   - Endpoint: http://export.arxiv.org/api/query?id={arxiv_id}
```

**问题**:
- ✅ API 端点正确
- ⚠️ 需要确认 Claude Code 能否直接调用这些 API
- ⚠️ 速率限制处理是否足够

**建议**:
- 测试 API 调用是否成功
- 如果需要，添加更详细的错误处理

### 2. 并行协调策略

**当前设计**:
```markdown
If queue_size <= 5: Deploy all agents simultaneously
If 6 <= queue_size <= 20: Deploy in batches of 5
If queue_size > 20: Use wave strategy (5 agents per wave)
```

**问题**:
- ✅ 策略清晰合理
- ⚠️ 是否需要根据实际性能调整批次大小？
- ⚠️ 上下文限制是否会影响大规模爬取？

**建议**:
- 从小规模测试开始（3-5 篇论文）
- 逐步增加到 10-20 篇
- 观察性能和上下文使用情况

### 3. 知识提取质量

**当前设计**:
```markdown
Extract the following structured knowledge:
1. Research Questions (2-4 questions)
2. Methodology (brief description)
3. Key Contributions (3-5 points)
4. Datasets & Benchmarks
5. Results Summary
6. Limitations
7. Research Direction Tags
```

**问题**:
- ✅ 提取维度全面
- ⚠️ 仅基于摘要和元数据，可能不够深入
- ⚠️ 没有全文时，提取质量如何？

**建议**:
- 测试提取质量
- 如果质量不够，考虑添加更详细的提示
- 可以标注"基于摘要"vs"基于全文"

### 4. 优先级计算

**当前公式**:
```
priority = w1 * citation_count + w2 * recency + w3 * relevance
w1 = 0.4, w2 = 0.3, w3 = 0.3
```

**问题**:
- ✅ 公式合理
- ⚠️ 权重是否需要根据领域调整？
- ⚠️ 相关性如何计算（关键词重叠？）

**建议**:
- 测试不同权重的效果
- 实现简单的关键词匹配作为相关性指标
- 考虑添加用户可配置的权重

### 5. 输出格式

**knowledge_base.json 结构**:
```json
{
  "papers": {},
  "citation_graph": {},
  "metadata": {},
  "queue": {}
}
```

**问题**:
- ✅ 结构清晰
- ⚠️ 是否需要添加版本号？
- ⚠️ 是否需要添加爬取配置记录？

**建议**:
- 添加 schema_version 字段
- 记录爬取参数（seed_papers, depth, 权重等）
- 添加时间戳

## 🧪 建议的测试计划

### 测试 1: 单篇论文基础测试
```bash
/literature_crawler "arXiv:1706.03762" 1 test_single
```

**预期结果**:
- 1 篇种子论文
- 30-50 篇引用论文
- 完整的知识库 JSON
- 爬取总结报告

**验证点**:
- [ ] API 调用成功
- [ ] 元数据提取完整
- [ ] 引用关系正确
- [ ] 知识提取有意义
- [ ] 输出文件格式正确

### 测试 2: 并行处理测试
```bash
/literature_crawler "arXiv:1706.03762,arXiv:1810.04805" 1 test_parallel
```

**预期结果**:
- 2 篇种子论文
- 50-80 篇引用论文
- 并行处理日志

**验证点**:
- [ ] 并行协调正常
- [ ] 去重机制有效
- [ ] 没有重复爬取
- [ ] 性能提升明显

### 测试 3: 多层爬取测试
```bash
/literature_crawler "arXiv:1706.03762" 2 test_deep
```

**预期结果**:
- 1 篇种子论文
- 80-150 篇论文（2 层网络）
- 多个波次的检查点

**验证点**:
- [ ] 队列管理正确
- [ ] 优先级计算合理
- [ ] 回归分析有效
- [ ] 检查点可恢复

### 测试 4: 主题搜索测试
```bash
/literature_crawler "Graph Neural Networks" 2 test_topic
```

**预期结果**:
- 自动推荐 3-5 篇种子论文
- 100-200 篇相关论文
- 研究领域分析

**验证点**:
- [ ] 种子论文推荐合理
- [ ] 相关性评分准确
- [ ] 领域覆盖全面

## 🔧 可能需要的调整

### 1. API 调用细节
如果 Claude Code 无法直接调用 API，可能需要：
- 使用 curl 命令
- 添加更详细的错误处理
- 实现备用数据源

### 2. 上下文优化
如果大规模爬取遇到上下文限制：
- 减少每个 Agent 的输出详细度
- 使用更激进的摘要策略
- 增加检查点频率

### 3. 知识提取优化
如果提取质量不够：
- 添加更详细的提取提示
- 使用示例引导
- 分阶段提取（先粗后细）

### 4. 性能优化
如果速度太慢：
- 调整批次大小
- 优化 API 调用策略
- 减少不必要的处理

## 📝 审查结论

### 总体评价
**命令设计质量**: ⭐⭐⭐⭐⭐ (5/5)

**优点**:
- ✅ 架构清晰，逻辑完整
- ✅ 并行策略合理
- ✅ 错误处理完善
- ✅ 输出格式标准化
- ✅ 可扩展性强

**需要验证的点**:
- 🧪 API 调用是否成功
- 🧪 并行性能如何
- 🧪 知识提取质量
- 🧪 大规模爬取的稳定性

### 建议的下一步

1. **立即测试**（今天）
   ```bash
   claude
   /literature_crawler "arXiv:1706.03762" 1 test_output
   ```

2. **验证核心功能**（今天-明天）
   - API 调用
   - 元数据提取
   - 知识库生成

3. **测试并行和多层**（本周）
   - 并行处理
   - 多层爬取
   - 回归优化

4. **优化和完善**（下周）
   - 根据测试结果调整
   - 添加缺失功能
   - 完善文档

## 🎯 准备好测试了吗？

**推荐的第一个测试命令**:
```bash
claude
/literature_crawler "arXiv:1706.03762" 1 test_attention
```

这将爬取著名的 "Attention is All You Need" 论文及其引用网络，是一个很好的测试案例。

---

**你想现在开始测试吗？还是需要先调整命令文件？** 🚀
