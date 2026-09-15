import os, json, html as _html

BLACK = "#0A0A0A"
CHARCOAL = "#26282B"
FIELD_WHITE = "#F5F5F3"
RED = "#FF002B"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"
TOTAL_TINT = "#F2E6E8"

HERE = os.path.dirname(os.path.abspath(__file__))
def b64(name):
    return open(os.path.join(HERE, name)).read().strip()

LOGO_BLACK = b64("valletta-mark-black.png.b64")
FONTS_CSS = open(os.path.join(HERE, "..", "fonts_embed.css")).read()

DATA = json.load(open(os.path.join(HERE, "source_data.json")))

MAJOR_HEADINGS = {
    "CIFSO Contractor Staffing",
    "OPERATIONS",
    "Contract Incident Reports:",
    "Daily Activity Report – Executive Summary",
    "Training Summary",
}

TOTAL_LABELS = {"total", "totals", "contract totals"}

def esc(s):
    return _html.escape(s, quote=False)

def sheet(inner, klass=""):
    return f'<section class="sheet {klass}">{inner}</section>'

def doc_header(period):
    return f'''<div class="doc-header">
      <img src="data:image/png;base64,{LOGO_BLACK}" alt="Valletta Industries"/>
      <div class="doc-title-block">
        <div class="doc-title">Contractor Combined Weekly Activity Report</div>
        <div class="doc-period">Reporting Period: {period}</div>
      </div>
    </div>'''

def doc_footer():
    return '<div class="doc-footer">Valletta Industries &nbsp;|&nbsp; Contractor Combined Weekly Activity Report<span class="pagenum"></span></div>'

def major_band(text):
    return f'<div class="major-band">{esc(text)}</div>'

def sub_heading(text):
    return f'<div class="sub-heading">{esc(text)}</div>'

def cell_lines(lines):
    if not lines:
        return "&nbsp;"
    return "".join(f'<div class="cell-line">{esc(l)}</div>' for l in lines)

def render_table(rows):
    header, *body = rows
    body = [r for r in body if any(c for c in r)]  # drop fully-blank rows
    ncols = len(header)
    first_w = 150
    other_w = None  # computed via CSS flex/equal share instead
    col_style = f'<col style="width:{first_w}px">' + f'<col>' * (ncols - 1)
    thead = "<tr>" + "".join(f'<th>{cell_lines(c)}</th>' for c in header) + "</tr>"
    body_rows = []
    for r in body:
        first_text = " ".join(r[0]).strip().lower() if r and r[0] else ""
        is_total = first_text in TOTAL_LABELS
        row_cls = "total-row" if is_total else ""
        cells = "".join(f'<td>{cell_lines(c)}</td>' for c in r)
        # pad short rows (ragged tables) with empty cells
        if len(r) < ncols:
            cells += "".join('<td>&nbsp;</td>' for _ in range(ncols - len(r)))
        body_rows.append(f'<tr class="{row_cls}">{cells}</tr>')
    return f'<table><colgroup>{col_style}</colgroup><thead>{thead}</thead><tbody>{"".join(body_rows)}</tbody></table>'

# ================= BUILD BLOCKS (heading(s) + table) per source order =================
BLOCKS = []
pending_headings = []
block_i = 0
for item in DATA:
    if item["type"] == "heading":
        pending_headings.append(item["text"])
    else:
        heads_html = ""
        for h in pending_headings:
            heads_html += major_band(h) if h in MAJOR_HEADINGS else sub_heading(h)
        pending_headings = []
        table_html = render_table(item["rows"])
        BLOCKS.append((f"block{block_i}", heads_html + table_html))
        block_i += 1

REPORT_PERIOD = "9/4/2026 thru 9/10/2026"

# ---- measure each block's natural height, then greedily pack onto landscape pages ----
MEASURE_CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; }}
.probe {{ width:972px; font-family:'Inter',sans-serif; color:{CHARCOAL}; position:absolute; left:0; top:0; }}
.major-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:13px;
  letter-spacing:1.4px; text-transform:uppercase; padding:8px 12px; margin:14px 0 8px; }}
.sub-heading {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:0.3px; color:{BLACK};
  text-transform:uppercase; margin:10px 0 6px; padding-bottom:4px; border-bottom:1.5px solid {RED}; }}
table {{ border-collapse:collapse; width:100%; table-layout:fixed; margin-bottom:6px; }}
th {{ background:{BLACK}; color:{WHITE}; font-family:'Inter'; font-weight:700; font-size:8.3px; letter-spacing:0.2px;
  text-transform:uppercase; text-align:left; padding:5px 6px; border:1px solid {BLACK}; line-height:1.25; }}
td {{ border:1px solid {LINE_GRAY}; padding:4px 6px; font-size:8.6px; line-height:1.32; color:{CHARCOAL}; vertical-align:top; word-wrap:break-word; }}
tbody tr:nth-child(even) {{ background:#EFEFEC; }}
.total-row td {{ background:{TOTAL_TINT}; font-weight:700; color:{BLACK}; }}
.cell-line + .cell-line {{ margin-top:1px; }}
'''
MEASURE_HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>{MEASURE_CSS}</style></head>
<body>{"".join(f'<div class="probe" id="probe-{i}">{html_}</div>' for i, (name, html_) in enumerate(BLOCKS))}</body></html>'''
measure_path = os.path.join(HERE, "_measure.html")
with open(measure_path, "w") as f:
    f.write(MEASURE_HTML)

from playwright.sync_api import sync_playwright
heights = {}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    page = browser.new_page(viewport={"width": 1100, "height": 400})
    page.goto("file://" + measure_path)
    page.wait_for_timeout(200)
    for i, (name, _) in enumerate(BLOCKS):
        h = page.evaluate(f'document.getElementById("probe-{i}").getBoundingClientRect().height')
        heights[name] = h
    browser.close()
os.remove(measure_path)

PAGE_BUDGET = 660
groups = []
cur, cur_h = [], 0
for name, html_ in BLOCKS:
    h = heights[name]
    if cur and cur_h + h > PAGE_BUDGET:
        groups.append(cur)
        cur, cur_h = [], 0
    cur.append(html_)
    cur_h += h
if cur:
    groups.append(cur)

def sheet_page(blocks_html):
    return sheet(doc_header(REPORT_PERIOD) + "".join(blocks_html) + doc_footer())

PAGES = [sheet_page(g) for g in groups]

CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#CBCCCA; counter-reset:pagenum; }}
.sheet {{ width:1056px; height:816px; background:{FIELD_WHITE}; position:relative; overflow:hidden;
  padding:34px 42px 44px; font-family:'Inter',sans-serif; color:{CHARCOAL}; break-after:page; margin:0 auto;
  counter-increment:pagenum; }}
.sheet + .sheet {{ margin-top:2px; }}
.sheet .pagenum::before {{ content:" \\2013  Page " counter(pagenum) " of {len(PAGES)}"; }}

.doc-header {{ display:flex; align-items:center; gap:20px; padding-bottom:10px;
  border-bottom:2px solid {RED}; margin-bottom:12px; }}
.doc-header img {{ height:28px; width:auto; display:block; }}
.doc-title-block {{ border-left:1px solid {LINE_GRAY}; padding-left:18px; }}
.doc-title {{ font-family:'Oswald'; font-weight:700; font-size:15px; letter-spacing:0.3px; text-transform:uppercase; color:{BLACK}; }}
.doc-period {{ font-family:'Inter'; font-weight:600; font-size:9.5px; letter-spacing:0.4px; color:{STEEL}; text-transform:uppercase; margin-top:2px; }}
.doc-footer {{ position:absolute; left:0; right:0; bottom:18px; text-align:center; font-family:'Inter';
  font-weight:600; font-size:8.5px; letter-spacing:0.5px; color:{STEEL}; }}

.major-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:13px;
  letter-spacing:1.4px; text-transform:uppercase; padding:8px 12px; margin:14px 0 8px; }}
.sub-heading {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:0.3px; color:{BLACK};
  text-transform:uppercase; margin:10px 0 6px; padding-bottom:4px; border-bottom:1.5px solid {RED}; }}

table {{ border-collapse:collapse; width:100%; table-layout:fixed; margin-bottom:6px; }}
th {{ background:{BLACK}; color:{WHITE}; font-family:'Inter'; font-weight:700; font-size:8.3px; letter-spacing:0.2px;
  text-transform:uppercase; text-align:left; padding:5px 6px; border:1px solid {BLACK}; line-height:1.25; }}
td {{ border:1px solid {LINE_GRAY}; padding:4px 6px; font-size:8.6px; line-height:1.32; color:{CHARCOAL}; vertical-align:top; word-wrap:break-word; }}
tbody tr:nth-child(even) {{ background:#EFEFEC; }}
.total-row td {{ background:{TOTAL_TINT}; font-weight:700; color:{BLACK}; }}
.cell-line + .cell-line {{ margin-top:1px; }}
'''

html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{"".join(PAGES)}
</body></html>'''

with open(os.path.join(HERE, "valletta_weekly_activity_report.html"), "w") as f:
    f.write(html)

print("written", len(PAGES), "pages,", len(BLOCKS), "table blocks")
