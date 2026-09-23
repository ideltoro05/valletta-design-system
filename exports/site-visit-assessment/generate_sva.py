import os
import fitz
from sva_data import (
    TITLE, SUBTITLE, DOC_TAG, VISIT_FIELDS, PURPOSE_TEXT, ASSESSMENT_AREAS,
    SECTIONS, NARRATIVE_FIELDS, TOTAL_SCORE_FIELD, TOTAL_SCORE_VALUE,
    TOTAL_SCORE_LABEL, TOTAL_SCORE_SUBLABEL, TOTAL_SCORE_JS,
)

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- palette (Valletta design system: black/red/white; red is an accent, never a fill) ----
BLACK = (10/255, 10/255, 10/255)
CHARCOAL = (38/255, 40/255, 43/255)
FIELD_WHITE = (245/255, 245/255, 243/255)
RED = (255/255, 0/255, 43/255)
STEEL = (91/255, 95/255, 102/255)
LINE_GRAY = (216/255, 217/255, 219/255)
WHITE = (1, 1, 1)
NOTE_TINT = (0xEF/255, 0xEF/255, 0xEC/255)

PAGE_W, PAGE_H = 612, 792
MARGIN_X = 50
CONTENT_W = PAGE_W - 2 * MARGIN_X
HEADER_H = 68
FOOTER_H = 34
TOP_Y = HEADER_H + 22
BOTTOM_Y = PAGE_H - FOOTER_H - 6

F_HEAD = "Oswald-Bold"
F_HEAD_MED = "Oswald-Medium"
F_BODY = "Inter-Reg"
F_BODY_SEMI = "Inter-Semi"
F_BODY_BOLD = "Inter-Bold"

FONT_FILES = {
    F_HEAD: "fonts/Oswald-Bold-Static.ttf",
    F_HEAD_MED: "fonts/Oswald-Medium-Static.ttf",
    F_BODY: "fonts/Inter-Regular-Static.ttf",
    F_BODY_SEMI: "fonts/Inter-SemiBold-Static.ttf",
    F_BODY_BOLD: "fonts/Inter-Bold-Static.ttf",
}

doc = fitz.open()
page_indices = []

def new_page():
    page = doc.new_page(width=PAGE_W, height=PAGE_H)
    for name, path in FONT_FILES.items():
        page.insert_font(fontname=name, fontfile=os.path.join(HERE, path))
    page_indices.append(page.number)
    return page

_FONT_OBJS = {name: fitz.Font(fontfile=os.path.join(HERE, path)) for name, path in FONT_FILES.items()}

def text_len(text, font, size):
    return _FONT_OBJS[font].text_length(text, fontsize=size)

def wrapped_lines(text, font, size, max_width):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_len(trial, font, size) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]

def draw_header(page, page_num, total_pages):
    page.draw_rect(fitz.Rect(0, 0, PAGE_W, HEADER_H), color=None, fill=BLACK)
    logo_rect = fitz.Rect(MARGIN_X, 18, MARGIN_X + 130, 18 + 32)
    page.insert_image(logo_rect, filename=os.path.join(HERE, "valletta-mark-white.png"), keep_proportion=True)
    tag_w = text_len(DOC_TAG.upper(), F_BODY_SEMI, 8.5)
    page.insert_text((PAGE_W - MARGIN_X - tag_w, 32), DOC_TAG.upper(), fontname=F_BODY_SEMI, fontsize=8.5, color=WHITE)
    site_val = VISIT_FIELDS[0][2]
    date_val = VISIT_FIELDS[1][2]
    sub = f"SITE: {site_val.upper()}  –  {date_val.upper()}"
    sub_w = text_len(sub, F_BODY, 8)
    page.insert_text((PAGE_W - MARGIN_X - sub_w, 46), sub, fontname=F_BODY, fontsize=8, color=(0.72, 0.73, 0.75))
    page.draw_line((0, HEADER_H), (PAGE_W, HEADER_H), color=RED, width=2)

def draw_footer(page, page_num, total_pages):
    txt = f"Valletta Industries  |  Site Visit Assessment  –  Page {page_num} of {total_pages}"
    w = text_len(txt, F_BODY_SEMI, 8)
    page.insert_text(((PAGE_W - w) / 2, PAGE_H - 18), txt, fontname=F_BODY_SEMI, fontsize=8, color=STEEL)

def section_band_height():
    return 26

def draw_section_band(page, y, roman, title):
    h = section_band_height()
    page.draw_rect(fitz.Rect(MARGIN_X, y, MARGIN_X + CONTENT_W, y + h), color=None, fill=BLACK)
    txt = f"SECTION {roman}  —  {title.upper()}"
    page.insert_text((MARGIN_X + 12, y + h - 8), txt, fontname=F_HEAD, fontsize=11.5, color=WHITE)
    return y + h

def draw_sub_heading(page, y, text):
    page.insert_text((MARGIN_X, y), text.upper(), fontname=F_BODY_BOLD, fontsize=11, color=BLACK)
    ry = y + 5
    page.draw_line((MARGIN_X, ry), (MARGIN_X + CONTENT_W, ry), color=RED, width=1.3)
    return ry + 14

def add_text_widget(page, rect, field_name, value, fontsize=9.5, multiline=False):
    w = fitz.Widget()
    w.field_name = field_name
    w.field_type = fitz.PDF_WIDGET_TYPE_TEXT
    w.rect = rect
    w.field_value = value or ""
    w.text_font = "Helv"  # form-field input text uses a base14 font; widget DA strings don't reliably carry embedded custom fonts
    w.text_fontsize = fontsize
    w.text_color = CHARCOAL
    w.fill_color = WHITE
    w.border_color = LINE_GRAY
    w.border_width = 0.8
    if multiline:
        w.field_flags = 4096  # multiline
    page.add_widget(w)

def add_choice_widget(page, rect, field_name, options, value):
    w = fitz.Widget()
    w.field_name = field_name
    w.field_type = fitz.PDF_WIDGET_TYPE_COMBOBOX
    w.rect = rect
    w.choice_values = options
    w.field_value = value or options[0]
    w.text_font = "Helv"
    w.text_fontsize = 9.5
    w.text_color = CHARCOAL
    w.fill_color = WHITE
    w.border_color = LINE_GRAY
    w.border_width = 0.8
    page.add_widget(w)

# ============================================================
# PAGE 1 — cover / visit information
# ============================================================
p1 = new_page()
y = TOP_Y + 10
p1.insert_text((MARGIN_X, y + 24), TITLE, fontname=F_HEAD, fontsize=26, color=BLACK)
p1.draw_line((MARGIN_X, y + 32), (MARGIN_X + 90, y + 32), color=RED, width=2.5)
y += 56
p1.insert_text((MARGIN_X, y), SUBTITLE, fontname=F_BODY, fontsize=11, color=STEEL)
y += 34

y = draw_sub_heading(p1, y, "Visit Information")
for label, fname, val in VISIT_FIELDS:
    p1.insert_text((MARGIN_X, y), label, fontname=F_BODY_BOLD, fontsize=8.5, color=RED)
    y += 6
    rect = fitz.Rect(MARGIN_X, y, MARGIN_X + CONTENT_W, y + 20)
    p1.draw_rect(rect, color=LINE_GRAY, fill=WHITE, width=0.8)
    add_text_widget(p1, rect, fname, val)
    y += 30
y += 6

y = draw_sub_heading(p1, y, "Purpose and Scope")
lines = wrapped_lines(PURPOSE_TEXT, F_BODY, 10, CONTENT_W - 28)
box_h = 16 + len(lines) * 14
p1.draw_rect(fitz.Rect(MARGIN_X, y, MARGIN_X + CONTENT_W, y + box_h), color=None, fill=NOTE_TINT)
ty = y + 20
for ln in lines:
    p1.insert_text((MARGIN_X + 14, ty), ln, fontname=F_BODY, fontsize=10, color=CHARCOAL)
    ty += 14
y += box_h + 20

y = draw_sub_heading(p1, y, "Assessment Areas")
areas_lines = wrapped_lines(ASSESSMENT_AREAS, F_BODY, 10.5, CONTENT_W)
for ln in areas_lines:
    p1.insert_text((MARGIN_X, y), ln, fontname=F_BODY, fontsize=10.5, color=CHARCOAL)
    y += 15

# ============================================================
# SECTION / QUESTION PAGES
# ============================================================
RATING_W = 190
GAP = 16
QTEXT_W = CONTENT_W - RATING_W - GAP

page = new_page()
y = TOP_Y

for roman, title, qs in SECTIONS:
    # keep the band with at least its first question; start a new page if too tight
    if y + section_band_height() + 70 > BOTTOM_Y:
        page = new_page()
        y = TOP_Y
    y = draw_section_band(page, y, roman, title)
    y += 12

    NUM_INDENT = 24  # reserved width for the "NN." prefix, covers up to "26."

    for num, text, rfield, cfield, opts, rating, comment in qs:
        q_lines = wrapped_lines(text, F_BODY_SEMI, 10, QTEXT_W - NUM_INDENT)
        q_block_h = max(len(q_lines) * 13, 13) + 4
        comment_lines_n = max(2, min(5, 1 + len(comment) // 70))
        comment_h = comment_lines_n * 12 + 10
        block_h = q_block_h + 6 + 14 + comment_h + 16  # question + gap + "comments" label + box + spacing

        if y + block_h > BOTTOM_Y:
            page = new_page()
            y = TOP_Y

        num_str = f"{num}."
        page.insert_text((MARGIN_X, y + 10), num_str, fontname=F_BODY_BOLD, fontsize=10, color=RED)
        tx = MARGIN_X + NUM_INDENT
        ty = y
        for ln in q_lines:
            page.insert_text((tx, ty + 10), ln, fontname=F_BODY_SEMI, fontsize=10, color=BLACK)
            ty += 13

        rate_rect = fitz.Rect(MARGIN_X + CONTENT_W - RATING_W, y, MARGIN_X + CONTENT_W, y + 18)
        page.draw_rect(rate_rect, color=LINE_GRAY, fill=WHITE, width=0.8)
        add_choice_widget(page, rate_rect, rfield, opts, rating)

        y += q_block_h + 6
        page.insert_text((MARGIN_X, y), "Comments / observations:", fontname=F_BODY, fontsize=8.5, color=STEEL)
        y += 6
        com_rect = fitz.Rect(MARGIN_X, y, MARGIN_X + CONTENT_W, y + comment_h)
        page.draw_rect(com_rect, color=LINE_GRAY, fill=WHITE, width=0.8)
        add_text_widget(page, com_rect, cfield, comment, multiline=True)
        y += comment_h + 16

# ============================================================
# NARRATIVE + TOTAL SCORE (continues on current page or a new one)
# ============================================================
narrative_block_h = 20 + sum(70 for _ in NARRATIVE_FIELDS) + 20 + 60
if y + 40 > BOTTOM_Y:
    page = new_page()
    y = TOP_Y

y = draw_sub_heading(page, y, "Management Narrative and Visit Summary")
for label, fname, val in NARRATIVE_FIELDS:
    box_h = 70
    if y + 16 + box_h > BOTTOM_Y:
        page = new_page()
        y = TOP_Y
    page.insert_text((MARGIN_X, y), label, fontname=F_BODY_BOLD, fontsize=8.5, color=RED)
    y += 6
    rect = fitz.Rect(MARGIN_X, y, MARGIN_X + CONTENT_W, y + box_h)
    page.draw_rect(rect, color=LINE_GRAY, fill=WHITE, width=0.8)
    add_text_widget(page, rect, fname, val, multiline=True)
    y += box_h + 18

total_h = 56
if y + total_h > BOTTOM_Y:
    page = new_page()
    y = TOP_Y
page.draw_rect(fitz.Rect(MARGIN_X, y, MARGIN_X + CONTENT_W, y + total_h), color=None, fill=BLACK)
page.insert_text((MARGIN_X + 16, y + 22), TOTAL_SCORE_LABEL, fontname=F_HEAD, fontsize=13, color=WHITE)
page.insert_text((MARGIN_X + 16, y + 38), TOTAL_SCORE_SUBLABEL, fontname=F_BODY, fontsize=8, color=(0.72, 0.73, 0.75))
score_rect = fitz.Rect(MARGIN_X + CONTENT_W - 150, y + 12, MARGIN_X + CONTENT_W - 16, y + total_h - 12)
w = fitz.Widget()
w.field_name = TOTAL_SCORE_FIELD
w.field_type = fitz.PDF_WIDGET_TYPE_TEXT
w.rect = score_rect
w.field_value = TOTAL_SCORE_VALUE
w.text_font = "Helv"
w.text_fontsize = 14
w.text_color = WHITE
w.fill_color = None
w.border_color = None
w.field_flags = 1  # read-only (calculated display field)
w.script_calc = TOTAL_SCORE_JS
page.add_widget(w)

# ============================================================
# finalize: headers/footers now that total page count is known
# ============================================================
total_pages = len(page_indices)
for i, idx in enumerate(page_indices, start=1):
    pg = doc[idx]
    draw_header(pg, i, total_pages)
    draw_footer(pg, i, total_pages)

doc.set_metadata({"title": "Site Visit Assessment — Whiskey", "author": "Valletta Industries"})

# Ensure viewers regenerate widget appearances from current values (the source PDF set this too).
catalog_xref = doc.pdf_catalog()
doc.xref_set_key(catalog_xref, "AcroForm/NeedAppearances", "true")

out_path = os.path.join(HERE, "valletta_site_visit_assessment_whiskey.pdf")
doc.save(out_path)
print("written", total_pages, "pages ->", out_path)
