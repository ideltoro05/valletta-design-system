# CIFSO Candidate Certification Forms — Valletta Templates

Four blank, branded Word templates in the Valletta Industries design system
(`../../DESIGN_SYSTEM.md`, `../../tokens.json`), built from four signed,
filled-in example PDFs:

| Source PDF | Template |
|---|---|
| `Contractor_Certification_Employment_Eligibility_-_CIFSO_CT_Lyles_Larry.pdf` | `valletta_new_hire_employment_eligibility.docx` |
| `Contractor_Certification_of_Shift_Supervisor_Candidate_Eligibility_CIFSO_WA_Freitas_Ryan_Signed.pdf` | `valletta_shift_supervisor_candidate_qualifications.docx` |
| `Contractor_Certification_of_Site_ManagerCandidate_Qualifications_-_CIFSO_Lima_Scott_John.pdf` | `valletta_site_manager_candidate_qualifications.docx` |
| `Contractor_Certification_of_Site_Trainer_Candidate_Qualifictions_CIFSO_Whiskey_-_Zimmerman_Harry.pdf` | `valletta_site_trainer_candidate_qualifications.docx` |

## Why these are blank, not filled

The four source PDFs are specific, already-signed examples (Larry Lyles,
Ryan Freitas, John Scott, Harry Zimmerman). The request was for documents
the client can fill out — i.e. the underlying **form templates**, not a
rebrand of one already-completed instance. Every field, checklist item,
and section from each source form is reproduced with an empty value, ready
for a new candidate.

## What confirms these were originally Word forms

Several unfilled fields in the source PDFs still show literal Word content
control placeholder text — `Choose an item.` (dropdown) and `Click or tap
to enter a date.` (date picker) — which only appears when a Word form
field was never filled in before the document was exported to PDF and
signed. That confirms the underlying documents are Word templates with
form fields, not flat forms, which is what these `.docx` templates restore.

## Field fidelity vs. interactivity trade-off

- **Checklist items that used a real checkbox glyph (☐/☒) in the source**
  (e.g. "Physical Security Experience," "Demonstrated Leadership Ability,"
  "Uniforms Issued") are rebuilt as genuine Word checkbox content controls
  — click to check them in Word, no typing required.
- **Everything else** (free-text fields, the unfilled dropdowns, the
  unfilled date pickers) is rebuilt as a labeled, underlined blank line —
  type directly on the line. True interactive Word dropdown/date-picker
  content controls were not used for these, because the source PDFs only
  preserve the *placeholder text* for unfilled dropdowns/date fields, not
  the underlying option lists — fabricating option lists we can't verify
  against the source risked introducing content that wasn't in the
  original. A blank fillable line is the faithful choice.

## Structure

Each template follows the same pattern: a Valletta-branded header/footer,
a black title band with the document name, black section bands for major
groupings (mirroring the section-band convention used across this repo),
red field labels with underlined blanks, and a signature block at the end
matching the source's signer roles (Site Manager / Site Trainer / NPM /
NQCM / NTM, as applicable to each form). Multi-part sections specific to
one form are preserved as-is:

- **New Hire Employment Eligibility** — qualifying experience, prior CIFSO
  employment, medical evaluation, employment requirements, appearance
  standard, training certifications, physical fitness assessment, OJT,
  additional training, uniforms/equipment/weapons issue, and the
  certification + 4-signature block (Site Manager, Site Trainer, NPM, NQCM).
- **Shift Supervisor Candidate Qualifications** — D.18 criteria checklist,
  FEMA certifications, annual PFT, annual firearms qualification, a blank
  candidate-biography box, and a 3-signer block (Site Manager, NPM, NQCM).
- **Site Manager Candidate Qualifications** — D.18 criteria checklist,
  FEMA certifications, current sustainment/range/PFT certifications, and a
  2-signer block (NPM, NQCM).
- **Site Trainer Candidate Qualifications** — D.21 criteria checklist, FEMA
  certifications, NRA LE Tactical Shooting Instructor certification detail,
  Tactical Medical Instructor course, pistol/rifle armorer schools, annual
  PFT/firearms qualification, all 7 on-the-job-training weeks (including the
  Week 7 National Training Manager review), the certification statement, a
  3-signer block (NTM, NPM, NQCM), and blank National Training Manager Notes
  and Candidate Biography boxes.

## Files

| File | Purpose |
|---|---|
| `shared.js` | Shared styling helpers (header/footer, section bands, field rows, checkbox items, signature rows) reused by all four builders |
| `employment_eligibility.js` | Builds the New Hire Employment Eligibility template |
| `shift_supervisor.js` | Builds the Shift Supervisor Candidate template |
| `site_manager.js` | Builds the Site Manager Candidate template |
| `site_trainer.js` | Builds the Site Trainer Candidate template |
| `valletta_*.docx` | The four output templates, US Letter |

## Verification

Each docx was validated with `python-docx`: zip integrity, every section
heading and subheading present, table-based paired fields (e.g. Age/
Gender, Pistol/Rifle scores) confirmed rendering correctly, checkbox
content controls present in the underlying XML at the expected counts, and
page size confirmed at 8.5"×11" for all four.

As with other native `.docx` deliverables in this repo, no LibreOffice
preview was available in this environment to visually confirm rendering —
structural validation via `python-docx` was used instead.
