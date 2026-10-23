"""
Module: chapter_study_pack_generator.py
Mục đích: Tự động hóa quy trình kiểm tra và chuẩn hóa cấu trúc Gói Học Liệu Tương Tác
(Executive Summary, Multiple Choice, Short Answer, Essay) từ Markdown chương giáo trình.
"""

import os
import re
import argparse
from typing import Dict, Any

class ChapterStudyPackValidator:
    """Kiểm tra và xác thực tính tuân thủ tiêu chuẩn của file học liệu tương tác."""

    @staticmethod
    def validate_file(file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            return {"valid": False, "error": f"File {file_path} không tồn tại."}

        with open(file_path, "r", encoding="utf-8") as fp:
            content = fp.read()

        # Kiểm tra 4 phần bắt buộc
        has_summary = bool(re.search(r"##\s+(?:PHẦN\s+1|1\.)\s*[:\-–]?\s*TÓM TẮT", content, re.IGNORECASE))
        has_mcq = bool(re.search(r"##\s+(?:PHẦN\s+2|2\.)\s*[:\-–]?\s*BÀI TẬP TRẮC NGHIỆM", content, re.IGNORECASE))
        has_short = bool(re.search(r"##\s+(?:PHẦN\s+3|3\.)\s*[:\-–]?\s*CÂU HỎI TRẢ LỜI NGẮN", content, re.IGNORECASE))
        has_essay = bool(re.search(r"##\s+(?:PHẦN\s+4|4\.)\s*[:\-–]?\s*BÀI TẬP TỰ LUẬN", content, re.IGNORECASE))

        # Đếm số câu trắc nghiệm
        mcq_count = len(re.findall(r"(?:###|####)\s*Câu\s+\d+", content))
        # Đếm số thẻ details
        details_count = content.count("<details>")
        # Đếm số block code và kiểm tra cân bằng
        ticks_count = content.count("```")
        even_ticks = (ticks_count % 2 == 0)

        # Đếm số bài tự luận
        essay_count = len(re.findall(r"(?:###|####)\s*Bài\s+\d+", content))

        valid = (has_summary and has_mcq and has_short and has_essay and 
                 mcq_count >= 10 and details_count >= 15 and even_ticks)

        return {
            "file": file_path,
            "valid": valid,
            "has_summary": has_summary,
            "has_mcq": has_mcq,
            "has_short": has_short,
            "has_essay": has_essay,
            "mcq_count": mcq_count,
            "essay_count": essay_count,
            "details_count": details_count,
            "even_ticks": even_ticks,
            "size_chars": len(content)
        }

def main():
    parser = argparse.ArgumentParser(description="Xác thực file học liệu tương tác.")
    parser.add_argument("file_path", help="Đường dẫn tới file học liệu .md")
    args = parser.parse_args()

    result = ChapterStudyPackValidator.validate_file(args.file_path)
    print(result)

if __name__ == "__main__":
    main()
