#!/usr/bin/env python3
"""
arXiv Literature Search Tool
Fetches related papers from arXiv API based on keywords
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from typing import List, Dict
import json
import sys


class ArxivSearcher:
    """Search arXiv for related papers"""

    BASE_URL = "http://export.arxiv.org/api/query?"

    def __init__(self, max_results: int = 10):
        self.max_results = max_results

    def search(self, query: str, categories: List[str] = None) -> List[Dict]:
        """
        Search arXiv for papers matching query

        Args:
            query: Search query (keywords, title, author, etc.)
            categories: arXiv categories to filter (e.g., ['cs.AI', 'cs.LG'])

        Returns:
            List of paper dictionaries with keys:
            - title, authors, abstract, published, arxiv_id, pdf_url, categories
        """
        # Build search query
        search_query = f"all:{query}"
        if categories:
            cat_query = " OR ".join([f"cat:{cat}" for cat in categories])
            search_query = f"({search_query}) AND ({cat_query})"

        # URL encode parameters
        params = {
            'search_query': search_query,
            'start': 0,
            'max_results': self.max_results,
            'sortBy': 'relevance',
            'sortOrder': 'descending'
        }

        url = self.BASE_URL + urllib.parse.urlencode(params)

        try:
            # Fetch data from arXiv
            with urllib.request.urlopen(url) as response:
                data = response.read().decode('utf-8')

            # Parse XML response
            papers = self._parse_arxiv_response(data)
            return papers

        except Exception as e:
            print(f"Error fetching from arXiv: {e}", file=sys.stderr)
            return []

    def _parse_arxiv_response(self, xml_data: str) -> List[Dict]:
        """Parse arXiv API XML response"""
        papers = []

        # Define namespace
        ns = {'atom': 'http://www.w3.org/2005/Atom',
              'arxiv': 'http://arxiv.org/schemas/atom'}

        root = ET.fromstring(xml_data)

        for entry in root.findall('atom:entry', ns):
            paper = {}

            # Title
            title_elem = entry.find('atom:title', ns)
            paper['title'] = title_elem.text.strip().replace('\n', ' ') if title_elem is not None else ''

            # Authors
            authors = []
            for author in entry.findall('atom:author', ns):
                name_elem = author.find('atom:name', ns)
                if name_elem is not None:
                    authors.append(name_elem.text)
            paper['authors'] = authors

            # Abstract
            summary_elem = entry.find('atom:summary', ns)
            paper['abstract'] = summary_elem.text.strip().replace('\n', ' ') if summary_elem is not None else ''

            # Published date
            published_elem = entry.find('atom:published', ns)
            paper['published'] = published_elem.text if published_elem is not None else ''

            # arXiv ID
            id_elem = entry.find('atom:id', ns)
            if id_elem is not None:
                arxiv_id = id_elem.text.split('/')[-1]
                paper['arxiv_id'] = arxiv_id
                paper['pdf_url'] = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                paper['abs_url'] = f"https://arxiv.org/abs/{arxiv_id}"

            # Categories
            categories = []
            for cat in entry.findall('atom:category', ns):
                term = cat.get('term')
                if term:
                    categories.append(term)
            paper['categories'] = categories

            papers.append(paper)

        return papers

    def format_as_markdown(self, papers: List[Dict]) -> str:
        """Format papers as markdown for easy reading"""
        if not papers:
            return "No papers found."

        md = f"# Found {len(papers)} Related Papers\n\n"

        for i, paper in enumerate(papers, 1):
            md += f"## {i}. {paper['title']}\n\n"
            md += f"**Authors:** {', '.join(paper['authors'])}\n\n"
            md += f"**Published:** {paper['published'][:10]}\n\n"
            md += f"**Categories:** {', '.join(paper['categories'])}\n\n"
            md += f"**arXiv ID:** [{paper['arxiv_id']}]({paper['abs_url']})\n\n"
            md += f"**PDF:** [Download]({paper['pdf_url']})\n\n"
            md += f"**Abstract:** {paper['abstract'][:500]}...\n\n"
            md += "---\n\n"

        return md


def main():
    """CLI interface"""
    if len(sys.argv) < 2:
        print("Usage: python arxiv_search.py <query> [max_results]")
        print("Example: python arxiv_search.py 'attention mechanism' 10")
        sys.exit(1)

    query = sys.argv[1]
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    searcher = ArxivSearcher(max_results=max_results)
    papers = searcher.search(query)

    # Output as JSON
    print(json.dumps(papers, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
