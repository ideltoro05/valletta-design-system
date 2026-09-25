import os

BLACK = "#0A0A0A"
CHARCOAL = "#26282B"
FIELD_WHITE = "#F5F5F3"
COBALT = "#1B4FA0"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"

HERE = os.path.dirname(os.path.abspath(__file__))
def b64(name):
    return open(os.path.join(HERE, name)).read().strip()

# combined Valletta+SOC lockup carries its own black backdrop, so the same asset
# works both in the running header and on the black cover (v2.0 co-branding directive)
LOGO_COMBINED = b64("valletta-soc-lockup.png.b64")
FONTS_CSS = open(os.path.join(HERE, "..", "fonts_embed.css")).read()

def header():
    return f'''<div class="doc-header">
      <img src="data:image/png;base64,{LOGO_COMBINED}" alt="Valletta Industries / SOC"/>
      <div class="doc-tag">SOP &ndash; Firearms Loading and Unloading</div>
    </div>'''

def footer():
    return '<div class="doc-footer">Valletta Industries &nbsp;|&nbsp; SOP &ndash; Firearms Loading and Unloading<span class="pagenum"></span></div>'

def sheet(inner, klass=""):
    return f'<section class="sheet {klass}">{inner}</section>'

def sec(num, title):
    return f'<div class="sec-title"><span class="sec-num">{num}.</span> {title}</div>'

def subhead(text):
    return f'<div class="h2-sub">{text}</div>'

def item(label, text, level=1, bold=False):
    cls = f"ol-lvl{level}" + (" ol-bold" if bold else "")
    lbl = f'<span class="ol-label">{label}</span>' if label else ""
    return f'<div class="{cls}">{lbl}<span class="ol-text">{text}</span></div>'

def bullet(text):
    return f'<li>{text}</li>'

def note(tag, lines):
    body = "".join(f'<div class="note-line">{l}</div>' for l in lines)
    return f'<div class="note-box"><span class="note-tag">{tag}</span>{body}</div>'

def field_row(label, value=""):
    return f'<div class="field-row"><span class="field-label">{label}</span><span class="field-line">{value}</span></div>'

def sig_row(label):
    return f'<div class="sig-row"><span class="sig-label">{label}</span><span class="sig-line"></span></div>'

# ================= CONTENT BLOCKS =================
BLOCKS = []

COVER_HTML = sheet(f'''
  <div class="cover-tick tl"></div><div class="cover-tick br"></div>
  <img class="cover-logo" src="data:image/png;base64,{LOGO_COMBINED}" alt="Valletta Industries / SOC"/>
  <div class="cover-eyebrow">Standard Operating Procedure</div>
  <div class="cover-title">Firearms Loading<br/>and Unloading</div>
  <div class="cover-meta-box">
    {field_row("Document Number", "")}
    {field_row("Effective Date", "")}
    {field_row("Revision", "1.0")}
    {field_row("Approved By", "")}
  </div>
''', "cover")

BLOCKS.append(("s1", sec(1, "Purpose") + item("1.1", "To establish safe, standardized, and accountable procedures for arming and disarming personnel, loading and unloading firearms, managing ammunition, and maintaining armory security during all guard force operations")))

BLOCKS.append(("s2", sec(2, "Scope") + item("2.1", "This SOP applies to all armed security personnel, supervisors, armorers, and other authorized personnel who issue, receive, handle, store, transport, or account for firearms and ammunition within the armory.")))

BLOCKS.append(("s3", sec(3, "Definitions and Acronyms")
    + item("3.1", "BCD &ndash; Bullet Containment Device")
    + item("3.2", "Armory &ndash; Secure location used for storage and accountability of firearms and ammunition.")
    + item("3.3", "Facility Ready &ndash; Condition of in-service duty firearms")
    + item("3.3.1", "Rifle &ndash; Full magazine inserted with empty chamber unless otherwise authorized.", 2)
    + item("3.3.2", "Pistol &ndash; Full magazine inserted with a round chambered.", 2)
    + item("3.4", "Safe Firearm &ndash; Firearm verified clear of ammunition and configured for storage.")
))

BLOCKS.append(("s4", sec(4, "Responsibility and Authority")
    + item("4.1", "Supervisors", 1, bold=True)
    + item("4.1.1", "Control access to the armory and firearms safe.", 2)
    + item("4.1.2", "Open and secure safes at shift change", 2)
    + item("4.1.3", "Observe and direct all loading and unloading operations", 2)
    + item("4.1.4", "Verify compliance with this SOP and stop unsafe acts immediately", 2)
    + item("4.1.5", "Conduct required daily armory inventory, records and discrepancy reporting", 2)
    + item("4.2", "Armed Officers", 1, bold=True)
    + item("4.2.1", "Follow all firearm safety rules", 2)
    + item("4.2.2", "Comply with Supervisor commands during loading/unloading", 2)
    + item("4.2.3", "Immediately report unsafe conditions, damaged equipment, or ammunition discrepancies.", 2)
    + item("4.3", "Site Trainers", 1, bold=True)
    + item("4.3.1", "Maintain serviceability of firearms and ammunition.", 2)
    + item("4.3.2", "Ensure inspections, maintenance, storage, and records are current.", 2)
))

BLOCKS.append(("s5", sec(5, "General Firearms Safety Rules")
    + item("5.1", "Treat every firearm as if it is loaded.")
    + item("5.2", "Keep muzzle pointed in a safe direction at all times.")
    + item("5.3", "Keep fingers off the trigger, outside the trigger guard, and safety engaged until you decide to fire.")
    + item("5.4", "Be sure of your target and what&rsquo;s beyond it.")
))

BLOCKS.append(("s6", sec(6, "Supervisor Requirements During Shift Change")
    + item("6.1", "Supervisor Shall:", 1, bold=True)
    + item("6.1.1", "Open the firearm safe and maintain positive control of issued firearms.", 2)
    + item("6.1.2", "Observe every loading and unloading action from start to finish.", 2)
    + item("6.1.3", "Verify firearms are clear before issue and before storage.", 2)
    + item("6.1.4", "Ensure use of the BCD during all chambering and clearing operations.", 2)
    + item("6.1.5", "Verify ammunition counts, magazine counts, and firearm serial numbers as required.", 2)
    + item("6.1.6", "Halt any unsafe act immediately.", 2)
    + item("6.1.7", "Ensure all issued firearms, ammunition, and equipment are accounted for before personnel depart.", 2)
    + item("6.1.8", "Secure all safes and armory access points after completion of shift-change operations.", 2)
    + item("6.1.9", "Maintain constant visual and physical control of contents inside the safe.", 2)
))

BLOCKS.append(("s7", sec(7, "Firearm Loading Procedure")
    + item("7.1", "Supervisor will retrieve the correct firearm from storage.")
    + item("7.2", "Insert muzzle into the BCD, visually verifying serial number.")
    + item("7.2.1", "Rifle &ndash; Verify safety is engaged.", 2)
    + item("7.3", "Lock the action to the rear, visually and physically verifying the firearm is clear.")
    + item("7.4", "The supervisor will transfer control of the firearm to the officer.")
    + item("7.5", "While still pointed into the BCD, the officer will re-verify the firearm is clear.")
    + item("7.6", "Source of Feed:")
    + item("7.6.1", "Pistol &ndash; Insert magazine and release the action, chambering a round.", 2)
    + item("7.6.2", "Rifle &ndash; Release the action before inserting magazine. No round will be chambered.", 2)
    + item("7.7", "Retain the firearm.")
    + note("NOTE", ["Officer may conduct press checks or magazine retention tests."])
))

BLOCKS.append(("s8", sec(8, "Firearm Unloading Procedure")
    + item("8.1", "Insert muzzle into the BCD, visually verifying serial number.")
    + item("8.1.1", "Rifle &ndash; Verify safety is engaged.", 2)
    + item("8.2", "Remove the magazine.")
    + item("8.3", "Lock action to the rear, ejecting the chambered round, if present.")
    + item("8.4", "Visually and physically verify the firearm is clear.")
    + item("8.5", "The officer will transfer control of the firearm to the supervisor.")
    + item("8.6", "While still pointed into the BCD, the supervisor will re-verify the firearm is clear.")
    + item("8.6.1", "Rifle &ndash; Verify safety is engaged.", 2)
    + item("8.7", "Release the action and place the firearm into storage.")
    + item("8.8", "Collect and replace ejected round if present, return all magazines to the proper storage.")
))

BLOCKS.append(("s9", sec(9, "Firearms Storage Requirements")
    + item("9.1", "Firearms shall be stored unloaded unless operation requirements dictate otherwise")
    + item("9.2", "Out-of-service firearms shall be tagged or segregated from service firearms.")
    + item("9.3", "Storage containers/firearms safes shall remain locked when not under direct supervisory observation and control.")
))

BLOCKS.append(("s10", sec(10, "Ammunition Accountability and Management")
    + item("10.1", "Only authorized duty ammunition shall be issued.")
    + item("10.2", "Ammunition counts shall be verified during issue and turn-in.")
    + item("10.3", "Damaged or suspected ammunition shall be removed.")
    + item("10.4", "Duty ammunition shall be inspected and rotated in accordance with organizational policy")
    + item("10.5", "Monthly ammunition inventories shall be completed, reconciled, and documented by the Site Trainer. Any discrepancies shall be immediately reported to the National Training Manager and Site Manager and investigated in accordance with established procedures.")
))

BLOCKS.append(("s11", sec(11, "Documentation and Reporting")
    + item("11.1", "All firearms issues, returns, inventories, discrepancies, damaged ammunition, unsafe acts, training completion, SOP acknowledgments, and out-of-service firearms shall be documented by the supervisor or trainer in the records management systems.")
    + item("11.2", "Training records and employee acknowledgments for this SOP shall be maintained by Training management and retained in accordance with company record retention requirements.")
    + item("11.3", "Training management shall ensure personnel under their supervision have completed all required training and acknowledgments for this SOP.")
    + item("11.4", "Supervisors shall promptly document and report any violation of this SOP through established reporting channels.")
))

BLOCKS.append(("s12", sec(12, "Training and Compliance")
    + item("12.1", "Personnel shall receive initial training on this SOP prior to being issued a firearm, assigned to an armed post, or performing any duties covered by this SOP. Refresher training shall be conducted periodically as determined by organizational requirements.")
    + item("12.2", "Upon completion of training, personnel shall acknowledge in writing or through an approved electronic system that they have received, reviewed, understand, and will comply with this SOP. Documentation of training and acknowledgment shall be maintained in accordance with Section 12.2.")
    + item("12.3", "Supervisors or Trainers shall conduct observations, inspections, and corrective actions to ensure continued compliance with this SOP.")
    + item("12.4", "Failure to comply with the requirements of this SOP may result in corrective action up to and including removal from armed duties, suspension of firearm authorization, disciplinary action, or other corrective measures in accordance with established Employee Relations policies and procedures.")
    + item("12.5", "Personnel who have not completed the required training and acknowledgment process shall not be issued a firearm, ammunition, or assigned to an armed post until all requirements have been satisfied and documented.")
))

# ---- Acknowledgment forms ----
def ack_form(title, fields, intro, lead_in, bullets, closing, sig_labels):
    html = (
        sec_plain(title)
        + "".join(field_row(l, v) for l, v in fields)
        + '<div class="ack-label">Acknowledgment</div>'
        + f'<p class="body-p">{intro}</p>'
        + f'<p class="body-p">{lead_in}</p>'
        + '<ul class="ack-list">' + "".join(bullet(b) for b in bullets) + '</ul>'
        + f'<p class="body-p">{closing}</p>'
        + "".join(sig_row(l) for l in sig_labels)
    )
    return html

def sec_plain(title):
    return f'<div class="sec-title-plain">{title}</div>'

supervisor_ack = ack_form(
    "Firearms Loading and Unloading &ndash; Armed Shift Supervisor Acknowledgement",
    [
        ("Employee Name", ""), ("Employee ID", ""), ("Site/Contract", ""),
        ("Position", "Armed Shift Supervisor"), ("Date of Training", ""),
    ],
    "I acknowledge that I have received training on, reviewed, and understand the requirements of the Loading and Unloading of Firearms SOP.",
    "I understand my responsibilities include:",
    [
        "Complying with all requirements of the SOP.",
        "Ensuring firearms loading and unloading activities are conducted only in designated locations and in accordance with established procedures.",
        "Conducting oversight of armed personnel under my supervision to verify compliance with this SOP.",
        "Ensuring required inspections, inventories, documentation, and reporting requirements are completed accurately and timely.",
        "Taking immediate corrective action when unsafe acts, policy violations, or procedural deficiencies are observed.",
        "Reporting incidents, discrepancies, unsafe conditions, damaged equipment, or violations through established reporting channels.",
        "Ensuring personnel complete required training and acknowledgment requirements before being issued firearms, ammunition, or assigned to armed duties.",
        "Understanding that failure to comply with this SOP may result in disciplinary action, including removal from armed duties, suspension of firearm authorization, or other corrective action in accordance with company policy.",
    ],
    "I agree to comply with the requirements of this SOP and to enforce its provisions within my area of responsibility.",
    ["Supervisor Employee Signature", "Date", "Trainer/Manager Signature", "Date"],
)

officer_ack = ack_form(
    "Firearms Loading and Unloading &ndash; Armed Officer Acknowledgement",
    [
        ("Employee Name", ""), ("Employee ID", ""), ("Site/Contract", ""),
        ("Position", "Armed Officer"), ("Date of Training", ""),
    ],
    "I acknowledge that I have received training on, reviewed, and understand the requirements of the Loading and Unloading of Firearms SOP.",
    "I understand and agree that:",
    [
        "I shall comply with all firearm loading, unloading, handling, storage, and accountability requirements contained in this SOP.",
        "I shall load and unload firearms only in designated locations and in accordance with approved procedures.",
        "I shall immediately report unsafe acts, firearm malfunctions, damaged ammunition, equipment deficiencies, or policy violations to my supervisor.",
        "I shall participate in required inspections, inventories, and documentation processes.",
        "I shall maintain accountability for all firearms, ammunition, and related equipment issued to me.",
        "I shall not deviate from established procedures unless directed by authorized management during an emergency situation.",
        "I understand that completion of SOP training and acknowledgment is required before I may be issued a firearm, ammunition, or assigned to an armed post.",
        "I understand that failure to comply with this SOP may result in disciplinary action, including removal from armed duties, suspension of firearm authorization, or other corrective action in accordance with company policy.",
    ],
    "I agree to comply with all requirements of this SOP and understand that I am responsible for following all applicable firearm safety and accountability requirements.",
    ["Officer Signature", "Date", "Trainer/Manager Signature", "Date"],
)

BLOCKS.append(("ack1", supervisor_ack))
BLOCKS.append(("ack2", officer_ack))

# ---- measure each block's natural height, then greedily pack onto pages ----
MEASURE_CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; }}
.probe {{ width:700px; font-family:'Inter',sans-serif; color:{CHARCOAL}; position:absolute; left:0; top:0; }}
.sec-title {{ font-family:'Oswald'; font-weight:700; font-size:15.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:18px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {COBALT}; }}
.sec-num {{ color:{COBALT}; }}
.sec-title-plain {{ font-family:'Oswald'; font-weight:700; font-size:14.5px; letter-spacing:0.2px; text-transform:uppercase;
  color:{BLACK}; margin:6px 0 14px; padding-bottom:6px; border-bottom:1.5px solid {COBALT}; }}
.h2-sub {{ font-family:'Inter'; font-weight:700; font-size:12px; letter-spacing:0.6px; color:{BLACK}; text-transform:uppercase; margin:12px 0 6px; }}
.ol-lvl1, .ol-lvl2 {{ font-size:10.7px; line-height:1.46; margin-bottom:6px; color:{CHARCOAL}; }}
.ol-lvl1 {{ padding-left:4px; }}
.ol-lvl2 {{ padding-left:30px; }}
.ol-bold > .ol-text {{ font-weight:700; color:{BLACK}; }}
.ol-label {{ color:{COBALT}; font-weight:700; display:inline-block; min-width:34px; }}
.note-box {{ border-left:2px solid {COBALT}; background:#EFEFEC; padding:8px 12px; margin:10px 0; }}
.note-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:9px; letter-spacing:1.2px; color:{COBALT}; text-transform:uppercase; margin-bottom:3px; }}
.note-line {{ font-size:10.5px; line-height:1.42; color:{CHARCOAL}; }}
.field-row {{ display:flex; align-items:flex-end; margin-bottom:9px; font-size:10.5px; }}
.field-label {{ flex:none; font-weight:700; color:{COBALT}; text-transform:uppercase; letter-spacing:0.4px; font-size:9px; width:150px; }}
.field-line {{ flex:1; border-bottom:1px solid {LINE_GRAY}; padding-bottom:2px; min-height:13px; color:{CHARCOAL}; }}
.ack-label {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:0.4px; color:{BLACK}; text-transform:uppercase; margin:12px 0 6px; }}
.body-p {{ font-size:10.7px; line-height:1.48; margin-bottom:8px; color:{CHARCOAL}; }}
.ack-list {{ list-style:none; margin:6px 0 10px; }}
.ack-list li {{ position:relative; padding-left:15px; font-size:10.5px; line-height:1.48; margin-bottom:5px; color:{CHARCOAL}; }}
.ack-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{COBALT}; }}
.sig-row {{ display:flex; align-items:flex-end; margin-bottom:14px; margin-top:8px; font-size:10.5px; }}
.sig-label {{ flex:none; font-weight:600; color:{CHARCOAL}; width:190px; }}
.sig-line {{ flex:1; border-bottom:1px solid {LINE_GRAY}; min-height:13px; }}
.cover-meta-box .field-label {{ color:{COBALT}; }}
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
    page = browser.new_page(viewport={"width": 900, "height": 400})
    page.goto("file://" + measure_path)
    page.wait_for_timeout(200)
    for i, (name, _) in enumerate(BLOCKS):
        h = page.evaluate(f'document.getElementById("probe-{i}").getBoundingClientRect().height')
        heights[name] = h
    browser.close()
os.remove(measure_path)

PAGE_BUDGET = 862
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

PAGES = [COVER_HTML] + [sheet(header() + "".join(g) + footer()) for g in groups]

CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#CBCCCA; counter-reset:pagenum; }}
.sheet {{ width:816px; height:1056px; background:{FIELD_WHITE}; position:relative; overflow:hidden;
  padding:54px 58px 64px; font-family:'Inter',sans-serif; color:{CHARCOAL}; break-after:page; margin:0 auto;
  counter-increment:pagenum; }}
.sheet + .sheet {{ margin-top:2px; }}
.sheet .pagenum::before {{ content:" \\2013  Page " counter(pagenum) " of {len(PAGES)}"; }}

.doc-header {{ display:flex; align-items:center; justify-content:space-between; padding-bottom:12px;
  border-bottom:2px solid {COBALT}; margin-bottom:20px; }}
.doc-header img {{ height:46px; width:auto; display:block; }}
.doc-header .doc-tag {{ font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.4px; color:{STEEL}; text-transform:uppercase; }}
.doc-footer {{ position:absolute; left:0; right:0; bottom:26px; text-align:center; font-family:'Inter';
  font-weight:600; font-size:9px; letter-spacing:0.6px; color:{STEEL}; }}

.sec-title {{ font-family:'Oswald'; font-weight:700; font-size:15.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:18px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {COBALT}; }}
.sec-num {{ color:{COBALT}; }}
.sec-title-plain {{ font-family:'Oswald'; font-weight:700; font-size:14.5px; letter-spacing:0.2px; text-transform:uppercase;
  color:{BLACK}; margin:6px 0 14px; padding-bottom:6px; border-bottom:1.5px solid {COBALT}; }}
.h2-sub {{ font-family:'Inter'; font-weight:700; font-size:12px; letter-spacing:0.6px; color:{BLACK}; text-transform:uppercase; margin:12px 0 6px; }}

.ol-lvl1, .ol-lvl2 {{ font-size:10.7px; line-height:1.46; margin-bottom:6px; color:{CHARCOAL}; }}
.ol-lvl1 {{ padding-left:4px; }}
.ol-lvl2 {{ padding-left:30px; }}
.ol-bold > .ol-text {{ font-weight:700; color:{BLACK}; }}
.ol-label {{ color:{COBALT}; font-weight:700; display:inline-block; min-width:34px; }}

.note-box {{ border-left:2px solid {COBALT}; background:#EFEFEC; padding:8px 12px; margin:10px 0; }}
.note-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:9px; letter-spacing:1.2px; color:{COBALT}; text-transform:uppercase; margin-bottom:3px; }}
.note-line {{ font-size:10.5px; line-height:1.42; color:{CHARCOAL}; }}

.field-row {{ display:flex; align-items:flex-end; margin-bottom:9px; font-size:10.5px; }}
.field-label {{ flex:none; font-weight:700; color:{COBALT}; text-transform:uppercase; letter-spacing:0.4px; font-size:9px; width:150px; }}
.field-line {{ flex:1; border-bottom:1px solid {LINE_GRAY}; padding-bottom:2px; min-height:13px; color:{CHARCOAL}; }}

.ack-label {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:0.4px; color:{BLACK}; text-transform:uppercase; margin:12px 0 6px; }}
.body-p {{ font-size:10.7px; line-height:1.48; margin-bottom:8px; color:{CHARCOAL}; }}
.ack-list {{ list-style:none; margin:6px 0 10px; }}
.ack-list li {{ position:relative; padding-left:15px; font-size:10.5px; line-height:1.48; margin-bottom:5px; color:{CHARCOAL}; }}
.ack-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{COBALT}; }}
.sig-row {{ display:flex; align-items:flex-end; margin-bottom:14px; margin-top:8px; font-size:10.5px; }}
.sig-label {{ flex:none; font-weight:600; color:{CHARCOAL}; width:190px; }}
.sig-line {{ flex:1; border-bottom:1px solid {LINE_GRAY}; min-height:13px; }}

.cover {{ background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:0 90px; }}
.cover-tick {{ position:absolute; width:26px; height:26px; border-color:{COBALT}; border-style:solid; }}
.cover-tick.tl {{ left:40px; top:40px; border-width:3px 0 0 3px; }}
.cover-tick.br {{ right:40px; bottom:40px; border-width:0 3px 3px 0; }}
.cover-logo {{ height:110px; width:auto; margin-bottom:36px; }}
.cover-eyebrow {{ font-family:'Inter'; font-weight:700; font-size:13px; letter-spacing:3px; color:{COBALT}; text-transform:uppercase; margin-bottom:14px; }}
.cover-title {{ font-family:'Oswald'; font-weight:700; font-size:38px; line-height:1.2; letter-spacing:0.3px;
  text-transform:uppercase; color:{WHITE}; }}
.cover-meta-box {{ margin-top:44px; width:100%; max-width:420px; text-align:left; }}
.cover-meta-box .field-label {{ color:{COBALT}; width:170px; }}
.cover-meta-box .field-line {{ border-bottom:1px solid #4A4B4E; color:{WHITE}; }}
'''

html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{"".join(PAGES)}
</body></html>'''

with open(os.path.join(HERE, "valletta_weapons_sop.html"), "w") as f:
    f.write(html)

print("written", len(PAGES), "pages")
