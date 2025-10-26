**RESEARCH DEEP DIVE COMMAND - Seed Paper to Research Exploration**

You are embarking on an **academic research exploration** starting from a seed paper. This command orchestrates parallel research agents to deeply investigate related work, methodologies, and novel research directions.

---

**Variables:**

seed_paper_path: $ARGUMENTS
output_dir: $ARGUMENTS
exploration_count: $ARGUMENTS

---

**ARGUMENTS PARSING:**
Parse the following arguments from "$ARGUMENTS":
1. `seed_paper_path` - Path to the seed paper (PDF/markdown/text) or a brief description
2. `output_dir` - Directory where research outputs will be saved
3. `exploration_count` - Number of research explorations (1-N or "infinite")

---

## **PHASE 1: SEED PAPER ANALYSIS**

**Deep Understanding of the Seed Paper:**

If `seed_paper_path` is a file:
- Read the file content thoroughly
- Extract: Title, Authors, Abstract, Key Contributions, Methods, Results, Limitations
- Identify: Core research questions, theoretical frameworks, datasets used, evaluation metrics

If `seed_paper_path` is a description/topic:
- Treat it as a research area specification
- Identify the core themes and subfields

**Critical Analysis:**
- What problem does this paper solve?
- What are the novel contributions?
- What assumptions does it make?
- What are the explicitly stated limitations?
- What are the implicit gaps not addressed?

**Research Frontier Mapping:**
- Identify related work mentioned in the paper
- Map out the theoretical lineage (what prior work it builds on)
- Identify competing approaches
- Spot unexplored variations or combinations

---

## **PHASE 2: RESEARCH DIRECTION GENERATION**

Based on the seed paper analysis, generate diverse research exploration vectors:

### **Exploration Dimensions:**

1. **Theoretical Extensions**
   - Apply the method to different theoretical frameworks
   - Relax key assumptions and explore implications
   - Generalize specific techniques to broader domains

2. **Methodological Variations**
   - Alternative algorithms for the same problem
   - Hybrid approaches combining multiple methods
   - Simplified versions for resource-constrained settings

3. **Application Domains**
   - Transfer the approach to different fields
   - Adapt for edge cases or specialized scenarios
   - Scale to larger/smaller problem instances

4. **Limitation Addressing**
   - Directly tackle stated limitations
   - Improve weaknesses in evaluation
   - Enhance robustness or generalization

5. **Critical Analysis & Alternatives**
   - Challenge core assumptions
   - Propose fundamentally different approaches
   - Identify potential negative societal impacts

6. **Cross-Disciplinary Synthesis**
   - Combine insights from other fields
   - Apply techniques from unrelated domains
   - Bridge theoretical gaps between disciplines

---

## **PHASE 3: EXISTING RESEARCH RECONNAISSANCE**

Analyze the `output_dir` to understand what research has already been explored:
- List all existing research documents
- Identify iteration numbers and research angles covered
- Map the research space already explored
- Determine the next iteration number
- Identify unexplored combinations or gaps

---

## **PHASE 4: PARALLEL RESEARCH AGENT COORDINATION**

Deploy multiple **Research Agents** in parallel, each exploring a unique research direction:

### **Sub-Agent Distribution Strategy:**
- For count 1-5: Launch all agents simultaneously
- For count 6-15: Launch in batches of 5 agents
- For count 16+: Launch in batches of 5 agents with progressive sophistication
- For "infinite": Launch waves of 3-5 agents until context limits

### **Agent Assignment Protocol:**

Each Research Agent receives:

1. **Seed Paper Summary**: Complete analysis from Phase 1
2. **Assigned Research Direction**: One of the exploration dimensions
3. **Iteration Number**: Specific research_[N].md file to generate
4. **Uniqueness Constraint**: Must not duplicate angles from existing research
5. **Quality Standards**: Academic rigor, novelty, feasibility requirements

### **Agent Task Specification Template:**

```
RESEARCH AGENT [N] - TASK SPECIFICATION

SEED PAPER CONTEXT:
[Complete seed paper analysis including title, contributions, methods, limitations]

YOUR ASSIGNED RESEARCH DIRECTION:
[Specific exploration dimension: e.g., "Theoretical Extension - Apply to reinforcement learning domain"]

YOUR ITERATION NUMBER: research_{iteration_number}.md

EXISTING RESEARCH LANDSCAPE:
[Summary of what previous iterations have explored to avoid duplication]

YOUR MISSION:
Generate a comprehensive research exploration document that:
1. Builds upon the seed paper's insights
2. Explores your assigned direction deeply
3. Proposes concrete research questions
4. Outlines potential methodologies
5. Identifies expected contributions
6. Discusses feasibility and challenges

OUTPUT FORMAT:
Create a markdown file named research_{iteration_number}.md with this structure:

# Research Exploration {iteration_number}: [Title]

## 1. Connection to Seed Paper
- How this research builds on/extends/challenges the seed paper
- Key insights borrowed or refuted

## 2. Core Research Question(s)
- 2-4 specific, answerable research questions

## 3. Motivation & Novelty
- Why this direction matters
- What gap it fills
- How it differs from existing work (including prior iterations)

## 4. Proposed Approach
- High-level methodology
- Key techniques or algorithms
- Theoretical frameworks to leverage

## 5. Expected Contributions
- Anticipated novel insights
- Potential impact on the field

## 6. Evaluation Strategy
- How to validate the approach
- Metrics, baselines, datasets
- Success criteria

## 7. Challenges & Limitations
- Technical difficulties
- Resource requirements
- Potential pitfalls

## 8. Related Work Beyond Seed Paper
- Additional papers/theories to investigate
- Connections to other subfields

## 9. Future Directions
- Follow-up questions if this succeeds
- Long-term research trajectory

---

CRITICAL REQUIREMENTS:
- **Novelty**: Must propose genuinely new ideas not in seed paper or existing iterations
- **Rigor**: Methodologically sound and technically feasible
- **Specificity**: Concrete research questions, not vague ideas
- **Feasibility**: Achievable within 1-3 years with reasonable resources
- **Academic Quality**: Suitable for submission to top-tier conferences/journals

Execute this task independently and generate the complete research exploration document.
```

---

## **PHASE 5: PARALLEL EXECUTION MANAGEMENT**

**Coordination Strategy:**

1. **Batch Launching**:
   - For small counts (1-5): Launch all agents in one batch using parallel Task tool calls
   - For larger counts: Launch in waves of 5 agents to manage context

2. **Progress Monitoring**:
   - Track completion of each agent
   - Handle failures by reassigning iteration numbers
   - Ensure no duplicate iteration numbers

3. **Quality Validation** (after agents complete):
   - Check each output for novelty vs existing iterations
   - Verify academic rigor and completeness
   - Ensure proper markdown formatting

---

## **PHASE 6: INFINITE MODE ORCHESTRATION**

For `exploration_count = "infinite"`, implement wave-based continuous research:

### **Wave Strategy:**

```
WHILE context_capacity > threshold:
    1. Assess current research_output state
    2. Identify unexplored research dimensions
    3. Plan next wave (3-5 agents) with increasingly sophisticated directions
    4. Assign progressive exploration goals:
       - Early waves: Direct extensions and variations
       - Middle waves: Cross-disciplinary combinations
       - Later waves: Radical paradigm shifts and critiques
    5. Launch parallel agent wave
    6. Monitor completion
    7. Update research landscape summary
    8. Evaluate context remaining
    9. If sufficient: Continue next wave
    10. If approaching limits: Final wave + comprehensive synthesis
```

### **Progressive Sophistication:**

- **Wave 1-2**: Methodological variations and direct extensions
- **Wave 3-4**: Cross-domain applications and theoretical generalizations
- **Wave 5-6**: Limitation-addressing and hybrid approaches
- **Wave 7+**: Paradigm-challenging and radical alternatives

### **Context Optimization:**

- Each wave uses fresh agent instances
- Maintain lightweight research landscape summary
- Progressive abstraction of earlier iterations
- Focus context on unexplored dimensions

---

## **EXECUTION PRINCIPLES**

### **Quality Over Quantity:**
- Each research exploration must be academically rigorous
- Prioritize depth over breadth in individual explorations
- Ensure methodological soundness and feasibility

### **Diversity Maximization:**
- Assign distinct exploration dimensions to each agent
- Explicitly instruct agents to avoid overlapping angles
- Cover theoretical, methodological, and application spaces

### **Academic Rigor:**
- All outputs must meet publication standards
- Proper citation of seed paper and related work
- Clear research questions and evaluation plans

### **Novelty Enforcement:**
- Each iteration must propose genuinely new ideas
- Agents must analyze existing iterations before generating
- Cross-agent coordination to prevent duplication

---

## **ULTRA-THINKING DIRECTIVE**

Before launching research agents, engage in extended thinking:

**Seed Paper Deep Dive:**
- What are the most significant contributions?
- What assumptions are critical but potentially relaxable?
- What interdisciplinary connections could be made?
- What are the unstated limitations?

**Research Space Mapping:**
- What dimensions of exploration offer highest novelty potential?
- Which directions are most feasible vs most impactful?
- How can we ensure diverse coverage of the research space?
- What radical alternatives might challenge the seed paper's core premises?

**Agent Coordination Strategy:**
- How to assign research directions for maximum diversity?
- What progressive sophistication strategy for infinite mode?
- How to prevent conceptual overlap between parallel agents?
- What quality checks to apply post-generation?

**Feasibility & Impact:**
- Which research directions are achievable within academic timelines?
- Which have highest potential for top-tier publication?
- What resources (data, compute, theory) are required?
- How do these explorations advance the overall field?

---

## **FINAL DELIVERABLE**

After all agents complete, provide a summary:

```
=== RESEARCH EXPLORATION SUMMARY ===

SEED PAPER: [Title]
EXPLORATIONS GENERATED: [N]
OUTPUT DIRECTORY: [output_dir]

RESEARCH DIMENSIONS COVERED:
- [List unique angles explored]

NOVELTY HIGHLIGHTS:
- [Most innovative research directions identified]

RECOMMENDED NEXT STEPS:
- [Which explorations to prioritize for deeper investigation]
- [Potential collaboration opportunities]
- [Suggested follow-up readings]

```

---

**Begin execution by deeply analyzing the seed paper, then systematically deploy research agents to explore the frontiers of knowledge.**
