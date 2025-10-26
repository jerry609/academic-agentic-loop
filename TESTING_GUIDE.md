# 测试指南 - 验证系统功能

## 🧪 快速测试流程

### 测试 1: 最小测试（单个研究探索）

**目标**: 验证系统基本功能

```bash
# 在 Claude Code 中运行
/research_deep_dive seed_papers/transformer_attention_summary.md test_single 1
```

**预期输出:**
- `test_single/research_1.md` 文件生成
- 包含完整的 9 个章节
- 探索一个独特的研究方向（如理论扩展或方法变体）

**验证清单:**
- [ ] 文件成功创建
- [ ] 包含所有必需章节（1-9）
- [ ] 研究问题具体且可行
- [ ] 方法论描述清晰

---

### 测试 2: 小批量并行（3 个探索）

**目标**: 验证并行代理协调

```bash
/research_deep_dive seed_papers/transformer_attention_summary.md test_parallel 3
```

**预期输出:**
```
test_parallel/
├── research_1.md  # 例：理论扩展到强化学习
├── research_2.md  # 例：高效稀疏注意力机制
└── research_3.md  # 例：视觉Transformer应用
```

**验证清单:**
- [ ] 3 个文件同时生成（并行执行）
- [ ] 每个文件探索不同维度
- [ ] 无内容重复
- [ ] 生成时间 < 5 分钟

---

### 测试 3: 中等批量（10 个探索）

**目标**: 验证批次管理和多样性

```bash
/research_deep_dive seed_papers/transformer_attention_summary.md test_medium 10
```

**预期行为:**
- **阶段 1**: 启动第一批 5 个代理（并行）
- **阶段 2**: 等待第一批完成
- **阶段 3**: 启动第二批 5 个代理（并行）

**预期输出:** 10 个研究探索文件，覆盖：
1-2. 理论扩展（不同方向）
3-4. 方法论变体
5-6. 应用领域迁移
7-8. 局限性解决
9-10. 批判分析或跨学科

**验证清单:**
- [ ] 10 个文件成功生成
- [ ] 分 2 批执行（观察输出日志）
- [ ] 研究方向多样化
- [ ] 生成时间 < 15 分钟

---

### 测试 4: 使用自定义种子论文

**步骤 1: 创建简单的种子论文**

创建 `seed_papers/test_custom.md`:

```markdown
# Test Paper: Simple Convolutional Neural Network

**Authors:** Test Author, 2025

## Key Contributions
- Simple 3-layer CNN for image classification
- Achieves 85% accuracy on CIFAR-10

## Methods
- Conv layers with ReLU activation
- Max pooling
- Fully connected output layer

## Limitations
- Only works on small images (32x32)
- Not robust to rotations
- Requires large training data

## Potential Research Directions
- Improve data efficiency
- Add rotation invariance
- Scale to larger images
```

**步骤 2: 运行测试**

```bash
/research_deep_dive seed_papers/test_custom.md test_custom 5
```

**预期输出:** 5 个针对简单 CNN 的研究探索：
- 提升数据效率的方法
- 增加旋转不变性
- 扩展到大图像
- 理论分析
- 替代架构

**验证清单:**
- [ ] 成功解析自定义种子论文
- [ ] 生成的研究与 CNN 主题相关
- [ ] 针对性解决列出的局限性

---

### 测试 5: 使用主题描述（无文件）

**目标**: 验证直接使用文本描述

```bash
/research_deep_dive "Graph Neural Networks for molecular property prediction" test_gnn 3
```

**预期输出:** 3 个关于 GNN 用于分子性质预测的研究探索

**验证清单:**
- [ ] 系统接受文本描述作为输入
- [ ] 生成的研究与 GNN 和分子相关
- [ ] 无需创建种子论文文件

---

## 🔍 调试常见问题

### 问题 1: 命令未识别

**症状:**
```
Unknown command: /research_deep_dive
```

**解决方案:**
```bash
# 检查命令文件是否存在
ls .claude/commands/research_deep_dive.md

# 如果不存在，确认你在正确的项目目录
pwd

# 重启 Claude Code
exit
claude
```

---

### 问题 2: 文件未生成

**症状:**
输出目录为空

**排查步骤:**
1. 检查种子论文路径是否正确
   ```bash
   ls seed_papers/transformer_attention_summary.md
   ```

2. 查看 Claude Code 输出是否有错误信息

3. 检查权限设置
   ```bash
   cat .claude/settings.json
   # 确保包含 "Write" 权限
   ```

---

### 问题 3: 生成内容重复

**症状:**
多个 `research_N.md` 文件内容相似

**原因:**
- 种子论文太简单，探索空间有限
- 并发代理过多（如 20+）

**解决方案:**
- 使用更复杂的种子论文
- 减少生成数量（推荐 5-10）
- 运行无限模式以获得渐进复杂度

---

### 问题 4: 生成速度慢

**症状:**
10 个探索耗时 > 20 分钟

**正常吗?**
是的，取决于：
- 种子论文复杂度
- Claude Code 响应时间
- 批次数量

**优化建议:**
- 从小数量开始（3-5）
- 避免过度复杂的种子论文
- 检查网络连接

---

## 📊 性能基准

### 预期性能指标

| 测试 | 生成数 | 批次 | 预期时间 | 文件大小 |
|------|--------|------|----------|----------|
| Test 1 | 1 | 1 | 2-4 min | 3-5 KB |
| Test 2 | 3 | 1 | 3-6 min | 9-15 KB |
| Test 3 | 10 | 2 | 8-15 min | 30-50 KB |
| Test 4 | 5 | 1 | 5-10 min | 15-25 KB |
| Test 5 | 3 | 1 | 3-6 min | 9-15 KB |

*实际时间因系统��载和网络条件而异*

---

## ✅ 完整测试清单

运行所有测试以验证系统完整性：

```bash
# 测试 1: 单个探索
/research_deep_dive seed_papers/transformer_attention_summary.md test1_single 1

# 测试 2: 并行 3 个
/research_deep_dive seed_papers/transformer_attention_summary.md test2_parallel 3

# 测试 3: 批量 10 个
/research_deep_dive seed_papers/transformer_attention_summary.md test3_medium 10

# 测试 4: 自定义种子论文（需先创建 test_custom.md）
/research_deep_dive seed_papers/test_custom.md test4_custom 5

# 测试 5: 主题描述
/research_deep_dive "Causal inference in machine learning" test5_topic 3
```

**全部通过标准:**
- [ ] 所有测试成功生成文件
- [ ] 无重复内容
- [ ] 每个文件包含 9 个完整章节
- [ ] 研究问题具体可行
- [ ] 总耗时 < 45 分钟

---

## 🎯 高级测试场景

### 场景 1: 迭代深化

```bash
# 第一轮：广度探索
/research_deep_dive seed_papers/transformer_attention_summary.md round1 10

# 人工选择 round1/research_3.md（假设是视觉Transformer）

# 第二轮：深度探索
/research_deep_dive round1/research_3.md round2_vision 8

# 结果：
# round1/ - 10 个广度方向
# round2_vision/ - 8 个深度方向
```

**验证:**
- [ ] round2 的研究比 round1 更具体
- [ ] round2 聚焦于视觉领域
- [ ] 无跨轮次重复

---

### 场景 2: 无限模式（谨慎测试）

```bash
# 警告：可能生成 20-50+ 文件，耗时 20-60 分钟
/research_deep_dive seed_papers/transformer_attention_summary.md test_infinite infinite
```

**观察要点:**
- [ ] 第一波（5 个）：基础扩展
- [ ] 第二波（5 个）：跨领域应用
- [ ] 第三波+：理论深化、范式转换
- [ ] 自动停止（接近上下文限制）

---

## 📝 测试报告模板

完成测试后，填写报告：

```markdown
## 测试环境
- 日期：2025-XX-XX
- Claude Code 版本：X.X.X
- 操作系统：macOS/Linux/Windows

## 测试结果

### Test 1: 单个探索
- ✅/❌ 文件生成
- 耗时：X 分钟
- 文件大小：X KB
- 备注：

### Test 2: 并行 3 个
- ✅/❌ 并行执行
- 耗时：X 分钟
- 多样性：✅/❌
- 备注：

### Test 3: 批量 10 个
- ✅/❌ 分批执行
- 耗时：X 分钟
- 覆盖维度数：X/6
- 备注：

### Test 4: 自定义种子论文
- ✅/❌ 成功解析
- 相关性：✅/❌
- 备注：

### Test 5: 主题描述
- ✅/❌ 无文件输入
- 结果质量：✅/❌
- 备注：

## 总体评估
- 整体通过率：X/5
- 建议改进：
```

---

## 🚀 下一步

测试通过后：

1. **阅读完整文档**: [RESEARCH_USAGE_GUIDE.md](RESEARCH_USAGE_GUIDE.md)
2. **创建自己的种子论文**: 在 `seed_papers/` 目录
3. **探索实际研究主题**: 使用你感兴趣的领域
4. **优化工作流**: 结合广度-深度探索策略

---

**祝测试成功！🎉**
