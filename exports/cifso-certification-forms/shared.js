const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, PageBreak,
  convertInchesToTwip, TabStopType, Table, TableRow, TableCell, WidthType,
  CheckBox, VerticalAlign,
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
const MARGIN = convertInchesToTwip(0.85);
const CONTENT_W = PAGE_W - 2 * MARGIN;

function pageBreak() { return new Paragraph({ children: [new PageBreak()] }); }

function noBorderCell(children, widthPct) {
  return new TableCell({
    width: { size: widthPct, type: WidthType.PERCENTAGE },
    verticalAlign: VerticalAlign.TOP,
    margins: { left: 0, right: 200 },
    borders: {
      top: { style: BorderStyle.NONE, size: 0, color: "auto" },
      bottom: { style: BorderStyle.NONE, size: 0, color: "auto" },
      left: { style: BorderStyle.NONE, size: 0, color: "auto" },
      right: { style: BorderStyle.NONE, size: 0, color: "auto" },
    },
    children,
  });
}

function docTitle(title, subtitle) {
  return [
    new Paragraph({ spacing: { before: 100, after: 40 }, children: [new TextRun({ text: title, font: F_HEAD, bold: true, size: 40, color: BLACK })] }),
    new Paragraph({ border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 18 } }, spacing: { after: 160 }, children: [new TextRun({ text: "", size: 2 })] }),
    new Paragraph({ spacing: { after: 220 }, children: [new TextRun({ text: subtitle, font: F_BODY, size: 20, color: STEEL })] }),
  ];
}

function sectionHeading(text) {
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { before: 260, after: 160 },
    indent: { left: 100 },
    children: [new TextRun({ text: text.toUpperCase(), font: F_HEAD, bold: true, size: 21, color: WHITE })],
  });
}

function subHeading(text) {
  return new Paragraph({
    spacing: { before: 200, after: 120 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 10 } },
    children: [new TextRun({ text: text.toUpperCase(), font: F_LABEL, bold: true, size: 18, color: BLACK })],
  });
}

// full-width fillable field: red label, blank underlined line
function fieldRow(label) {
  return new Paragraph({
    border: { bottom: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 120, after: 60 },
    children: [
      new TextRun({ text: label.toUpperCase(), font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 }),
      new TextRun({ text: " ".repeat(6), size: 15 }),
    ],
  });
}

// two short fillable fields side by side (e.g. "Age" / "Gender")
function fieldPairRow(label1, label2) {
  const cell = (label) => noBorderCell([
    new Paragraph({
      border: { bottom: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 } },
      spacing: { before: 120, after: 60 },
      children: [new TextRun({ text: label.toUpperCase(), font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 })],
    }),
  ], 50);
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [new TableRow({ children: [cell(label1), cell(label2)] })],
  });
}

function fieldTripleRow(label1, label2, label3) {
  const cell = (label) => noBorderCell([
    new Paragraph({
      border: { bottom: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 } },
      spacing: { before: 120, after: 60 },
      children: [new TextRun({ text: label.toUpperCase(), font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 })],
    }),
  ], 33.33);
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [new TableRow({ children: [cell(label1), cell(label2), cell(label3)] })],
  });
}

// interactive checkbox content control + label text
function checkboxItem(text, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.tight ? 40 : 90, after: opts.tight ? 40 : 90 },
    indent: { left: opts.indent || 0 },
    children: [
      new CheckBox({ checked: false }),
      new TextRun({ text: "  " + text, font: F_BODY, size: 20, color: CHARCOAL, bold: !!opts.bold }),
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

function blankNoteBox(minLines = 4) {
  const paras = [];
  for (let i = 0; i < minLines; i++) {
    paras.push(new Paragraph({
      shading: { type: ShadingType.CLEAR, color: "auto", fill: FIELD_WHITE },
      border: i === minLines - 1
        ? { bottom: { color: LINE_GRAY, space: 2, style: BorderStyle.SINGLE, size: 4 }, left: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 }, right: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 } }
        : { left: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 }, right: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 } },
      spacing: { before: i === 0 ? 120 : 0, after: i === minLines - 1 ? 200 : 0 },
      indent: { left: 80, right: 80 },
      children: [new TextRun({ text: " ", size: 20 })],
    }));
  }
  return paras;
}

function sigRow(label) {
  return new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 3600 }],
    border: { bottom: { color: LINE_GRAY, space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 200, after: 60 },
    children: [new TextRun({ text: label + "\t", font: F_BODY, bold: true, size: 19, color: CHARCOAL })],
  });
}

function bodyPara(text) {
  return new Paragraph({ spacing: { after: 140, line: 270 }, children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })] });
}

// ---- header/footer ----
function makeHeader(docTag) {
  const logoBuf = img("valletta-mark-black.png");
  return new Header({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
      border: { bottom: { color: RED, space: 8, style: BorderStyle.SINGLE, size: 16 } },
      children: [
        new ImageRun({ type: "png", data: logoBuf, transformation: { width: 150, height: 30 } }),
        new TextRun({ text: "\t" }),
        new TextRun({ text: docTag.toUpperCase(), font: F_LABEL, bold: true, size: 14, color: STEEL, characterSpacing: 6 }),
      ],
    })],
  });
}
function makeFooter(docTag) {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: `Valletta Industries  |  ${docTag}  –  Page `, font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.CURRENT], font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ text: " of ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_BODY, size: 15, color: STEEL }),
      ],
    })],
  });
}
const emptyHeader = () => new Header({ children: [new Paragraph({ children: [] })] });
const emptyFooter = () => new Footer({ children: [new Paragraph({ children: [] })] });

function buildDocument(docTag, content) {
  return new Document({
    sections: [{
      properties: {
        page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } },
        titlePage: true,
      },
      headers: { default: makeHeader(docTag), first: emptyHeader() },
      footers: { default: makeFooter(docTag), first: emptyFooter() },
      children: content,
    }],
  });
}

function writeDoc(doc, outName) {
  return Packer.toBuffer(doc).then((buf) => {
    fs.writeFileSync(path.join(HERE, outName), buf);
    console.log(outName, "written", buf.length, "bytes");
  });
}

module.exports = {
  BLACK, CHARCOAL, FIELD_WHITE, RED, STEEL, LINE_GRAY, WHITE, NOTE_TINT,
  F_HEAD, F_LABEL, F_BODY, CONTENT_W,
  pageBreak, docTitle, sectionHeading, subHeading, fieldRow, fieldPairRow, fieldTripleRow,
  checkboxItem, tintedBox, blankNoteBox, sigRow, bodyPara, buildDocument, writeDoc,
  Paragraph, TextRun, BorderStyle, ShadingType,
};
