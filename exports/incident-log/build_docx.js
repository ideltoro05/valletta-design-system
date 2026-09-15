const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  ShadingType, BorderStyle, WidthType, ImageRun, Header, Footer, PageNumber,
  convertInchesToTwip, Table, TableRow, TableCell, VerticalAlign, TableLayoutType,
} = require("docx");

const HERE = __dirname;
const img = (name) => fs.readFileSync(path.join(HERE, name));

const BLACK = "0A0A0A";
const CHARCOAL = "26282B";
const RED = "FF002B";
const STEEL = "5B5F66";
const LINE_GRAY = "D8D9DB";
const WHITE = "FFFFFF";
const ZEBRA = "EFEFEC";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

// Landscape US Letter — docx's page.size swaps width/height itself when
// orientation is landscape, so these must be the PORTRAIT base dimensions.
const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = convertInchesToTwip(0.55);
const CONTENT_W = PAGE_H - 2 * MARGIN; // rendered landscape width = portrait height (11in)

// column widths in DXA, proportional to the PDF's 90/46/250/58/512 (total 956)
const COL_FRAC = [90, 46, 250, 58, 512];
const COL_TOTAL = COL_FRAC.reduce((a, b) => a + b, 0);
const COL_W = COL_FRAC.map((f) => Math.round((f / COL_TOTAL) * CONTENT_W));

const cellBorder = { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };

function headerCell(text, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 100, bottom: 100, left: 120, right: 120 },
    borders: { top: { style: BorderStyle.SINGLE, size: 2, color: BLACK }, bottom: { style: BorderStyle.SINGLE, size: 2, color: BLACK }, left: { style: BorderStyle.SINGLE, size: 2, color: BLACK }, right: { style: BorderStyle.SINGLE, size: 2, color: BLACK } },
    children: [new Paragraph({ children: [new TextRun({ text, font: F_LABEL, bold: true, size: 15, color: WHITE, characterSpacing: 4 })] })],
  });
}

function bodyCell(children, width, opts = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: opts.zebra ? { type: ShadingType.CLEAR, color: "auto", fill: ZEBRA } : undefined,
    verticalAlign: VerticalAlign.TOP,
    margins: { top: 90, bottom: 90, left: 120, right: 120 },
    borders,
    children,
  });
}

function textPara(text, opts = {}) {
  return new Paragraph({
    alignment: opts.center ? AlignmentType.CENTER : AlignmentType.LEFT,
    spacing: { after: opts.after ?? 0, line: 240 },
    children: [new TextRun({ text, font: F_BODY, size: 16, color: opts.color ?? CHARCOAL, bold: !!opts.bold })],
  });
}

function statusParas(text) {
  const lines = text.split("\n");
  const first = lines[0];
  const m = first.match(/^(Open|Closed)(\s*[–-]\s*)(.*)$/);
  const isOpen = m && m[1] === "Open";
  const paras = [];
  if (m) {
    paras.push(new Paragraph({
      spacing: { after: lines.length > 1 ? 40 : 0, line: 240 },
      children: [
        new TextRun({ text: m[1].toUpperCase(), font: F_BODY, bold: true, size: 16, color: isOpen ? RED : STEEL }),
        new TextRun({ text: " – " + m[3], font: F_BODY, size: 16, color: CHARCOAL }),
      ],
    }));
  } else {
    paras.push(textPara(first, { after: lines.length > 1 ? 40 : 0 }));
  }
  lines.slice(1).forEach((l, i) => {
    paras.push(textPara(l, { after: i === lines.length - 2 ? 0 : 40 }));
  });
  return paras;
}

// ================= DATA (verbatim from source table) =================
const ROWS = [
  ["Charlie", "1", "Perimeter Fence and Exterior Security Assessment", "26C-0054", "9/9",
    "Closed – No deficiencies were noted."],
  ["Charlie", "1", "Building Perimeter Doors Security Assessment", "26C-0055", "9/10",
    "Closed – No deficiencies were noted."],
  ["District", "1", "Water Leak Outside of Building", "26DR-0026", "9/9",
    "Open – Water Leak Outside of Building.\nSprinkle Pipe broke outside next to the East entry door.\nNo water came inside the building.\nWater was shut off by the Facility Manager.\nFacility Manager is awaiting repairs from technicians."],
  ["District", "1", "Weekly Security Assessment", "26DR-0027", "9/10",
    "Open – The following deficiencies were noted:\nBuilding Light #5 is not operational.\nParking Lot Light is not operational.\nFacility Manager is still waiting for repairs from technician."],
  ["India", "3", "Scheduled Power Outage", "26I-0059", "9/4",
    "Closed – Scheduled Power Outage\nScheduled outage for generator / main power renovations.\nSupplemental generators are installed until the main power is restored.\nMain power restored successfully ahead of the original scheduled date.\nNo lasting effect on the facility. Operations are now normal."],
  ["India", "1", "A100 Ceiling Leak", "26I-0060", "9/7",
    "Closed – A100 Ceiling Leak\nMinor leak found on A100 with no effect on product.\nLeak patched and under monitoring from 3PL staff as a precaution."],
  ["India", "1", "Building Perimeter Doors Security Assessment", "26I-0061", "9/9",
    "Closed – No deficiencies were noted."],
  ["Lima", "1", "Building Perimeter Doors Security Assessment", "26L-0046", "9/9",
    "Open – The following deficiencies were noted:\nComplete Building Perimeter Doors.\nDoor #204 failed to call up due to the Camera INT FX 27-204 shot is misaligned.\nFacilities were notified."],
  ["Papa", "1", "Building Perimeter Doors Security Assessment", "26P-0075", "9/9",
    "Open – The following deficiencies were noted:\nComplete Building Perimeter Doors.\nDoors M29, M34, M36 and Alarms room do not receive an audible alarm.\nFacilities were notified."],
  ["Papa", "1", "Perimeter Fence False Alarm Zone 5", "26P-0074", "9/8",
    "Open – Perimeter Fence False Alarm Zone 5\nZone 5 falsely triggers.\nFacilities were notified."],
  ["Sierra", "1", "Pedestrian Gate Equipment Failure", "26S-0048", "9/4",
    "Open – Pedestrian Gate Equipment Failure\nMagnet on pedestrian gate has broken off the wire due to a stripped screw\nFacilities were notified"],
  ["Sierra", "1", "Building Perimeter Doors Security Assessment", "26S-0049", "9/9",
    "Open – The following deficiencies were noted:\nOHD #163 did not trigger a visual call-up\nOHD #72 did not trigger an audible alarm or visual call-up\nPED #106 did not trigger and audible alarm or visual call-up\nFacilities were notified"],
  ["Sigma", "1", "Building Perimeter Doors Security Assessment", "26G-0047", "9/10",
    "Closed – No deficiencies were noted."],
  ["Tango", "1", "Building Perimeter Doors Security Assessment", "26T-0042", "9/7",
    "Closed – No deficiencies were noted."],
  ["Victor", "2", "Pedestrian Gate Magnet Broke", "26V-0073", "9/10",
    "Closed – Pedestrian Gate Magnet Broke.\nRepairs were made by technician\nThe pedestrian gate is fully operational."],
  ["Victor", "1", "Building Perimeter Doors Security Assessment", "26V-0074", "9/10",
    "Closed – No deficiencies were noted."],
  ["Whiskey", "1", "Building Perimeter Doors Security Assessment", "26W-0065", "9/9",
    "Closed – No deficiencies were noted."],
  ["Xray", "1", "Building Perimeter Doors Security Assessment", "26X-0057", "9/7",
    "Open - The following deficiencies were noted:\nComplete Building Perimeter Doors\nMan-Doors M16, M17, M18, M19, M20, and M21 are offline due to construction.\nMan-Doors 6, 8, 9, 29 do not open all the way.\nMan-Door M17 unserviceable Plates.\nFacilities were notified."],
];

const HEADERS = ["SITE", "TYPE", "INCIDENT DESCRIPTION", "DATE", "STATUS & ACTION TAKEN"];

const headerRow = new TableRow({
  tableHeader: true,
  children: HEADERS.map((h, i) => headerCell(h, COL_W[i])),
});

const bodyRows = ROWS.map(([site, type, desc, caseNo, date, status], i) => {
  const zebra = i % 2 === 1;
  return new TableRow({
    children: [
      bodyCell([textPara(site)], COL_W[0], { zebra }),
      bodyCell([textPara(type, { center: true })], COL_W[1], { zebra }),
      bodyCell([textPara(desc, { bold: true, color: BLACK, after: 20 }), textPara(caseNo, { color: STEEL })], COL_W[2], { zebra }),
      bodyCell([textPara(date, { center: true })], COL_W[3], { zebra }),
      bodyCell(statusParas(status), COL_W[4], { zebra }),
    ],
  });
});

const table = new Table({
  width: { size: CONTENT_W, type: WidthType.DXA },
  layout: TableLayoutType.FIXED,
  rows: [headerRow, ...bodyRows],
});

// ---- header/footer ----
const logoBuf = img("valletta-mark-black.png");
function makeHeader() {
  return new Header({
    children: [
      new Paragraph({
        border: { bottom: { color: RED, space: 8, style: BorderStyle.SINGLE, size: 16 } },
        spacing: { after: 40 },
        children: [new ImageRun({ type: "png", data: logoBuf, transformation: { width: 165, height: 33 } })],
      }),
      new Paragraph({
        spacing: { before: 60, after: 0 },
        children: [new TextRun({ text: "CONTRACTOR COMBINED INCIDENT REPORT LOG", font: F_HEAD, bold: true, size: 24, color: BLACK })],
      }),
      new Paragraph({
        spacing: { before: 20, after: 120 },
        children: [new TextRun({ text: "REPORTING PERIOD: 9/4 – 9/10/2026", font: F_LABEL, bold: true, size: 15, color: STEEL, characterSpacing: 4 })],
      }),
    ],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Valletta Industries  |  Contractor Combined Incident Report Log  –  Page ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.CURRENT], font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ text: " of ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_BODY, size: 15, color: STEEL }),
      ],
    })],
  });
}

// ================= DOCUMENT =================
const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: PAGE_H, orientation: "landscape" },
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
      },
    },
    headers: { default: makeHeader() },
    footers: { default: makeFooter() },
    children: [table],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(HERE, "valletta_incident_report_log.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
