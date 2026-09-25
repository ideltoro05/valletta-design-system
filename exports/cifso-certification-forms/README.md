# CIFSO Candidate Certification Forms — Valletta Templates

Four blank, branded Word templates in the Valletta Industries design system
(`../../DESIGN_SYSTEM.md`, `../../tokens.json`), built from four signed,
filled-in example PDFs:

**2026-09-25 update (design system v2.0, per Sam's directive):** recolored from
Valletta Red to Valletta Cobalt (`#1B4FA0`) and switched from the Valletta-only mark
to the combined Valletta + SOC lockup in the header. Every field, checklist item, and
control (checkboxes, dropdowns, date pickers) is unchanged — verified identical field
counts before/after the recolor. See `../../COBALT_REBRAND_PLAN.md` for the full
package this is part of.

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

## Field types: checkbox, dropdown, date picker, or plain text

Every field in all four templates is one of four genuine Word content
control types, chosen per field rather than applied uniformly:

- **Checkbox** — every checklist item that used a real checkbox glyph
  (☐/☒) in the source (e.g. "Physical Security Experience," "Uniforms
  Issued") is a real Word checkbox content control. Click to check it.
- **Dropdown list** — every field with a small, enumerable set of answers
  is a real Word dropdown content control (click it, pick from the list):
  every Yes/No field (employment requirements, appearance standard, FEMA
  certification completion), Gender, Branch, Type of Service, Type of
  Termination, and every "Years" / "Years of experience" field.
- **Date picker** — every field asking for a date (dates of hire/
  termination/completion/qualification, expiration dates, signature dates,
  OJT start/end dates, etc.) is a real Word date-picker content control
  (click the calendar icon in Word to pick a date).
- **Plain fillable line** — open-ended fields with no bounded set of valid
  answers (candidate name, location, school/agency name, certifier name,
  scores, hours, narrative boxes) stay as a labeled, underlined blank line.

### Why some fields use inferred option lists, and why some don't

The four source PDFs only reveal a dropdown's real option list when that
specific field happened to be left unfilled (it then shows Word's literal
"Choose an item." placeholder instead of a chosen value). That directly
confirmed only a handful of fields as dropdowns. Rather than restrict real
dropdown/date controls to only those few evidenced fields, two things were
applied consistently:

1. **Dates.** Every "Date"-labeled field across all four documents is a
   date-picker control — this is unambiguous regardless of which specific
   control the original template happened to use for that one field.
2. **Yes/No and other clearly bounded fields.** Fields whose filled-in
   value in the source was obviously one of a small closed set (Yes/No;
   Male/Female; a numeric years-of-experience count) were given a
   reasonable, clearly-labeled dropdown option list. These option lists
   (e.g. military branches, termination types, a 0–20+ years range) are
   **reconstructed, not transcribed** — the source never revealed the
   underlying list, since the field was already filled with one answer.
   They're reasonable, standard choices for the category, not source data.

**Left as plain text, deliberately:** open-ended fields with no true
bounded answer set (school/agency names, certifier names, narrative boxes)
were not forced into a dropdown just because the source showed
"Choose an item." for one of them (Tactical Medical Instructor Course's
School/Agency Name field) — inventing a fixed list of schools would be
fabricating specific content, which this rebrand avoids. The **Medical
Evaluation** section in the New Hire Employment Eligibility form was also
kept as plain text rather than turned into Yes/No dropdowns — those
answers (vision, hearing, psychological fitness standards) are
compound/qualified statements, not simple Yes/No, and inventing fixed
categories for a medical certification section risked misrepresenting the
actual standard being certified against.

## Confirmed empty

All four templates were checked against every candidate and signer name
that appeared in the four source PDFs (Larry Lyles, Ryan Freitas, John
Scott, Harry Zimmerman, Joshua Gallagher, Michael Schuster, Otilio
Miranda, Michael Selleck, Jason Johns, Kurt Wetzold, JB Nance, Kevin
Cadiente) — none of those names appear anywhere in the templates' text or
table content. Every dropdown defaults to "Choose an item." and every date
picker defaults to "Click or tap to enter a date." (Word's own standard
placeholders), and every checkbox defaults to unchecked.

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
| `shared.js` | Shared styling helpers (header/footer, section bands, field rows, checkbox/dropdown/date-picker content controls, signature rows) reused by all four builders |
| `employment_eligibility.js` | Builds the New Hire Employment Eligibility template |
| `shift_supervisor.js` | Builds the Shift Supervisor Candidate template |
| `site_manager.js` | Builds the Site Manager Candidate template |
| `site_trainer.js` | Builds the Site Trainer Candidate template |
| `valletta_*.docx` | The four output templates, US Letter |

## Verification

Each docx was validated with `python-docx` plus a raw-XML check: zip
integrity, every section heading and subheading present, table-based
paired fields (e.g. Age/Gender, Pistol/Rifle scores) confirmed rendering
correctly, and checkbox/dropdown/date content controls present in the
underlying XML at exactly the counts expected from each document's field
list (e.g. the Employment Eligibility form: 11 checkboxes, 19 dropdowns,
15 date pickers). Page size confirmed at 8.5"×11" for all four. A sample
dropdown and date control's raw XML was inspected directly to confirm it
matches Word's native `w:sdt`/`w:dropDownList`/`w:date` structure.

As with other native `.docx` deliverables in this repo, no LibreOffice
preview was available in this environment to visually confirm rendering —
structural validation via `python-docx` was used instead.
