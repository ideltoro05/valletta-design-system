TITLE = "SITE VISIT ASSESSMENT"
SUBTITLE = "Operational Readiness, Contract Performance & Management Support Review"
DOC_TAG = "Management Support Team Site Visit Assessment"

VISIT_FIELDS = [
    ("SITE / LOCATION", "site_location", "Whiskey"),
    ("VISIT DATE(S)", "visit_dates", "15 September 2026"),
    ("MST MEMBER(S)", "mst_members", "Michael Flanagan"),
    ("MST ROLE(S)", "mst_roles", "NTM"),
    ("SITE MANAGER", "site_manager", "ST: Harry Zimmerman"),
]

PURPOSE_TEXT = (
    "This Management Support Team Site Visit Assessment provides leadership with a structured, "
    "evidence-based snapshot of site operations, personnel readiness, supervisory effectiveness, "
    "training, equipment, weapons accountability, emergency readiness, and support requirements. "
    "Findings are based on conditions observed, records sampled, and personnel engaged during the "
    "visit. The assessment identifies strengths, risks, trends, and areas requiring follow-up or "
    "higher-headquarters support. It does not replace a formal quality-control inspection."
)

ASSESSMENT_AREAS = "Staffing & Post Operations | Leadership & Supervision | Training & Readiness | Equipment & Weapons | Overall Performance"

# each section: (roman, title, [questions])
# each question: (num, text, rating_field, comments_field, options[], current_rating, current_comment)
SECTIONS = [
    ("I", "Staffing and Post Operations", [
        (1, "Were all contractually required posts staffed during the visit, and does review of recent records indicate the site is meeting the 99.5% post-coverage standard?",
         "s1_q1_rating", "s1_q1_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Not Inspected (N/S)", ""),
        (2, "Do weekly staffing records reflect an overtime utilization rate below 3% (overtime hours divided by total weekly hours) and a 0% open-shift rate resulting from call-outs, tardiness, or other staffing gaps?",
         "s1_q2_rating", "s1_q2_comments",
         ["Select...", "Meets Both Targets (5)", "Overtime Target Missed (3)", "Open-Shift Target Missed (3)", "Both Targets Missed (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Not Inspected (N/S)", ""),
        (3, "Are only properly certified personnel being assigned to security posts based on the records sampled?",
         "s1_q3_rating", "s1_q3_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Meets Standard (5)", ""),
        (4, "Were personnel observed properly uniformed, equipped, and performing duties consistent with current post orders?",
         "s1_q4_rating", "s1_q4_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Meets Standard (5)", "Of the personnel inspected, all were in appropriate uniforms, and carried requisite equipment."),
        (5, "Are current post orders, duty logs, and required operational records available and being maintained at the site?",
         "s1_q5_rating", "s1_q5_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Unable to Verify (N/S)", "Post orders are in the process of being promulgated."),
        (6, "Are incidents, uncovered posts, unusual occurrences, and other reportable matters being documented and elevated as required?",
         "s1_q6_rating", "s1_q6_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "No Recent Events (N/S)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Not Inspected (N/S)", ""),
    ]),
    ("II", "Leadership, Supervision and Management", [
        (7, "Does the Site Manager demonstrate effective oversight of staffing, post operations, personnel accountability, and contract requirements?",
         "s2_q7_rating", "s2_q7_comments",
         ["Select...", "High (5)", "Acceptable (3)", "Needs Improvement (2)", "Significant Concern (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Not Inspected (N/S)", ""),
        (8, "Do Shift Supervisors demonstrate active supervision of assigned personnel and posts across the shifts observed?",
         "s2_q8_rating", "s2_q8_comments",
         ["Select...", "High (5)", "Acceptable (3)", "Needs Improvement (2)", "Significant Concern (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Not Inspected (N/S)", ""),
        (9, "Are identified deficiencies or recurring operational issues tracked to corrective action and closure?",
         "s2_q9_rating", "s2_q9_comments",
         ["Select...", "Yes (5)", "Partially (3)", "No (1)", "No Open Deficiencies (5)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Not Inspected (N/S)", ""),
        (10, "Does site leadership maintain effective communication with the Management Support Team and elevate issues requiring higher-level support?",
         "s2_q10_rating", "s2_q10_comments",
         ["Select...", "High (5)", "Acceptable (3)", "Needs Improvement (2)", "Significant Concern (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Not Inspected (N/S)", ""),
        (11, "Based on personnel interaction and observation, is site leadership maintaining professional standards and an effective command climate?",
         "s2_q11_rating", "s2_q11_comments",
         ["Select...", "High (5)", "Acceptable (3)", "Needs Improvement (2)", "Significant Concern (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Acceptable (3)", "The site was professionally managed, with no noteworthy observations to indicate otherwise."),
    ]),
    ("III", "Training and Personnel Readiness", [
        (12, "Does a sample review of personnel files show required training, weapons qualifications, certifications, and PFT requirements are current?",
         "s3_q12_rating", "s3_q12_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Meets Standard (5)", "In site managers office (hard copy). Electronics are held with ST. Current as of 15 Sep."),
        (13, "Are required on-site training records and individual training documentation current, organized, and readily accessible?",
         "s3_q13_rating", "s3_q13_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Minor Deficiency (3)", "Site manager folder. Trainers do not currently electronically maintain. Area to improve."),
        (14, "Is the Site Trainer prepared to execute scheduled basic/sustainment training and maintain required training support materials?",
         "s3_q14_rating", "s3_q14_comments",
         ["Select...", "Ready (5)", "Minor Concerns (3)", "Not Ready (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Ready (5)", "Yes, Site Trainer is fully prepped to execute training."),
        (15, "Do personnel sampled demonstrate working knowledge of post orders, access control, emergency/alarm response, and notification procedures?",
         "s3_q15_rating", "s3_q15_comments",
         ["Select...", "High (5)", "Acceptable (3)", "Needs Improvement (2)", "Significant Concern (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "High (5)", "Yes, CP inquiries were answered in a professional and efficient manner."),
        (16, "Are required refresher, combatives, use-of-force, and other recurring training requirements being maintained or scheduled appropriately?",
         "s3_q16_rating", "s3_q16_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Meets Standard (5)", "When not in transition between contracts, the ST believes they are more efficient."),
    ]),
    ("IV", "Equipment, Weapons and Emergency Readiness", [
        (17, "Is required contractor-furnished operational equipment present, serviceable, and available for mission use based on the sample observed?",
         "s4_q17_rating", "s4_q17_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Minor Deficiency (3)", "Due to shortfalls in appropriate armory tools, some weapons were noted to have light dusting of rust"),
        (18, "Are firearms, ammunition, and related weapons equipment securely stored, controlled, and accountable?",
         "s4_q18_rating", "s4_q18_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Meets Standard (5)", "Weapons were secured, with ammunition in a separate controlled space.  Logbooks accurate."),
        (19, "Are radios, emergency communications, visitor-management systems, and other mission-critical systems operational?",
         "s4_q19_rating", "s4_q19_comments",
         ["Select...", "Operational (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Minor Deficiency (3)", "Yes. Battery life spans in radios are a concern."),
        (20, "Are required individual duty items and protective equipment available and serviceable for personnel observed?",
         "s4_q20_rating", "s4_q20_comments",
         ["Select...", "Meets Standard (5)", "Minor Deficiency (3)", "Significant Deficiency (1)", "Unable to Verify (N/S)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Minor Deficiency (3)", "Med bags are reaching shelf life and require replacement."),
        (21, "Does the site appear prepared to execute site-specific emergency, alarm, active-threat, and incident-response procedures?",
         "s4_q21_rating", "s4_q21_comments",
         ["Select...", "Ready (5)", "Minor Concerns (3)", "Not Ready (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Select...", "It is my observation that they are."),
    ]),
    ("V", "Overall Performance and Support Requirements", [
        (22, "Were any conditions identified that could adversely affect contract performance, officer safety, security, or mission accomplishment?",
         "s5_q22_rating", "s5_q22_comments",
         ["Select...", "None (5)", "Minor (3)", "Significant (2)", "Critical (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Select...", ""),
        (23, "Are there staffing, equipment, training, policy, or administrative issues requiring Management Support Team action?",
         "s5_q23_rating", "s5_q23_comments",
         ["Select...", "None (5)", "Routine Follow-Up (3)", "Priority Action (2)", "Immediate Action (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Select...", ""),
        (24, "Were any noteworthy best practices, improvements, or strong performance indicators identified during the visit?",
         "s5_q24_rating", "s5_q24_comments",
         ["Select...", "Yes (5)", "No (3)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Select...", ""),
        (25, "Based on the visit, how would you assess the site's current ability to meet contractual and operational requirements?",
         "s5_q25_rating", "s5_q25_comments",
         ["Select...", "High (5)", "Acceptable (3)", "Needs Improvement (2)", "Significant Concern (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Select...", ""),
        (26, "What level of follow-up is recommended following this visit?",
         "s5_q26_rating", "s5_q26_comments",
         ["Select...", "None (5)", "Routine (4)", "30-Day Follow-Up (3)", "Priority Follow-Up (2)", "Immediate Leadership Action (1)", "N/A (N/S)", "Not Inspected (N/S)"],
         "Select...", ""),
    ]),
]

NARRATIVE_FIELDS = [
    ("KEY OBSERVATIONS, STRENGTHS & CONCERNS", "narrative_observations", ""),
    ("RECOMMENDED ACTIONS & OVERALL ASSESSMENT", "narrative_actions_assessment", ""),
]

TOTAL_SCORE_FIELD = "total_score"
TOTAL_SCORE_VALUE = "417 / 500"
TOTAL_SCORE_LABEL = "TOTAL SCORE"
TOTAL_SCORE_SUBLABEL = "AUTO-CALCULATED"

TOTAL_SCORE_JS = '''var sum = 0; var n = 0;
for (var s=1; s<=5; s++) {
  var q0 = (s==1?1:(s==2?7:(s==3?12:(s==4?17:22))));
  var q1 = (s==1?6:(s==2?11:(s==3?16:(s==4?21:26))));
  for (var q=q0; q<=q1; q++) {
    var f=this.getField("s"+s+"_q"+q+"_rating");
    if (!f) continue;
    var v=f.valueAsString;
    var m=v.match(/\\(([1-5])\\)\\s*$/);
    if (m) { sum += parseInt(m[1],10); n++; }
  }
}
if (n > 0) {
  var scaled=Math.round((sum/(n*5))*500);
  event.value=scaled+" / 500";
} else { event.value=""; }'''
