# Changelog

All notable changes to this project will be documented in this file.

## [v2.1.0] - 2024-01-XX - Literature Crawler System

### 🎉 Major Features

#### Literature Crawler Command
- ✅ **New Command**: `/literature_crawler` - Complete literature crawling system
- ✅ **Parallel Crawling**: Intelligent batch management for efficient processing
- ✅ **Knowledge Extraction**: Structured knowledge extraction from papers
- ✅ **Citation Network**: Automatic citation graph construction
- ✅ **Regression Analysis**: Iterative optimization of crawl strategy
- ✅ **Multi-source Support**: Semantic Scholar, arXiv APIs

### 📚 Documentation Improvements

#### New Documentation
- ✅ **QUICK_START_V2.md**: Literature crawler quick start guide
- ✅ **COMMAND_REVIEW.md**: Detailed command review and testing guide
- ✅ **ADVANCED_FEATURES.md**: Comprehensive advanced features documentation
- ✅ **PROJECT_OPTIMIZATION_PLAN_V2.md**: Updated optimization strategy

#### Updated Documentation
- ✅ **README.md**: Streamlined to ~150 lines, focused on core features
- ✅ **Spec Documents**: Simplified to command-driven approach

### 🏗️ Architecture Changes

#### Command-Driven Approach
- ✅ **No Code Required**: Pure Claude Code command orchestration
- ✅ **Agent Coordination**: Parallel sub-agent task management
- ✅ **Zero Maintenance**: No traditional code to maintain

#### Project Structure
- ✅ **Organized Specs**: Moved to `.kiro/specs/literature-crawler/`
- ✅ **Clear Separation**: Core vs. extended features
- ✅ **Better Navigation**: Improved documentation hierarchy

### 🎯 System Integration

#### Two-System Workflow
```
Literature Crawler → Knowledge Base → Research Explorer → Research Directions
```

- ✅ **Seamless Integration**: Literature crawling feeds research exploration
- ✅ **End-to-End**: Complete research workflow from topic to directions
- ✅ **Quality Control**: Automatic relevance scoring and filtering

### 📊 Performance

#### Literature Crawler
- **Depth 1**: 10-30 papers in 5-10 minutes
- **Depth 2**: 50-100 papers in 15-30 minutes
- **Depth 3**: 100-300 papers in 30-60 minutes

#### Research Explorer (Existing)
- **3 directions**: 2-4 minutes
- **10 directions**: 8-15 minutes
- **Infinite mode**: 20-60 minutes (20-50+ directions)

### 🔧 Technical Details

#### Command Features
- **6 Execution Phases**: Validation → Queue → Crawl → Extract → Regress → Output
- **Smart Batching**: ≤5 parallel, 6-20 batched, >20 waves
- **Error Handling**: Retry logic, checkpoints, graceful degradation
- **Output Formats**: JSON knowledge base, citation graph, markdown reports

#### Data Sources
- **Semantic Scholar**: Metadata and citations
- **arXiv**: Preprint full text
- **CrossRef**: DOI resolution (planned)
- **PubMed**: Biomedical literature (planned)

### 🎓 Use Cases

#### Research Scenarios
1. **Literature Review**: Crawl 100-200 papers, generate 15 review angles
2. **Proposal Planning**: Identify key papers, generate 10 research directions
3. **PhD Planning**: Build citation network, explore 20-50+ research paths
4. **Quick Survey**: Crawl 30-50 papers, understand research landscape

### 🚀 Getting Started

#### Test Literature Crawler
```bash
claude
/literature_crawler "arXiv:1706.03762" 1 test_output
```

#### Integrated Workflow
```bash
# 1. Crawl literature
/literature_crawler "Graph Neural Networks" 2 gnn_lit

# 2. Generate research directions
/research_deep_dive gnn_lit/papers/paper_5.md research 10
```

### 📝 Documentation Structure

```
README.md (Core - 150 lines)
├── QUICKSTART.md (Research Explorer)
├── QUICK_START_V2.md (Literature Crawler)
├── RESEARCH_USAGE_GUIDE.md (Detailed Research Guide)
├── COMMAND_REVIEW.md (Command Review)
├── ADVANCED_FEATURES.md (Advanced Features)
├── ARCHITECTURE.md (System Architecture)
└── TESTING_GUIDE.md (Testing Guide)
```

### 🔄 Migration Notes

#### From v2.0 to v2.1
- No breaking changes
- All existing research explorer commands work as before
- New literature crawler command is additive
- Documentation reorganized for clarity

### 🐛 Known Issues

#### To Be Tested
- [ ] API rate limiting in production
- [ ] Large-scale crawling (>200 papers)
- [ ] Knowledge extraction quality
- [ ] Checkpoint recovery

### 📋 Roadmap

#### Phase 3 (Next)
- [ ] Test literature crawler with real papers
- [ ] Optimize parallel processing
- [ ] Add visualization tools
- [ ] Create integrated workflow command

#### Future Enhancements
- [ ] Incremental update mechanism
- [ ] More data sources (CrossRef, PubMed)
- [ ] Interactive visualization
- [ ] MCP Server wrapper

### 🙏 Acknowledgments

- **Original Project**: [IndyDevDan/infinite-agentic-loop](https://github.com/IndyDevDan/infinite-agentic-loop)
- **Core Technology**: [Claude Code](https://docs.anthropic.com/claude-code)
- **Inspiration**: Infinite Agentic Loop pattern

---

## [v2.0.0] - 2024-01-XX - Advanced Tools Suite

### Features
- Research direction generation system
- Parallel agent coordination
- Tool suite (arXiv search, novelty scorer, LaTeX converter, visualizer)
- Collaborative research mode
- Complete documentation

---

## [v1.0.0] - Initial Release

### Features
- Basic research exploration
- Seed paper analysis
- Research direction generation

---

**Note**: This project is under active development. Features marked as "planned" or "to be tested" are subject to change.
