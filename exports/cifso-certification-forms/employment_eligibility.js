const {
  docTitle, sectionHeading, subHeading, fieldRow, fieldPairRow, fieldTripleRow,
  checkboxItem, tintedBox, blankNoteBox, sigRow, bodyPara, buildDocument, writeDoc,
  Paragraph, TextRun, F_BODY, COBALT, Dt, Dd, YES_NO,
} = require("./shared");

const DOC_TAG = "New Hire Employment Eligibility";
const content = [];

const BRANCHES = ["Army", "Navy", "Air Force", "Marine Corps", "Coast Guard", "Space Force", "N/A"];
const SERVICE_TYPES = ["Active Duty", "Reserve", "National Guard", "N/A"];
const TERMINATION_TYPES = ["Voluntary – In Good Standing", "Voluntary – Not in Good Standing", "Involuntary – For Cause", "Involuntary – Reduction in Force", "N/A"];

content.push(...docTitle(
  "New Hire Employment Eligibility",
  "Contractor Certification – Paragon Systems New Hire Employment Eligibility"
));

content.push(fieldRow("Location"));
content.push(fieldRow("Candidate Name"));
content.push(fieldPairRow("Age", Dd("Gender", ["Male", "Female"])));

content.push(sectionHeading("Qualifying Experience"));
content.push(checkboxItem("Military"));
content.push(fieldPairRow(Dd("Branch", BRANCHES), Dd("Type of Service (DD214 member copy 4)", SERVICE_TYPES)));
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
content.push(fieldPairRow(Dt("Date of Hire"), Dt("Date of Termination")));
content.push(fieldRow(Dd("Type of Termination", TERMINATION_TYPES)));
content.push(fieldRow("Approved by MST"));

content.push(sectionHeading("Medical Evaluation (Completed by NQCM or Designee)"));
content.push(fieldRow("Vision – Binocular vision correctable to 20/20 (Snellen)"));
content.push(fieldRow("Colorblind"));
content.push(fieldRow("Hearing – Normal speech range with a loss of up to 30 decibels in both ears or 35 decibels in the poorer ear"));
content.push(fieldRow("Fully Capable of Performing Duties Which Require Moderate to Arduous Physical Exertion"));
content.push(fieldRow("No Neurological or Psychological Condition That Adversely Affects the Candidate's Ability to Safely and Efficiently Perform During Situations That Adversely Affect Mental Stress"));

content.push(sectionHeading("Employment Requirements"));
content.push(fieldRow(Dd("Prior ASPR Employee", YES_NO)));
content.push(fieldRow(Dd("Currently Providing Services to ASPR as Vendor/Contractor", YES_NO)));
content.push(fieldRow(Dd("Immediate Family Member of Current ASPR Employee", YES_NO)));
content.push(fieldRow(Dd("Possess Sufficient English Language Proficiency", YES_NO)));
content.push(fieldRow(Dd("Possess Valid State Issued Driver's License", YES_NO)));
content.push(fieldPairRow(Dd("Possess a Public Trust Level 4 (High Risk) Suitability Determination", YES_NO), Dt("Date Verified")));
content.push(fieldPairRow(Dd("Possesses Valid State Issued Armed License", YES_NO), Dt("Expiration Date")));
content.push(fieldPairRow(Dd("Possesses Valid State Issued Guard Card", YES_NO), Dt("Expiration Date")));

content.push(sectionHeading("Appearance Standard"));
content.push(fieldRow(Dd("Male – Hair Style Meets/Exceeds SOW Standard", YES_NO)));
content.push(fieldRow(Dd("Female – Hair Style Meets/Exceeds SOW Standard", YES_NO)));
content.push(fieldRow(Dd("Facial Hair Meets/Exceeds SOW Standard", YES_NO)));
content.push(fieldRow(Dd("Body Art and Piercings Meets/Exceeds SOW Standard", YES_NO)));
content.push(fieldRow(Dd("Cosmetic Metallic Dental Ornaments Meets/Exceeds SOW Standard", YES_NO)));
content.push(fieldRow(Dd("Jewelry Meets/Exceeds SOW Standard", YES_NO)));

content.push(sectionHeading("Training Certifications – Basic New Hire Course"));
content.push(fieldPairRow(Dt("Date Began"), Dt("Date Ended")));
content.push(fieldPairRow("Total Training Hours", "Certified By"));

content.push(sectionHeading("Physical Fitness Assessment"));
content.push(checkboxItem("For Record"));
content.push(fieldPairRow(Dt("Date"), "Certified By"));
content.push(fieldRow("Performance Location"));
content.push(fieldTripleRow("Push-Ups", "Sit-Ups", "300-Meter Sprint (seconds)"));
content.push(fieldRow("165 Lb. Victim Drag x 25 Meters"));

content.push(sectionHeading("New Hire On-the-Job Training"));
content.push(fieldPairRow(Dt("Date Started"), Dt("Date Ended")));
content.push(fieldRow("Total Hours"));
content.push(fieldRow(Dd("Topics Covered Include Those Enumerated in SOW D.28", YES_NO)));
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
content.push(fieldPairRow("Certifying Site Manager", Dt("Date")));

content.push(subHeading("Contractor Certification of Employee Eligibility"));
content.push(new Paragraph({
  spacing: { after: 140, line: 270 },
  children: [
    new TextRun({ text: "The Contractor Certifies that the above-named New Hire Candidate meets or exceeds all conditions of employment as enumerated in the Statement of Work. We request approval for (type) ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "_______________________", font: F_BODY, size: 20, color: COBALT }),
    new TextRun({ text: " to be placed into the working schedule as a fully certified CIFSO on ", font: F_BODY, size: 20, color: "26282B" }),
    new TextRun({ text: "____________", font: F_BODY, size: 20, color: COBALT }),
  ],
}));

content.push(sigRow("Site Manager Signature"));
content.push(fieldRow(Dt("Date")));
content.push(sigRow("Site Trainer Signature"));
content.push(fieldRow(Dt("Date")));
content.push(sigRow("NPM"));
content.push(fieldRow(Dt("Date")));
content.push(sigRow("NQCM"));
content.push(fieldRow(Dt("Date")));

const doc = buildDocument(DOC_TAG, content);
writeDoc(doc, "valletta_new_hire_employment_eligibility.docx");
