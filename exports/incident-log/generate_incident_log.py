import os, re

BLACK = "#0A0A0A"
CHARCOAL = "#26282B"
FIELD_WHITE = "#F5F5F3"
RED = "#FF002B"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"

HERE = os.path.dirname(os.path.abspath(__file__))
def b64(name):
    return open(os.path.join(HERE, name)).read().strip()

LOGO_BLACK = b64("valletta-mark-black.png.b64")
FONTS_CSS = open(os.path.join(HERE, "..", "fonts_embed.css")).read()

COLS = [
    ("SITE", 90),
    ("TYPE", 46),
    ("INCIDENT DESCRIPTION", 250),
    ("DATE", 58),
    ("STATUS & ACTION TAKEN", 512),
]

# ================= RAW DATA (verbatim from source table) =================
ROWS = [
    ("Charlie", "1", "Perimeter Fence and Exterior Security Assessment", "26C-0054", "9/9",
     "Closed – No deficiencies were noted."),
    ("Charlie", "1", "Building Perimeter Doors Security Assessment", "26C-0055", "9/10",
     "Closed – No deficiencies were noted."),
    ("District", "1", "Water Leak Outside of Building", "26DR-0026", "9/9",
     "Open – Water Leak Outside of Building.\n"
     "Sprinkle Pipe broke outside next to the East entry door.\n"
     "No water came inside the building.\n"
     "Water was shut off by the Facility Manager.\n"
     "Facility Manager is awaiting repairs from technicians."),
    ("District", "1", "Weekly Security Assessment", "26DR-0027", "9/10",
     "Open – The following deficiencies were noted:\n"
     "Building Light #5 is not operational.\n"
     "Parking Lot Light is not operational.\n"
     "Facility Manager is still waiting for repairs from technician."),
    ("India", "3", "Scheduled Power Outage", "26I-0059", "9/4",
     "Closed – Scheduled Power Outage\n"
     "Scheduled outage for generator / main power renovations.\n"
     "Supplemental generators are installed until the main power is restored.\n"
     "Main power restored successfully ahead of the original scheduled date.\n"
     "No lasting effect on the facility. Operations are now normal."),
    ("India", "1", "A100 Ceiling Leak", "26I-0060", "9/7",
     "Closed – A100 Ceiling Leak\n"
     "Minor leak found on A100 with no effect on product.\n"
     "Leak patched and under monitoring from 3PL staff as a precaution."),
    ("India", "1", "Building Perimeter Doors Security Assessment", "26I-0061", "9/9",
     "Closed – No deficiencies were noted."),
    ("Lima", "1", "Building Perimeter Doors Security Assessment", "26L-0046", "9/9",
     "Open – The following deficiencies were noted:\n"
     "Complete Building Perimeter Doors.\n"
     "Door #204 failed to call up due to the Camera INT FX 27-204 shot is misaligned.\n"
     "Facilities were notified."),
    ("Papa", "1", "Building Perimeter Doors Security Assessment", "26P-0075", "9/9",
     "Open – The following deficiencies were noted:\n"
     "Complete Building Perimeter Doors.\n"
     "Doors M29, M34, M36 and Alarms room do not receive an audible alarm.\n"
     "Facilities were notified."),
    ("Papa", "1", "Perimeter Fence False Alarm Zone 5", "26P-0074", "9/8",
     "Open – Perimeter Fence False Alarm Zone 5\n"
     "Zone 5 falsely triggers.\n"
     "Facilities were notified."),
    ("Sierra", "1", "Pedestrian Gate Equipment Failure", "26S-0048", "9/4",
     "Open – Pedestrian Gate Equipment Failure\n"
     "Magnet on pedestrian gate has broken off the wire due to a stripped screw\n"
     "Facilities were notified"),
    ("Sierra", "1", "Building Perimeter Doors Security Assessment", "26S-0049", "9/9",
     "Open – The following deficiencies were noted:\n"
     "OHD #163 did not trigger a visual call-up\n"
     "OHD #72 did not trigger an audible alarm or visual call-up\n"
     "PED #106 did not trigger and audible alarm or visual call-up\n"
     "Facilities were notified"),
    ("Sigma", "1", "Building Perimeter Doors Security Assessment", "26G-0047", "9/10",
     "Closed – No deficiencies were noted."),
    ("Tango", "1", "Building Perimeter Doors Security Assessment", "26T-0042", "9/7",
     "Closed – No deficiencies were noted."),
    ("Victor", "2", "Pedestrian Gate Magnet Broke", "26V-0073", "9/10",
     "Closed – Pedestrian Gate Magnet Broke.\n"
     "Repairs were made by technician\n"
     "The pedestrian gate is fully operational."),
    ("Victor", "1", "Building Perimeter Doors Security Assessment", "26V-0074", "9/10",
     "Closed – No deficiencies were noted."),
    ("Whiskey", "1", "Building Perimeter Doors Security Assessment", "26W-0065", "9/9",
     "Closed – No deficiencies were noted."),
    ("Xray", "1", "Building Perimeter Doors Security Assessment", "26X-0057", "9/7",
     "Open - The following deficiencies were noted:\n"
     "Complete Building Perimeter Doors\n"
     "Man-Doors M16, M17, M18, M19, M20, and M21 are offline due to construction.\n"
     "Man-Doors 6, 8, 9, 29 do not open all the way.\n"
     "Man-Door M17 unserviceable Plates.\n"
     "Facilities were notified."),
]

def status_html(text):
    lines = text.split("\n")
    first = lines[0]
    rest = lines[1:]
    m = re.match(r"^(Open|Closed)(\s*[–-]\s*)(.*)$", first)
    cls = "st-open" if (m and m.group(1) == "Open") else "st-closed"
    label = m.group(1) if m else ""
    lead_rest = m.group(3) if m else first
    out = f'<div class="status-cell {cls}"><span class="status-label">{label}</span> – {lead_rest}'
    for l in rest:
        out += f'<div class="status-line">{l}</div>'
    out += '</div>'
    return out

def header_row():
    cells = "".join(f'<th style="width:{w}px">{name}</th>' for name, w in COLS)
    return f'<thead><tr>{cells}</tr></thead>'

def data_row(site, typ, desc, case, date, status):
    return (
        '<tr>'
        f'<td>{site}</td>'
        f'<td class="cell-center">{typ}</td>'
        f'<td><div class="desc-main">{desc}</div><div class="desc-case">{case}</div></td>'
        f'<td class="cell-center">{date}</td>'
        f'<td>{status_html(status)}</td>'
        '</tr>'
    )

BLOCKS = [(f"row{i}", data_row(*r)) for i, r in enumerate(ROWS)]

def sheet(inner, klass=""):
    return f'<section class="sheet {klass}">{inner}</section>'

def page_header(period):
    return f'''<div class="doc-header">
      <img src="data:image/png;base64,{LOGO_BLACK}" alt="Valletta Industries"/>
      <div class="doc-title-block">
        <div class="doc-title">Contractor Combined Incident Report Log</div>
        <div class="doc-period">Reporting Period: {period}</div>
      </div>
    </div>'''

def page_footer():
    return '<div class="doc-footer">Valletta Industries &nbsp;|&nbsp; Contractor Combined Incident Report Log<span class="pagenum"></span></div>'

REPORT_PERIOD = "9/4 &ndash; 9/10/2026"

# ---- measure each row's natural height (rendered inside the real table width), then paginate ----
COL_GROUP = "".join(f'<col style="width:{w}px">' for _, w in COLS)
MEASURE_CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; }}
table {{ border-collapse:collapse; font-family:'Inter',sans-serif; table-layout:fixed; width:{sum(w for _, w in COLS)}px; }}
td, th {{ border:1px solid {LINE_GRAY}; padding:8px 10px; font-size:9.7px; line-height:1.42; color:{CHARCOAL}; vertical-align:top; word-wrap:break-word; }}
.cell-center {{ text-align:center; }}
.desc-main {{ font-weight:600; color:{BLACK}; margin-bottom:2px; }}
.desc-case {{ font-size:8.7px; color:{STEEL}; letter-spacing:0.2px; }}
.status-cell {{ }}
.status-label {{ font-weight:700; text-transform:uppercase; letter-spacing:0.3px; }}
.st-open .status-label {{ color:{RED}; }}
.st-closed .status-label {{ color:{STEEL}; }}
.status-line {{ margin-top:2px; }}
.probe {{ position:absolute; left:0; top:0; }}
.probe table {{ }}
'''
MEASURE_HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>{MEASURE_CSS}</style></head>
<body>{"".join(f'<div class="probe" id="probe-{i}"><table>{html_}</table></div>' for i, (name, html_) in enumerate(BLOCKS))}</body></html>'''
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

PAGE_BUDGET = 660  # usable table height per landscape page below header
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

def table_page(rows_html):
    return f'<table>{header_row()}<tbody>{"".join(rows_html)}</tbody></table>'

PAGES = [sheet(page_header(REPORT_PERIOD) + table_page(g) + page_footer()) for g in groups]

CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#CBCCCA; counter-reset:pagenum; }}
.sheet {{ width:1056px; height:816px; background:{FIELD_WHITE}; position:relative; overflow:hidden;
  padding:36px 42px 46px; font-family:'Inter',sans-serif; color:{CHARCOAL}; break-after:page; margin:0 auto;
  counter-increment:pagenum; }}
.sheet + .sheet {{ margin-top:2px; }}
.sheet .pagenum::before {{ content:" \\2013  Page " counter(pagenum) " of {len(PAGES)}"; }}

.doc-header {{ display:flex; align-items:center; gap:22px; padding-bottom:12px;
  border-bottom:2px solid {RED}; margin-bottom:16px; }}
.doc-header img {{ height:32px; width:auto; display:block; }}
.doc-title-block {{ border-left:1px solid {LINE_GRAY}; padding-left:20px; }}
.doc-title {{ font-family:'Oswald'; font-weight:700; font-size:16px; letter-spacing:0.3px; text-transform:uppercase; color:{BLACK}; }}
.doc-period {{ font-family:'Inter'; font-weight:600; font-size:10px; letter-spacing:0.5px; color:{STEEL}; text-transform:uppercase; margin-top:2px; }}
.doc-footer {{ position:absolute; left:0; right:0; bottom:20px; text-align:center; font-family:'Inter';
  font-weight:600; font-size:9px; letter-spacing:0.6px; color:{STEEL}; }}

table {{ border-collapse:collapse; font-family:'Inter',sans-serif; table-layout:fixed; width:100%; }}
th {{ background:{BLACK}; color:{WHITE}; font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:0.6px;
  text-transform:uppercase; text-align:left; padding:9px 10px; border:1px solid {BLACK}; }}
td {{ border:1px solid {LINE_GRAY}; padding:8px 10px; font-size:9.7px; line-height:1.42; color:{CHARCOAL}; vertical-align:top; word-wrap:break-word; }}
tbody tr:nth-child(even) {{ background:#EFEFEC; }}
.cell-center {{ text-align:center; }}
.desc-main {{ font-weight:600; color:{BLACK}; margin-bottom:2px; }}
.desc-case {{ font-size:8.7px; color:{STEEL}; letter-spacing:0.2px; }}
.status-label {{ font-weight:700; text-transform:uppercase; letter-spacing:0.3px; }}
.st-open .status-label {{ color:{RED}; }}
.st-closed .status-label {{ color:{STEEL}; }}
.status-line {{ margin-top:2px; }}
'''

html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{"".join(PAGES)}
</body></html>'''

with open(os.path.join(HERE, "valletta_incident_report_log.html"), "w") as f:
    f.write(html)

print("written", len(PAGES), "pages,", len(ROWS), "rows")
