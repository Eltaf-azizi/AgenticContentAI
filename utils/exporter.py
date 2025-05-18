# utils/exporter.py


import os
from fpdf import FPDF


EXPORT_DIR = "static/exports"



def save_as_markdown(content: str, topic: str) -> str:
    os.makedirs(EXPORT_DIR, exit_ok=True)
    filename = f"{topic.replace(' ', '_').lower()}.md"
    filepath = os.path.join(EXPORT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filename



def save_as_pdf(content: str, topic: str) -> str:
    os.makedirs(EXPORT_DIR, exit_ok=True)