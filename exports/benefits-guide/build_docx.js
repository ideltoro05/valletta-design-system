const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  ImageRun, Header, Footer, PageNumber, PageBreak,
  VerticalAlign, convertInchesToTwip, LevelFormat, UnderlineType,
} = require("docx");

const HERE = __dirname;
const img = (name) => fs.readFileSync(path.join(HERE, name));

// ---- Brand tokens ----
const BLACK = "0A0A0A";
const CHARCOAL = "26282B";
const ROW_TINT = "ECECE9";
const RED = "FF002B";
const STEEL = "5B5F66";
const LINE_GRAY = "D8D9DB";
const WHITE = "FFFFFF";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

const PAGE_W = 12240, PAGE_H = 15840; // US Letter DXA
const MARGIN = convertInchesToTwip(0.85);
const CONTENT_W = PAGE_W - 2 * MARGIN; // DXA, for table widths

// ---- small helpers ----
function pageTitle(text, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before ?? 200, after: 160 },
    border: { bottom: { color: LINE_GRAY, space: 6, style: BorderStyle.SINGLE, size: 4 } },
    children: [new TextRun({ text: text.toUpperCase(), font: F_HEAD, bold: true, size: 40, color: BLACK })],
  });
}
function sectionTitle(text, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before ?? 260, after: 120 },
    children: [new TextRun({ text: text.toUpperCase(), font: F_HEAD, bold: true, size: 27, color: BLACK })],
  });
}
function sub(text) {
  return new Paragraph({
    spacing: { before: 200, after: 70 },
    children: [new TextRun({ text: text.toUpperCase(), font: F_LABEL, bold: true, size: 20, color: RED, characterSpacing: 10 })],
  });
}
function body(runsOrText, opts = {}) {
  const children = typeof runsOrText === "string"
    ? [new TextRun({ text: runsOrText, font: F_BODY, size: 21, color: CHARCOAL })]
    : runsOrText;
  return new Paragraph({ spacing: { after: opts.after ?? 130, line: 264 }, children });
}
function boldBody(text) {
  return new Paragraph({
    spacing: { after: 130, line: 264 },
    children: [new TextRun({ text, font: F_BODY, bold: true, size: 21, color: BLACK })],
  });
}
function bulletPara(text) {
  return new Paragraph({
    numbering: { reference: "brand-bullets", level: 0 },
    spacing: { after: 60, line: 250 },
    children: [new TextRun({ text, font: F_BODY, size: 21, color: CHARCOAL })],
  });
}
function centerCallout(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 160, after: 60 },
    border: { top: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } },
    children: [new TextRun({ text, font: F_LABEL, bold: true, size: 21, color: RED })],
  });
}
function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

function cell(content, { header = false, width, shade } = {}) {
  const lines = Array.isArray(content) ? content : [content];
  const paragraphs = lines.map((line, i) => new Paragraph({
    spacing: { after: i === lines.length - 1 ? 0 : 40 },
    children: [new TextRun({
      text: line, font: F_BODY, size: header ? 17 : 19,
      bold: header, color: header ? WHITE : CHARCOAL,
      allCaps: header,
    })],
  }));
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: shade ? { type: ShadingType.CLEAR, color: "auto", fill: shade } : undefined,
    verticalAlign: VerticalAlign.TOP,
    margins: { top: 90, bottom: 90, left: 120, right: 120 },
    children: paragraphs,
  });
}

function dataTable(headers, rows, colFractions) {
  const widths = colFractions.map((f) => Math.round(CONTENT_W * f));
  const headerRow = new TableRow({
    tableHeader: true,
    children: headers.map((h, i) => cell(h, { header: true, width: widths[i], shade: BLACK })),
  });
  const bodyRows = rows.map((r, ri) => new TableRow({
    children: r.map((c, ci) => cell(c, { width: widths[ci], shade: ri % 2 === 1 ? ROW_TINT : undefined })),
  }));
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      left: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      right: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      insideVertical: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
    },
    rows: [headerRow, ...bodyRows],
  });
}

function spacer(h = 160) {
  return new Paragraph({ spacing: { after: h }, children: [] });
}

function figure(imgName, w, h) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 100, after: 160 },
    children: [new ImageRun({ type: "png", data: img(imgName), transformation: { width: w, height: h } })],
    border: { top: {style:BorderStyle.NONE,size:0,color:"FFFFFF"} },
  });
}

// ---- header / footer ----
const logoBuf = img("valletta-mark-black.png"); // 694x140

function makeHeader() {
  return new Header({
    children: [
      new Paragraph({
        tabStops: [{ type: "right", position: CONTENT_W }],
        border: { bottom: { color: RED, space: 8, style: BorderStyle.SINGLE, size: 16 } },
        children: [
          new ImageRun({ type: "png", data: logoBuf, transformation: { width: 150, height: 30 } }),
          new TextRun({ text: "\t" }),
          new TextRun({ text: "EMPLOYEE BENEFITS GUIDE  |  2026–2027", font: F_LABEL, bold: true, size: 15, color: STEEL, characterSpacing: 10 }),
        ],
      }),
    ],
  });
}
function makeFooter() {
  return new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "Valletta Industries  |  Employee Benefits Guide  |  2026–2027  –  Page ", font: F_BODY, size: 15, color: STEEL }),
          new TextRun({ children: [PageNumber.CURRENT], font: F_BODY, size: 15, color: STEEL }),
          new TextRun({ text: " of ", font: F_BODY, size: 15, color: STEEL }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_BODY, size: 15, color: STEEL }),
        ],
      }),
    ],
  });
}
const emptyHeader = new Header({ children: [new Paragraph({ children: [] })] });
const emptyFooter = new Footer({ children: [new Paragraph({ children: [] })] });

// ================= CONTENT =================
const content = [];

// ---- Cover ----
content.push(
  new Paragraph({ spacing: { before: 2600 }, alignment: AlignmentType.CENTER,
    children: [new ImageRun({ type: "png", data: logoBuf, transformation: { width: 300, height: 60 } })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500 },
    children: [new TextRun({ text: "EMPLOYEE BENEFITS GUIDE", font: F_HEAD, bold: true, size: 56, color: BLACK })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 260 },
    children: [new TextRun({ text: "AUGUST 1, 2026 – JULY 31, 2027", font: F_LABEL, bold: true, size: 24, color: RED, characterSpacing: 16 })] }),
  pageBreak(),
);

// ---- Welcome ----
content.push(
  pageTitle("Welcome", { before: 0 }),
  body("Valletta Industries is committed to providing a comprehensive benefits program that helps employees and their families stay healthy, feel secure, and maintain work/life balance. This guide brings the available benefit information together in one place so you can review your options and use your benefits throughout the year."),
  body("Use this guide as a convenient reference. For complete plan terms, limitations, exclusions, and eligibility requirements, always refer to the applicable plan documents. If there is a discrepancy between this guide and the governing plan documents, the plan documents will control."),
  sectionTitle("Benefits at a Glance"),
  dataTable(["Item", "Information"], [
    ["Plan Year", "August 1, 2026 – July 31, 2027"],
    ["New-Hire Eligibility", "Benefits begin the 1st of the month following 60 days"],
    ["Open Enrollment", "Annually during July; 2026 elections are effective August 1, 2026 – July 31, 2027"],
  ], [0.34, 0.66]),
  spacer(120),
  sectionTitle("Eligibility & Enrollment"),
  sub("Who Is Eligible?"),
  ...[
    "Employees who are full-time and work 30 or more hours per week.",
    "Legally married spouse.",
    "Biological, adopted, or stepchildren up to age 26.",
    "Children over age 26 who are disabled and depend on you for support.",
    "Children named in a Qualified Medical Child Support Order (QMCSO).",
  ].map(bulletPara),
  sub("When Can I Change My Benefits?"),
  body("If you experience a qualifying life event that results in the gain or loss of insurance for you or your dependents, report the event to HR within 30 days."),
  ...[
    "Marriage or divorce", "Birth or adoption", "Death of a spouse or child", "Gain or loss of other coverage",
    "A change in employment status that affects benefit eligibility", "Dependent child reaches age 26",
    "FMLA leave, COBRA event, court judgment or decree", "Becoming eligible for Medicare",
    "Loss of Medicaid and/or CHIP", "Receiving a Qualified Medical Child Support Order",
  ].map(bulletPara),
  sub("Enrollment Reminder"),
  body("If you do not enroll during the applicable enrollment period, you must wait until the next open enrollment period unless you experience a qualifying life event."),
  pageBreak(),
);

// ---- Medical Insurance ----
const medRows = [
  ["Annual Deductible (Individual / Family)", "$0 / $0", "$0 / $0", "$0 / $0"],
  ["Annual OOP Maximum (Individual / Family)", "$9,100 / $18,200", "$9,100 / $18,200", "$9,100 / $18,200"],
  ["Preventive Care", "100%", "100%", "100%"],
  ["Office / Specialist Visit", "$25 / $50", "$25 / $50; 8 per year", "$25 / $50; 12 per year"],
  ["Urgent Care", "$75", "$75; 2 per year", "$50; 3 per year"],
  ["Chiropractic", "Not Covered", "Not Covered", "Not Covered"],
  ["Lab & X-Ray (freestanding)", "MedMo 100%; outside MedMo $50", "MedMo 100%; outside MedMo $50; 1 per year", "MedMo 100%; outside MedMo $50; 3 per year"],
  ["Imaging", "MedMo 100%; outside MedMo $350", "MedMo 100%; outside MedMo $350", "MedMo 100%; outside MedMo $350"],
  ["Outpatient Hospital", "$350", "Hospital-based $350; non-hospital-based $750", "Hospital-based $350; non-hospital-based $750"],
  ["Inpatient Hospital", "Not Covered", "$750; 1x per year", "$750; 2x per year"],
  ["Physician Fees", "Not Covered", "$350", "$350"],
  ["Emergency Room", "Not Covered", "$750", "$750"],
  ["Generic Rx (Tier 1)", "$10", "$10", "$10"],
  ["Preferred Brand (Tier 2)", "Not Covered", "Not Covered", "$75"],
  ["Non-Preferred Brand (Tier 3)", "Not Covered", "Not Covered", "$150"],
  ["Specialty (Tier 4)", "Not Covered", "Not Covered", "Not Covered"],
];
content.push(
  pageTitle("Medical Insurance", { before: 0 }),
  body("Valletta Industries offers three medical plan options through Tres Health. The plan summaries below reflect the in-network information contained in the current benefits materials."),
  dataTable(["Benefit", "MEC Advantage PPO", "Core $0 RBP PPO", "Prime $0 RBP PPO"], medRows, [0.27, 0.243, 0.243, 0.244]),
  pageBreak(),
);

// ---- Medical cost + support ----
const costRows = [
  ["Employee", "$104.22", "$185.79", "$273.37"],
  ["Employee + Spouse", "$155.11", "$320.04", "$507.91"],
  ["Employee + Child(ren)", "$133.66", "$277.33", "$418.71"],
  ["Family", "$188.70", "$424.89", "$683.38"],
];
content.push(
  sectionTitle("Medical Plan Cost Per Pay Period", { before: 0 }),
  dataTable(["Coverage Tier", "MEC Advantage", "Core $0 RBP", "Prime $0 RBP"], costRows, [0.27, 0.243, 0.243, 0.244]),
  spacer(100),
  boldBody("Valletta Industries contributes $5.09 per hour, approximately $880 per month, through a fringe benefit allowance. The funds may be allocated toward available benefit plans selected."),
  sub("Medical Plan Support"),
  ...["Tres Health Member Portal: member.tres.health", "Tres Health Member Services: 1-888-341-5606", "Group Number: 6607850"].map(bulletPara),
  sub("Find an In-Network Provider"),
  ...[
    "Log in to member.tres.health or use the Tres Health mobile app.",
    "Select Find a Provider.",
    "Search by service, specialty, or facility type and enter the ZIP code where services are needed.",
    "Filter by distance and review provider details.",
    "For assistance in finding an in-network provider, call 888-341-5606.",
  ].map(bulletPara),
  centerCallout("There is a limit of 3 doctor or specialist visits per year."),
  pageBreak(),
);

// ---- Prescription + Medical Resources ----
content.push(
  pageTitle("Prescription Resources", { before: 0 }),
  body("If you are a Tres Health member, log onto www.TresHealthTX.com to learn more about your prescription drug benefits. Be sure to review your benefit materials for details. If you have any questions about your prescription drug benefits, call the Pharmacy Program number on the back of your member ID card."),
  sub("Prescription Drug List"),
  body("A drug list is a list of drugs that are covered under your prescription drug benefit. How much you pay out of pocket is determined by whether your drug is on the list and at what coverage level, or tier. A generic drug is often at the lower tier."),
  figure("goodrx.png", 460, 240),
  sectionTitle("Medical Resources"),
  sub("MDLIVE Telemedicine"),
  body("All Tres Health plans include 24/7 healthcare by phone or video through MDLIVE. Services include urgent care for common, non-emergency conditions and mental health services, including therapy and psychiatry."),
  body("MDLIVE: 888-863-5292. Members may access services by phone or through the member app."),
  sub("Medmo Imaging Center Advocacy"),
  body("Medmo provides imaging support and care coordination, including facility matching, scheduling support, report retrieval, appointment reminders, and rescheduling. The source guide notes that Medmo does not apply to MEC Preventive Plans."),
  body("Medmo: 888-341-5606 | PathwaysConcierge@urmedwatch.com"),
  sub("Preventive Care"),
  body("All medical plan options provide 100% coverage for preventive care, including wellness visits, mammograms, immunizations, screening tests, and other preventive services, subject to applicable plan requirements."),
  pageBreak(),
);

// ---- Urgent care / contacts / portal ----
content.push(
  body("For a complete list of preventive services, visit Healthcare.gov's preventive care information or review the applicable plan documents.", { after: 160 }),
  sectionTitle("Urgent Care vs. Emergency Room", { before: 0 }),
  dataTable(
    ["Urgent Care May Be Appropriate For", "Emergency Room May Be Appropriate For"],
    [[
      "Sprains and strains; minor broken bones; mild asthma attacks; minor infections; small cuts; minor burns; urinary tract infections; pelvic infections; sore throats; rashes",
      "Heavy bleeding; trouble breathing; severe head injury; chest pain or pressure; sudden or severe pain; coughing or vomiting blood; sudden dizziness, weakness, or vision changes; severe/persistent vomiting or diarrhea; changes in mental status; loss of consciousness; major burns",
    ]],
    [0.5, 0.5]
  ),
  spacer(120),
  sectionTitle("Benefit Contacts"),
  dataTable(["Resource", "Contact"], [
    ["Tres Health / Medical", "1-888-341-5606 | Group #6607850 | member.tres.health"],
    ["MDLIVE Telemedicine", "888-863-5292"],
    ["Medmo Imaging Advocacy", "888-341-5606 | PathwaysConcierge@urmedwatch.com"],
    ["Benefits Contact", ["Mark Grace   mark.grace@hubinternational.com", "(817) 529-5353 Benefits Consultant", "Sylvia Uranga   sylvia.uranga@hubinternational.com", "(817) 529-5314 Account Manager"]],
  ], [0.3, 0.7]),
  spacer(120),
  body("TresTech Member Portal provides quick access to your health insurance information through the web or mobile app. Access the portal at member.tres.health or through the Tres Health mobile app."),
  ...[
    "DOWNLOAD the app from the Apple App Store or Google Play Store by searching for “Tres Health,” or access it online at member.tres.health.",
    "REGISTER in the app using your Social Security Number and Date of Birth; your information remains private and secure.",
    "ENTER YOUR INFORMATION – Enter your Email Address and First and Last Name, then Create a Password.",
    "REVIEW dependents and invite adult dependents to register, too.",
  ].map(bulletPara),
  pageBreak(),
);

// ---- App features ----
content.push(
  figure("tresapp.png", 190, 214),
  body("In the app or on the Tres Health website you can:"),
  ...[
    "ID CARDS – Get digital access to your ID Card thru the mobile app or portal.",
    "TELEMEDICINE – Access telemedicine services (MDLive) through both the portal and app with the single sign on feature.",
    "CLAIM STATUS – Review all active, pending, paid, and previous claims history.",
    "PRESCRIPTIONS – Search prescription costs and pharmacy locations.",
    "BENEFITS DETAILS – Review benefit details such as: deductibles and accumulations, co-insurance co-pays, plan documents and summaries.",
    "PROVIDER SEARCH – Search for providers in your network.",
  ].map(bulletPara),
  body("For technical assistance, contact portals@tres.health.", { after: 0 }),
  pageBreak(),
);

// ---- Dental ----
const dentalRows = [
  ["Individual Deductible", "$50", "$50"],
  ["Family Deductible", "$150", "$150"],
  ["Annual Maximum", "$1,500", "$1,500"],
  ["Preventive Services", "100%", "100%"],
  ["Basic Services", "80%", "80%"],
  ["Major Services", "50%", "50%"],
  ["Endodontic Services", "80%", "80%"],
  ["Simple Extractions", "80%", "80%"],
  ["Implant Services", "N/A", "N/A"],
  ["Periodontal Services", "80%", "80%"],
  ["Oral Surgery Services", "80%", "80%"],
  ["Orthodontic Services", "N/A", "N/A"],
  ["Waiting Period for Major Services", "0 months", "0 months"],
  ["OON Reimbursement", "—", "MAC"],
  ["Network", "Options PPO 20", "—"],
];
content.push(
  pageTitle("Dental Insurance", { before: 0 }),
  body([
    new TextRun({ text: "This is a voluntary, passive PPO with an effective date of January 1, 2026, and provided through United Healthcare. ", font: F_BODY, size: 21, color: CHARCOAL }),
    new TextRun({ text: "The Dental Plan Code is P5425.", font: F_BODY, size: 21, bold: true, color: BLACK }),
  ]),
  dataTable(["Dental Benefit", "In-Network", "Out-of-Network"], dentalRows, [0.46, 0.27, 0.27]),
  pageBreak(),
);

// ---- Vision ----
const visionRows = [
  ["Exam Frequency", "Every 12 months"],
  ["Lenses (Eyeglasses or Contacts) Frequency", "Every 12 months"],
  ["Frame Frequency", "Every 12 months"],
  ["Exam Copay", "$10"],
  ["Materials Copay", "$25"],
  ["Retinal Screening for Diabetics", "$0"],
  ["2nd Exam for Diabetics", "$10"],
  ["Elective Contact Lens Allowance", "$105"],
  ["Elective Contact Lens Fitting Allowance", "$30"],
  ["Non-Formulary Contact Lenses", "N/A"],
  ["Necessary Contact Lenses", "100%"],
  ["Frame Allowance", "$130"],
  ["Covered Lens Options", "Standard Scratch Coating; Polycarbonate to age 19"],
];
const oonRows = [
  ["Exam", "$40"], ["Eyeglass Lenses", "$80"], ["Frame", "$45"],
  ["Elective Contact Lenses", "$80"], ["Necessary Contact Lenses", "$210"],
];
content.push(
  pageTitle("Vision Insurance", { before: 0 }),
  body([
    new TextRun({ text: "This plan is voluntary and effective January 1, 2026, and provided through United Healthcare. ", font: F_BODY, size: 21, color: CHARCOAL }),
    new TextRun({ text: "The Vision Plan Code is S1006.", font: F_BODY, size: 21, bold: true, color: BLACK }),
  ]),
  dataTable(["Vision Benefit", "In-Network"], visionRows, [0.6, 0.4]),
  spacer(140),
  dataTable(["Out-of-Network Benefit", "Reimbursement Up To"], oonRows, [0.6, 0.4]),
  pageBreak(),
);

// ---- 401k ----
content.push(
  pageTitle("401(k) Retirement Plan", { before: 0 }),
  sub("Voya Financial"),
  body("Valletta Industries offers a 401(k) retirement savings plan through Voya Financial to help employees save for their future."),
  sub("Mandatory Enrollment"),
  body("Eligible employees are automatically enrolled in the 401(k) plan at a contribution rate of 3% of eligible pay."),
  sub("Employer Match"),
  body("Valletta Industries does not currently provide an employer matching contribution."),
  sub("Want to Change or Stop Your Contribution?"),
  body("If you do not wish to participate in the 401(k) plan, you must contact Human Resources for assistance with the applicable process."),
  sub("Voya Resources"),
  body("Voya provides retirement planning resources, educational materials, and tools to help you understand your retirement savings and make informed financial decisions."),
  body([
    new TextRun({ text: "Voya Financial: ", font: F_BODY, size: 21, bold: true, color: BLACK }),
    new TextRun({ text: "Voya Financial – Individual Resources", font: F_BODY, size: 21, color: CHARCOAL }),
  ]),
  body("Employees are encouraged to review their Voya account and available resources to understand their retirement savings, investment options, and account information."),
  boldBody("Important: This section is intended as a summary of the Valletta Industries 401(k) benefit. The official plan documents and applicable Voya plan materials govern the terms of the plan."),
  pageBreak(),
);

// ---- Important Notes ----
content.push(
  pageTitle("Important Notes", { before: 0 }),
  ...[
    "This guide is intended as an employee-friendly summary of current benefits information.",
    "The Medical, dental, and vision information is based on the UHC summary provided to Valletta Industries. Those source documents show a January 1, 2026 effective date; the benefits are presented here as active until further notice based on current company direction.",
    "The source benefits materials contain detailed plan provisions, limitations, exclusions, and eligibility rules that may not all be reproduced in this guide.",
    "If this guide conflicts with an official plan document, the official plan document will prevail.",
    "Plan availability, rates, networks, and benefit provisions may change. Employees should review current enrollment materials and plan documents before making benefit decisions.",
  ].map(bulletPara),
  sectionTitle("A Final Reminder"),
  body("Take time to review your coverage and understand how to use your benefits before you need them. Keep this guide available throughout the plan year and contact HR, or the applicable benefit provider when you need help."),
);

// ================= DOCUMENT =================
const doc = new Document({
  numbering: {
    config: [{
      reference: "brand-bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "■",
        alignment: AlignmentType.LEFT,
        style: {
          paragraph: { indent: { left: 360, hanging: 220 } },
          run: { color: RED, font: F_BODY, size: 16 },
        },
      }],
    }],
  },
  sections: [{
    properties: {
      page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } },
      titlePage: true,
    },
    headers: { default: makeHeader(), first: emptyHeader },
    footers: { default: makeFooter(), first: emptyFooter },
    children: content,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(HERE, "valletta_benefits_guide.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
