from pathlib import Path
from zipfile import ZipFile
import sys

from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT = Path(r"D:\VentureLab\tmp\review\wang-yingqi-20260922")
sys.stdout.reconfigure(encoding="utf-8")

pdf_path = Path(r"E:\88888\王英琦-山东交通学院-简历.pdf")
reader = PdfReader(str(pdf_path))
print(f"PDF pages: {len(reader.pages)}")
for index, page in enumerate(reader.pages, start=1):
    print(f"\n--- PDF PAGE {index} ---")
    print(page.extract_text() or "")

pdf = pdfium.PdfDocument(str(pdf_path))
pdf_out = ROOT / "resume-pdf"
pdf_out.mkdir(parents=True, exist_ok=True)
for index in range(len(pdf)):
    image = pdf[index].render(scale=2.0).to_pil()
    image.save(pdf_out / f"page-{index + 1}.png")

for label, docx_path in [
    ("second-round", Path(r"E:\88888\第二轮作业-王英琦.docx")),
    ("application", Path(r"E:\88888\AI应用实习生申请-王英琦-山东交通学院-AI应用.docx")),
]:
    media_out = ROOT / label / "media"
    media_out.mkdir(parents=True, exist_ok=True)
    with ZipFile(docx_path) as archive:
        media_files = [name for name in archive.namelist() if name.startswith("word/media/")]
        print(f"{label} media count: {len(media_files)}")
        for name in media_files:
            target = media_out / Path(name).name
            target.write_bytes(archive.read(name))
            print(f"  {target.name}: {target.stat().st_size}")
