#!/usr/bin/env python3
"""
Research Novelty Scorer
Analyzes research proposals for originality and novelty
"""

import re
import json
import sys
from typing import List, Dict, Tuple
from collections import Counter
import math


class NoveltyScorer:
    """Score research proposals for novelty and originality"""

    def __init__(self):
        self.common_phrases = self._load_common_phrases()

    def _load_common_phrases(self) -> set:
        """Load common research phrases that don't indicate novelty"""
        return {
            'machine learning', 'deep learning', 'neural network',
            'data analysis', 'experimental results', 'future work',
            'related work', 'state of the art', 'baseline method',
            'performance improvement', 'evaluation metrics', 'dataset',
            'training data', 'test set', 'validation', 'optimization',
            'algorithm', 'model', 'framework', 'approach', 'method'
        }

    def score_proposal(self, proposal_text: str,
                      existing_proposals: List[str] = None) -> Dict:
        """
        Score a research proposal for novelty

        Args:
            proposal_text: The research proposal to score
            existing_proposals: List of existing proposals to compare against

        Returns:
            Dictionary with novelty metrics:
            - overall_score: 0-100
            - conceptual_novelty: 0-100
            - methodological_novelty: 0-100
            - uniqueness_score: 0-100 (vs existing proposals)
            - key_innovations: List of identified novel concepts
            - similarity_warnings: Areas of potential overlap
        """
        results = {}

        # 1. Extract key concepts
        concepts = self._extract_concepts(proposal_text)
        results['key_concepts'] = concepts

        # 2. Conceptual novelty (unique concepts vs common ones)
        conceptual_score = self._score_conceptual_novelty(concepts)
        results['conceptual_novelty'] = conceptual_score

        # 3. Methodological novelty (novel combinations, approaches)
        method_score = self._score_methodological_novelty(proposal_text)
        results['methodological_novelty'] = method_score

        # 4. Uniqueness compared to existing proposals
        if existing_proposals:
            uniqueness = self._score_uniqueness(proposal_text, existing_proposals)
            results['uniqueness_score'] = uniqueness['score']
            results['similarity_warnings'] = uniqueness['warnings']
        else:
            results['uniqueness_score'] = 100
            results['similarity_warnings'] = []

        # 5. Identify key innovations
        innovations = self._identify_innovations(proposal_text, concepts)
        results['key_innovations'] = innovations

        # 6. Calculate overall score
        weights = {
            'conceptual': 0.35,
            'methodological': 0.35,
            'uniqueness': 0.30
        }

        overall = (
            weights['conceptual'] * conceptual_score +
            weights['methodological'] * method_score +
            weights['uniqueness'] * results['uniqueness_score']
        )
        results['overall_score'] = round(overall, 2)

        # 7. Generate recommendation
        results['recommendation'] = self._generate_recommendation(results)

        return results

    def _extract_concepts(self, text: str) -> List[str]:
        """Extract key concepts from proposal"""
        # Convert to lowercase
        text = text.lower()

        # Extract noun phrases (simple heuristic)
        # Look for capitalized multi-word phrases and technical terms
        patterns = [
            r'\b[a-z]+[-][a-z]+\b',  # hyphenated terms
            r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b',  # Capitalized phrases
        ]

        concepts = []
        for pattern in patterns:
            matches = re.findall(pattern, text)
            concepts.extend(matches)

        # Remove common phrases
        concepts = [c for c in concepts if c.lower() not in self.common_phrases]

        # Count frequency
        concept_counts = Counter(concepts)

        # Return top concepts
        return [c for c, count in concept_counts.most_common(20)]

    def _score_conceptual_novelty(self, concepts: List[str]) -> float:
        """Score based on uniqueness of concepts"""
        if not concepts:
            return 50.0

        # Check how many concepts are NOT in common phrases
        novel_concepts = [c for c in concepts if c.lower() not in self.common_phrases]

        ratio = len(novel_concepts) / len(concepts) if concepts else 0
        return round(ratio * 100, 2)

    def _score_methodological_novelty(self, text: str) -> float:
        """Score based on novel methodological indicators"""
        # Keywords indicating novelty
        novelty_indicators = [
            'novel', 'new', 'innovative', 'unprecedented', 'first',
            'unique', 'original', 'pioneering', 'groundbreaking',
            'paradigm shift', 'breakthrough', 'alternative approach',
            'different from', 'unlike previous', 'in contrast to'
        ]

        # Keywords indicating incremental work
        incremental_indicators = [
            'similar to', 'based on', 'extends', 'improves',
            'variation of', 'inspired by', 'follows', 'adopts'
        ]

        text_lower = text.lower()

        novel_count = sum(1 for ind in novelty_indicators if ind in text_lower)
        incremental_count = sum(1 for ind in incremental_indicators if ind in text_lower)

        # Calculate score
        if novel_count + incremental_count == 0:
            return 50.0

        ratio = novel_count / (novel_count + incremental_count)
        return round(ratio * 100, 2)

    def _score_uniqueness(self, proposal: str,
                         existing: List[str]) -> Dict:
        """Score uniqueness vs existing proposals"""
        # Simple word-overlap similarity
        proposal_words = set(self._tokenize(proposal.lower()))

        similarities = []
        warnings = []

        for i, exist in enumerate(existing):
            exist_words = set(self._tokenize(exist.lower()))

            # Jaccard similarity
            intersection = proposal_words & exist_words
            union = proposal_words | exist_words

            if union:
                similarity = len(intersection) / len(union)
                similarities.append(similarity)

                if similarity > 0.3:
                    warnings.append(f"High similarity ({similarity:.2%}) with existing proposal #{i+1}")

        avg_similarity = sum(similarities) / len(similarities) if similarities else 0
        uniqueness_score = round((1 - avg_similarity) * 100, 2)

        return {
            'score': uniqueness_score,
            'warnings': warnings
        }

    def _tokenize(self, text: str) -> List[str]:
        """Simple word tokenization"""
        # Remove punctuation and split
        text = re.sub(r'[^\w\s]', ' ', text)
        return [w for w in text.split() if len(w) > 3]

    def _identify_innovations(self, text: str, concepts: List[str]) -> List[str]:
        """Identify key innovative aspects"""
        innovations = []

        # Look for sentences with novelty indicators
        sentences = text.split('.')

        novelty_patterns = [
            r'novel\s+(\w+(?:\s+\w+){0,3})',
            r'new\s+(\w+(?:\s+\w+){0,3})',
            r'first\s+to\s+(\w+(?:\s+\w+){0,3})',
            r'unprecedented\s+(\w+(?:\s+\w+){0,3})',
        ]

        for sentence in sentences:
            for pattern in novelty_patterns:
                matches = re.findall(pattern, sentence, re.IGNORECASE)
                innovations.extend(matches[:3])  # Limit per sentence

        return list(set(innovations))[:10]  # Top 10 unique

    def _generate_recommendation(self, results: Dict) -> str:
        """Generate human-readable recommendation"""
        score = results['overall_score']

        if score >= 80:
            return "✅ HIGHLY NOVEL - Strong potential for publication in top-tier venues"
        elif score >= 60:
            return "✓ MODERATELY NOVEL - Good research direction with room for enhancement"
        elif score >= 40:
            return "⚠️ SOMEWHAT INCREMENTAL - Consider emphasizing unique aspects more"
        else:
            return "❌ LOW NOVELTY - Significant revision needed to differentiate from existing work"

    def format_report(self, results: Dict) -> str:
        """Format novelty analysis as markdown report"""
        md = "# Research Novelty Analysis Report\n\n"
        md += f"## Overall Novelty Score: {results['overall_score']}/100\n\n"
        md += f"**Recommendation:** {results['recommendation']}\n\n"
        md += "---\n\n"

        md += "## Detailed Breakdown\n\n"
        md += f"- **Conceptual Novelty:** {results['conceptual_novelty']}/100\n"
        md += f"- **Methodological Novelty:** {results['methodological_novelty']}/100\n"
        md += f"- **Uniqueness Score:** {results['uniqueness_score']}/100\n\n"

        if results.get('key_innovations'):
            md += "## Key Innovations Identified\n\n"
            for innovation in results['key_innovations']:
                md += f"- {innovation}\n"
            md += "\n"

        if results.get('similarity_warnings'):
            md += "## ⚠️ Similarity Warnings\n\n"
            for warning in results['similarity_warnings']:
                md += f"- {warning}\n"
            md += "\n"

        md += "## Key Concepts\n\n"
        for concept in results.get('key_concepts', [])[:10]:
            md += f"- {concept}\n"

        return md


def main():
    """CLI interface"""
    if len(sys.argv) < 2:
        print("Usage: python novelty_scorer.py <proposal_file> [existing_proposals_dir]")
        sys.exit(1)

    proposal_file = sys.argv[1]

    with open(proposal_file, 'r') as f:
        proposal = f.read()

    existing = []
    if len(sys.argv) > 2:
        import os
        import glob
        existing_dir = sys.argv[2]
        for file in glob.glob(os.path.join(existing_dir, "*.md")):
            with open(file, 'r') as f:
                existing.append(f.read())

    scorer = NoveltyScorer()
    results = scorer.score_proposal(proposal, existing)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
