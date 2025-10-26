# Research Deep Dive - Usage Guide

## 🎯 Purpose

This command enables you to **automatically explore research frontiers** starting from a seed paper. It deploys parallel AI research agents that investigate different theoretical, methodological, and application dimensions.

---

## 📋 Prerequisites

1. **Claude Code installed** and running
2. **Seed paper** prepared as:
   - PDF file in `seed_papers/` directory, OR
   - Markdown summary (like `transformer_attention_summary.md`), OR
   - Plain text description of research topic

---

## 🚀 Quick Start

### 1. Start Claude Code
```bash
cd /Users/jerry/Sec4AI/academic-agentic-loop
claude
```

### 2. Use the Research Deep Dive Command

#### Example 1: Single Research Exploration
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md research_output 1
```
This generates **1** research exploration document based on the Transformer paper.

#### Example 2: Small Batch (5 explorations)
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md research_output 5
```
Launches **5 parallel agents**, each exploring a different research direction:
- Agent 1: Theoretical extension
- Agent 2: Methodological variation
- Agent 3: Application domain transfer
- Agent 4: Limitation addressing
- Agent 5: Critical analysis

#### Example 3: Large Batch (15 explorations)
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md research_output 15
```
Generates **15 diverse research explorations** in batches of 5 agents.

#### Example 4: Infinite Research Mode
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md research_output_infinite infinite
```
Continuously generates research explorations until context limits, with progressive sophistication:
- **Wave 1-2**: Direct extensions (efficient attention, different domains)
- **Wave 3-4**: Theoretical analysis and hybrid methods
- **Wave 5+**: Paradigm-shifting alternatives

---

## 📂 Output Structure

After running, you'll find:

```
research_output/
├── research_1.md    # Theoretical extension to RL
├── research_2.md    # Efficient sparse attention
├── research_3.md    # Vision transformer application
├── research_4.md    # Addressing quadratic complexity
├── research_5.md    # Interpretability analysis
└── ...
```

Each file contains:
- Connection to seed paper
- Core research questions
- Proposed methodology
- Expected contributions
- Evaluation strategy
- Challenges and limitations

---

## 🎨 Customization Options

### Different Research Topics

Create your own seed paper summaries:

```bash
# For diffusion models research
/research_deep_dive seed_papers/diffusion_models_summary.md research_diffusion 10

# For reinforcement learning
/research_deep_dive seed_papers/ppo_algorithm_summary.md research_rl 8

# For a research area (without specific paper)
/research_deep_dive "Graph Neural Networks for molecular property prediction" research_gnn 5
```

### Adjusting Exploration Count

- `1`: Quick single exploration
- `3-5`: Diverse perspectives on the problem
- `10-15`: Comprehensive research space coverage
- `20+`: Exhaustive exploration (may take time)
- `infinite`: Continuous until context exhaustion

---

## 🔍 What Happens Under the Hood

### Phase 1: Seed Paper Analysis (1-2 minutes)
- Extracts key contributions, methods, limitations
- Maps theoretical frameworks and related work
- Identifies research gaps and opportunities

### Phase 2: Research Direction Generation (1 minute)
- Generates diverse exploration vectors:
  - Theoretical extensions
  - Methodological variations
  - Application transfers
  - Limitation fixes
  - Critical alternatives

### Phase 3: Parallel Agent Deployment (varies by count)
- Launches multiple research agents simultaneously
- Each receives unique research direction assignment
- Agents work independently to avoid duplication

### Phase 4: Output Generation (2-5 min per agent)
- Each agent produces a comprehensive research exploration document
- Quality checks ensure novelty and academic rigor

---

## 💡 Pro Tips

### 1. Start Small
```bash
# First, test with 1-3 explorations
/research_deep_dive seed_papers/your_paper.md test_output 3
```

### 2. Review and Iterate
After initial explorations:
- Read the generated research directions
- Identify the most promising ones
- Create **new seed papers** from those directions
- Run deeper dives on specific promising areas

### 3. Combine with Manual Curation
```bash
# Generate 10 explorations
/research_deep_dive seed_papers/transformer.md output 10

# Manually review, pick top 3
# Create refined seed papers for those 3
# Run another round with 5 explorations each
```

### 4. Use for Literature Review
Generate broad coverage first:
```bash
/research_deep_dive "Self-supervised learning in NLP" lit_review 15
```
Then synthesize the explorations into a comprehensive literature review.

---

## 🛠️ Troubleshooting

### Issue: "File not found"
**Solution:** Ensure seed paper path is correct
```bash
# Check file exists
ls seed_papers/

# Use correct relative path
/research_deep_dive seed_papers/transformer_attention_summary.md output 5
```

### Issue: Duplicate research directions
**Solution:** The system automatically analyzes existing files to avoid duplication. If you see duplicates:
1. Delete the duplicate files
2. Re-run with lower count to ensure diversity

### Issue: Low-quality outputs
**Solution:**
- Use more detailed seed paper summaries
- Start with smaller counts (3-5) for higher quality
- Review and provide feedback for refinement

---

## 🎓 Example Workflow: Comprehensive Research Exploration

### Step 1: Initial Broad Exploration
```bash
/research_deep_dive seed_papers/transformer_attention_summary.md phase1_broad 10
```

### Step 2: Review Top 3 Directions
Manually read `phase1_broad/research_1.md` through `research_10.md` and identify:
- Most novel: `research_3.md` (Vision Transformer)
- Most feasible: `research_7.md` (Efficient Attention)
- Most impactful: `research_4.md` (Theoretical Analysis)

### Step 3: Deep Dive on Promising Directions
Create refined seed papers for each:

```bash
# Vision Transformer deep dive
/research_deep_dive phase1_broad/research_3.md phase2_vision_deep 8

# Efficient Attention deep dive
/research_deep_dive phase1_broad/research_7.md phase2_efficient_deep 8

# Theoretical Analysis deep dive
/research_deep_dive phase1_broad/research_4.md phase2_theory_deep 8
```

### Step 4: Synthesize Final Research Agenda
Now you have:
- 10 broad explorations
- 24 deep-dive explorations (3 × 8)
- **Total: 34 research directions** to choose from

---

## 🌟 Advanced: Infinite Research Mode

For exhaustive exploration:

```bash
/research_deep_dive seed_papers/transformer_attention_summary.md infinite_research infinite
```

**What happens:**
- **Wave 1** (5 agents): Basic extensions (efficient attention, different tasks)
- **Wave 2** (5 agents): Cross-domain applications (vision, audio, graphs)
- **Wave 3** (5 agents): Theoretical deep dives (why self-attention works, convergence)
- **Wave 4** (5 agents): Hybrid methods (attention + CNNs, attention + RNNs)
- **Wave 5+**: Paradigm shifts (alternatives to attention, graph-based approaches)
- Continues until context window is nearly full

**Expected output:** 20-50+ research explorations covering the entire frontier

---

## 📊 Integration with Your Workflow

### For Literature Review
```bash
/research_deep_dive "Your research area" lit_review_output 15
# Generates 15 different angles to review literature from
```

### For Grant Proposal Ideation
```bash
/research_deep_dive seed_papers/your_preliminary_work.md grant_ideas 10
# Generates 10 potential research directions for proposal
```

### For PhD Research Planning
```bash
/research_deep_dive seed_papers/thesis_topic.md phd_explorations infinite
# Generates comprehensive research agenda for 3-5 year PhD
```

---

## 🤝 Next Steps

1. **Try the example:**
   ```bash
   claude
   /research_deep_dive seed_papers/transformer_attention_summary.md test_output 3
   ```

2. **Create your own seed paper** in `seed_papers/`

3. **Experiment with different counts** (1, 5, 10, infinite)

4. **Build your research pipeline**:
   - Seed paper → Broad exploration → Deep dives → Synthesis

---

**Happy Researching! 🚀**
