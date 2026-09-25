# Cobalt Rebrand — Government Package Plan

**Context:** Email from Sam, 2026-09-25. Government client submission due **Sunday,
October 4**. Internal target: **Close of business, Tuesday, September 29** (built-in
review/adjustment margin before submission).

**Design directive (now in `DESIGN_SYSTEM.md` v2.0 / `tokens.json` v2.0 — done):**
- Cobalt Blue (`#1B4FA0`) replaces Valletta Red as the primary document accent. Red is
  retired everywhere except inside the fixed Valletta shield logo mark itself (not
  being redesigned).
- Co-branding is back on: the combined **Valletta Industries + SOC** lockup
  (`/assets/logo/valletta-soc-lockup.png`) is the default header/cover mark for this
  package, not the Valletta-only mark used on several documents built earlier in this
  project.
- **Output format matches input format** — a PDF source gets a PDF back, a Word source
  gets a Word file back. (Several earlier documents in this repo were delivered as both
  PDF *and* docx regardless of source format; that's not the operating rule for this
  package going forward.)

## Document inventory — Sam's 12 vs. what's already in this repo

Sam's list numbering preserved. "Status" reflects the repo as of 2026-09-25, before any
recolor/rebrand work on this new directive has started.

| # | Sam's document | Existing in repo | Status | Work needed |
|---|---|---|---|---|
| 1 | Contractor certificate for employment eligibility | `exports/cifso-certification-forms/valletta_new_hire_employment_eligibility.docx` | Built (black/red/Valletta-only) | Recolor + relogo |
| 2 | Site Manager approval form | `exports/cifso-certification-forms/valletta_site_manager_candidate_qualifications.docx` | Built | Recolor + relogo |
| 3 | Supervisor approval form | `exports/cifso-certification-forms/valletta_shift_supervisor_candidate_qualifications.docx` | Built | Recolor + relogo |
| 4 | Site Trainer approval form | `exports/cifso-certification-forms/valletta_site_trainer_candidate_qualifications.docx` | Built | Recolor + relogo — **possible duplicate of #9, see below** |
| 5 | Site visit assessment form (working dropdowns + fillable narrative) | `exports/site-visit-assessment/` — interactive PDF (AcroForm dropdowns + narrative fields) and a flattened docx | Built | Recolor + relogo — **possible duplicate of #8, see below** |
| 6 | Physical Fitness Test (PFT) Assessment Policy | *(none found)* | **Not started** | New — need source document |
| 7 | Weapons and Ammunition Policy | `exports/weapons-sop/` covers *Firearms Loading and Unloading* specifically, not a general ammunition policy | **Likely new** | Need source to confirm scope vs. the existing SOP |
| 8 | Valletta Site Assessment | — | **Ambiguous** | Possible duplicate of #5 — confirm when uploaded |
| 9 | Valletta Site Trainer Candidate Qualifications | `exports/cifso-certification-forms/valletta_site_trainer_candidate_qualifications.docx` | Built | **Possible duplicate of #4** — confirm when uploaded |
| 10 | Valletta Incident Report Log | `exports/incident-log/valletta_incident_report_log.docx` | Built | Recolor + relogo — **possible overlap with #12, see below** |
| 11 | Valletta Weekly Activity Report | `exports/weekly-activity-report/valletta_weekly_activity_report.docx` | Built | Recolor + relogo |
| 12 | Incident Event Form | — | **Ambiguous** | Possible overlap with #10 (a single-event intake form vs. the running log/register) — confirm when uploaded |

**Bottom line:** 7 of the 12 already exist and only need a recolor + relogo pass (fast,
mechanical, no new content decisions). 2 appear to be genuinely new documents needing a
source upload (PFT Assessment Policy, Weapons and Ammunition Policy). 3 are possible
duplicates/near-duplicates of documents already built (#4/#9, #5/#8, #10/#12) — flagged
rather than assumed, since collapsing them wrong would mean missing a real deliverable.

## Recolor + relogo pass (the 7 already-built documents)

Mechanical, low-risk, no content changes — same method used throughout this project:
update each document's generator script (color constants, logo asset reference) and
re-run it. Concretely, per document: swap the red hex constant to Cobalt Blue
`#1B4FA0`, swap the Valletta-only logo reference to the combined
`valletta-soc-lockup.png`, regenerate, re-verify (structural checks + visual QA as
already established), redeliver in the source's original format only.

## New documents (need Sam/the client to upload source)

- **Physical Fitness Test (PFT) Assessment Policy**
- **Weapons and Ammunition Policy**

These get built fresh in the cobalt/co-branded system from the start — no legacy
red/Valletta-only version to convert.

## Sequencing, given the Sept 29 internal target

1. **Now:** design system updated (done, this pass).
2. **As each document is uploaded:** confirm whether it's a recolor of an existing
   build or new content, per the table above, then process it in its native format
   (PDF in → PDF out, Word in → Word out).
3. **Prioritize the 7 recolors first** where possible — they're the fastest wins and
   bank progress early, leaving the two genuinely new policy documents (which need
   source content read and structured from scratch) more runway before the 29th.
4. **Flag, don't guess, on the three ambiguous pairs** (#4/#9, #5/#8, #10/#12) — when
   each is uploaded, confirm with Sam/Israel whether it's the same document as one
   already built or something distinct before spending build time on it.

## Open questions for Sam / Israel

1. Are #4 (Site Trainer approval form) and #9 (Valletta Site Trainer Candidate
   Qualifications) the same document?
2. Are #5 (Site visit assessment form) and #8 (Valletta Site Assessment) the same
   document?
3. Are #10 (Valletta Incident Report Log) and #12 (Incident Event Form) two different
   documents (a running log vs. a single-incident intake form), or the same thing?
4. Does "Weapons and Ammunition Policy" (#7) supersede/absorb the existing "Firearms
   Loading and Unloading SOP," or is it a separate, broader policy document?
