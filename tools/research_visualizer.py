#!/usr/bin/env python3
"""
Research Evolution Visualizer
Creates visual representations of research exploration evolution
"""

import os
import sys
import json
import re
from typing import List, Dict
from collections import defaultdict


class ResearchVisualizer:
    """Visualize research exploration evolution"""

    def __init__(self):
        self.dimensions = [
            'Theoretical Extension',
            'Methodological Variation',
            'Application Transfer',
            'Limitation Addressing',
            'Critical Analysis',
            'Cross-Disciplinary'
        ]

    def analyze_directory(self, directory: str) -> Dict:
        """Analyze all research files in a directory"""
        research_files = []

        for file in sorted(os.listdir(directory)):
            if file.endswith('.md') and file.startswith('research_'):
                filepath = os.path.join(directory, file)
                with open(filepath, 'r') as f:
                    content = f.read()

                analysis = self._analyze_research(content, file)
                research_files.append(analysis)

        return {
            'total_count': len(research_files),
            'researches': research_files,
            'dimension_distribution': self._calculate_distribution(research_files),
            'evolution_trajectory': self._calculate_trajectory(research_files)
        }

    def _analyze_research(self, content: str, filename: str) -> Dict:
        """Analyze a single research file"""
        # Extract title
        title_match = re.search(r'^#\s+Research Exploration \d+:\s*(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Untitled"

        # Classify dimension
        dimension = self._classify_dimension(content)

        # Extract key concepts (simple heuristic)
        concepts = self._extract_keywords(content)

        # Count words
        word_count = len(content.split())

        return {
            'filename': filename,
            'title': title,
            'dimension': dimension,
            'key_concepts': concepts,
            'word_count': word_count
        }

    def _classify_dimension(self, content: str) -> str:
        """Classify which dimension this research belongs to"""
        content_lower = content.lower()

        # Keywords for each dimension
        dimension_keywords = {
            'Theoretical Extension': ['theory', 'theoretical', 'framework', 'formal', 'mathematical'],
            'Methodological Variation': ['algorithm', 'method', 'approach', 'technique', 'efficient'],
            'Application Transfer': ['application', 'domain', 'vision', 'audio', 'nlp', 'applied'],
            'Limitation Addressing': ['limitation', 'solve', 'address', 'improve', 'overcome'],
            'Critical Analysis': ['critique', 'challenge', 'question', 'assumption', 'alternative'],
            'Cross-Disciplinary': ['interdisciplinary', 'neuroscience', 'biology', 'physics', 'combining']
        }

        scores = {}
        for dim, keywords in dimension_keywords.items():
            score = sum(1 for kw in keywords if kw in content_lower)
            scores[dim] = score

        # Return dimension with highest score
        best_dim = max(scores.items(), key=lambda x: x[1])
        return best_dim[0] if best_dim[1] > 0 else 'Theoretical Extension'

    def _extract_keywords(self, content: str) -> List[str]:
        """Extract key concepts"""
        # Simple extraction: look for capitalized phrases
        matches = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', content)

        # Count and return top 5
        from collections import Counter
        counter = Counter(matches)
        return [word for word, count in counter.most_common(5)]

    def _calculate_distribution(self, researches: List[Dict]) -> Dict:
        """Calculate distribution across dimensions"""
        distribution = defaultdict(int)

        for research in researches:
            distribution[research['dimension']] += 1

        return dict(distribution)

    def _calculate_trajectory(self, researches: List[Dict]) -> List[str]:
        """Calculate evolution trajectory"""
        return [r['dimension'] for r in researches]

    def generate_mermaid_diagram(self, analysis: Dict) -> str:
        """Generate Mermaid flowchart for research evolution"""
        mermaid = "```mermaid\ngraph TD\n"
        mermaid += "    Start[Seed Paper] --> Research\n"
        mermaid += "    Research[Research Exploration]\n"

        # Group by dimension
        dim_groups = defaultdict(list)
        for r in analysis['researches']:
            dim_groups[r['dimension']].append(r)

        # Create nodes for each dimension
        dim_abbrev = {
            'Theoretical Extension': 'Theory',
            'Methodological Variation': 'Method',
            'Application Transfer': 'Application',
            'Limitation Addressing': 'Limitation',
            'Critical Analysis': 'Critique',
            'Cross-Disciplinary': 'CrossDis'
        }

        for i, (dim, researches) in enumerate(dim_groups.items()):
            abbrev = dim_abbrev.get(dim, dim[:8])
            count = len(researches)
            mermaid += f"    Research --> {abbrev}[{dim}<br/>{count} explorations]\n"

            # Add some individual research nodes
            for j, r in enumerate(researches[:3]):  # Show first 3
                node_id = f"{abbrev}{j}"
                title_short = r['title'][:30] + "..." if len(r['title']) > 30 else r['title']
                mermaid += f"    {abbrev} --> {node_id}[\"{title_short}\"]\n"

        mermaid += "```\n"
        return mermaid

    def generate_ascii_chart(self, analysis: Dict) -> str:
        """Generate ASCII chart of dimension distribution"""
        distribution = analysis['dimension_distribution']

        chart = "\n# Research Dimension Distribution\n\n"

        max_count = max(distribution.values()) if distribution else 1

        for dim in self.dimensions:
            count = distribution.get(dim, 0)
            bar_length = int((count / max_count) * 40) if max_count > 0 else 0
            bar = '█' * bar_length

            chart += f"{dim:25s} | {bar} {count}\n"

        return chart

    def generate_report(self, directory: str) -> str:
        """Generate complete visualization report"""
        analysis = self.analyze_directory(directory)

        report = f"# Research Evolution Analysis Report\n\n"
        report += f"**Directory:** `{directory}`\n\n"
        report += f"**Total Research Explorations:** {analysis['total_count']}\n\n"
        report += "---\n\n"

        # ASCII chart
        report += self.generate_ascii_chart(analysis)
        report += "\n---\n\n"

        # Evolution trajectory
        report += "## Evolution Trajectory\n\n"
        trajectory = analysis['evolution_trajectory']
        for i, dim in enumerate(trajectory, 1):
            report += f"{i}. {dim}\n"
        report += "\n---\n\n"

        # Mermaid diagram
        report += "## Visual Exploration Map\n\n"
        report += self.generate_mermaid_diagram(analysis)
        report += "\n---\n\n"

        # Details
        report += "## Research Details\n\n"
        for r in analysis['researches']:
            report += f"### {r['filename']}\n"
            report += f"**Title:** {r['title']}\n\n"
            report += f"**Dimension:** {r['dimension']}\n\n"
            report += f"**Key Concepts:** {', '.join(r['key_concepts'])}\n\n"
            report += f"**Word Count:** {r['word_count']}\n\n"
            report += "---\n\n"

        return report


def main():
    """CLI interface"""
    if len(sys.argv) < 2:
        print("Usage: python research_visualizer.py <research_directory> [output_file]")
        sys.exit(1)

    directory = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "research_evolution_report.md"

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory")
        sys.exit(1)

    visualizer = ResearchVisualizer()
    report = visualizer.generate_report(directory)

    with open(output_file, 'w') as f:
        f.write(report)

    print(f"✅ Visualization report saved to: {output_file}")


if __name__ == "__main__":
    main()
