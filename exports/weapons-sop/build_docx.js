const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, PageBreak,
  convertInchesToTwip, LevelFormat, TabStopType,
} = require("docx");

const HERE = __dirname;
const img = (name) => fs.readFileSync(path.join(HERE, name));

const BLACK = "0A0A0A";
const CHARCOAL = "26282B";
const RED = "FF002B";
const STEEL = "5B5F66";
const LINE_GRAY = "D8D9DB";
const WHITE = "FFFFFF";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = convertInchesToTwip(0.9);
const CONTENT_W = PAGE_W - 2 * MARGIN;

function secTitle(num, title) {
  return new Paragraph({
    spacing: { before: 260, after: 140 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 10 } },
    children: [new TextRun({ text: `${num}.  ${title.toUpperCase()}`, font: F_HEAD, bold: true, size: 25, color: BLACK })],
  });
}

function plainTitle(title) {
  return new Paragraph({
    spacing: { before: 260, after: 140 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 10 } },
    children: [new TextRun({ text: title.toUpperCase(), font: F_HEAD, bold: true, size: 23, color: BLACK })],
  });
}

const IND = [0, 260, 620];
function item(label, text, level = 1, bold = false) {
  return new Paragraph({
    indent: { left: IND[level] },
    spacing: { after: 90, line: 255 },
    children: [
      new TextRun({ text: label + "  ", font: F_BODY, bold: true, size: 20, color: RED }),
      new TextRun({ text, font: F_BODY, size: 20, bold, color: bold ? BLACK : CHARCOAL }),
    ],
  });
}

function note(tag, lines) {
  const paras = [];
  paras.push(new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: "EFEFEC" },
    border: { left: { color: RED, space: 10, style: BorderStyle.SINGLE, size: 16 } },
    spacing: { before: 90, after: 20 },
    children: [new TextRun({ text: tag, font: F_LABEL, bold: true, size: 14, color: RED, characterSpacing: 6 })],
  }));
  lines.forEach((l, i) => {
    paras.push(new Paragraph({
      shading: { type: ShadingType.CLEAR, color: "auto", fill: "EFEFEC" },
      border: { left: { color: RED, space: 10, style: BorderStyle.SINGLE, size: 16 } },
      spacing: { after: i === lines.length - 1 ? 90 : 20 },
      children: [new TextRun({ text: l, font: F_BODY, size: 19, color: CHARCOAL })],
    }));
  });
  return paras;
}

function fieldRow(label, value) {
  return new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 2400 }],
    border: { bottom: { color: LINE_GRAY, space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 60, after: 100 },
    children: [
      new TextRun({ text: label.toUpperCase() + "\t", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 }),
      new TextRun({ text: value || "", font: F_BODY, size: 20, color: CHARCOAL }),
    ],
  });
}

function sigRow(label) {
  return new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 3400 }],
    border: { bottom: { color: LINE_GRAY, space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 140, after: 60 },
    children: [new TextRun({ text: label + "\t", font: F_BODY, bold: true, size: 19, color: CHARCOAL })],
  });
}

function ackBullet(text) {
  return new Paragraph({
    numbering: { reference: "brand-bullets", level: 0 },
    spacing: { after: 80, line: 255 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

function bodyPara(text) {
  return new Paragraph({ spacing: { after: 130, line: 270 }, children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })] });
}

function pageBreak() { return new Paragraph({ children: [new PageBreak()] }); }

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
        new TextRun({ text: "SOP – FIREARMS LOADING AND UNLOADING", font: F_LABEL, bold: true, size: 15, color: STEEL, characterSpacing: 8 }),
      ],
    })],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Valletta Industries  |  SOP – Firearms Loading and Unloading  –  Page ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.CURRENT], font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ text: " of ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_BODY, size: 15, color: STEEL }),
      ],
    })],
  });
}
const emptyHeader = new Header({ children: [new Paragraph({ children: [] })] });
const emptyFooter = new Footer({ children: [new Paragraph({ children: [] })] });

// ================= CONTENT =================
const content = [];

// ---- cover ----
content.push(
  new Paragraph({ spacing: { before: 2400 }, alignment: AlignmentType.CENTER,
    children: [new ImageRun({ type: "png", data: img("valletta-mark-white.png"), transformation: { width: 300, height: 60 } })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400 },
    children: [new TextRun({ text: "STANDARD OPERATING PROCEDURE", font: F_LABEL, bold: true, size: 19, color: RED, characterSpacing: 16 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 220 },
    children: [new TextRun({ text: "FIREARMS LOADING", font: F_HEAD, bold: true, size: 46, color: WHITE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
    children: [new TextRun({ text: "AND UNLOADING", font: F_HEAD, bold: true, size: 46, color: WHITE })] }),
  new Paragraph({ spacing: { before: 700 }, children: [] }),
  new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 4500 }],
    border: { bottom: { color: "4A4B4E", space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { after: 160 },
    children: [new TextRun({ text: "DOCUMENT NUMBER\t", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 }), new TextRun({ text: "", font: F_BODY, size: 20, color: WHITE })],
  }),
  new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 4500 }],
    border: { bottom: { color: "4A4B4E", space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { after: 160 },
    children: [new TextRun({ text: "EFFECTIVE DATE\t", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 }), new TextRun({ text: "", font: F_BODY, size: 20, color: WHITE })],
  }),
  new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 4500 }],
    border: { bottom: { color: "4A4B4E", space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { after: 160 },
    children: [new TextRun({ text: "REVISION\t", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 }), new TextRun({ text: "1.0", font: F_BODY, size: 20, color: WHITE })],
  }),
  new Paragraph({
    tabStops: [{ type: TabStopType.LEFT, position: 4500 }],
    border: { bottom: { color: "4A4B4E", space: 2, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { after: 160 },
    children: [new TextRun({ text: "APPROVED BY\t", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 3 }), new TextRun({ text: "", font: F_BODY, size: 20, color: WHITE })],
  }),
  pageBreak(),
);

// ---- 1-5 ----
content.push(
  secTitle(1, "Purpose"),
  item("1.1", "To establish safe, standardized, and accountable procedures for arming and disarming personnel, loading and unloading firearms, managing ammunition, and maintaining armory security during all guard force operations"),

  secTitle(2, "Scope"),
  item("2.1", "This SOP applies to all armed security personnel, supervisors, armorers, and other authorized personnel who issue, receive, handle, store, transport, or account for firearms and ammunition within the armory."),

  secTitle(3, "Definitions and Acronyms"),
  item("3.1", "BCD – Bullet Containment Device"),
  item("3.2", "Armory – Secure location used for storage and accountability of firearms and ammunition."),
  item("3.3", "Facility Ready – Condition of in-service duty firearms"),
  item("3.3.1", "Rifle – Full magazine inserted with empty chamber unless otherwise authorized.", 2),
  item("3.3.2", "Pistol – Full magazine inserted with a round chambered.", 2),
  item("3.4", "Safe Firearm – Firearm verified clear of ammunition and configured for storage."),

  secTitle(4, "Responsibility and Authority"),
  item("4.1", "Supervisors", 1, true),
  item("4.1.1", "Control access to the armory and firearms safe.", 2),
  item("4.1.2", "Open and secure safes at shift change", 2),
  item("4.1.3", "Observe and direct all loading and unloading operations", 2),
  item("4.1.4", "Verify compliance with this SOP and stop unsafe acts immediately", 2),
  item("4.1.5", "Conduct required daily armory inventory, records and discrepancy reporting", 2),
  item("4.2", "Armed Officers", 1, true),
  item("4.2.1", "Follow all firearm safety rules", 2),
  item("4.2.2", "Comply with Supervisor commands during loading/unloading", 2),
  item("4.2.3", "Immediately report unsafe conditions, damaged equipment, or ammunition discrepancies.", 2),
  item("4.3", "Site Trainers", 1, true),
  item("4.3.1", "Maintain serviceability of firearms and ammunition.", 2),
  item("4.3.2", "Ensure inspections, maintenance, storage, and records are current.", 2),

  secTitle(5, "General Firearms Safety Rules"),
  item("5.1", "Treat every firearm as if it is loaded."),
  item("5.2", "Keep muzzle pointed in a safe direction at all times."),
  item("5.3", "Keep fingers off the trigger, outside the trigger guard, and safety engaged until you decide to fire."),
  item("5.4", "Be sure of your target and what’s beyond it."),
);

content.push(pageBreak());

// ---- 6-8 ----
content.push(
  secTitle(6, "Supervisor Requirements During Shift Change"),
  item("6.1", "Supervisor Shall:", 1, true),
  item("6.1.1", "Open the firearm safe and maintain positive control of issued firearms.", 2),
  item("6.1.2", "Observe every loading and unloading action from start to finish.", 2),
  item("6.1.3", "Verify firearms are clear before issue and before storage.", 2),
  item("6.1.4", "Ensure use of the BCD during all chambering and clearing operations.", 2),
  item("6.1.5", "Verify ammunition counts, magazine counts, and firearm serial numbers as required.", 2),
  item("6.1.6", "Halt any unsafe act immediately.", 2),
  item("6.1.7", "Ensure all issued firearms, ammunition, and equipment are accounted for before personnel depart.", 2),
  item("6.1.8", "Secure all safes and armory access points after completion of shift-change operations.", 2),
  item("6.1.9", "Maintain constant visual and physical control of contents inside the safe.", 2),

  secTitle(7, "Firearm Loading Procedure"),
  item("7.1", "Supervisor will retrieve the correct firearm from storage."),
  item("7.2", "Insert muzzle into the BCD, visually verifying serial number."),
  item("7.2.1", "Rifle – Verify safety is engaged.", 2),
  item("7.3", "Lock the action to the rear, visually and physically verifying the firearm is clear."),
  item("7.4", "The supervisor will transfer control of the firearm to the officer."),
  item("7.5", "While still pointed into the BCD, the officer will re-verify the firearm is clear."),
  item("7.6", "Source of Feed:"),
  item("7.6.1", "Pistol – Insert magazine and release the action, chambering a round.", 2),
  item("7.6.2", "Rifle – Release the action before inserting magazine. No round will be chambered.", 2),
  item("7.7", "Retain the firearm."),
  ...note("NOTE", ["Officer may conduct press checks or magazine retention tests."]),

  secTitle(8, "Firearm Unloading Procedure"),
  item("8.1", "Insert muzzle into the BCD, visually verifying serial number."),
  item("8.1.1", "Rifle – Verify safety is engaged.", 2),
  item("8.2", "Remove the magazine."),
  item("8.3", "Lock action to the rear, ejecting the chambered round, if present."),
  item("8.4", "Visually and physically verify the firearm is clear."),
  item("8.5", "The officer will transfer control of the firearm to the supervisor."),
  item("8.6", "While still pointed into the BCD, the supervisor will re-verify the firearm is clear."),
  item("8.6.1", "Rifle – Verify safety is engaged.", 2),
  item("8.7", "Release the action and place the firearm into storage."),
  item("8.8", "Collect and replace ejected round if present, return all magazines to the proper storage."),
);

content.push(pageBreak());

// ---- 9-12 ----
content.push(
  secTitle(9, "Firearms Storage Requirements"),
  item("9.1", "Firearms shall be stored unloaded unless operation requirements dictate otherwise"),
  item("9.2", "Out-of-service firearms shall be tagged or segregated from service firearms."),
  item("9.3", "Storage containers/firearms safes shall remain locked when not under direct supervisory observation and control."),

  secTitle(10, "Ammunition Accountability and Management"),
  item("10.1", "Only authorized duty ammunition shall be issued."),
  item("10.2", "Ammunition counts shall be verified during issue and turn-in."),
  item("10.3", "Damaged or suspected ammunition shall be removed."),
  item("10.4", "Duty ammunition shall be inspected and rotated in accordance with organizational policy"),
  item("10.5", "Monthly ammunition inventories shall be completed, reconciled, and documented by the Site Trainer. Any discrepancies shall be immediately reported to the National Training Manager and Site Manager and investigated in accordance with established procedures."),

  secTitle(11, "Documentation and Reporting"),
  item("11.1", "All firearms issues, returns, inventories, discrepancies, damaged ammunition, unsafe acts, training completion, SOP acknowledgments, and out-of-service firearms shall be documented by the supervisor or trainer in the records management systems."),
  item("11.2", "Training records and employee acknowledgments for this SOP shall be maintained by Training management and retained in accordance with company record retention requirements."),
  item("11.3", "Training management shall ensure personnel under their supervision have completed all required training and acknowledgments for this SOP."),
  item("11.4", "Supervisors shall promptly document and report any violation of this SOP through established reporting channels."),

  secTitle(12, "Training and Compliance"),
  item("12.1", "Personnel shall receive initial training on this SOP prior to being issued a firearm, assigned to an armed post, or performing any duties covered by this SOP. Refresher training shall be conducted periodically as determined by organizational requirements."),
  item("12.2", "Upon completion of training, personnel shall acknowledge in writing or through an approved electronic system that they have received, reviewed, understand, and will comply with this SOP. Documentation of training and acknowledgment shall be maintained in accordance with Section 12.2."),
  item("12.3", "Supervisors or Trainers shall conduct observations, inspections, and corrective actions to ensure continued compliance with this SOP."),
  item("12.4", "Failure to comply with the requirements of this SOP may result in corrective action up to and including removal from armed duties, suspension of firearm authorization, disciplinary action, or other corrective measures in accordance with established Employee Relations policies and procedures."),
  item("12.5", "Personnel who have not completed the required training and acknowledgment process shall not be issued a firearm, ammunition, or assigned to an armed post until all requirements have been satisfied and documented."),
);

content.push(pageBreak());

// ---- Supervisor acknowledgment ----
content.push(
  plainTitle("Firearms Loading and Unloading – Armed Shift Supervisor Acknowledgement"),
  fieldRow("Employee Name", ""),
  fieldRow("Employee ID", ""),
  fieldRow("Site/Contract", ""),
  fieldRow("Position", "Armed Shift Supervisor"),
  fieldRow("Date of Training", ""),
  new Paragraph({ spacing: { before: 140, after: 100 }, children: [new TextRun({ text: "ACKNOWLEDGMENT", font: F_BODY, bold: true, size: 22, color: BLACK })] }),
  bodyPara("I acknowledge that I have received training on, reviewed, and understand the requirements of the Loading and Unloading of Firearms SOP."),
  bodyPara("I understand my responsibilities include:"),
  ackBullet("Complying with all requirements of the SOP."),
  ackBullet("Ensuring firearms loading and unloading activities are conducted only in designated locations and in accordance with established procedures."),
  ackBullet("Conducting oversight of armed personnel under my supervision to verify compliance with this SOP."),
  ackBullet("Ensuring required inspections, inventories, documentation, and reporting requirements are completed accurately and timely."),
  ackBullet("Taking immediate corrective action when unsafe acts, policy violations, or procedural deficiencies are observed."),
  ackBullet("Reporting incidents, discrepancies, unsafe conditions, damaged equipment, or violations through established reporting channels."),
  ackBullet("Ensuring personnel complete required training and acknowledgment requirements before being issued firearms, ammunition, or assigned to armed duties."),
  ackBullet("Understanding that failure to comply with this SOP may result in disciplinary action, including removal from armed duties, suspension of firearm authorization, or other corrective action in accordance with company policy."),
  bodyPara("I agree to comply with the requirements of this SOP and to enforce its provisions within my area of responsibility."),
  sigRow("Supervisor Employee Signature"),
  sigRow("Date"),
  sigRow("Trainer/Manager Signature"),
  sigRow("Date"),
);

content.push(pageBreak());

// ---- Officer acknowledgment ----
content.push(
  plainTitle("Firearms Loading and Unloading – Armed Officer Acknowledgement"),
  fieldRow("Employee Name", ""),
  fieldRow("Employee ID", ""),
  fieldRow("Site/Contract", ""),
  fieldRow("Position", "Armed Officer"),
  fieldRow("Date of Training", ""),
  new Paragraph({ spacing: { before: 140, after: 100 }, children: [new TextRun({ text: "ACKNOWLEDGMENT", font: F_BODY, bold: true, size: 22, color: BLACK })] }),
  bodyPara("I acknowledge that I have received training on, reviewed, and understand the requirements of the Loading and Unloading of Firearms SOP."),
  bodyPara("I understand and agree that:"),
  ackBullet("I shall comply with all firearm loading, unloading, handling, storage, and accountability requirements contained in this SOP."),
  ackBullet("I shall load and unload firearms only in designated locations and in accordance with approved procedures."),
  ackBullet("I shall immediately report unsafe acts, firearm malfunctions, damaged ammunition, equipment deficiencies, or policy violations to my supervisor."),
  ackBullet("I shall participate in required inspections, inventories, and documentation processes."),
  ackBullet("I shall maintain accountability for all firearms, ammunition, and related equipment issued to me."),
  ackBullet("I shall not deviate from established procedures unless directed by authorized management during an emergency situation."),
  ackBullet("I understand that completion of SOP training and acknowledgment is required before I may be issued a firearm, ammunition, or assigned to an armed post."),
  ackBullet("I understand that failure to comply with this SOP may result in disciplinary action, including removal from armed duties, suspension of firearm authorization, or other corrective action in accordance with company policy."),
  bodyPara("I agree to comply with all requirements of this SOP and understand that I am responsible for following all applicable firearm safety and accountability requirements."),
  sigRow("Officer Signature"),
  sigRow("Date"),
  sigRow("Trainer/Manager Signature"),
  sigRow("Date"),
);

// ================= DOCUMENT =================
const doc = new Document({
  numbering: {
    config: [{
      reference: "brand-bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "■",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 220 } }, run: { color: RED, font: F_BODY, size: 16 } },
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
  fs.writeFileSync(path.join(HERE, "valletta_weapons_sop.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
