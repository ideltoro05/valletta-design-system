const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber,
  convertInchesToTwip, TabStopType, Table, TableRow, TableCell, WidthType, VerticalAlign,
} = require("docx");

const HERE = __dirname;
const img = (name) => fs.readFileSync(path.join(HERE, name));
const DATA = JSON.parse(fs.readFileSync(path.join(HERE, "pft_data.json"), "utf-8"));

const BLACK = "0A0A0A";
const CHARCOAL = "26282B";
const FIELD_WHITE = "F5F5F3";
const COBALT = "1B4FA0";
const STEEL = "5B5F66";
const LINE_GRAY = "D8D9DB";
const WHITE = "FFFFFF";
const NOTE_TINT = "EFEFEC";
const ZEBRA = "EFEFEC";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = convertInchesToTwip(1.0);
const HEADER_DISTANCE = convertInchesToTwip(0.35);
const CONTENT_W = PAGE_W - 2 * MARGIN;

const DOC_TAG = "PFT Policy and Administration Plan";

// ============================================================
// helpers
// ============================================================
function noBorderCell(children, widthPct, opts = {}) {
  return new TableCell({
    width: { size: widthPct, type: WidthType.PERCENTAGE },
    verticalAlign: VerticalAlign.TOP,
    shading: opts.fill ? { type: ShadingType.CLEAR, color: "auto", fill: opts.fill } : undefined,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      left: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      right: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
    },
    children,
  });
}

function sectionHeading(text) {
  // "N. TITLE" -> cobalt number, black title, cobalt rule beneath
  const m = text.match(/^(\d+)\.\s+(.*)$/);
  const numPart = m ? `${m[1]}. ` : "";
  const titlePart = m ? m[2] : text;
  return new Paragraph({
    spacing: { before: 280, after: 140 },
    border: { bottom: { color: COBALT, space: 4, style: BorderStyle.SINGLE, size: 12 } },
    children: [
      new TextRun({ text: numPart, font: F_HEAD, bold: true, size: 25, color: COBALT }),
      new TextRun({ text: titlePart, allCaps: true, font: F_HEAD, bold: true, size: 25, color: BLACK }),
    ],
  });
}

function subHeading(text) {
  return new Paragraph({
    spacing: { before: 200, after: 100 },
    border: { bottom: { color: COBALT, space: 3, style: BorderStyle.SINGLE, size: 8 } },
    children: [new TextRun({ text, allCaps: true, font: F_LABEL, bold: true, size: 17, color: BLACK, characterSpacing: 2 })],
  });
}

function eventLabel(text) {
  return new Paragraph({
    spacing: { before: 220, after: 80 },
    children: [new TextRun({ text, allCaps: true, font: F_LABEL, bold: true, size: 16, color: COBALT, characterSpacing: 4 })],
  });
}

function bodyPara(text) {
  return new Paragraph({
    spacing: { after: 130, line: 268 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

function bulletPara(text) {
  return new Paragraph({
    numbering: { reference: "pft-bullets", level: 0 },
    spacing: { after: 90, line: 260 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

function tintedCallout(text) {
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: NOTE_TINT },
    border: { left: { color: COBALT, space: 10, style: BorderStyle.SINGLE, size: 16 } },
    indent: { left: 160, right: 160 },
    spacing: { before: 140, after: 200, line: 262 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

// generic data table: first row = header (black fill, white bold caps text),
// remaining rows = zebra-striped body
function dataTable(rows) {
  const nCols = rows[0].length;
  const colWidthPct = 100 / nCols;
  const headerRow = new TableRow({
    tableHeader: true,
    children: rows[0].map((text) => new TableCell({
      width: { size: colWidthPct, type: WidthType.PERCENTAGE },
      shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
      verticalAlign: VerticalAlign.CENTER,
      margins: { top: 90, bottom: 90, left: 100, right: 100 },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
        bottom: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
        left: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
        right: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
      },
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text, allCaps: true, font: F_LABEL, bold: true, size: 14, color: WHITE, characterSpacing: 3 })],
      })],
    })),
  });
  const bodyRows = rows.slice(1).map((r, i) => new TableRow({
    children: r.map((text, ci) => new TableCell({
      width: { size: colWidthPct, type: WidthType.PERCENTAGE },
      shading: { type: ShadingType.CLEAR, color: "auto", fill: i % 2 === 1 ? ZEBRA : WHITE },
      verticalAlign: VerticalAlign.CENTER,
      margins: { top: 80, bottom: 80, left: 100, right: 100 },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
        bottom: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
        left: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
        right: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      },
      children: [new Paragraph({
        alignment: ci === 0 ? AlignmentType.LEFT : AlignmentType.CENTER,
        children: [new TextRun({ text, font: F_BODY, bold: ci === 0, size: 18, color: ci === 0 ? BLACK : CHARCOAL })],
      })],
    })),
  }));
  return new Table({ width: { size: 100, type: WidthType.PERCENTAGE }, rows: [headerRow, ...bodyRows] });
}

// 2-column doc-control table: label (bold, cobalt) / value
function controlTable(rows) {
  const trs = rows.map((r) => new TableRow({
    children: [
      noBorderCell(
        [new Paragraph({ children: [new TextRun({ text: r[0], allCaps: true, font: F_LABEL, bold: true, size: 15, color: COBALT, characterSpacing: 2 })] })],
        28, { fill: FIELD_WHITE }
      ),
      noBorderCell(
        [new Paragraph({ children: [new TextRun({ text: r[1], font: F_BODY, size: 19, color: CHARCOAL })] })],
        72
      ),
    ],
  }));
  return new Table({ width: { size: 100, type: WidthType.PERCENTAGE }, rows: trs });
}

function pageBreakPara() {
  const { PageBreak } = require("docx");
  return new Paragraph({ children: [new PageBreak()] });
}

// ---- header/footer ----
function makeHeader() {
  const logoBuf = img("valletta-soc-lockup.png");
  return new Header({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
      border: { bottom: { color: COBALT, space: 8, style: BorderStyle.SINGLE, size: 16 } },
      children: [
        new ImageRun({ type: "png", data: logoBuf, transformation: { width: 63, height: 48 } }),
        new TextRun({ text: "\t" }),
        new TextRun({ text: DOC_TAG.toUpperCase(), font: F_LABEL, bold: true, size: 14, color: STEEL, characterSpacing: 6 }),
      ],
    })],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: `Valletta Industries  |  ${DOC_TAG}  –  Page `, font: F_BODY, size: 15, color: STEEL }),
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
// render DATA (true source document order) into content blocks
// ============================================================
const content = [];
const EVENT_LABELS = new Set(["Push-Ups", "Sit-Ups", "300-Meter Sprint", "165-lb Victim Drag"]);
let tableCount = 0;

// --- title block (items 0-2) ---
const titleItem = DATA[0]; // "PHYSICAL FITNESS TEST (PFT)\nPOLICY AND ADMINISTRATION PLAN"
const titleLines = titleItem.text.split("\n");
content.push(new Paragraph({
  spacing: { before: 80, after: 40 },
  children: titleLines.flatMap((line, i) => (i === 0 ? [] : [new TextRun({ break: 1 })]).concat([
    new TextRun({ text: line, font: F_HEAD, bold: true, size: i === 0 ? 40 : 30, color: BLACK }),
  ])),
}));
content.push(new Paragraph({
  border: { bottom: { color: COBALT, space: 4, style: BorderStyle.SINGLE, size: 18 } },
  spacing: { after: 160 },
  children: [new TextRun({ text: "", size: 2 })],
}));
content.push(new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: DATA[1].text, font: F_BODY, size: 20, color: STEEL })] }));
content.push(new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: DATA[2].text, font: F_BODY, bold: true, size: 18, color: CHARCOAL })] }));

for (let idx = 3; idx < DATA.length; idx++) {
  const item = DATA[idx];
  if (item.type === "table") {
    tableCount++;
    if (item.idx === 0) {
      content.push(controlTable(item.rows));
      content.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
    } else {
      content.push(dataTable(item.rows));
      content.push(new Paragraph({ spacing: { after: 200 }, children: [] }));
    }
    continue;
  }
  const text = item.text;
  if (item.style === "Heading 1" || /^11\.\s+STANDARDIZED/.test(text)) {
    content.push(sectionHeading(text));
  } else if (item.style === "Heading 2") {
    content.push(subHeading(text));
  } else if (item.style === "List Bullet") {
    content.push(bulletPara(text));
  } else if (text.startsWith("POLICY CONTROL:")) {
    content.push(tintedCallout(text));
  } else if (EVENT_LABELS.has(text)) {
    content.push(eventLabel(text));
  } else {
    content.push(bodyPara(text));
  }
}

// ============================================================
// DOCUMENT
// ============================================================
const { LevelFormat } = require("docx");
const doc = new Document({
  numbering: {
    config: [{
      reference: "pft-bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "■",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 220 } }, run: { color: COBALT, font: F_BODY, size: 16 } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: PAGE_H },
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN, header: HEADER_DISTANCE, footer: HEADER_DISTANCE },
      },
      titlePage: true,
    },
    headers: { default: makeHeader(), first: emptyHeader },
    footers: { default: makeFooter(), first: emptyFooter },
    children: content,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(HERE, "valletta_pft_policy.docx"), buf);
  console.log("docx written", buf.length, "bytes; tables rendered:", tableCount);
});
