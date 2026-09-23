const {
  docTitle, sectionHeading, subHeading, fieldRow, fieldPairRow, fieldTripleRow,
  checkboxItem, tintedBox, blankNoteBox, sigRow, bodyPara, buildDocument, writeDoc,
  Paragraph, TextRun, F_BODY, RED,
} = require("./shared");

const DOC_TAG = "Site Trainer Candidate Qualifications";
const content = [];

content.push(...docTitle(
  "Site Trainer Candidate Qualifications",
  "Contractor Certification of Site Trainer Candidate Qualifications"
));

content.push(fieldRow("Candidate Name"));
content.push(fieldRow("Location"));

content.push(subHeading("In Accordance with D.21, CIFSO Site Trainer Candidates Must Possess the Following Criteria (One of LE or Security)"));
content.push(checkboxItem("C.I.F.S.O Experience: One + Year of Service"));
content.push(fieldPairRow("Years", "Months"));
content.push(checkboxItem("Operational Experience – Law Enforcement"));
content.push(fieldRow("Years of Experience"));
content.push(checkboxItem("Operational Experience – Security"));
content.push(fieldRow("Years of Experience"));
content.push(checkboxItem("Working Knowledge of Physical Security"));

content.push(sectionHeading("Required Certifications – FEMA Certifications"));
content.push(fieldRow("FEMA ICS-100 – Date of Completion"));
content.push(fieldRow("FEMA ICS-200 – Date of Completion"));
content.push(fieldRow("FEMA IS-700 – Date of Completion"));
content.push(fieldRow("FEMA IS-800 – Date of Completion"));

content.push(subHeading("NRA LE Tactical Shooting Firearms Instructor School or Similar Approved by the COR"));
content.push(checkboxItem("Candidate Is Certified as a LE Firearms Instructor"));
content.push(fieldRow("School/Agency"));
content.push(fieldPairRow("Date of Completion", "Pending Date of Completion"));
content.push(fieldRow("Certification Expiration Date"));
content.push(checkboxItem("Candidate Is Certified as a LE Tactical Firearms Instructor"));
content.push(fieldRow("School/Agency"));
content.push(fieldPairRow("Date of Completion", "Pending Date of Completion"));
content.push(fieldRow("Certification Expiration Date"));

content.push(sectionHeading("Additional Training and Certifications"));
content.push(subHeading("Tactical Medical Instructor Course"));
content.push(fieldRow("School/Agency Name"));
content.push(fieldPairRow("Date of Completion", "Course Date"));
content.push(checkboxItem("To Be Determined"));

content.push(subHeading("Armorer School – Pistol"));
content.push(fieldRow("School/Agency Name"));
content.push(fieldPairRow("Date of Completion", "Anticipated Course Date"));

content.push(subHeading("Armorer School – Rifle"));
content.push(fieldRow("School/Agency Name"));
content.push(fieldPairRow("Date of Completion", "Anticipated Course Date"));

content.push(subHeading("Annual Physical Fitness Test"));
content.push(fieldPairRow("Date Successfully Completed", "Location"));
content.push(fieldRow("Certified By"));

content.push(subHeading("Annual Firearms Qualification – Pistol/Rifle"));
content.push(fieldPairRow("Date Qualified", "Location"));
content.push(fieldRow("Certified By"));

content.push(...tintedBox(["Certifications available upon request."]));

content.push(sectionHeading("On-the-Job Training"));
for (let i = 1; i <= 7; i++) {
  content.push(subHeading(i === 7 ? "Week #7: National Training Manager Review for Basic New Hire" : `Week #${i}`));
  content.push(fieldRow("Location"));
  content.push(fieldPairRow("Start Date", "End Date"));
  content.push(fieldRow("CST Conducting Training"));
}

content.push(subHeading("Contractor Certifications"));
content.push(new Paragraph({
  spacing: { after: 100, line: 270 },
  children: [
    new TextRun({ text: "The contractor certifies the above-named candidate meets or exceeds all SOW required conditions enumerated in Section D – Contract Documents, Exhibits or Attachments; D.21. The contractor requests that ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "_______________________", font: F_BODY, size: 20, color: RED }),
    new TextRun({ text: " be approved as a qualified CIFSO Site Trainer effective ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "____________", font: F_BODY, size: 20, color: RED }),
  ],
}));
content.push(bodyPara("The contractor certifies that all certifications are located in the personnel file of the candidate at their respective site."));

content.push(subHeading("Electronic Signature Section"));
content.push(sigRow("NTM Signature"));
content.push(sigRow("Email"));
content.push(sigRow("NPM Signature"));
content.push(sigRow("Email"));
content.push(sigRow("NQCM Signature"));
content.push(sigRow("Email"));

content.push(subHeading("National Training Manager Notes"));
content.push(...blankNoteBox(6));

content.push(subHeading("Candidate Biography"));
content.push(...blankNoteBox(6));

const doc = buildDocument(DOC_TAG, content);
writeDoc(doc, "valletta_site_trainer_candidate_qualifications.docx");
