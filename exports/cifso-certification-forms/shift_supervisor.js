const {
  docTitle, sectionHeading, subHeading, fieldRow, fieldPairRow, fieldTripleRow,
  checkboxItem, tintedBox, blankNoteBox, sigRow, bodyPara, buildDocument, writeDoc,
  Paragraph, TextRun, F_BODY, COBALT, Dt, Dd, YES_NO, yearsOptions,
} = require("./shared");

const DOC_TAG = "Shift Supervisor Candidate Qualifications";
const content = [];

content.push(...docTitle(
  "Shift Supervisor Candidate Qualifications",
  "Contractor Certification of CIFSO Shift Supervisor Candidate Qualifications"
));

content.push(fieldRow("Candidate Name"));
content.push(fieldRow("Location"));
content.push(fieldRow("Site Manager"));

content.push(subHeading("In Accordance with D.18, CIFSO Shift Supervisors Must Possess the Following Criteria"));
content.push(checkboxItem("C.I.F.S.O Experience: One + Year of Service"));
content.push(fieldPairRow(Dd("Years", yearsOptions()), "Months"));
content.push(checkboxItem("Physical Security Experience"));
content.push(fieldPairRow(Dd("Years", yearsOptions()), "Months"));
content.push(checkboxItem("Demonstrated Leadership Ability"));
content.push(checkboxItem("Demonstrated Integrity and Maturity"));
content.push(checkboxItem("Demonstrated Ability to Deal with Subordinates and Managers"));
content.push(checkboxItem("Demonstrated Planning and Ability to Implement Projects"));
content.push(checkboxItem("Demonstrated Basic Typing and Computer Skills"));
content.push(checkboxItem("Demonstrated Working Knowledge of All Procedures, Policies, and Regulations Related to Their Respective Site"));

content.push(sectionHeading("Required Certifications – FEMA Certifications"));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.100.c Introduction to the Incident Command System", YES_NO), Dt("Date of Completion")));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.200.c Basic Incident Command System for Initial Response", YES_NO), Dt("Date of Completion")));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.700.b An Introduction to the National Incident Management System", YES_NO), Dt("Date of Completion")));
content.push(fieldPairRow(Dd("TX Div. of Emergency Management G-IS.800.d National Response Framework, An Introduction", YES_NO), Dt("Date of Completion")));

content.push(sectionHeading("Compliance"));
content.push(subHeading("Annual Physical Fitness Test"));
content.push(fieldPairRow(Dt("Date Successfully Completed"), "Location"));
content.push(fieldTripleRow("Push-Ups", "Sit-Ups", "300-Meter Sprint (seconds)"));
content.push(fieldRow("Certified By"));

content.push(subHeading("Annual Firearms Qualification – Pistol/Rifle"));
content.push(fieldPairRow(Dt("Date Qualified"), "Location"));
content.push(fieldPairRow("Pistol Range Score", "Rifle Range Score"));
content.push(fieldRow("Certified By"));

content.push(subHeading("Candidate Biography"));
content.push(...blankNoteBox(6));

content.push(subHeading("Contractor Certification"));
content.push(new Paragraph({
  spacing: { after: 140, line: 270 },
  children: [
    new TextRun({ text: "The Contractor Certifies that the above-named Shift Supervisor Candidate meets or exceeds all qualifications and certifications as enumerated in the Statement of Work. Documents and certifications related to the above-named candidate are available for review upon request. The contractor requests approval for (print) ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "_______________________", font: F_BODY, size: 20, color: COBALT }),
    new TextRun({ text: " to be appointed CIFSO Shift Supervisor on ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "____________", font: F_BODY, size: 20, color: COBALT }),
  ],
}));

content.push(subHeading("Electronic Signature Section – Site Manager, National Program Manager, National QC Manager"));
content.push(sigRow("Site Manager Signature"));
content.push(fieldRow("Email"));
content.push(sigRow("NPM Signature"));
content.push(fieldRow("Email"));
content.push(sigRow("NQCM Signature"));
content.push(fieldRow("Email"));

const doc = buildDocument(DOC_TAG, content);
writeDoc(doc, "valletta_shift_supervisor_candidate_qualifications.docx");
