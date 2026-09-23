const {
  docTitle, sectionHeading, subHeading, fieldRow, fieldPairRow, fieldTripleRow,
  checkboxItem, tintedBox, blankNoteBox, sigRow, bodyPara, buildDocument, writeDoc,
  Paragraph, TextRun, F_BODY, RED, Dt, Dd, YES_NO, yearsOptions,
} = require("./shared");

const DOC_TAG = "Site Manager Candidate Qualifications";
const content = [];

content.push(...docTitle(
  "Site Manager Candidate Qualifications",
  "Contractor Certification of Site Management Candidate Qualifications"
));

content.push(fieldRow("Candidate Name"));
content.push(fieldRow("Location"));

content.push(subHeading("In Accordance with D.18, CIFSO Site Managers Must Possess the Following Criteria"));
content.push(checkboxItem("C.I.F.S.O Experience: One + Year of Service"));
content.push(fieldPairRow(Dd("Years", yearsOptions()), "Months"));
content.push(checkboxItem("Physical Security Experience"));
content.push(checkboxItem("Leadership Ability"));
content.push(checkboxItem("Integrity and Maturity"));
content.push(checkboxItem("Ability to Deal with Subordinates and Managers"));
content.push(checkboxItem("Planning and Ability to Implement Projects"));
content.push(checkboxItem("Basic Typing and Computer Skills"));
content.push(checkboxItem("Working Knowledge of All Procedures, Policies, and Regulations Related to Their Respective Site"));

content.push(sectionHeading("Required Certifications – FEMA Certifications (or Government Approved Equivalent)"));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.100.c Introduction to the Incident Command System", YES_NO), Dt("Date of Completion")));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.200.c Basic Incident Command System for Initial Response", YES_NO), Dt("Date of Completion")));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.700.b Introduction to the National Incident Management System", YES_NO), Dt("Date of Completion")));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.800.d National Response Framework, an Introduction", YES_NO), Dt("Date of Completion")));

content.push(sectionHeading("Current Sustainment Certification"));
content.push(fieldRow(Dt("Date")));

content.push(sectionHeading("Current Range Certification"));
content.push(fieldRow(Dt("Date")));
content.push(fieldPairRow("Pistol Score", "Rifle Score"));

content.push(sectionHeading("Current Physical Fitness Assessment"));
content.push(fieldRow(Dt("Date")));
content.push(fieldTripleRow("Push-Ups", "Sit-Ups", "300-Meter Sprint"));
content.push(fieldRow("165 Lb. Victim Drag"));

content.push(subHeading("Signatures"));
content.push(new Paragraph({
  spacing: { after: 140, line: 270 },
  children: [
    new TextRun({ text: "The Contractor Certifies the above-named Site Manager Candidate meets or exceeds all qualifications and certifications as enumerated in the Statement of Work. We request approval for ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "_______________________", font: F_BODY, size: 20, color: RED }),
    new TextRun({ text: " to be appointed CIFSO ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "_________", font: F_BODY, size: 20, color: RED }),
    new TextRun({ text: " Site Manager on ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "____________", font: F_BODY, size: 20, color: RED }),
  ],
}));

content.push(sigRow("NPM Signature"));
content.push(fieldRow("Email"));
content.push(sigRow("NQCM Signature"));
content.push(fieldRow("Email"));

const doc = buildDocument(DOC_TAG, content);
writeDoc(doc, "valletta_site_manager_candidate_qualifications.docx");
