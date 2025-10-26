**COLLABORATIVE RESEARCH COMMAND - Agent Cooperation Mode**

This command enables multiple research agents to collaborate, critique, and refine each other's research explorations.

---

**Variables:**

seed_paper_path: $ARGUMENTS
output_dir: $ARGUMENTS
exploration_count: $ARGUMENTS
mode: $ARGUMENTS

---

**ARGUMENTS PARSING:**
Parse the following arguments from "$ARGUMENTS":
1. `seed_paper_path` - Path to the seed paper or description
2. `output_dir` - Directory where collaborative research will be saved
3. `exploration_count` - Number of initial explorations (recommended 3-5)
4. `mode` - Collaboration mode: "critique", "refine", or "synthesize"

---

## **COLLABORATION MODES**

### **Mode 1: Critique (Peer Review)**
Agents review each other's proposals and provide critical feedback.

### **Mode 2: Refine (Iterative Improvement)**
Agents iteratively improve proposals based on peer feedback.

### **Mode 3: Synthesize (Integration)**
Agents combine insights from multiple proposals into unified directions.

---

## **PHASE 1: INITIAL GENERATION**

Generate initial research explorations using the standard research_deep_dive process:
- Deploy N agents (exploration_count)
- Each generates independent research proposal
- Save to `{output_dir}/round1/`

---

## **PHASE 2: COLLABORATIVE INTERACTION**

### **For Mode = "critique":**

```
FOR each research proposal R_i in round1:
    1. Assign 2-3 peer reviewer agents
    2. Each reviewer receives:
       - The proposal R_i
       - Seed paper context
       - All other proposals (for comparison)

    3. Reviewer task:
       - Identify strengths
       - Identify weaknesses
       - Suggest improvements
       - Rate novelty (1-10)
       - Compare to other proposals

    4. Generate critique document: {output_dir}/critiques/critique_R_i.md
```

**Reviewer Agent Specification:**

```
RESEARCH CRITIC AGENT - TASK

PROPOSAL TO REVIEW: {proposal_filename}

SEED PAPER CONTEXT: {seed_paper_summary}

OTHER PROPOSALS FOR COMPARISON:
{list_of_other_proposals}

YOUR MISSION:
Provide constructive academic peer review of this research proposal.

OUTPUT FORMAT (critique_{filename}.md):

# Peer Review: {proposal_title}

## Strengths
- List 3-5 strong points
- What makes this proposal valuable?

## Weaknesses
- List 3-5 areas for improvement
- What could be more rigorous?

## Novelty Assessment
**Score:** X/10
**Justification:** Why this score?

## Comparison to Other Proposals
- How does this differ from proposal Y?
- Is there redundancy with proposal Z?

## Suggestions for Improvement
1. Concrete suggestion 1
2. Concrete suggestion 2
3. Concrete suggestion 3

## Verdict
[ ] Accept as is
[ ] Accept with minor revisions
[ ] Major revisions needed
[ ] Reject - insufficient novelty

EXECUTE this peer review task independently and thoroughly.
```

---

### **For Mode = "refine":**

```
ITERATION 1:
- Generate initial proposals (round1/)
- Generate critiques (critiques/)

ITERATION 2:
FOR each proposal R_i:
    1. Assign refinement agent
    2. Agent receives:
       - Original proposal R_i
       - Critique(s) of R_i
       - Seed paper

    3. Agent task: Refine proposal addressing critique feedback
    4. Generate: {output_dir}/round2/research_i_v2.md

ITERATION 3 (optional):
- Repeat refinement with new critiques
- Generate: {output_dir}/round3/research_i_v3.md
```

**Refinement Agent Specification:**

```
RESEARCH REFINEMENT AGENT - TASK

ORIGINAL PROPOSAL: {original_proposal}

PEER REVIEW FEEDBACK:
{critique_content}

YOUR MISSION:
Refine the research proposal to address peer review concerns while maintaining core novelty.

REQUIREMENTS:
1. Address each weakness identified
2. Strengthen methodology based on suggestions
3. Improve novelty and differentiation
4. Maintain coherence and feasibility

OUTPUT: Refined research proposal with:
- [REVISED] markers showing major changes
- Brief response to reviewers at end

EXECUTE independently.
```

---

### **For Mode = "synthesize":**

```
PHASE 2A: Group related proposals
1. Analyze all proposals for thematic similarity
2. Create groups of 2-3 related proposals

PHASE 2B: Synthesis
FOR each group:
    1. Assign synthesis agent
    2. Agent receives all proposals in group + seed paper
    3. Agent task: Combine insights into stronger unified proposal
    4. Generate: {output_dir}/synthesized/synthesis_group_X.md
```

**Synthesis Agent Specification:**

```
RESEARCH SYNTHESIS AGENT - TASK

PROPOSALS TO SYNTHESIZE:
- Proposal A: {summary_A}
- Proposal B: {summary_B}
- Proposal C: {summary_C}

SEED PAPER: {seed_context}

YOUR MISSION:
Synthesize these related proposals into a single, more powerful research direction that combines their best insights.

SYNTHESIS STRATEGY:
1. Identify common themes
2. Extract unique contributions from each
3. Resolve contradictions
4. Combine methodologies where complementary
5. Create unified research questions

OUTPUT FORMAT:
# Synthesized Research Proposal: {new_title}

## Source Proposals
Brief summary of each input proposal

## Integrated Research Questions
Combined and refined questions

## Unified Methodology
How methods from different proposals complement each other

## Expected Contributions
Stronger contributions from synthesis

## Synthesis Justification
Why this combination is more powerful than individual proposals

EXECUTE synthesis independently.
```

---

## **PHASE 3: COLLABORATIVE OUTPUT**

Based on mode, produce final outputs:

**Critique Mode:**
- `{output_dir}/round1/` - Initial proposals
- `{output_dir}/critiques/` - Peer reviews
- `{output_dir}/summary_report.md` - Overall analysis

**Refine Mode:**
- `{output_dir}/round1/` - Initial proposals
- `{output_dir}/round2/` - Refined proposals (v2)
- `{output_dir}/round3/` - Further refined (v3, if needed)
- `{output_dir}/improvement_report.md` - Tracking improvements

**Synthesize Mode:**
- `{output_dir}/initial/` - Original proposals
- `{output_dir}/synthesized/` - Synthesized proposals
- `{output_dir}/synthesis_map.md` - How proposals were combined

---

## **EXECUTION STRATEGY**

### **Parallel + Sequential Pattern:**

```
ROUND 1: Parallel generation
- Launch N agents simultaneously
- Generate initial proposals
- Wait for all to complete

ROUND 2: Parallel critique/refinement/synthesis
- Launch reviewer/refiner/synthesizer agents
- Process proposals in parallel
- Wait for all to complete

ROUND 3 (if refine mode): Parallel final refinement
- Launch final refinement agents
- Generate v3 proposals
- Complete
```

### **Agent Communication:**

Agents don't directly communicate, but share context via:
1. Reading each other's outputs
2. Receiving summaries of other proposals
3. Accessing critique documents

This maintains Claude Code's architecture while enabling collaboration.

---

## **QUALITY METRICS**

Track across iterations:
1. **Novelty progression** - How scores improve
2. **Differentiation** - Reduced overlap between proposals
3. **Rigor** - Increased methodological detail
4. **Feasibility** - More realistic evaluation plans

---

## **FINAL REPORT GENERATION**

Generate comprehensive report:

```markdown
# Collaborative Research Exploration Report

## Overview
- Mode: {mode}
- Initial proposals: {count}
- Rounds completed: {rounds}

## Key Findings

### Most Promising Direction
{highest_rated_proposal}

### Highest Novelty Score
{best_novelty_proposal}

### Best Synthesis (if applicable)
{best_synthesis}

## Iteration Improvements
- Round 1 avg novelty: X/10
- Round 2 avg novelty: Y/10
- Improvement: +Z%

## Recommendations
Based on collaborative analysis, we recommend:
1. {top_recommendation}
2. {second_recommendation}

## Next Steps
{suggested_actions}
```

---

## **EXAMPLE WORKFLOW**

### Critique Mode Example:

```bash
# Generate 5 proposals and have them peer-reviewed
/research_collaborative seed_papers/transformer.md collab_output 5 critique

# Expected:
# collab_output/
#   round1/
#     research_1.md
#     research_2.md
#     research_3.md
#     research_4.md
#     research_5.md
#   critiques/
#     critique_research_1.md
#     critique_research_2.md
#     ...
#   summary_report.md
```

### Refine Mode Example:

```bash
# Generate 3 proposals, critique them, refine twice
/research_collaborative seed_papers/transformer.md collab_output 3 refine

# Expected:
# collab_output/
#   round1/ (initial)
#   critiques/ (reviews)
#   round2/ (refined v2)
#   round3/ (refined v3)
#   improvement_report.md
```

---

**Execute collaborative research exploration with sophisticated agent interaction patterns for higher quality research directions.**
