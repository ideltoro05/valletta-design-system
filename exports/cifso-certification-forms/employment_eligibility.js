const {
  docTitle, sectionHeading, subHeading, fieldRow, fieldPairRow, fieldTripleRow,
  checkboxItem, tintedBox, blankNoteBox, sigRow, bodyPara, buildDocument, writeDoc,
  Paragraph, TextRun, F_BODY, RED,
} = require("./shared");

const DOC_TAG = "New Hire Employment Eligibility";
const content = [];

content.push(...docTitle(
  "New Hire Employment Eligibility",
  "Contractor Certification – Paragon Systems New Hire Employment Eligibility"
));

content.push(fieldRow("Location"));
content.push(fieldRow("Candidate Name"));
content.push(fieldPairRow("Age", "Gender"));

content.push(sectionHeading("Qualifying Experience"));
content.push(checkboxItem("Military"));
content.push(fieldPairRow("Branch", "Type of Service (DD214 member copy 4)"));
content.push(checkboxItem("Three Years Armed Security"));
content.push(checkboxItem("Satisfactory Service Verified"));
content.push(checkboxItem("Law Enforcement"));
content.push(checkboxItem("Post Certified"));
content.push(checkboxItem("Satisfactory Service Verified"));
content.push(checkboxItem("College Degree"));
content.push(fieldPairRow("Type of Degree", "Field"));

content.push(sectionHeading("Prior CIFSO Employment"));
content.push(fieldRow("Prior Employment on CIFSO Contract"));
content.push(fieldRow("Location"));
content.push(fieldPairRow("Date of Hire", "Date of Termination"));
content.push(fieldRow("Type of Termination"));
content.push(fieldRow("Approved by MST"));

content.push(sectionHeading("Medical Evaluation (Completed by NQCM or Designee)"));
content.push(fieldRow("Vision – Binocular vision correctable to 20/20 (Snellen)"));
content.push(fieldRow("Colorblind"));
content.push(fieldRow("Hearing – Normal speech range with a loss of up to 30 decibels in both ears or 35 decibels in the poorer ear"));
content.push(fieldRow("Fully Capable of Performing Duties Which Require Moderate to Arduous Physical Exertion"));
content.push(fieldRow("No Neurological or Psychological Condition That Adversely Affects the Candidate's Ability to Safely and Efficiently Perform During Situations That Adversely Affect Mental Stress"));

content.push(sectionHeading("Employment Requirements"));
content.push(fieldRow("Prior ASPR Employee"));
content.push(fieldRow("Currently Providing Services to ASPR as Vendor/Contractor"));
content.push(fieldRow("Immediate Family Member of Current ASPR Employee"));
content.push(fieldRow("Possess Sufficient English Language Proficiency"));
content.push(fieldRow("Possess Valid State Issued Driver's License"));
content.push(fieldPairRow("Possess a Public Trust Level 4 (High Risk) Suitability Determination", "Date Verified"));
content.push(fieldPairRow("Possesses Valid State Issued Armed License", "Expiration Date"));
content.push(fieldPairRow("Possesses Valid State Issued Guard Card", "Expiration Date"));

content.push(sectionHeading("Appearance Standard"));
content.push(fieldRow("Male – Hair Style Meets/Exceeds SOW Standard"));
content.push(fieldRow("Female – Hair Style Meets/Exceeds SOW Standard"));
content.push(fieldRow("Facial Hair Meets/Exceeds SOW Standard"));
content.push(fieldRow("Body Art and Piercings Meets/Exceeds SOW Standard"));
content.push(fieldRow("Cosmetic Metallic Dental Ornaments Meets/Exceeds SOW Standard"));
content.push(fieldRow("Jewelry Meets/Exceeds SOW Standard"));

content.push(sectionHeading("Training Certifications – Basic New Hire Course"));
content.push(fieldPairRow("Date Began", "Date Ended"));
content.push(fieldPairRow("Total Training Hours", "Certified By"));

content.push(sectionHeading("Physical Fitness Assessment"));
content.push(checkboxItem("For Record"));
content.push(fieldPairRow("Date", "Certified By"));
content.push(fieldRow("Performance Location"));
content.push(fieldTripleRow("Push-Ups", "Sit-Ups", "300-Meter Sprint (seconds)"));
content.push(fieldRow("165 Lb. Victim Drag x 25 Meters"));

content.push(sectionHeading("New Hire On-the-Job Training"));
content.push(fieldPairRow("Date Started", "Date Ended"));
content.push(fieldRow("Total Hours"));
content.push(fieldRow("Topics Covered Include Those Enumerated in SOW D.28"));
content.push(fieldPairRow("Provided By (Site Manager)", "Provided By (Site Trainer)"));

content.push(sectionHeading("Additional Training"));
content.push(fieldRow("FA/CPR/AED – Adult/Pediatric"));
content.push(fieldPairRow("Total Hours", "Certified By"));

content.push(sectionHeading("Required Uniforms, Equipment and Pistol/Rifle"));
content.push(checkboxItem("Uniforms Issued"));
content.push(checkboxItem("Duty Belt Issued"));
content.push(checkboxItem("Pistol/Rifle Issued"));
content.push(fieldRow("Issued By (Site Manager)"));

content.push(subHeading("Certifications: Training Records, Licensure and Documents"));
content.push(...tintedBox([
  "The Contractor Certifies In-Accordance-With SOW Section D.27 #8 & #9, that associated training records/licensure and documents for this employee are filed in the employee's personnel file at the above listed ASPR location and are available for SNSPS personnel auditing.",
]));
content.push(fieldPairRow("Certifying Site Manager", "Date"));

content.push(subHeading("Contractor Certification of Employee Eligibility"));
content.push(new Paragraph({
  spacing: { after: 140, line: 270 },
  children: [
    new TextRun({ text: "The Contractor Certifies that the above-named New Hire Candidate meets or exceeds all conditions of employment as enumerated in the Statement of Work. We request approval for (type) ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "_______________________", font: F_BODY, size: 20, color: RED }),
    new TextRun({ text: " to be placed into the working schedule as a fully certified CIFSO on ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "____________", font: F_BODY, size: 20, color: RED }),
  ],
}));

content.push(sigRow("Site Manager Signature"));
content.push(sigRow("Date"));
content.push(sigRow("Site Trainer Signature"));
content.push(sigRow("Date"));
content.push(sigRow("NPM"));
content.push(sigRow("Date"));
content.push(sigRow("NQCM"));
content.push(sigRow("Date"));

const doc = buildDocument(DOC_TAG, content);
writeDoc(doc, "valletta_new_hire_employment_eligibility.docx");
