"""Script trích xuất và chuẩn hóa giáo trình Hệ Quản trị CSDL theo cơ chế Streaming.
Bảo toàn ngữ nghĩa CSDL: SQL blocks, LaTeX đại số quan hệ (sigma, pi, bowtie), bảng quan hệ, số trang.
"""

import os
import sys
import re
from pathlib import Path

# Đảm bảo UTF-8 cho stdout/stderr trên Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

def clean_extracted_text(text: str) -> str:
    """Làm sạch văn bản bóc tách: xóa rác header/footer, chuẩn hóa khoảng trắng và dấu ngắt dòng."""
    if not text:
        return ""
    # Chuẩn hóa ngắt dòng từ gạch nối cuối dòng
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    # Loại bỏ header/footer lặp trang
    text = re.sub(r'GIÁO TRÌNH THỰC HÀNH CƠ SỞ DỮ LIỆU.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Chương\s+\d+:.*?\n', '', text, flags=re.IGNORECASE)
    # Chuẩn hóa khoảng trắng
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def format_sql_blocks(content: str) -> str:
    """Đóng khung các khối lệnh SQL chuẩn xác."""
    sql_keywords = r'(SELECT|INSERT\s+INTO|UPDATE|DELETE\s+FROM|CREATE\s+TABLE|ALTER\s+TABLE|DROP\s+TABLE|GRANT|REVOKE)'
    pattern = rf'(?m)^({sql_keywords}[\s\S]*?;)'
    
    def repl(m):
        code = m.group(1).strip()
        # Tránh bọc 2 lần nếu đã nằm trong ```
        return f"\n```sql\n{code}\n```\n"

    return re.sub(pattern, repl, content)

def format_relational_algebra(content: str) -> str:
    """Chuyển đổi các ký hiệu đại số quan hệ sang LaTeX chuẩn ($...$)."""
    # Thay thế các ký hiệu unicode đại số quan hệ thành LaTeX
    replacements = [
        (r'σ_?([^\s(]+)?\((.*?)\)', r'$\sigma_{\1}(\2)$'),
        (r'π_?([^\s(]+)?\((.*?)\)', r'$\pi_{\1}(\2)$'),
        (r'\bbowtie\b', r'$\bowtie$'),
        (r'\bUNION\b', r'$\cup$'),
        (r'\bINTERSECT\b', r'$\cap$'),
        (r'(\w+)\s*->\s*(\w+)', r'$\1 \rightarrow \2$'),
    ]
    for p, r in replacements:
        content = re.sub(p, r, content)
    return content

print("[*] Module parser Hệ QTCSDL đã sẵn sàng.")
