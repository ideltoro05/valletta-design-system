const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel,
  ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber,
  convertInchesToTwip, TabStopType, Table, TableRow, TableCell, WidthType, VerticalAlign,
  LevelFormat, TableOfContents,
} = require("docx");

const HERE = __dirname;
const img = (name) => fs.readFileSync(path.join(HERE, name));

const BLACK = "0A0A0A";
const CHARCOAL = "26282B";
const FIELD_WHITE = "F5F5F3";
const COBALT = "1B4FA0";
const STEEL = "5B5F66";
const LINE_GRAY = "D8D9DB";
const WHITE = "FFFFFF";
const NOTE_TINT = "EFEFEC";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = convertInchesToTwip(1.0);
const HEADER_DISTANCE = convertInchesToTwip(0.35);
const CONTENT_W = PAGE_W - 2 * MARGIN;

const DOC_TAG = "Use of Force Policy and Procedure";

// ============================================================
// low-level helpers
// ============================================================
function noBorderCell(children, widthPct, opts = {}) {
  return new TableCell({
    width: { size: widthPct, type: WidthType.PERCENTAGE },
    verticalAlign: VerticalAlign.TOP,
    shading: opts.fill ? { type: ShadingType.CLEAR, color: "auto", fill: opts.fill } : undefined,
    margins: { top: 40, bottom: 40, left: 100, right: 100 },
    borders: {
      top: { style: BorderStyle.NONE, size: 0, color: "auto" },
      bottom: { style: BorderStyle.NONE, size: 0, color: "auto" },
      left: { style: BorderStyle.NONE, size: 0, color: "auto" },
      right: { style: BorderStyle.NONE, size: 0, color: "auto" },
    },
    children,
  });
}

function sectionHeading(num, title) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 280, after: 140 },
    border: { bottom: { color: COBALT, space: 4, style: BorderStyle.SINGLE, size: 12 } },
    children: [
      new TextRun({ text: `${num}  `, font: F_HEAD, bold: true, size: 25, color: COBALT }),
      new TextRun({ text: title, font: F_HEAD, bold: true, size: 25, color: BLACK }),
    ],
  });
}

function subHeading(num, title) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 220, after: 110 },
    children: [
      new TextRun({ text: `${num}  `, font: F_LABEL, bold: true, size: 19, color: COBALT }),
      new TextRun({ text: title, font: F_LABEL, bold: true, size: 19, color: BLACK }),
    ],
  });
}

function bodyPara(text, opts = {}) {
  return new Paragraph({
    spacing: { after: opts.after ?? 130, line: 268 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

function termPara(term, def) {
  return new Paragraph({
    spacing: { after: 110, line: 264 },
    children: [
      new TextRun({ text: term + ": ", font: F_BODY, bold: true, size: 20, color: BLACK }),
      new TextRun({ text: def, font: F_BODY, size: 20, color: CHARCOAL }),
    ],
  });
}

function labelBulletPara(label, text, ref) {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 90, line: 260 },
    children: [
      new TextRun({ text: label + ": ", font: F_BODY, bold: true, size: 20, color: BLACK }),
      new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL }),
    ],
  });
}

function plainBulletPara(text, ref, level = 0) {
  return new Paragraph({
    numbering: { reference: ref, level },
    spacing: { after: 90, line: 260 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

function romanPara(text, ref = "roman-list") {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 100, line: 260 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

function decimalPara(text, ref = "decimal-list") {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 100, line: 260 },
    children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })],
  });
}

function fieldRow(label) {
  return new Paragraph({
    border: { bottom: { color: LINE_GRAY, space: 4, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 160, after: 60 },
    children: [
      new TextRun({ text: label, allCaps: true, font: F_LABEL, bold: true, size: 15, color: COBALT, characterSpacing: 3 }),
      new TextRun({ text: " ".repeat(6), size: 15 }),
    ],
  });
}

function metaCell(label, value, widthPct, opts = {}) {
  return noBorderCell(
    [
      new Paragraph({
        border: opts.bottomRule ? { bottom: { color: COBALT, space: 6, style: BorderStyle.SINGLE, size: 16 } } : undefined,
        children: [
          new TextRun({ text: label + "  ", allCaps: true, font: F_LABEL, bold: true, size: 13, color: "8FA8D9", characterSpacing: 2 }),
          new TextRun({ text: value, font: F_BODY, size: 16, color: WHITE }),
        ],
      }),
    ],
    widthPct,
    { fill: BLACK }
  );
}

function pageBreakPara() {
  const { PageBreak } = require("docx");
  return new Paragraph({ children: [new PageBreak()] });
}

// ---- header/footer ----
function makeHeaderFinal() {
  const logoBuf = img("valletta-soc-lockup.png");
  const metaRow = new TableRow({
    children: [
      metaCell("Policy Level", "Companywide", 25, { bottomRule: true }),
      metaCell("Policy Number", "Valletta Industries - A", 30, { bottomRule: true }),
      metaCell("Version No.", "1.0", 20, { bottomRule: true }),
      metaCell("Approved By", "CEO", 25, { bottomRule: true }),
    ],
  });
  const metaTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [metaRow],
  });
  return new Header({
    children: [
      new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
        spacing: { after: 80 },
        children: [
          new ImageRun({ type: "png", data: logoBuf, transformation: { width: 63, height: 48 } }),
          new TextRun({ text: "\t" }),
          new TextRun({ text: DOC_TAG, allCaps: true, font: F_LABEL, bold: true, size: 14, color: STEEL, characterSpacing: 6 }),
        ],
      }),
      metaTable,
    ],
  });
}

function makeFooter() {
  return new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 60 },
        children: [
          new TextRun({ text: "VALLETTA INDUSTRIES PROPRIETARY & CONFIDENTIAL INFORMATION", font: F_LABEL, bold: true, size: 12, color: STEEL, characterSpacing: 2 }),
        ],
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: `${DOC_TAG}  –  Page `, font: F_BODY, size: 15, color: STEEL }),
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

// ============================================================
// CONTENT
// ============================================================
const content = [];

content.push(
  new Paragraph({ spacing: { before: 200, after: 40 }, children: [new TextRun({ text: "USE OF FORCE POLICY AND PROCEDURE", font: F_HEAD, bold: true, size: 40, color: BLACK })] }),
  new Paragraph({ border: { bottom: { color: COBALT, space: 4, style: BorderStyle.SINGLE, size: 18 } }, spacing: { after: 260 }, children: [new TextRun({ text: "", size: 2 })] })
);

content.push(new Paragraph({ spacing: { before: 100, after: 140 }, children: [new TextRun({ text: "Table of Contents", allCaps: true, font: F_LABEL, bold: true, size: 19, color: BLACK, characterSpacing: 3 })] }));
content.push(
  new TableOfContents("Table of Contents", {
    hyperlink: true,
    headingStyleRange: "1-2",
  })
);
content.push(pageBreakPara());

// ---- 1.0 Purpose ----
content.push(sectionHeading("1.0", "Purpose"));
content.push(bodyPara(
  "The purpose of this Policy is to establish governing standards for the use of force by Valletta Industries (“Company”) personnel. This Policy sets forth the principles under which less than lethal force and deadly force may be used in the performance of assigned duties, consistent with applicable Federal, state, and local law."
));

// ---- 2.0 Scope ----
content.push(sectionHeading("2.0", "Scope"));
content.push(bodyPara(
  "This Policy applies to all sworn and non-sworn Valletta Industries security personnel engaged in security operations on behalf of the Company. Use of force decisions and actions must comply with all applicable Federal, state, and local laws, regulations, and contract requirements governing less than lethal force and deadly force."
));

// ---- 3.0 Terms and Definitions ----
content.push(sectionHeading("3.0", "Terms and Definitions"));
content.push(termPara("Use of Force", "an immediate means of overcoming resistance and controlling the threat of imminent harm to self or others."));
content.push(termPara("Deadly Force", "A degree of force that a reasonable and prudent person would consider likely to cause death or serious bodily harm."));
content.push(termPara("Less Than Lethal Force", "Any use of force other than that which is considered deadly force that involves physical effort to control, restrain, or overcome the resistance of another."));
content.push(termPara("Objectively Reasonable", "The determination that the necessity for using force and the level of force used is based upon the officer’s evaluation of the situation considering the totality of the circumstances known to the officer at the time the force is used and upon what a reasonably prudent security officer would use under the same or similar situations."));
content.push(termPara("Seriously Bodily Injury", "Injury that involves a substantial risk of death, protracted and obvious disfigurement, or extended loss or impairment of the function of a body part or organ."));
content.push(termPara("Excessive Force", "Refers to a situation where an officer uses more force than is reasonably necessary under the circumstances as outlined by the U.S. Supreme Court to return a situation to normal."));
content.push(termPara("De-escalation", "Taking action(s) or communicating verbally or non-verbally during a potential force encounter in an attempt to stabilize a situation and reduce the immediacy of a threat so that more time, options, and resources can be called upon to assist in resolving a situation without having to use force or the least amount of force necessary. De-escalation may include the use of such techniques as command presence, advisements, warnings, verbal persuasion, and tactical repositioning."));
content.push(termPara("Exigent Circumstances", "Those circumstances that would cause a reasonable and prudent person to believe that a particular action is necessary to prevent physical harm to an individual, the destruction of relevant evidence, the escape of a suspect, or some other consequence frustrating legitimate law enforcement efforts."));

content.push(new Paragraph({ spacing: { before: 120, after: 20 }, children: [new TextRun({ text: "Levels of Force:", font: F_BODY, bold: true, size: 20, color: BLACK })] }));
content.push(new Paragraph({ spacing: { after: 90 }, children: [new TextRun({ text: "Levels of Force Include but are not limited to:", font: F_BODY, size: 20, color: CHARCOAL })] }));
content.push(plainBulletPara("Officer Presence: No force is used.", "square-bullets"));
content.push(plainBulletPara("Verbalization: Force is not physical.", "square-bullets"));
content.push(plainBulletPara("Empty-Hand Control: Officers use bodily force to gain control of a situation.", "square-bullets"));
content.push(plainBulletPara("Less-Lethal Methods: Officers use less-lethal technologies to gain control.", "square-bullets"));
content.push(plainBulletPara("Lethal Force: Officers use lethal weapons to gain control", "square-bullets"));

// ---- 4.0 Roles and Responsibilities ----
content.push(sectionHeading("4.0", "Roles and Responsibilities"));
content.push(labelBulletPara("Security Officer", "Reports any use of force promptly and cooperates in investigations.", "square-bullets"));
content.push(labelBulletPara("Immediate Supervisor", "Reviews reports and escalates incidents to the Contract Manager.", "square-bullets"));
content.push(labelBulletPara("Contract Manager", "Ensures timely reporting to leadership, manages documentation, and secures officers' credentials if needed.", "square-bullets"));
content.push(labelBulletPara("Director of Operations", "Coordinates investigations, and ensures cooperation with authorities.", "square-bullets"));
content.push(labelBulletPara("Director of Compliance", "Oversees compliance and document control.", "square-bullets"));
content.push(labelBulletPara("Investigative Personnel & Law Enforcement", "Conduct investigations, gather evidence, and assess legal outcomes.", "square-bullets"));
content.push(labelBulletPara("Valletta Industries Management Team", "Maintains oversight, ensures transparency, and enforces policy adherence.", "square-bullets"));

// ---- 5.0 Guidelines ----
content.push(sectionHeading("5.0", "Guidelines"));
content.push(plainBulletPara("Individuals It is the policy of Valletta Industries to value and preserve human life. Security Officers are authorized by applicable law to use force, up to and including deadly force, when necessary to preserve the life of themselves or others.", "arrow-bullets"));
content.push(plainBulletPara("Security Officers shall use only the necessary level of force that is objectively reasonable to effectively bring an incident under control while protecting the safety of the security officer and others.", "arrow-bullets"));
content.push(plainBulletPara("Security Officers shall use force only when no reasonably effective alternative appears to exist and shall use only the level of force that a reasonably prudent security officer would use under the same or similar circumstances.", "arrow-bullets"));
content.push(plainBulletPara("No two situations are the same, nor are any two security officers. In a potentially threatening situation, an officer will quickly tailor a response and apply a level of force that is necessary to restore order.", "arrow-bullets"));
content.push(plainBulletPara("Situational awareness is essential, and security officers are trained to judge when a crisis requires the use of force to regain control of a situation. In most cases, time becomes the key variable in determining when a security officer chooses to use force.", "arrow-bullets"));
content.push(plainBulletPara("The decision to use any level of force requires careful attention to the facts and circumstances of each particular case, including the severity of the crime at issue and whether the suspect poses an immediate threat to the safety of the officer or others.", "arrow-bullets"));
content.push(plainBulletPara("The level of force a security officer uses varies based on the situation; thus, guidelines for the use of force are based on many factors, such as local law, and the security officer’s level of training or experience.", "arrow-bullets"));
content.push(plainBulletPara("The goal of any use of force application is to regain control of a situation as quickly as possible, using the least amount of force, while protecting the community. Use of force is a security officer’s last option — a necessary course of action to restore safety in a community when other practices are ineffective.", "arrow-bullets"));

// ---- 6.0 Procedures ----
content.push(sectionHeading("6.0", "Procedures"));

content.push(subHeading("6.1", "General Provisions"));
content.push(romanPara("Use of physical force should be discontinued when resistance ceases or when the incident is under control."));
content.push(romanPara("Physical force shall not be used against individuals in restraints, except as objectively reasonable to prevent their escape or prevent imminent bodily injury to the individual, the security officer, or another person. In these situations, only the minimal amount of force necessary to control the situation shall be used."));
content.push(romanPara("Once the scene is safe and as soon as practical, a security officer shall provide appropriate medical care consistent with his or her training to any individual who has visible injuries, complains of being injured, or requests medical attention. This may include providing first aid, requesting emergency medical services, and/or arranging for transportation to an emergency medical facility."));
content.push(romanPara("An officer has a duty to intervene to prevent or stop the use of excessive force by another officer when it is safe and reasonable to do so. All actions must be reported to a supervisor without delay."));
content.push(romanPara("All uses of force shall be reported without delay, documented and investigated pursuant to our policies."));

content.push(subHeading("6.2", "De-Escalation"));
content.push(romanPara("An officer shall use de-escalation techniques and other alternatives consistent with his or her training whenever possible and appropriate before resorting to use of force and to reduce the need for force.", "roman-list-2"));
content.push(romanPara("Whenever possible and when such delay will not compromise the safety of the officer or another and will not result in the destruction of evidence, escape of a suspect, or commission of a crime, an officer shall allow an individual time and opportunity to submit to verbal commands before force is used.", "roman-list-2"));

content.push(subHeading("6.3", "Use of Less Than Lethal Force"));
content.push(bodyPara("When de-escalation techniques are not effective or appropriate, a security officer may consider the use of less than lethal force to control a non-compliant or actively resistant individual. A trained and qualified security officer is authorized to use agency-approved, less-lethal force techniques and issued equipment to protect the officer or others from immediate physical harm, to restrain or subdue an individual who is actively resisting or evading a legitimate arrest, or to bring an unlawful situation safely and effectively under control"));

content.push(subHeading("6.4", "Medical Attention"));
content.push(bodyPara("Anytime force is used against an individual, or a subject is injured, or a subject complains of an injury as a result of a security officer’s use of force, the officer will provide medical assistance within his training and abilities for the subject as soon as the immediate threat/danger to the officer has passed. The officer will immediately summon additional emergency medical response as required. Control will be maintained over the subject both pending and during emergency medical treatment. The safety and security of medical response personnel, security personnel, and bystanders must be ensured.  All actions taken in rendering medical aid to a subject must be documented and reported to a supervisor without delay."));

content.push(subHeading("6.5", "Crime Scene Prevention"));
content.push(bodyPara("In the case of the use of deadly force by a security officer, the location will be treated as a crime scene with all provisions for the preservation of evidence, identification of witnesses, and other safeguards implemented."));

content.push(subHeading("6.6", "Use of Deadly Force"));
content.push(bodyPara("In accordance with applicable local law, a security officer is authorized to use deadly force when it is objectively reasonable under the totality of the circumstances. Use of deadly force is justified when one or both of the following apply:"));
content.push(romanPara("to protect the security officer or others from what is reasonably believed to be an immediate threat of death or serious bodily injury", "roman-list-3"));
content.push(romanPara("to prevent the escape of a fleeing subject when the security officer has probable cause to believe that the person has committed or intends to commit a felony involving serious bodily injury or death, and the security officer reasonably believes that there is an imminent and immediate risk of serious bodily injury or death to the security officer or another if the subject is not immediately apprehended.", "roman-list-3"));
content.push(bodyPara("Where feasible, the security officer shall identify himself or herself and warn of his or her intent to use deadly force."));

content.push(subHeading("6.7", "Deadly Force Restrictions"));
content.push(romanPara("The unreasonable use of force (i.e., the use of force in excess of the degree required to overcome resistance) is considered serious misconduct. Such misconduct may result in administrative, civil, and/or criminal action against the perpetrator.", "roman-list-4"));
content.push(romanPara("Verbal abuse, verbal threats of violence, or non-physical threats cannot, by themselves, be the basis under any circumstances for the use of force.", "roman-list-4"));
content.push(romanPara("Deadly force shall not be used against persons whose actions are a threat only to themselves or property.", "roman-list-4"));
content.push(romanPara("Firearms will not be discharged at escaping detainees who do not present an immediate and serious danger that will likely result in serious bodily harm or death to the officer or another, regardless of pending charges.", "roman-list-4"));
content.push(romanPara("Firearms will not be discharged while seeking to apprehend persons violating laws that amount to misdemeanors or non-violent felons.", "roman-list-4"));
content.push(romanPara("Firearms will not be fired when the officer could reasonably foresee that the safety of innocent persons would be endangered by the discharge of such weapon.", "roman-list-4"));
content.push(romanPara("Firearms will not be fired into or over crowds.", "roman-list-4"));
content.push(romanPara("Warning shots are prohibited.", "roman-list-4"));
content.push(romanPara("Choke holds are prohibited.", "roman-list-4"));
content.push(romanPara("Firearms shall not be discharged at a moving vehicle unless:", "roman-list-4"));
content.push(plainBulletPara("a person in the vehicle is threatening the security officer or another person with deadly force by means other than the vehicle; or", "circle-bullets-nested", 0));
content.push(plainBulletPara("the vehicle is operated in a manner deliberately intended to strike a security officer or another person, and all other reasonable means of defense have been exhausted (or are not present or practical), which includes moving out of the path of the vehicle.", "circle-bullets-nested", 0));

// ---- 7.0 Administration ----
content.push(sectionHeading("7.0", "Administration"));

content.push(subHeading("7.1", "Reporting Procedures, Use of Force"));
content.push(decimalPara("Any officer that uses deadly or non-deadly physical force will report the use of force as expeditiously as possible to his/her immediate supervisor."));
content.push(decimalPara("The immediate supervisor will report the use of force to the Contract Manager as expeditiously as possible, with as many details supplied as are available."));
content.push(decimalPara("The Contract Manager will personally contact the Director of Operations or the SVP of Operations and Administration as expeditiously as possible, with as many details as are available. In no case will a use of force incident not be reported within 4 hours of occurrence."));
content.push(decimalPara("A report of investigation will be completed as soon as possible after the event and submitted to the appropriate Leaders in the chain of command."));

content.push(subHeading("7.2", "Deadly Force Investigations"));
content.push(bodyPara("A security officer involved in a deadly use of force situation is at high risk for both physical and mental injury.  The officer will be provided immediate medical attention, to include hospitalization if needed.  In the event of hospitalization, a supervisor will be assigned to accompany the officer to the hospital, secure the officer’s property and weapon, and remain with the officer until properly relieved."));
content.push(bodyPara("A security officer involved in a deadly use of force situation shall be promptly placed on administrative leave pending an investigation of the incident."));
content.push(bodyPara("A deadly use of force situation is considered a crime scene and all steps to preserve evidence will be taken.  As with any crime scene, security personnel will not hinder law enforcement from conducting their investigation."));
content.push(bodyPara("The involved security officers’ handguns will be treated as evidence with appropriate safeguards."));
content.push(bodyPara("The involved security officers’ official licenses, registrations, and identifications will be held by the Contract Manager pending investigation."));
content.push(bodyPara("Typically, the use of deadly force by an officer will be investigated by Federal/State/local law enforcement authorities, Investigative personnel, and members of the Valletta Industries management team. All Valletta Industries personnel will cooperate fully with each of these investigations."));

// ---- 8.0-10.0 ----
content.push(sectionHeading("8.0", "Policy Supersedes"));
content.push(bodyPara("This policy and procedure supersedes all previously dated policies, or parts of policies, dealing with the use of deadly and non-deadly force. This policy is to be reviewed annually, and any questions or concerns should be addressed to the immediate supervisor for clarification."));

content.push(sectionHeading("9.0", "Deviation"));
content.push(bodyPara("This policy and procedure may be updated as needed to maintain compliance with contractual requirements, and overall business operations. No part of this document should be interpreted as compensation-related, and all content remains the proprietary property of the company."));

content.push(sectionHeading("10.0", "Safety and Compliance"));
content.push(bodyPara("To ensure efficient business operations and maintain compliance with federal contract requirements, all processes and procedures must be clearly documented and consistently tracked. Valletta Industries Security is committed to providing up-to-date policy and procedural guidance that aligns with all applicable state and federal laws."));

content.push(new Paragraph({ spacing: { before: 160, after: 80 }, children: [new TextRun({ text: "References:", font: F_BODY, bold: true, size: 20, color: BLACK })] }));
content.push(bodyPara("National Consensus Policy on the Use of Force, International Association Chiefs of Police January 2017"));
content.push(bodyPara("Overview of Police Use of Force, National Institutes of Justice March 5, 2020"));

content.push(pageBreakPara());

// ---- Policy Acknowledgement ----
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 100, after: 140 },
  border: { bottom: { color: COBALT, space: 4, style: BorderStyle.SINGLE, size: 12 } },
  children: [new TextRun({ text: "POLICY ACKNOWLEDGEMENT", font: F_HEAD, bold: true, size: 25, color: BLACK })],
}));
content.push(bodyPara(
  "I acknowledge that I have received and reviewed the Valletta Industries Use of Force Policy and Procedure. I understand that I am responsible for complying with the requirements of this policy and for seeking clarification from my supervisor or the appropriate Company representative if I have questions regarding its requirements.",
  { after: 200 }
));
content.push(fieldRow("Printed Name"));
content.push(fieldRow("Signature"));
content.push(fieldRow("Date"));

content.push(new Paragraph({ spacing: { before: 260, after: 120 }, children: [new TextRun({ text: "Reviews and Edits", font: F_LABEL, bold: true, size: 19, color: BLACK })] }));

function reviewHeaderCell(text, widthPct) {
  return new TableCell({
    width: { size: widthPct, type: WidthType.PERCENTAGE },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 90, bottom: 90, left: 100, right: 100 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
      left: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
      right: { style: BorderStyle.SINGLE, size: 2, color: BLACK },
    },
    children: [new Paragraph({ children: [new TextRun({ text, allCaps: true, font: F_LABEL, bold: true, size: 15, color: WHITE, characterSpacing: 2 })] })],
  });
}
function reviewBodyCell(text, widthPct) {
  return new TableCell({
    width: { size: widthPct, type: WidthType.PERCENTAGE },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      left: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
      right: { style: BorderStyle.SINGLE, size: 2, color: LINE_GRAY },
    },
    children: [new Paragraph({ children: [new TextRun({ text, font: F_BODY, size: 18, color: CHARCOAL })] })],
  });
}

content.push(new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  rows: [
    new TableRow({ tableHeader: true, children: [
      reviewHeaderCell("Date", 15),
      reviewHeaderCell("Requested Edit", 35),
      reviewHeaderCell("Author", 35),
      reviewHeaderCell("Date", 15),
    ] }),
    new TableRow({ children: [
      reviewBodyCell("August 17, 2026", 15),
      reviewBodyCell("Initial Policy", 35),
      reviewBodyCell("Jose Perou – Human Resources Director", 35),
      reviewBodyCell("August 17, 2026", 15),
    ] }),
  ],
}));

// ============================================================
// DOCUMENT
// ============================================================
const doc = new Document({
  numbering: {
    config: [
      {
        reference: "square-bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "■", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 220 } }, run: { color: COBALT, font: F_BODY, size: 16 } } }],
      },
      {
        reference: "arrow-bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "➤", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 220 } }, run: { color: COBALT, font: F_BODY, size: 16 } } }],
      },
      {
        reference: "circle-bullets-nested",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "○", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 220 } }, run: { color: STEEL, font: F_BODY, size: 16 } } }],
      },
      {
        reference: "roman-list",
        levels: [{ level: 0, format: LevelFormat.LOWER_ROMAN, text: "%1)", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 300 } }, run: { color: COBALT, bold: true, font: F_BODY, size: 20 } } }],
      },
      {
        reference: "roman-list-2",
        levels: [{ level: 0, format: LevelFormat.LOWER_ROMAN, text: "%1)", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 300 } }, run: { color: COBALT, bold: true, font: F_BODY, size: 20 } } }],
      },
      {
        reference: "roman-list-3",
        levels: [{ level: 0, format: LevelFormat.LOWER_ROMAN, text: "%1)", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 300 } }, run: { color: COBALT, bold: true, font: F_BODY, size: 20 } } }],
      },
      {
        reference: "roman-list-4",
        levels: [{ level: 0, format: LevelFormat.LOWER_ROMAN, text: "%1)", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 300 } }, run: { color: COBALT, bold: true, font: F_BODY, size: 20 } } }],
      },
      {
        reference: "decimal-list",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 360, hanging: 300 } }, run: { color: COBALT, bold: true, font: F_BODY, size: 20 } } }],
      },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: PAGE_H },
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN, header: HEADER_DISTANCE, footer: HEADER_DISTANCE },
      },
      titlePage: true,
    },
    headers: { default: makeHeaderFinal(), first: emptyHeader },
    footers: { default: makeFooter(), first: emptyFooter },
    children: content,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(HERE, "valletta_use_of_force_policy.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
