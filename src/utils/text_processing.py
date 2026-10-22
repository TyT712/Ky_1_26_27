"""Text processing and Markdown manipulation utilities for academic materials."""

import re
from typing import List, Dict, Any, Optional

def clean_text(text: str) -> str:
    """
    Clean raw text extracted from PDF or notes:
    - Fix broken hyphens at end of lines (e.g., 'nghiên-\\n cứu' -> 'nghiên cứu')
    - Normalize unicode spaces and excessive blank lines
    - Standardize quotation marks
    """
    if not text:
        return ""
    
    # Fix broken hyphenations
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    
    # Normalize multiple newlines (keep max 2 for markdown paragraphs)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Clean whitespace on individual lines
    lines = [re.sub(r'[ \t]+', ' ', line).strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    
    return text.strip()


def extract_sections_hierarchy(markdown_content: str) -> List[Dict[str, Any]]:
    """
    Extract heading tree hierarchy from markdown content.
    Returns list of sections with level, title, and content.
    """
    heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
    matches = list(heading_pattern.finditer(markdown_content))
    
    sections = []
    for i, match in enumerate(matches):
        level = len(match.group(1))
        title = match.group(2).strip()
        start_pos = match.end()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(markdown_content)
        
        section_text = markdown_content[start_pos:end_pos].strip()
        sections.append({
            "level": level,
            "title": title,
            "content": section_text,
            "char_count": len(section_text)
        })
        
    return sections


def chunk_markdown(
    markdown_content: str, 
    subject_code: str = "general",
    source_file: str = "",
    max_chunk_chars: int = 1500,
    overlap_chars: int = 150
) -> List[Dict[str, Any]]:
    """
    Semantic chunking for academic markdown documents:
    - Respects heading sections where possible
    - Detects embedded page markers: <!-- PAGE X -->
    - Attaches rich academic metadata to each chunk
    """
    sections = extract_sections_hierarchy(markdown_content)
    chunks = []
    
    current_page = 1
    page_marker_pattern = re.compile(r'<!--\s*PAGE\s+(\d+)\s*-->')
    
    # If no headers detected, split by double newlines (paragraphs)
    if not sections:
        sections = [{
            "level": 1,
            "title": "Chung",
            "content": markdown_content,
            "char_count": len(markdown_content)
        }]

    for sec in sections:
        title = sec["title"]
        level = sec["level"]
        content = sec["content"]
        
        # Check if page marker appears in this section
        page_match = page_marker_pattern.search(content)
        if page_match:
            current_page = int(page_match.group(1))

        if len(content) <= max_chunk_chars:
            chunks.append({
                "subject_code": subject_code,
                "source_file": source_file,
                "section_title": title,
                "section_level": level,
                "page": current_page,
                "text": f"### {title}\n{content}".strip()
            })
        else:
            # Split longer sections by paragraphs while keeping title context
            paragraphs = content.split('\n\n')
            current_chunk = []
            current_len = 0
            
            for p in paragraphs:
                p_clean = p.strip()
                if not p_clean:
                    continue
                    
                p_page = page_marker_pattern.search(p_clean)
                if p_page:
                    current_page = int(p_page.group(1))
                    
                if current_len + len(p_clean) > max_chunk_chars and current_chunk:
                    chunks.append({
                        "subject_code": subject_code,
                        "source_file": source_file,
                        "section_title": title,
                        "section_level": level,
                        "page": current_page,
                        "text": f"### {title} (tiếp tục)\n" + "\n\n".join(current_chunk)
                    })
                    current_chunk = [p_clean]
                    current_len = len(p_clean)
                else:
                    current_chunk.append(p_clean)
                    current_len += len(p_clean)
                    
            if current_chunk:
                chunks.append({
                    "subject_code": subject_code,
                    "source_file": source_file,
                    "section_title": title,
                    "section_level": level,
                    "page": current_page,
                    "text": f"### {title}\n" + "\n\n".join(current_chunk)
                })

    return chunks


def extract_latex_equations(content: str) -> Dict[str, List[str]]:
    """Extract inline and block LaTeX formulas from markdown text."""
    block_formulas = re.findall(r'\$\$(.*?)\$\$', content, re.DOTALL)
    inline_formulas = re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', content)
    
    return {
        "block": [f.strip() for f in block_formulas],
        "inline": [f.strip() for f in inline_formulas]
    }


def format_citation(
    subject_code: str,
    source_file: str,
    section_title: Optional[str] = None,
    page: Optional[int] = None
) -> str:
    """Format standardized academic citation tag."""
    parts = [f"Môn học: {subject_code}"]
    if source_file:
        parts.append(f"Tài liệu: {source_file}")
    if section_title:
        parts.append(f"Mục: {section_title}")
    if page:
        parts.append(f"Trang: {page}")
    return f"[{' | '.join(parts)}]"
