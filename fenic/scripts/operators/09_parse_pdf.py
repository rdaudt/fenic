from __future__ import annotations

from pathlib import Path

import fenic as fc
from common import get_session


def write_minimal_pdf(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        b"%PDF-1.4\n"
        b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
        b"2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n"
        b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R/Resources<</Font<</F1 5 0 R>>>>>>endobj\n"
        b"4 0 obj<</Length 68>>stream\nBT /F1 18 Tf 72 720 Td (Fenic parses PDF files into Markdown.) Tj ET\nendstream\nendobj\n"
        b"5 0 obj<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>endobj\n"
        b"xref\n0 6\n0000000000 65535 f \n0000000009 00000 n \n0000000056 00000 n \n"
        b"0000000111 00000 n \n0000000223 00000 n \n0000000341 00000 n \n"
        b"trailer<</Size 6/Root 1 0 R>>\nstartxref\n411\n%%EOF\n"
    )


session = get_session("fenic_operator_parse_pdf")
pdf_path = Path(__file__).with_name("sample_parse_pdf.pdf")
markdown_path = pdf_path.with_suffix(".md")
write_minimal_pdf(pdf_path)

df = session.create_dataframe([{"id": 1, "pdf_path": str(pdf_path)}])

result = df.select(
    "id",
    fc.semantic.parse_pdf("pdf_path", page_separator="\n\n--- page {page} ---\n\n").alias("markdown"),
)

rows = result.to_pylist()
markdown = rows[0]["markdown"]

print(markdown)
markdown_path.write_text(markdown, encoding="utf-8")
print(f"\nWrote parsed markdown to {markdown_path}")
