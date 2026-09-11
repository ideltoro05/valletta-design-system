import os

BLACK = "#0A0A0A"
CHARCOAL = "#26282B"
FIELD_WHITE = "#F5F5F3"
ROW_TINT = "#ECECE9"
RED = "#FF002B"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"

HERE = os.path.dirname(os.path.abspath(__file__))
def b64(name):
    return open(os.path.join(HERE, name)).read().strip()

LOGO_BLACK = b64("valletta-mark-black.png.b64")
LOGO_WHITE = b64("valletta-mark-white.png.b64")
GOODRX = b64("goodrx.png.b64")
TRESAPP = b64("tresapp.png.b64")
FONTS_CSS = open(os.path.join(HERE, "..", "fonts_embed.css")).read()

def table(headers, rows, col_widths=None, first_col_left=True):
    widths = ""
    if col_widths:
        cols = "".join(f'<col style="width:{w}">' for w in col_widths)
        widths = f"<colgroup>{cols}</colgroup>"
    th = "".join(f'<th>{h}</th>' for h in headers)
    trs = []
    for r in rows:
        tds = []
        for cell in r:
            if isinstance(cell, (list, tuple)):
                inner = "<br/>".join(cell)
            else:
                inner = cell
            tds.append(f'<td>{inner}</td>')
        trs.append(f'<tr>{"".join(tds)}</tr>')
    return f'<table class="dtable">{widths}<thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table>'

def bullets(items):
    return '<ul class="bullets">' + "".join(f'<li>{i}</li>' for i in items) + '</ul>'

def header(tag_right="Employee Benefits Guide &nbsp;|&nbsp; 2026&ndash;2027"):
    return f'''<div class="doc-header">
      <img src="data:image/png;base64,{LOGO_BLACK}" alt="Valletta Industries"/>
      <div class="doc-tag">{tag_right}</div>
    </div>'''

def footer():
    return '<div class="doc-footer">Valletta Industries &nbsp;|&nbsp; Employee Benefits Guide &nbsp;|&nbsp; 2026&ndash;2027<span class="pagenum"></span></div>'

PAGES = []

# ---------- PAGE 1: COVER ----------
PAGES.append(f'''
<section class="sheet cover">
  <div class="cover-tick tl"></div><div class="cover-tick br"></div>
  <img class="cover-logo" src="data:image/png;base64,{LOGO_WHITE}" alt="Valletta Industries"/>
  <div class="cover-title">Employee<br/>Benefits Guide</div>
  <div class="cover-sub">August 1, 2026 &ndash; July 31, 2027</div>
</section>''')

# ---------- PAGE 2: Welcome + Benefits at a Glance + Eligibility & Enrollment ----------
PAGES.append(f'''
<section class="sheet">
  {header()}
  <h1 class="page-title">Welcome</h1>
  <p>Valletta Industries is committed to providing a comprehensive benefits program that helps employees and their
  families stay healthy, feel secure, and maintain work/life balance. This guide brings the available benefit
  information together in one place so you can review your options and use your benefits throughout the year.</p>
  <p>Use this guide as a convenient reference. For complete plan terms, limitations, exclusions, and eligibility
  requirements, always refer to the applicable plan documents. If there is a discrepancy between this guide and the
  governing plan documents, the plan documents will control.</p>

  <h2 class="section-title">Benefits at a Glance</h2>
  {table(["Item","Information"], [
    ["Plan Year","August 1, 2026 &ndash; July 31, 2027"],
    ["New-Hire Eligibility","Benefits begin the 1st of the month following 60 days"],
    ["Open Enrollment","Annually during July; 2026 elections are effective August 1, 2026 &ndash; July 31, 2027"],
  ], col_widths=["34%","66%"])}

  <h2 class="section-title">Eligibility &amp; Enrollment</h2>
  <h3 class="sub">Who Is Eligible?</h3>
  {bullets([
    "Employees who are full-time and work 30 or more hours per week.",
    "Legally married spouse.",
    "Biological, adopted, or stepchildren up to age 26.",
    "Children over age 26 who are disabled and depend on you for support.",
    "Children named in a Qualified Medical Child Support Order (QMCSO).",
  ])}
  <h3 class="sub">When Can I Change My Benefits?</h3>
  <p>If you experience a qualifying life event that results in the gain or loss of insurance for you or your
  dependents, report the event to HR within 30 days.</p>
  {bullets([
    "Marriage or divorce","Birth or adoption","Death of a spouse or child","Gain or loss of other coverage",
    "A change in employment status that affects benefit eligibility","Dependent child reaches age 26",
    "FMLA leave, COBRA event, court judgment or decree","Becoming eligible for Medicare",
    "Loss of Medicaid and/or CHIP","Receiving a Qualified Medical Child Support Order",
  ])}
  <h3 class="sub">Enrollment Reminder</h3>
  <p>If you do not enroll during the applicable enrollment period, you must wait until the next open enrollment
  period unless you experience a qualifying life event.</p>
  {footer()}
</section>''')

# ---------- PAGE 3: Medical Insurance ----------
med_rows = [
    ["Annual Deductible (Individual / Family)","$0 / $0","$0 / $0","$0 / $0"],
    ["Annual OOP Maximum (Individual / Family)","$9,100 / $18,200","$9,100 / $18,200","$9,100 / $18,200"],
    ["Preventive Care","100%","100%","100%"],
    ["Office / Specialist Visit","$25 / $50","$25 / $50; 8 per year","$25 / $50; 12 per year"],
    ["Urgent Care","$75","$75; 2 per year","$50; 3 per year"],
    ["Chiropractic","Not Covered","Not Covered","Not Covered"],
    ["Lab &amp; X-Ray (freestanding)","MedMo 100%; outside MedMo $50","MedMo 100%; outside MedMo $50; 1 per year","MedMo 100%; outside MedMo $50; 3 per year"],
    ["Imaging","MedMo 100%; outside MedMo $350","MedMo 100%; outside MedMo $350","MedMo 100%; outside MedMo $350"],
    ["Outpatient Hospital","$350","Hospital-based $350; non-hospital-based $750","Hospital-based $350; non-hospital-based $750"],
    ["Inpatient Hospital","Not Covered","$750; 1x per year","$750; 2x per year"],
    ["Physician Fees","Not Covered","$350","$350"],
    ["Emergency Room","Not Covered","$750","$750"],
    ["Generic Rx (Tier 1)","$10","$10","$10"],
    ["Preferred Brand (Tier 2)","Not Covered","Not Covered","$75"],
    ["Non-Preferred Brand (Tier 3)","Not Covered","Not Covered","$150"],
    ["Specialty (Tier 4)","Not Covered","Not Covered","Not Covered"],
]
cost_rows = [
    ["Employee","$104.22","$185.79","$273.37"],
    ["Employee + Spouse","$155.11","$320.04","$507.91"],
    ["Employee + Child(ren)","$133.66","$277.33","$418.71"],
    ["Family","$188.70","$424.89","$683.38"],
]
PAGES.append(f'''
<section class="sheet">
  {header()}
  <h1 class="page-title">Medical Insurance</h1>
  <p>Valletta Industries offers three medical plan options through Tres Health. The plan summaries below reflect the
  in-network information contained in the current benefits materials.</p>
  {table(["Benefit","MEC Advantage PPO","Core $0 RBP PPO","Prime $0 RBP PPO"], med_rows,
         col_widths=["27%","24.3%","24.3%","24.4%"])}
  {footer()}
</section>''')

PAGES.append(f'''
<section class="sheet">
  {header()}
  <h2 class="section-title" style="margin-top:0;">Medical Plan Cost Per Pay Period</h2>
  {table(["Coverage Tier","MEC Advantage","Core $0 RBP","Prime $0 RBP"], cost_rows,
         col_widths=["27%","24.3%","24.3%","24.4%"])}
  <p class="note-strong">Valletta Industries contributes $5.09 per hour, approximately $880 per month, through a
  fringe benefit allowance. The funds may be allocated toward available benefit plans selected.</p>
  <h3 class="sub">Medical Plan Support</h3>
  {bullets([
    "Tres Health Member Portal: member.tres.health",
    "Tres Health Member Services: 1-888-341-5606",
    "Group Number: 6607850",
  ])}
  <h3 class="sub">Find an In-Network Provider</h3>
  {bullets([
    "Log in to member.tres.health or use the Tres Health mobile app.",
    "Select Find a Provider.",
    "Search by service, specialty, or facility type and enter the ZIP code where services are needed.",
    "Filter by distance and review provider details.",
    "For assistance in finding an in-network provider, call 888-341-5606.",
  ])}
  <p class="callout-center">There is a limit of 3 doctor or specialist visits per year.</p>
  {footer()}
</section>''')

# ---------- PAGE 4: Prescription Resources + Medical Resources ----------
PAGES.append(f'''
<section class="sheet">
  {header()}
  <h1 class="page-title">Prescription Resources</h1>
  <p>If you are a Tres Health member, log onto www.TresHealthTX.com to learn more about your prescription drug
  benefits. Be sure to review your benefit materials for details. If you have any questions about your prescription
  drug benefits, call the Pharmacy Program number on the back of your member ID card.</p>
  <h3 class="sub">Prescription Drug List</h3>
  <p>A drug list is a list of drugs that are covered under your prescription drug benefit. How much you pay out of
  pocket is determined by whether your drug is on the list and at what coverage level, or tier. A generic drug is
  often at the lower tier.</p>
  <div class="figure"><img src="data:image/png;base64,{GOODRX}" alt="GoodRx"/></div>

  <h1 class="page-title tight">Medical Resources</h1>
  <h3 class="sub">MDLIVE Telemedicine</h3>
  <p>All Tres Health plans include 24/7 healthcare by phone or video through MDLIVE. Services include urgent care
  for common, non-emergency conditions and mental health services, including therapy and psychiatry.</p>
  <p>MDLIVE: 888-863-5292. Members may access services by phone or through the member app.</p>
  <h3 class="sub">Medmo Imaging Center Advocacy</h3>
  <p>Medmo provides imaging support and care coordination, including facility matching, scheduling support, report
  retrieval, appointment reminders, and rescheduling. The source guide notes that Medmo does not apply to MEC
  Preventive Plans.</p>
  <p>Medmo: 888-341-5606 | PathwaysConcierge@urmedwatch.com</p>
  <h3 class="sub">Preventive Care</h3>
  <p>All medical plan options provide 100% coverage for preventive care, including wellness visits, mammograms,
  immunizations, screening tests, and other preventive services, subject to applicable plan requirements.</p>
  {footer()}
</section>''')

# ---------- PAGE 5: preventive cont'd + Urgent care vs ER + Benefit Contacts + Portal intro ----------
PAGES.append(f'''
<section class="sheet">
  {header()}
  <p>For a complete list of preventive services, visit Healthcare.gov's preventive care information or review the
  applicable plan documents.</p>
  <h2 class="section-title">Urgent Care vs. Emergency Room</h2>
  {table(["Urgent Care May Be Appropriate For","Emergency Room May Be Appropriate For"], [
    ["Sprains and strains; minor broken bones; mild asthma attacks; minor infections; small cuts; minor burns; urinary tract infections; pelvic infections; sore throats; rashes",
     "Heavy bleeding; trouble breathing; severe head injury; chest pain or pressure; sudden or severe pain; coughing or vomiting blood; sudden dizziness, weakness, or vision changes; severe/persistent vomiting or diarrhea; changes in mental status; loss of consciousness; major burns"],
  ], col_widths=["50%","50%"])}

  <h2 class="section-title">Benefit Contacts</h2>
  {table(["Resource","Contact"], [
    ["Tres Health / Medical","1-888-341-5606 | Group #6607850 | member.tres.health"],
    ["MDLIVE Telemedicine","888-863-5292"],
    ["Medmo Imaging Advocacy","888-341-5606 | PathwaysConcierge@urmedwatch.com"],
    ["Benefits Contact",["Mark Grace &nbsp; mark.grace@hubinternational.com","(817) 529-5353 Benefits Consultant",
                          "Sylvia Uranga &nbsp; sylvia.uranga@hubinternational.com","(817) 529-5314 Account Manager"]],
  ], col_widths=["30%","70%"])}

  <p>TresTech Member Portal provides quick access to your health insurance information through the web or mobile
  app. Access the portal at member.tres.health or through the Tres Health mobile app.</p>
  {bullets([
    "DOWNLOAD the app from the Apple App Store or Google Play Store by searching for &ldquo;Tres Health,&rdquo; or access it online at member.tres.health.",
    "REGISTER in the app using your Social Security Number and Date of Birth; your information remains private and secure.",
    "ENTER YOUR INFORMATION &ndash; Enter your Email Address and First and Last Name, then Create a Password.",
    "REVIEW dependents and invite adult dependents to register, too.",
  ])}
  {footer()}
</section>''')

# ---------- PAGE 6: App features ----------
PAGES.append(f'''
<section class="sheet">
  {header()}
  <div class="figure figure-small"><img src="data:image/png;base64,{TRESAPP}" alt="Tres Health App"/></div>
  <p>In the app or on the Tres Health website you can:</p>
  {bullets([
    "ID CARDS &ndash; Get digital access to your ID Card thru the mobile app or portal.",
    "TELEMEDICINE &ndash; Access telemedicine services (MDLive) through both the portal and app with the single sign on feature.",
    "CLAIM STATUS &ndash; Review all active, pending, paid, and previous claims history.",
    "PRESCRIPTIONS &ndash; Search prescription costs and pharmacy locations.",
    "BENEFITS DETAILS &ndash; Review benefit details such as: deductibles and accumulations, co-insurance co-pays, plan documents and summaries.",
    "PROVIDER SEARCH &ndash; Search for providers in your network.",
  ])}
  <p>For technical assistance, contact portals@tres.health.</p>
  {footer()}
</section>''')

# ---------- PAGE 7: Dental + Vision ----------
dental_rows = [
    ["Individual Deductible","$50","$50"],
    ["Family Deductible","$150","$150"],
    ["Annual Maximum","$1,500","$1,500"],
    ["Preventive Services","100%","100%"],
    ["Basic Services","80%","80%"],
    ["Major Services","50%","50%"],
    ["Endodontic Services","80%","80%"],
    ["Simple Extractions","80%","80%"],
    ["Implant Services","N/A","N/A"],
    ["Periodontal Services","80%","80%"],
    ["Oral Surgery Services","80%","80%"],
    ["Orthodontic Services","N/A","N/A"],
    ["Waiting Period for Major Services","0 months","0 months"],
    ["OON Reimbursement","&mdash;","MAC"],
    ["Network","Options PPO 20","&mdash;"],
]
vision_rows = [
    ["Exam Frequency","Every 12 months"],
    ["Lenses (Eyeglasses or Contacts) Frequency","Every 12 months"],
    ["Frame Frequency","Every 12 months"],
    ["Exam Copay","$10"],
    ["Materials Copay","$25"],
    ["Retinal Screening for Diabetics","$0"],
    ["2nd Exam for Diabetics","$10"],
    ["Elective Contact Lens Allowance","$105"],
    ["Elective Contact Lens Fitting Allowance","$30"],
    ["Non-Formulary Contact Lenses","N/A"],
    ["Necessary Contact Lenses","100%"],
    ["Frame Allowance","$130"],
    ["Covered Lens Options","Standard Scratch Coating; Polycarbonate to age 19"],
]
oon_rows = [
    ["Exam","$40"],["Eyeglass Lenses","$80"],["Frame","$45"],
    ["Elective Contact Lenses","$80"],["Necessary Contact Lenses","$210"],
]
PAGES.append(f'''
<section class="sheet">
  {header()}
  <h1 class="page-title">Dental Insurance</h1>
  <p>This is a voluntary, passive PPO with an effective date of January 1, 2026, and provided through United
  Healthcare. <strong>The Dental Plan Code is P5425.</strong></p>
  {table(["Dental Benefit","In-Network","Out-of-Network"], dental_rows, col_widths=["46%","27%","27%"])}
  {footer()}
</section>''')

PAGES.append(f'''
<section class="sheet">
  {header()}
  <h1 class="page-title">Vision Insurance</h1>
  <p>This plan is voluntary and effective January 1, 2026, and provided through United Healthcare.
  <strong>The Vision Plan Code is S1006.</strong></p>
  {table(["Vision Benefit","In-Network"], vision_rows, col_widths=["60%","40%"])}
  <div class="table-gap"></div>
  {table(["Out-of-Network Benefit","Reimbursement Up To"], oon_rows, col_widths=["60%","40%"])}
  {footer()}
</section>''')

# ---------- PAGE 8: 401(k) ----------
PAGES.append(f'''
<section class="sheet">
  {header()}
  <h1 class="page-title">401(k) Retirement Plan</h1>
  <div class="kicker">Voya Financial</div>
  <p>Valletta Industries offers a 401(k) retirement savings plan through Voya Financial to help employees save for
  their future.</p>
  <h3 class="sub">Mandatory Enrollment</h3>
  <p>Eligible employees are automatically enrolled in the 401(k) plan at a contribution rate of 3% of eligible pay.</p>
  <h3 class="sub">Employer Match</h3>
  <p>Valletta Industries does not currently provide an employer matching contribution.</p>
  <h3 class="sub">Want to Change or Stop Your Contribution?</h3>
  <p>If you do not wish to participate in the 401(k) plan, you must contact Human Resources for assistance with the
  applicable process.</p>
  <h3 class="sub">Voya Resources</h3>
  <p>Voya provides retirement planning resources, educational materials, and tools to help you understand your
  retirement savings and make informed financial decisions.</p>
  <p><strong>Voya Financial:</strong> Voya Financial &ndash; Individual Resources</p>
  <p>Employees are encouraged to review their Voya account and available resources to understand their retirement
  savings, investment options, and account information.</p>
  <p class="note-strong">Important: This section is intended as a summary of the Valletta Industries 401(k) benefit.
  The official plan documents and applicable Voya plan materials govern the terms of the plan.</p>
  {footer()}
</section>''')

# ---------- PAGE 9: Important Notes ----------
PAGES.append(f'''
<section class="sheet">
  {header()}
  <h1 class="page-title">Important Notes</h1>
  {bullets([
    "This guide is intended as an employee-friendly summary of current benefits information.",
    "The Medical, dental, and vision information is based on the UHC summary provided to Valletta Industries. Those source documents show a January 1, 2026 effective date; the benefits are presented here as active until further notice based on current company direction.",
    "The source benefits materials contain detailed plan provisions, limitations, exclusions, and eligibility rules that may not all be reproduced in this guide.",
    "If this guide conflicts with an official plan document, the official plan document will prevail.",
    "Plan availability, rates, networks, and benefit provisions may change. Employees should review current enrollment materials and plan documents before making benefit decisions.",
  ])}
  <h2 class="section-title">A Final Reminder</h2>
  <p>Take time to review your coverage and understand how to use your benefits before you need them. Keep this
  guide available throughout the plan year and contact HR, or the applicable benefit provider when you need help.</p>
  {footer()}
</section>''')

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
  border-bottom:2px solid {RED}; margin-bottom:26px; }}
.doc-header img {{ height:30px; width:auto; display:block; }}
.doc-header .doc-tag {{ font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.6px; color:{STEEL}; text-transform:uppercase; }}

.page-title {{ font-family:'Oswald'; font-weight:700; font-size:25px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin-bottom:14px; padding-bottom:8px; border-bottom:1px solid {LINE_GRAY}; }}
.page-title.tight {{ margin-top:26px; }}
.section-title {{ font-family:'Oswald'; font-weight:700; font-size:17px; letter-spacing:0.2px; text-transform:uppercase;
  color:{BLACK}; margin:18px 0 9px; }}
.section-title.tight {{ margin-top:16px; }}
.sub {{ font-family:'Inter'; font-weight:700; font-size:12.5px; letter-spacing:0.3px; color:{RED}; text-transform:uppercase;
  margin:16px 0 6px; }}

p {{ font-size:11.3px; line-height:1.5; margin-bottom:7px; color:{CHARCOAL}; }}
strong {{ color:{BLACK}; }}
.note-strong {{ font-size:11.3px; line-height:1.55; font-weight:700; color:{BLACK}; margin:10px 0 12px; }}
.callout-center {{ text-align:center; font-family:'Inter'; font-weight:700; font-size:12px; color:{RED};
  border-top:1px solid {LINE_GRAY}; padding-top:12px; margin-top:14px; }}
.kicker {{ font-family:'Inter'; font-weight:700; font-size:11px; letter-spacing:1.2px; color:{RED}; text-transform:uppercase; margin-bottom:12px; }}

ul.bullets {{ list-style:none; margin:0 0 10px; }}
ul.bullets li {{ position:relative; padding-left:14px; font-size:11.3px; line-height:1.42; margin-bottom:4px; color:{CHARCOAL}; }}
ul.bullets li::before {{ content:''; position:absolute; left:0; top:5px; width:5px; height:5px; background:{RED}; }}

table.dtable {{ width:100%; border-collapse:collapse; margin:8px 0 14px; }}
table.dtable th {{ background:{BLACK}; color:{WHITE}; font-family:'Inter'; font-weight:700; font-size:9.8px;
  letter-spacing:0.5px; text-transform:uppercase; text-align:left; padding:7px 10px; border:1px solid {BLACK}; }}
table.dtable td {{ font-size:10.3px; line-height:1.42; color:{CHARCOAL}; padding:6px 10px; border:1px solid {LINE_GRAY};
  vertical-align:top; }}
table.dtable tbody tr:nth-child(even) td {{ background:{ROW_TINT}; }}
.table-gap {{ height:14px; }}

.figure {{ margin:8px 0 12px; text-align:center; }}
.figure img {{ max-width:100%; max-height:230px; border:1px solid {LINE_GRAY}; }}
.figure-small img {{ max-height:210px; width:auto; }}

.doc-footer {{ position:absolute; left:0; right:0; bottom:26px; text-align:center; font-family:'Inter';
  font-weight:600; font-size:9px; letter-spacing:0.6px; color:{STEEL}; }}

.cover {{ background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:0; }}
.cover-tick {{ position:absolute; width:26px; height:26px; border-color:{RED}; border-style:solid; }}
.cover-tick.tl {{ left:40px; top:40px; border-width:3px 0 0 3px; }}
.cover-tick.br {{ right:40px; bottom:40px; border-width:0 3px 3px 0; }}
.cover-logo {{ height:64px; width:auto; margin-bottom:56px; }}
.cover-title {{ font-family:'Oswald'; font-weight:700; font-size:46px; line-height:1.18; letter-spacing:0.5px;
  text-transform:uppercase; color:{WHITE}; }}
.cover-sub {{ margin-top:22px; font-family:'Inter'; font-weight:600; font-size:14px; letter-spacing:1.2px;
  color:{RED}; text-transform:uppercase; }}
'''

html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{"".join(PAGES)}
</body></html>'''

with open(os.path.join(HERE, "valletta_benefits_guide.html"), "w") as f:
    f.write(html)

print("written", len(PAGES), "pages")
