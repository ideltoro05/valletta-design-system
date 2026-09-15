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
const TOTAL_TINT = "F2E6E8";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

// Landscape US Letter — docx's page.size swaps width/height itself when
// orientation is landscape, so these must be the PORTRAIT base dimensions.
const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = convertInchesToTwip(0.5);
const CONTENT_W = PAGE_H - 2 * MARGIN; // rendered landscape width = portrait height (11in)

const DATA = JSON.parse(fs.readFileSync(path.join(HERE, "source_data.json"), "utf8"));
const MAJOR_HEADINGS = new Set([
  "CIFSO Contractor Staffing",
  "OPERATIONS",
  "Contract Incident Reports:",
  "Daily Activity Report – Executive Summary",
  "Training Summary",
]);
const TOTAL_LABELS = new Set(["total", "totals", "contract totals"]);

const cellBorder = { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };

function majorBand(text) {
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { before: 160, after: 90 },
    children: [new TextRun({ text: text.toUpperCase(), font: F_HEAD, bold: true, size: 21, color: WHITE, characterSpacing: 6 })],
  });
}

function subHeading(text) {
  return new Paragraph({
    spacing: { before: 120, after: 70 },
    border: { bottom: { color: RED, space: 3, style: BorderStyle.SINGLE, size: 8 } },
    children: [new TextRun({ text: text.toUpperCase(), font: F_LABEL, bold: true, size: 15, color: BLACK, characterSpacing: 3 })],
  });
}

function cellParas(lines, opts = {}) {
  if (!lines || lines.length === 0) {
    return [new Paragraph({ children: [new TextRun({ text: "", size: 12 })] })];
  }
  return lines.map((l, i) => new Paragraph({
    spacing: { after: i === lines.length - 1 ? 0 : 20, line: 200 },
    children: [new TextRun({ text: l, font: F_BODY, size: opts.size ?? 12, bold: !!opts.bold, color: opts.color ?? CHARCOAL })],
  }));
}

function headerCell(lines, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    borders: { top: { style: BorderStyle.SINGLE, size: 2, color: BLACK }, bottom: { style: BorderStyle.SINGLE, size: 2, color: BLACK }, left: { style: BorderStyle.SINGLE, size: 2, color: BLACK }, right: { style: BorderStyle.SINGLE, size: 2, color: BLACK } },
    children: cellParas(lines.length ? lines : [""], { size: 11, bold: true, color: WHITE }),
  });
}

function bodyCell(lines, width, opts = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: opts.total ? TOTAL_TINT : (opts.zebra ? ZEBRA : undefined) },
    verticalAlign: VerticalAlign.TOP,
    margins: { top: 50, bottom: 50, left: 80, right: 80 },
    borders,
    children: cellParas(lines, { bold: !!opts.total }),
  });
}

function buildTable(rows) {
  const [header, ...rest] = rows;
  const body = rest.filter((r) => r.some((c) => c && c.length));
  const ncols = header.length;
  const firstW = 1400;
  const otherW = Math.max(600, Math.floor((CONTENT_W - firstW) / (ncols - 1)));
  const widths = [firstW, ...Array(ncols - 1).fill(otherW)];

  const headerRow = new TableRow({
    tableHeader: true,
    children: header.map((c, i) => headerCell(c, widths[i])),
  });

  const bodyRows = body.map((r, ri) => {
    const firstText = (r[0] || []).join(" ").trim().toLowerCase();
    const isTotal = TOTAL_LABELS.has(firstText);
    const zebra = ri % 2 === 1;
    const cells = [];
    for (let i = 0; i < ncols; i++) {
      cells.push(bodyCell(r[i] || [], widths[i], { zebra, total: isTotal }));
    }
    return new TableRow({ children: cells });
  });

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    rows: [headerRow, ...bodyRows],
  });
}

// ---- header/footer ----
const logoBuf = img("valletta-mark-black.png");
function makeHeader() {
  return new Header({
    children: [
      new Paragraph({
        border: { bottom: { color: RED, space: 8, style: BorderStyle.SINGLE, size: 16 } },
        spacing: { after: 40 },
        children: [new ImageRun({ type: "png", data: logoBuf, transformation: { width: 155, height: 31 } })],
      }),
      new Paragraph({
        spacing: { before: 60, after: 0 },
        children: [new TextRun({ text: "CONTRACTOR COMBINED WEEKLY ACTIVITY REPORT", font: F_HEAD, bold: true, size: 22, color: BLACK })],
      }),
      new Paragraph({
        spacing: { before: 20, after: 100 },
        children: [new TextRun({ text: "REPORTING PERIOD: 9/4/2026 THRU 9/10/2026", font: F_LABEL, bold: true, size: 14, color: STEEL, characterSpacing: 3 })],
      }),
    ],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Valletta Industries  |  Contractor Combined Weekly Activity Report  –  Page ", font: F_BODY, size: 14, color: STEEL }),
        new TextRun({ children: [PageNumber.CURRENT], font: F_BODY, size: 14, color: STEEL }),
        new TextRun({ text: " of ", font: F_BODY, size: 14, color: STEEL }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_BODY, size: 14, color: STEEL }),
      ],
    })],
  });
}

// ================= CONTENT =================
const content = [];
let pendingHeadings = [];
for (const item of DATA) {
  if (item.type === "heading") {
    pendingHeadings.push(item.text);
  } else {
    for (const h of pendingHeadings) {
      content.push(MAJOR_HEADINGS.has(h) ? majorBand(h) : subHeading(h));
    }
    pendingHeadings = [];
    content.push(buildTable(item.rows));
    content.push(new Paragraph({ spacing: { after: 60 }, children: [] }));
  }
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
    children: content,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(HERE, "valletta_weekly_activity_report.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
