"""Knowledge Retriever Skill: Truy xuất ngữ nghĩa và từ khóa đối chiếu chéo giữa giáo trình và NotebookLM."""

import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from src.utils.text_processing import chunk_markdown, format_citation

class AcademicRetriever:
    """Truy xuất đa tầng đối chiếu Giáo trình gốc (Parsed Markdown) & Tóm tắt NotebookLM."""

    def __init__(
        self,
        textbook_root: str = "data/parsed_markdown",
        notebook_root: str = "data/notebook_exports"
    ):
        self.textbook_root = Path(textbook_root)
        self.notebook_root = Path(notebook_root)

    def _score_chunk(self, query_terms: List[str], chunk_text: str, section_title: str) -> float:
        """Heuristic scoring based on term frequency and heading matches."""
        score = 0.0
        text_lower = chunk_text.lower()
        title_lower = section_title.lower()

        for term in query_terms:
            t_low = term.lower()
            if not t_low:
                continue
            # Heavy bonus if term is in heading
            if t_low in title_lower:
                score += 5.0
            # Frequency in body text
            matches = len(re.findall(re.escape(t_low), text_lower))
            score += matches * 1.0

        return score

    def search_layer(
        self,
        base_dir: Path,
        query: str,
        subject_code: Optional[str] = None,
        top_k: int = 5,
        source_type: str = "textbook"
    ) -> List[Dict[str, Any]]:
        """Search markdown files in a given knowledge layer."""
        if not base_dir.exists():
            return []

        search_glob = f"{subject_code}/**/*.md" if subject_code else "**/*.md"
        md_files = list(base_dir.glob(search_glob))
        if not md_files and subject_code:
            # Fallback to direct files in directory
            md_files = list(base_dir.glob("*.md"))

        query_terms = [q.strip() for q in query.split() if len(q.strip()) > 1]
        all_scored_chunks = []

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception:
                continue

            file_subject = md_file.parent.name if md_file.parent != base_dir else "general"
            chunks = chunk_markdown(
                markdown_content=content,
                subject_code=file_subject,
                source_file=md_file.name
            )

            for chunk in chunks:
                score = self._score_chunk(
                    query_terms=query_terms,
                    chunk_text=chunk["text"],
                    section_title=chunk["section_title"]
                )
                if score > 0:
                    chunk["score"] = score
                    chunk["source_type"] = source_type
                    chunk["citation"] = format_citation(
                        subject_code=chunk["subject_code"],
                        source_file=chunk["source_file"],
                        section_title=chunk["section_title"],
                        page=chunk["page"]
                    )
                    all_scored_chunks.append(chunk)

        # Sort descending by score
        all_scored_chunks.sort(key=lambda x: x["score"], reverse=True)
        return all_scored_chunks[:top_k]

    def dual_retrieve(
        self,
        query: str,
        subject_code: Optional[str] = None,
        top_k: int = 3
    ) -> Dict[str, Any]:
        """
        Execute Dual-Layer Academic Retrieval:
        1. Layer 1: NotebookLM summaries (overview & core insights)
        2. Layer 2: Original parsed textbook markdown (deep rigor & formulas)
        """
        notebook_results = self.search_layer(
            base_dir=self.notebook_root,
            query=query,
            subject_code=subject_code,
            top_k=top_k,
            source_type="notebooklm_summary"
        )

        textbook_results = self.search_layer(
            base_dir=self.textbook_root,
            query=query,
            subject_code=subject_code,
            top_k=top_k,
            source_type="textbook_official"
        )

        # Construct consolidated context for LLM grounding
        context_parts = []

        if notebook_results:
            context_parts.append("### [NGUỒN 1: TÓM TẮT TỔNG QUAN NOTEBOOKLM]")
            for item in notebook_results:
                context_parts.append(f"\n{item['citation']}:\n{item['text']}")

        if textbook_results:
            context_parts.append("\n### [NGUỒN 2: NỘI DUNG GIÁO TRÌNH CHÍNH THỐNG]")
            for item in textbook_results:
                context_parts.append(f"\n{item['citation']}:\n{item['text']}")

        consolidated_context = "\n".join(context_parts)

        return {
            "query": query,
            "subject_code": subject_code or "all",
            "notebook_matches": notebook_results,
            "textbook_matches": textbook_results,
            "total_matches": len(notebook_results) + len(textbook_results),
            "consolidated_context": consolidated_context
        }

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Skill Academic Retriever")
    parser.add_argument("query", type=str, help="Câu hỏi hoặc từ khóa cần tra cứu")
    parser.add_argument("--subject", type=str, default=None, help="Mã môn học")
    parser.add_argument("--top_k", type=int, default=3, help="Số lượng trích đoạn cần lấy")

    args = parser.parse_args()
    retriever = AcademicRetriever()
    res = retriever.dual_retrieve(args.query, subject_code=args.subject, top_k=args.top_k)

    print(f"\n=== KẾT QUẢ ĐỐI CHIẾU HỌC THUẬT CHO: '{args.query}' ===")
    print(f"Tổng số đoạn trích tìm thấy: {res['total_matches']}\n")
    if res["consolidated_context"]:
        print(res["consolidated_context"])
    else:
        print("[!] Không tìm thấy nội dung liên quan trong kho dữ liệu hiện tại.")

if __name__ == "__main__":
    main()
