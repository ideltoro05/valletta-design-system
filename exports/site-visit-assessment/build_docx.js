const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, PageBreak,
  convertInchesToTwip, TabStopType,
} = require("docx");

const HERE = __dirname;
const img = (name) => fs.readFileSync(path.join(HERE, name));

const BLACK = "0A0A0A";
const CHARCOAL = "26282B";
const FIELD_WHITE = "F5F5F3";
const RED = "FF002B";
const STEEL = "5B5F66";
const LINE_GRAY = "D8D9DB";
const WHITE = "FFFFFF";
const NOTE_TINT = "EFEFEC";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = convertInchesToTwip(0.9);
const CONTENT_W = PAGE_W - 2 * MARGIN;

// ============================================================
// DATA (mirrors sva_data.py — content unchanged from the source)
// ============================================================
const TITLE = "SITE VISIT ASSESSMENT";
const SUBTITLE = "Operational Readiness, Contract Performance & Management Support Review";
const DOC_TAG = "Management Support Team Site Visit Assessment";

const VISIT_FIELDS = [
  ["SITE / LOCATION", "Whiskey"],
  ["VISIT DATE(S)", "15 September 2026"],
  ["MST MEMBER(S)", "Michael Flanagan"],
  ["MST ROLE(S)", "NTM"],
  ["SITE MANAGER", "ST: Harry Zimmerman"],
];

const PURPOSE_TEXT =
  "This Management Support Team Site Visit Assessment provides leadership with a structured, " +
  "evidence-based snapshot of site operations, personnel readiness, supervisory effectiveness, " +
  "training, equipment, weapons accountability, emergency readiness, and support requirements. " +
  "Findings are based on conditions observed, records sampled, and personnel engaged during the " +
  "visit. The assessment identifies strengths, risks, trends, and areas requiring follow-up or " +
  "higher-headquarters support. It does not replace a formal quality-control inspection.";

const ASSESSMENT_AREAS = "Staffing & Post Operations | Leadership & Supervision | Training & Readiness | Equipment & Weapons | Overall Performance";

const SECTIONS = [
  ["I", "Staffing and Post Operations", [
    [1, "Were all contractually required posts staffed during the visit, and does review of recent records indicate the site is meeting the 99.5% post-coverage standard?", "Not Inspected (N/S)", ""],
    [2, "Do weekly staffing records reflect an overtime utilization rate below 3% (overtime hours divided by total weekly hours) and a 0% open-shift rate resulting from call-outs, tardiness, or other staffing gaps?", "Not Inspected (N/S)", ""],
    [3, "Are only properly certified personnel being assigned to security posts based on the records sampled?", "Meets Standard (5)", ""],
    [4, "Were personnel observed properly uniformed, equipped, and performing duties consistent with current post orders?", "Meets Standard (5)", "Of the personnel inspected, all were in appropriate uniforms, and carried requisite equipment."],
    [5, "Are current post orders, duty logs, and required operational records available and being maintained at the site?", "Unable to Verify (N/S)", "Post orders are in the process of being promulgated."],
    [6, "Are incidents, uncovered posts, unusual occurrences, and other reportable matters being documented and elevated as required?", "Not Inspected (N/S)", ""],
  ]],
  ["II", "Leadership, Supervision and Management", [
    [7, "Does the Site Manager demonstrate effective oversight of staffing, post operations, personnel accountability, and contract requirements?", "Not Inspected (N/S)", ""],
    [8, "Do Shift Supervisors demonstrate active supervision of assigned personnel and posts across the shifts observed?", "Not Inspected (N/S)", ""],
    [9, "Are identified deficiencies or recurring operational issues tracked to corrective action and closure?", "Not Inspected (N/S)", ""],
    [10, "Does site leadership maintain effective communication with the Management Support Team and elevate issues requiring higher-level support?", "Not Inspected (N/S)", ""],
    [11, "Based on personnel interaction and observation, is site leadership maintaining professional standards and an effective command climate?", "Acceptable (3)", "The site was professionally managed, with no noteworthy observations to indicate otherwise."],
  ]],
  ["III", "Training and Personnel Readiness", [
    [12, "Does a sample review of personnel files show required training, weapons qualifications, certifications, and PFT requirements are current?", "Meets Standard (5)", "In site managers office (hard copy). Electronics are held with ST. Current as of 15 Sep."],
    [13, "Are required on-site training records and individual training documentation current, organized, and readily accessible?", "Minor Deficiency (3)", "Site manager folder. Trainers do not currently electronically maintain. Area to improve."],
    [14, "Is the Site Trainer prepared to execute scheduled basic/sustainment training and maintain required training support materials?", "Ready (5)", "Yes, Site Trainer is fully prepped to execute training."],
    [15, "Do personnel sampled demonstrate working knowledge of post orders, access control, emergency/alarm response, and notification procedures?", "High (5)", "Yes, CP inquiries were answered in a professional and efficient manner."],
    [16, "Are required refresher, combatives, use-of-force, and other recurring training requirements being maintained or scheduled appropriately?", "Meets Standard (5)", "When not in transition between contracts, the ST believes they are more efficient."],
  ]],
  ["IV", "Equipment, Weapons and Emergency Readiness", [
    [17, "Is required contractor-furnished operational equipment present, serviceable, and available for mission use based on the sample observed?", "Minor Deficiency (3)", "Due to shortfalls in appropriate armory tools, some weapons were noted to have light dusting of rust"],
    [18, "Are firearms, ammunition, and related weapons equipment securely stored, controlled, and accountable?", "Meets Standard (5)", "Weapons were secured, with ammunition in a separate controlled space.  Logbooks accurate."],
    [19, "Are radios, emergency communications, visitor-management systems, and other mission-critical systems operational?", "Minor Deficiency (3)", "Yes. Battery life spans in radios are a concern."],
    [20, "Are required individual duty items and protective equipment available and serviceable for personnel observed?", "Minor Deficiency (3)", "Med bags are reaching shelf life and require replacement."],
    [21, "Does the site appear prepared to execute site-specific emergency, alarm, active-threat, and incident-response procedures?", "Select...", "It is my observation that they are."],
  ]],
  ["V", "Overall Performance and Support Requirements", [
    [22, "Were any conditions identified that could adversely affect contract performance, officer safety, security, or mission accomplishment?", "Select...", ""],
    [23, "Are there staffing, equipment, training, policy, or administrative issues requiring Management Support Team action?", "Select...", ""],
    [24, "Were any noteworthy best practices, improvements, or strong performance indicators identified during the visit?", "Select...", ""],
    [25, "Based on the visit, how would you assess the site's current ability to meet contractual and operational requirements?", "Select...", ""],
    [26, "What level of follow-up is recommended following this visit?", "Select...", ""],
  ]],
];

const NARRATIVE_FIELDS = [
  ["KEY OBSERVATIONS, STRENGTHS & CONCERNS", ""],
  ["RECOMMENDED ACTIONS & OVERALL ASSESSMENT", ""],
];

const TOTAL_SCORE_LABEL = "TOTAL SCORE";
const TOTAL_SCORE_SUBLABEL = "AUTO-CALCULATED (SOURCE PDF)";
const TOTAL_SCORE_VALUE = "417 / 500";

// ============================================================
// helpers
// ============================================================
function pageBreak() { return new Paragraph({ children: [new PageBreak()] }); }

function subHeading(text) {
  return new Paragraph({
    spacing: { before: 260, after: 140 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 12 } },
    children: [new TextRun({ text: text.toUpperCase(), font: F_LABEL, bold: true, size: 22, color: BLACK })],
  });
}

function fieldRow(label, value) {
  return new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 2600 }],
    border: { bottom: { color: LINE_GRAY, space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 60, after: 120 },
    children: [
      new TextRun({ text: label + "\t", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 }),
      new TextRun({ text: value || "", font: F_BODY, size: 20, color: CHARCOAL }),
    ],
  });
}

function tintedBox(lines) {
  return lines.map((l, i) => new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: NOTE_TINT },
    spacing: { before: i === 0 ? 120 : 0, after: i === lines.length - 1 ? 120 : 20 },
    indent: { left: 160, right: 160 },
    children: [new TextRun({ text: l, font: F_BODY, size: 20, color: CHARCOAL })],
  }));
}

function sectionBand(roman, title) {
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { before: 200, after: 160 },
    indent: { left: 100 },
    children: [new TextRun({ text: `SECTION ${roman}  —  ${title.toUpperCase()}`, font: F_HEAD, bold: true, size: 22, color: WHITE })],
  });
}

function questionPara(num, text) {
  return new Paragraph({
    spacing: { before: 120, after: 60 },
    children: [
      new TextRun({ text: `${num}.  `, font: F_BODY, bold: true, size: 20, color: RED }),
      new TextRun({ text, font: F_BODY, bold: true, size: 20, color: BLACK }),
    ],
  });
}

function ratingRow(value) {
  const notRated = value === "Select...";
  return new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 1600 }],
    shading: { type: ShadingType.CLEAR, color: "auto", fill: FIELD_WHITE },
    border: {
      top: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      bottom: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      left: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      right: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
    },
    spacing: { after: 60 },
    children: [
      new TextRun({ text: "RATING\t", font: F_LABEL, bold: true, size: 14, color: STEEL, characterSpacing: 3 }),
      new TextRun({ text: notRated ? "—" : value, font: F_BODY, bold: true, size: 20, color: notRated ? STEEL : BLACK }),
    ],
  });
}

function commentsBlock(text) {
  const paras = [
    new Paragraph({
      spacing: { before: 40, after: 20 },
      children: [new TextRun({ text: "Comments / observations:", font: F_BODY, italics: true, size: 16, color: STEEL })],
    }),
  ];
  paras.push(new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: text ? "FFFFFF" : FIELD_WHITE },
    border: {
      top: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      bottom: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      left: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      right: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
    },
    indent: { left: 80, right: 80 },
    spacing: { before: 100, after: 240 },
    children: [new TextRun({ text: text || "—", font: F_BODY, size: 20, color: text ? CHARCOAL : STEEL })],
  }));
  return paras;
}

function totalScoreBlock() {
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { before: 300, after: 200 },
    indent: { left: 120, right: 120 },
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W - 240 }],
    children: [
      new TextRun({ text: TOTAL_SCORE_LABEL, font: F_HEAD, bold: true, size: 26, color: WHITE }),
      new TextRun({ text: "   " + TOTAL_SCORE_SUBLABEL, font: F_BODY, size: 15, color: "B8B9BB" }),
      new TextRun({ text: "\t" + TOTAL_SCORE_VALUE, font: F_HEAD, bold: true, size: 30, color: WHITE }),
    ],
  });
}

// ---- header/footer ----
const logoBuf = img("valletta-mark-black.png");
function makeHeader() {
  return new Header({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
      border: { bottom: { color: RED, space: 8, style: BorderStyle.SINGLE, size: 16 } },
      children: [
        new ImageRun({ type: "png", data: logoBuf, transformation: { width: 150, height: 30 } }),
        new TextRun({ text: "\t" }),
        new TextRun({ text: "SITE: WHISKEY – 15 SEPTEMBER 2026", font: F_LABEL, bold: true, size: 15, color: STEEL, characterSpacing: 6 }),
      ],
    })],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Valletta Industries  |  Site Visit Assessment  –  Page ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.CURRENT], font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ text: " of ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_BODY, size: 15, color: STEEL }),
      ],
    })],
  });
}
const emptyHeader = new Header({ children: [new Paragraph({ children: [] })] });
const emptyFooter = new Footer({ children: [new Paragraph({ children: [] })] });

// ============================================================
// CONTENT
// ============================================================
const content = [];

content.push(
  new Paragraph({ spacing: { before: 200, after: 40 }, children: [new TextRun({ text: TITLE, font: F_HEAD, bold: true, size: 44, color: BLACK })] }),
  new Paragraph({
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 20 } },
    spacing: { after: 160 },
    indent: { right: 8400 },
    children: [new TextRun({ text: "", size: 2 })],
  }),
  new Paragraph({ spacing: { after: 260 }, children: [new TextRun({ text: SUBTITLE, font: F_BODY, size: 21, color: STEEL })] }),
);

content.push(subHeading("Visit Information"));
for (const [label, val] of VISIT_FIELDS) content.push(fieldRow(label, val));

content.push(subHeading("Purpose and Scope"));
content.push(...tintedBox([PURPOSE_TEXT]));

content.push(subHeading("Assessment Areas"));
content.push(new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: ASSESSMENT_AREAS, font: F_BODY, size: 21, color: CHARCOAL })] }));

content.push(pageBreak());

for (const [roman, title, qs] of SECTIONS) {
  content.push(sectionBand(roman, title));
  for (const [num, text, rating, comment] of qs) {
    content.push(questionPara(num, text));
    content.push(ratingRow(rating));
    content.push(...commentsBlock(comment));
  }
}

content.push(subHeading("Management Narrative and Visit Summary"));
for (const [label, val] of NARRATIVE_FIELDS) {
  content.push(new Paragraph({
    spacing: { before: 100, after: 20 },
    children: [new TextRun({ text: label, font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 })],
  }));
  content.push(new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: FIELD_WHITE },
    border: {
      top: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      bottom: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      left: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
      right: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 },
    },
    indent: { left: 80, right: 80 },
    spacing: { before: 60, after: 220 },
    children: [new TextRun({ text: val || "—", font: F_BODY, size: 20, color: val ? CHARCOAL : STEEL })],
  }));
}

content.push(totalScoreBlock());

// ============================================================
// DOCUMENT
// ============================================================
const doc = new Document({
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
  fs.writeFileSync(path.join(HERE, "valletta_site_visit_assessment_whiskey.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
