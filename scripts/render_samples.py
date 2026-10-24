import pypdfium2 as pdfium
import os

pdf_path = os.path.join("data", "raw_pdfs", "chu_nghia_xa_hoi_khoa_hoc.pdf")
doc = pdfium.PdfDocument(pdf_path)
print("Doc page count:", len(doc))

out_dir = "scripts/temp_renders"
os.makedirs(out_dir, exist_ok=True)

# Render pages 1..8 and 268..273
pages_to_render = [0, 1, 2, 3, 4, 5, 6, 7, 267, 268, 269, 270, 271, 272]
for pno in pages_to_render:
    if pno < len(doc):
        page = doc[pno]
        image = page.render(scale=1.5).to_pil()
        image_path = os.path.join(out_dir, f"page_{pno+1}.jpg")
        image.save(image_path)
        print(f"Rendered page {pno+1} -> {image_path}")

# Check if textpage extracts anything
for pno in [0, 1, 2, 3, 4, 5]:
    page = doc[pno]
    textpage = page.get_textpage()
    text = textpage.get_text_range()
    print(f"Page {pno+1} textpage length: {len(text)}")
