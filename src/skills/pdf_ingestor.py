"""PDF Ingestor Skill: Bóc tách giáo trình PDF sang định dạng Markdown chuẩn học thuật."""

import os
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, Optional, List

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from src.utils.text_processing import clean_text
from src.utils.gemini_client import GeminiClient

class PDFIngestor:
    """Skill bóc tách PDF giáo trình sang Markdown có cấu trúc mục lục và công thức."""

    def __init__(
        self,
        raw_pdf_root: str = "data/raw_pdfs",
        output_markdown_root: str = "data/parsed_markdown",
        gemini_client: Optional[GeminiClient] = None
    ):
        self.raw_pdf_root = Path(raw_pdf_root)
        self.output_markdown_root = Path(output_markdown_root)
        self.gemini_client = gemini_client or GeminiClient()

    def ingest_pdf_local(self, pdf_path: Path) -> str:
        """
        Local extraction fallback if pypdf or PyPDF2 is installed, 
        or minimal binary stream reader.
        """
        try:
            import pypdf
            reader = pypdf.PdfReader(str(pdf_path))
            pages_text = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                pages_text.append(f"<!-- PAGE {i + 1} -->\n\n{text}")
            return "\n\n".join(pages_text)
        except ImportError:
            # Informative placeholder if pypdf is not yet installed and Gemini API not configured
            return (
                f"# Tài liệu trích xuất từ: {pdf_path.name}\n\n"
                f"> [!NOTE]\n"
                f"> Cần cài đặt thư viện `pypdf` (`pip install pypdf`) hoặc cung cấp `GEMINI_API_KEY`\n"
                f"> để thực hiện trích xuất PDF tự động chất lượng cao.\n"
            )

    def process_file(
        self, 
        pdf_path: str, 
        subject_code: Optional[str] = None, 
        force_gemini: bool = False
    ) -> Dict[str, Any]:
        """
        Process a single PDF textbook into standardized academic markdown.
        """
        file_path = Path(pdf_path)
        if not file_path.exists():
            return {"success": False, "error": f"Tệp không tồn tại: {pdf_path}"}

        # Auto-detect subject_code from parent directory if not provided
        if not subject_code:
            parent_name = file_path.parent.name
            subject_code = parent_name if parent_name != "raw_pdfs" else "general"

        output_dir = self.output_markdown_root / subject_code
        output_dir.mkdir(parents=True, exist_ok=True)
        target_md_path = output_dir / f"{file_path.stem}.md"

        print(f"[*] Đang xử lý: {file_path.name} (Môn: {subject_code})...")

        markdown_content = ""
        method_used = "local"

        # Strategy 1: Gemini multimodal parsing for optimal math & tables
        if (force_gemini or self.gemini_client.is_configured()) and not os.getenv("DISABLE_GEMINI_PDF"):
            print("  -> Sử dụng Gemini Multimodal Engine để phân tích cấu trúc & LaTeX...")
            res = self.gemini_client.parse_pdf_with_gemini(str(file_path))
            if res.get("success"):
                markdown_content = res.get("markdown", "")
                method_used = "gemini_multimodal"
            else:
                print(f"  [!] Gemini parse cảnh báo: {res.get('error')}. Chuyển sang local fallback.")

        # Strategy 2: Local extraction fallback
        if not markdown_content:
            raw_text = self.ingest_pdf_local(file_path)
            markdown_content = clean_text(raw_text)
            method_used = "local_pypdf"

        # Write result to parsed_markdown
        target_md_path.write_text(markdown_content, encoding="utf-8")
        print(f"  [+] Đã lưu file Markdown: {target_md_path}")

        return {
            "success": True,
            "subject_code": subject_code,
            "source_pdf": str(file_path),
            "output_markdown": str(target_md_path),
            "char_count": len(markdown_content),
            "method": method_used
        }

    def batch_ingest(self) -> List[Dict[str, Any]]:
        """Scan all PDFs in data/raw_pdfs/ recursively and convert them."""
        results = []
        if not self.raw_pdf_root.exists():
            print(f"[!] Thư mục {self.raw_pdf_root} chưa tồn tại.")
            return results

        pdf_files = list(self.raw_pdf_root.glob("**/*.pdf"))
        if not pdf_files:
            print(f"[*] Không tìm thấy file PDF nào trong {self.raw_pdf_root}.")
            return results

        print(f"[*] Bắt đầu xử lý hàng loạt {len(pdf_files)} giáo trình PDF...")
        for pdf in pdf_files:
            res = self.process_file(str(pdf))
            results.append(res)
            
        return results

def main():
    parser = argparse.ArgumentParser(description="Skill PDF Ingestor cho giáo trình học thuật")
    parser.add_argument("--file", type=str, help="Đường dẫn file PDF cần bóc tách")
    parser.add_argument("--subject", type=str, help="Mã môn học")
    parser.add_argument("--batch", action="store_true", help="Xử lý toàn bộ kho PDF trong data/raw_pdfs")
    parser.add_argument("--gemini", action="store_true", help="Ưu tiên dùng Gemini API")

    args = parser.parse_args()
    ingestor = PDFIngestor()

    if args.batch:
        ingestor.batch_ingest()
    elif args.file:
        res = ingestor.process_file(args.file, subject_code=args.subject, force_gemini=args.gemini)
        print(res)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
