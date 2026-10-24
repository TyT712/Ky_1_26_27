import pypdf
import os

pdf_path = os.path.join("data", "raw_pdfs", "chu_nghia_xa_hoi_khoa_hoc.pdf")
print("Exists:", os.path.exists(pdf_path))
if os.path.exists(pdf_path):
    print("Size:", os.path.getsize(pdf_path))
    reader = pypdf.PdfReader(pdf_path)
    print("Num pages:", len(reader.pages))
    
    # Check text in first 20 pages and last 10 pages for table of contents
    print("\n--- SAMPLE PAGES TEXT ---")
    for idx in range(min(15, len(reader.pages))):
        text = reader.pages[idx].extract_text() or ""
        print(f"Page {idx+1}: {len(text)} chars | Preview: {repr(text[:120])}")
        if "mục lục" in text.lower() or "chương" in text.lower():
            print(f"--> Page {idx+1} has keywords:\n{text[:500]}\n")
            
    print("\n--- CHECKING END PAGES FOR TOC ---")
    for idx in range(max(0, len(reader.pages)-10), len(reader.pages)):
        text = reader.pages[idx].extract_text() or ""
        print(f"Page {idx+1}: {len(text)} chars | Preview: {repr(text[:120])}")
        if "mục lục" in text.lower() or "chương" in text.lower():
            print(f"--> Page {idx+1} has keywords:\n{text[:500]}\n")
