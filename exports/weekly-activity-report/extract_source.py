import json, re
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

SRC = "/root/.claude/uploads/740649a2-a5a9-5a9b-a94a-a0a642982174/f47f3dbc-CIFSO_Contractor_Combined_Weekly_Activity_Report_09-10-2026.docx"
HERE = "/home/user/valletta-design-system/exports/weekly-activity-report"

doc = Document(SRC)

def iter_block_items(parent):
    parent_elm = parent.element.body
    for child in parent_elm.iterchildren():
        if child.tag == qn('w:p'):
            yield "p", Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield "tbl", Table(child, parent)

def clean_cell(text):
    # normalize non-breaking spaces to regular spaces, strip outer whitespace,
    # but keep internal newlines (they separate meaningful sub-lines within a cell)
    lines = [re.sub(r"[\xa0]+", " ", ln).strip() for ln in text.split("\n")]
    lines = [l for l in lines if l != ""]
    return lines  # list of non-empty lines

blocks = []
for kind, item in iter_block_items(doc):
    if kind == "p":
        t = item.text.strip()
        if t:
            blocks.append({"type": "heading", "text": t})
    else:
        rows = []
        for row in item.rows:
            rows.append([clean_cell(c.text) for c in row.cells])
        blocks.append({"type": "table", "rows": rows})

with open(f"{HERE}/source_data.json", "w") as f:
    json.dump(blocks, f, indent=1)

print("blocks:", len(blocks))
print("headings:", sum(1 for b in blocks if b["type"] == "heading"))
print("tables:", sum(1 for b in blocks if b["type"] == "table"))
