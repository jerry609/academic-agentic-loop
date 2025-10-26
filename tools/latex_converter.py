#!/usr/bin/env python3
"""
Markdown to LaTeX Converter for Research Proposals
Converts research exploration markdown to LaTeX format
"""

import re
import sys
from typing import Dict


class LatexConverter:
    """Convert research markdown to LaTeX"""

    def __init__(self):
        self.template = self._get_latex_template()

    def convert(self, markdown_text: str, metadata: Dict = None) -> str:
        """
        Convert markdown research proposal to LaTeX

        Args:
            markdown_text: Markdown content
            metadata: Optional metadata (title, author, date)

        Returns:
            Complete LaTeX document
        """
        # Extract title
        title = self._extract_title(markdown_text)

        # Convert sections
        latex_body = self._convert_body(markdown_text)

        # Fill template
        latex_doc = self.template.format(
            title=title,
            author=metadata.get('author', 'Research Agent') if metadata else 'Research Agent',
            date=metadata.get('date', '\\today') if metadata else '\\today',
            body=latex_body
        )

        return latex_doc

    def _get_latex_template(self) -> str:
        """Get LaTeX document template"""
        return r"""\documentclass[11pt,a4paper]{{article}}

% Packages
\usepackage{{geometry}}
\usepackage{{hyperref}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{graphicx}}
\usepackage{{cite}}
\usepackage{{enumitem}}
\usepackage{{titlesec}}
\usepackage{{abstract}}

% Page geometry
\geometry{{margin=1in}}

% Hyperlinks
\hypersetup{{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue
}}

% Title formatting
\titleformat{{\section}}
  {{\normalfont\Large\bfseries}}{{\thesection}}{{1em}}{{}}
\titleformat{{\subsection}}
  {{\normalfont\large\bfseries}}{{\thesubsection}}{{1em}}{{}}

% Document metadata
\title{{{title}}}
\author{{{author}}}
\date{{{date}}}

\begin{{document}}

\maketitle

\begin{{abstract}}
This document presents a comprehensive research exploration, including research questions, proposed methodology, expected contributions, and evaluation strategies.
\end{{abstract}}

{body}

\end{{document}}
"""

    def _extract_title(self, md: str) -> str:
        """Extract title from markdown"""
        # Look for first # heading
        match = re.search(r'^#\s+(.+)$', md, re.MULTILINE)
        if match:
            title = match.group(1)
            # Remove markdown formatting
            title = re.sub(r'\*\*(.+?)\*\*', r'\1', title)
            title = re.sub(r'\*(.+?)\*', r'\1', title)
            return self._escape_latex(title)
        return "Research Exploration"

    def _convert_body(self, md: str) -> str:
        """Convert markdown body to LaTeX"""
        lines = md.split('\n')
        latex_lines = []
        in_list = False

        for line in lines:
            # Skip title line
            if line.startswith('# '):
                continue

            # Section headers (##)
            if line.startswith('## '):
                if in_list:
                    latex_lines.append(r'\end{itemize}')
                    in_list = False
                section_title = line[3:].strip()
                section_title = self._escape_latex(section_title)
                latex_lines.append(f'\\section{{{section_title}}}')
                latex_lines.append('')

            # Subsection headers (###)
            elif line.startswith('### '):
                if in_list:
                    latex_lines.append(r'\end{itemize}')
                    in_list = False
                subsection_title = line[4:].strip()
                subsection_title = self._escape_latex(subsection_title)
                latex_lines.append(f'\\subsection{{{subsection_title}}}')
                latex_lines.append('')

            # Bullet points
            elif line.startswith('- ') or line.startswith('* '):
                if not in_list:
                    latex_lines.append(r'\begin{itemize}')
                    in_list = True
                content = line[2:].strip()
                content = self._convert_inline_formatting(content)
                latex_lines.append(f'  \\item {content}')

            # Numbered lists
            elif re.match(r'^\d+\.\s+', line):
                if in_list:
                    latex_lines.append(r'\end{itemize}')
                latex_lines.append(r'\begin{enumerate}')
                in_list = 'enum'
                content = re.sub(r'^\d+\.\s+', '', line)
                content = self._convert_inline_formatting(content)
                latex_lines.append(f'  \\item {content}')

            # Bold text
            elif '**' in line:
                if in_list:
                    latex_lines.append(r'\end{itemize}')
                    in_list = False
                content = self._convert_inline_formatting(line)
                latex_lines.append(content)
                latex_lines.append('')

            # Regular paragraph
            elif line.strip():
                if in_list:
                    latex_lines.append(r'\end{itemize}')
                    in_list = False
                content = self._convert_inline_formatting(line)
                latex_lines.append(content)
                latex_lines.append('')

            # Empty line
            else:
                if in_list == 'enum':
                    latex_lines.append(r'\end{enumerate}')
                    in_list = False
                latex_lines.append('')

        if in_list:
            latex_lines.append(r'\end{itemize}')

        return '\n'.join(latex_lines)

    def _convert_inline_formatting(self, text: str) -> str:
        """Convert inline markdown to LaTeX"""
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)

        # Italic
        text = re.sub(r'\*(.+?)\*', r'\\textit{\1}', text)
        text = re.sub(r'_(.+?)_', r'\\textit{\1}', text)

        # Code
        text = re.sub(r'`(.+?)`', r'\\texttt{\1}', text)

        # Links [text](url)
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'\\href{\2}{\1}', text)

        # Escape special characters
        text = self._escape_latex(text)

        return text

    def _escape_latex(self, text: str) -> str:
        """Escape LaTeX special characters"""
        # Skip already escaped sequences
        replacements = [
            ('\\', r'\\textbackslash{}'),
            ('&', r'\&'),
            ('%', r'\%'),
            ('$', r'\$'),
            ('#', r'\#'),
            ('_', r'\_'),
            ('{', r'\{'),
            ('}', r'\}'),
            ('~', r'\textasciitilde{}'),
            ('^', r'\^{}'),
        ]

        for old, new in replacements:
            text = text.replace(old, new)

        return text


def main():
    """CLI interface"""
    if len(sys.argv) < 2:
        print("Usage: python latex_converter.py <markdown_file> [output_file]")
        sys.exit(1)

    md_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else md_file.replace('.md', '.tex')

    with open(md_file, 'r') as f:
        markdown = f.read()

    converter = LatexConverter()
    latex = converter.convert(markdown)

    with open(output_file, 'w') as f:
        f.write(latex)

    print(f"✅ LaTeX document saved to: {output_file}")
    print(f"\nTo compile:")
    print(f"  pdflatex {output_file}")


if __name__ == "__main__":
    main()
