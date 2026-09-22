from pathlib import Path
import sys

from pypdf import PdfReader
import pypdfium2 as pdfium

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\VentureLab\tmp\review\zou-zhenhao-20260922")
ROOT.mkdir(parents=True, exist_ok=True)

FILES = [
    ("second-round", Path(r"E:\88888\第二轮作业＋邹振豪.pdf")),
    ("resume", Path(r"E:\88888\邹振豪-27年应届生-大模型应用开发AI Agent工程师求职简历 (2) (1).pdf")),
]

for label, pdf_path in FILES:
    reader = PdfReader(str(pdf_path))
    print(f"\n=====PDF {label} pages={len(reader.pages)}=====")
    for index, page in enumerate(reader.pages, start=1):
        print(f"\n--- {label.upper()} PAGE {index} ---")
        print(page.extract_text() or "")
    pdf = pdfium.PdfDocument(str(pdf_path))
    out_dir = ROOT / f"{label}-pages"
    out_dir.mkdir(exist_ok=True)
    for index in range(len(pdf)):
        image = pdf[index].render(scale=1.8).to_pil()
        image.save(out_dir / f"page-{index + 1}.png")
