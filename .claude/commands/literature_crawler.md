**LITERATURE CRAWLER COMMAND - Academic Paper Network Exploration**

You are embarking on an **academic literature crawling** mission starting from seed papers. This command orchestrates parallel crawler agents to build a citation network, extract structured knowledge, and identify research frontiers.

---

**Variables:**

seed_papers: $ARGUMENTS
crawl_depth: $ARGUMENTS
output_dir: $ARGUMENTS

---

**ARGUMENTS PARSING:**
Parse the following arguments from "$ARGUMENTS":
1. `seed_papers` - Seed paper identifiers (DOI/arXiv ID/Title) or research topic, comma-separated for multiple
2. `crawl_depth` - Maximum crawl depth (1-3, default: 2)
3. `output_dir` - Directory where literature outputs will be saved (default: literature_output/)

---

## **PHASE 1: SEED PAPER VALIDATION & INITIALIZATION**

**Seed Paper Processing:**

For each seed paper identifier:
- Determine identifier type (DOI, arXiv ID, or Title)
- Validate accessibility through available APIs
- If it's a research topic instead of paper ID, search for top 3-5 representative papers

**Metadata Extraction:**
Use Semantic Scholar API or arXiv API to extract:
- Paper ID (DOI/arXiv)
- Title
- Authors
- Abstract
- Publication year
- Venue (journal/conference)
- Citation count
- Reference list (papers it cites)
- Cited-by list (papers that cite it)

**Knowledge Base Initialization:**
Create `{output_dir}/knowledge_base.json` with structure:
```json
{
  "papers": {},
  "citation_graph": {
    "nodes": [],
    "edges": []
  },
  "metadata": {
    "seed_papers": [],
    "crawl_depth": 2,
    "total_papers": 0,
    "waves_completed": 0,
    "last_updated": ""
  },
  "queue": {
    "pending": [],
    "processing": [],
    "completed": []
  }
}
```

**Output:**
- Save each seed paper as `{output_dir}/papers/seed_paper_{n}.md`
- Add to knowledge_base.json
- Initialize crawl queue with seed papers' references

---

## **PHASE 2: CRAWL QUEUE PREPARATION**

**Queue Building:**
From seed papers, extract all referenced papers and add to queue with priority scores.

**Priority Calculation:**
For each paper in queue, calculate priority = w1 * citation_count + w2 * recency + w3 * relevance
- w1 = 0.4 (citation importance)
- w2 = 0.3 (recency: papers from last 5 years get higher scores)
- w3 = 0.3 (relevance: keyword overlap with seed papers)

**Deduplication:**
- Check if paper already exists in knowledge_base
- Skip if already processed
- Merge if found in queue multiple times (increase priority)

**Queue Organization:**
Sort queue by priority (highest first) and organize into waves based on crawl_depth:
- Depth 1: Only direct references from seed papers
- Depth 2: References from depth 1 papers
- Depth 3: References from depth 2 papers

---

## **PHASE 3: PARALLEL CRAWLER AGENT COORDINATION**

**Agent Deployment Strategy:**

Determine batch size based on queue size:
- If queue_size <= 5: Deploy all agents simultaneously
- If 6 <= queue_size <= 20: Deploy in batches of 5
- If queue_size > 20: Use wave strategy (5 agents per wave)

**Sub Agent Task Specification:**

For each crawler agent, assign a specific set of papers to process:

```
**Crawler Agent {agent_id} Task:**

Papers to process: {paper_ids}

For each paper:
1. Fetch metadata from Semantic Scholar API:
   - Endpoint: https://api.semanticscholar.org/v1/paper/{paper_id}
   - Extract: title, authors, abstract, year, citations, references

2. If Semantic Scholar fails, try arXiv API:
   - Endpoint: http://export.arxiv.org/api/query?id={arxiv_id}
   
3. Create paper document:
   - Save as: {output_dir}/papers/paper_{n}.md
   - Format:
     ```markdown
     # {title}
     
     **Authors:** {authors}
     **Year:** {year}
     **Venue:** {venue}
     **Citations:** {citation_count}
     **DOI:** {doi}
     **arXiv:** {arxiv_id}
     
     ## Abstract
     {abstract}
     
     ## Key Information
     - **Research Area:** {inferred_area}
     - **Methods:** {extracted_methods}
     - **Datasets:** {mentioned_datasets}
     
     ## References ({ref_count})
     {reference_list}
     
     ## Cited By ({cited_by_count})
     {cited_by_list}
     ```

4. Extract citation relationships:
   - Add edges to citation graph: {paper_id} → {referenced_paper_id}
   
5. Return results:
   - paper_id
   - metadata_summary
   - reference_ids (for next wave)
   - processing_status (success/failed/partial)
```

**Parallel Execution:**
Deploy all agents in current batch using Task tool, wait for completion, then proceed.

**Error Handling:**
- If agent fails to fetch paper: mark as "failed", add to retry queue
- If API rate limit hit: wait 60 seconds, retry
- If paper not found: mark as "unavailable", continue with others

---

## **PHASE 4: KNOWLEDGE EXTRACTION**

**After each wave of crawling, deploy knowledge extraction agents:**

**Sub Agent Task: Extract Structured Knowledge**

For each successfully crawled paper:

```
**Knowledge Extractor Agent {agent_id} Task:**

Paper: {paper_id}
Content: {paper_abstract_and_metadata}

Extract the following structured knowledge:

1. **Research Questions** (2-4 questions):
   - What problem does this paper address?
   - What are the key research questions?

2. **Methodology** (brief description):
   - What approach/algorithm does it use?
   - What is novel about the method?

3. **Key Contributions** (3-5 points):
   - Main contributions to the field
   - Novel insights or techniques

4. **Datasets & Benchmarks**:
   - Datasets used for evaluation
   - Benchmark tasks

5. **Results Summary**:
   - Key performance metrics
   - Main findings

6. **Limitations** (if mentioned):
   - Stated limitations
   - Potential weaknesses

7. **Research Direction Tags**:
   - Classify into: Theory/Method/Application/Survey/Tool
   - Identify subfield tags

Output format: JSON object to be added to knowledge_base.json under paper entry
```

**Update Knowledge Base:**
Merge extracted knowledge into `knowledge_base.json` for each paper.

---

## **PHASE 5: REGRESSION ANALYSIS & ITERATION**

**Wave Completion Analysis:**

After each wave, analyze crawl quality:

1. **Relevance Scoring:**
   - Calculate semantic similarity between crawled papers and seed papers
   - Use keyword overlap, abstract similarity
   - Score range: 0.0 (irrelevant) to 1.0 (highly relevant)

2. **Quality Metrics:**
   - Average citation count of crawled papers
   - Percentage of high-impact papers (citations > 50)
   - Diversity of research areas covered

3. **Priority Weight Adjustment:**
   - If too many low-relevance papers: increase w3 (relevance weight)
   - If missing recent work: increase w2 (recency weight)
   - If missing influential papers: increase w1 (citation weight)

**Next Wave Preparation:**

If current_depth < crawl_depth:
1. Extract references from newly crawled papers
2. Add to queue with updated priority weights
3. Remove duplicates and already-processed papers
4. Sort by priority
5. Prepare next wave of agents

**Iteration Control:**
- Continue until: current_depth >= crawl_depth OR queue is empty OR total_papers >= 200
- Save checkpoint after each wave to `{output_dir}/checkpoints/wave_{n}.json`

---

## **PHASE 6: OUTPUT GENERATION & REPORTING**

**Final Knowledge Base:**
Ensure `knowledge_base.json` is complete and well-structured.

**Citation Graph Export:**
Generate `{output_dir}/citation_graph.json`:
```json
{
  "nodes": [
    {
      "id": "paper_1",
      "label": "Paper Title",
      "citations": 150,
      "year": 2020,
      "relevance_score": 0.85
    }
  ],
  "edges": [
    {
      "source": "paper_1",
      "target": "paper_2",
      "type": "cites"
    }
  ]
}
```

**Summary Report:**
Create `{output_dir}/crawl_summary.md`:
```markdown
# Literature Crawl Summary

## Overview
- **Seed Papers:** {count}
- **Total Papers Crawled:** {count}
- **Crawl Depth:** {depth}
- **Waves Completed:** {count}
- **Time Taken:** {duration}

## Statistics
- **Average Citations:** {avg}
- **Year Range:** {min_year} - {max_year}
- **Top Venues:** {top_5_venues}

## High-Impact Papers (Top 10 by citations)
1. [{title}]({url}) - {citations} citations
2. ...

## Research Areas Covered
- {area_1}: {count} papers
- {area_2}: {count} papers
- ...

## Key Findings
- {insight_1}
- {insight_2}
- ...

## Recommended Papers for Deep Dive
Based on relevance and impact:
1. {paper_title} - {reason}
2. ...
```

**Visualization Data:**
Prepare data for visualization (can be processed by external tools):
- Timeline data: papers by year
- Citation network: for graph visualization
- Topic clusters: papers grouped by research area

---

## **EXECUTION FLOW SUMMARY**

```
START
  ↓
PHASE 1: Validate seed papers → Initialize knowledge base
  ↓
PHASE 2: Build crawl queue → Calculate priorities
  ↓
PHASE 3: Deploy crawler agents (Wave 1) → Fetch metadata
  ↓
PHASE 4: Deploy extraction agents → Extract knowledge
  ↓
PHASE 5: Analyze results → Adjust priorities → Prepare next wave
  ↓
[If depth < max_depth] → PHASE 3 (next wave)
  ↓
PHASE 6: Generate outputs → Create reports
  ↓
END
```

---

## **USAGE EXAMPLES**

### Example 1: Single Paper, Depth 1
```
/literature_crawler "10.48550/arXiv.1706.03762" 1 attention_papers
```
Crawls the "Attention is All You Need" paper and its direct references.

### Example 2: Multiple Seeds, Depth 2
```
/literature_crawler "arXiv:1706.03762,arXiv:1810.04805" 2 transformer_network
```
Crawls Transformer and BERT papers, plus 2 layers of references.

### Example 3: Topic-Based Crawl
```
/literature_crawler "Graph Neural Networks" 2 gnn_literature
```
Searches for top GNN papers, then crawls their citation network.

### Example 4: Deep Crawl
```
/literature_crawler "10.1145/3292500.3330989" 3 deep_crawl
```
Performs a 3-layer deep crawl (may result in 100-300 papers).

---

## **API REFERENCE**

### Semantic Scholar API
- **Base URL:** `https://api.semanticscholar.org/v1/paper/`
- **Rate Limit:** 100 requests per 5 minutes
- **Paper Lookup:** `GET /paper/{DOI}` or `GET /paper/arXiv:{arxiv_id}`
- **Response:** JSON with title, authors, abstract, citations, references

### arXiv API
- **Base URL:** `http://export.arxiv.org/api/query`
- **Rate Limit:** 1 request per 3 seconds
- **Search:** `GET ?search_query=id:{arxiv_id}`
- **Response:** XML with paper metadata

---

## **ERROR HANDLING**

- **Network Timeout:** Retry up to 3 times with exponential backoff
- **API Rate Limit:** Wait and retry after cooldown period
- **Paper Not Found:** Mark as unavailable, continue with others
- **Parsing Error:** Log error, save partial data, continue
- **Checkpoint Recovery:** If interrupted, resume from last checkpoint

---

**END OF COMMAND SPECIFICATION**
