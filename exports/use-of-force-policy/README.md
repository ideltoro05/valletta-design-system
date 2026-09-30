# Use of Force Policy and Procedure — Valletta Redesign

Visual redesign of `Valletta_Industries_Use_of_Force_Policy_and_Procedure_081726_-_Fillable.pdf`
in the Valletta Industries design system v2.0 (`../../DESIGN_SYSTEM.md`,
`../../tokens.json`). Delivered as a native Word document per request.

**Redesign only — content unchanged.** Every section, definition, role
description, guideline, procedure, restriction, and reference is the same
wording as the source. Spot-verified 25 key passages (including the longer,
legally-sensitive ones — deadly force justification, firearm restrictions,
reporting timelines) against the source PDF's extracted text — all present
verbatim.

## What "no functionality changes" meant here

The source is a lightly-interactive PDF: 8 pages of static policy text plus
3 real AcroForm text fields on the signature page (Printed Name, Signature,
Date — no dropdowns, no calculated fields, nothing like the Site Visit
Assessment's complexity). The Word document reproduces those three as
labeled fillable blank lines, the same pattern used for every other
signature block built in this repo (weapons SOP, CIFSO certification
forms, etc.) — click the line, type. A native Word content control wasn't
necessary here; a blank line achieves the same practical outcome for a
"printed name / signature / date" block.

## Rebuild approach

Content was read out of the source PDF programmatically (`pypdf`/`fitz`
text and font-weight extraction, to correctly identify which terms and
labels are bold in the source — e.g. the defined-terms list in Section 3.0
and the role labels in Section 4.0) rather than retyped from a skim, then
built into `build_docx.js` and checked against the extracted text.

**Table of Contents:** the source's ToC lists page numbers tied to its own
layout; those numbers would be wrong the moment the document reflows under
new fonts/margins (which it does — different fonts and margins than the
source). Rather than copy stale numbers into a new document, this uses a
real Word Table of Contents field (`TOC \h \o "1-2"`, hyperlinked,
covering both the ten major sections and the 6.1–6.7 / 7.1–7.2
subsections). **Word needs the field updated once on open** — right-click
the ToC and choose "Update Field" (or Ctrl+A then F9) — to populate page
numbers; this is standard Word behavior for any ToC field, not specific to
this document.

**A same-class bug caught and fixed during verification** (same pattern as
the PFT Policy build): several labels — the header's Policy
Level/Number/Version/Approved-By strip, the acknowledgment section's
Printed Name/Signature/Date labels, and the Reviews-and-Edits table's
column headers — were initially built with `.toUpperCase()` on the actual
label text for the small-caps visual treatment used throughout this
design system. That silently changes the stored document text (e.g.
"Author" becomes "AUTHOR"). Fixed by switching every one of these to
Word's `allCaps` character property, which displays capitals without
altering the underlying text, then re-verified.

## A real formatting bug also caught and fixed

The header's black metadata strip (Policy Level / Policy Number / Version
No. / Approved By) was first built with white text but no black cell
shading — invisible white-on-white. Caught by checking the raw header XML
for the shading fill rather than assuming the visual result matched intent;
fixed by shading each metadata cell black.

## Design treatment

Same v2.0 system as the rest of the document package: Valletta Cobalt
(`#1B4FA0`) accents, the combined Valletta + SOC lockup in the header
(replacing the source's solid-red logo block), Bookman Old Style section
headings, Arial small-caps labels, Calibri body, 1in margins. The source's
four distinct list styles were preserved as genuine Word numbered/bulleted
lists rather than flattened to plain paragraphs: lowercase roman numerals
with a ")" suffix for the procedural sub-items (6.1, 6.2, 6.6, 6.7),
decimal numbering for the reporting-procedure steps (7.1), and two custom
bullet glyphs matching the source's own visual distinction between the
Guidelines section (▶-style) and the Roles/Levels-of-Force lists (■-style).

## Files

| File | Purpose |
|---|---|
| `valletta_use_of_force_policy.docx` | The redesigned document, US Letter |
| `build_docx.js` | Builds the docx — all content, list/table structures, and styling |

Delivered as docx only, per the explicit request (source was PDF, but a
Word document was specifically asked for).

## Verification

- Zip integrity OK; no red (`#FF002B`) anywhere in body or header XML;
  cobalt present (38 occurrences)
- All 10 major sections, all 9 subsections, both defined-term lists, all
  role descriptions, the References section, the Policy Acknowledgement
  block, and the Reviews and Edits table confirmed present with correct
  text
- 25 key passages spot-checked verbatim (whitespace-normalized) against
  the source's extracted text, zero mismatches
- Reviews and Edits table confirmed as 2×4 with the exact source values
  (Date / Requested Edit / Author / Date; August 17, 2026 / Initial Policy
  / Jose Perou – Human Resources Director / August 17, 2026)
- TOC field confirmed present and scoped to heading levels 1–2 (11
  Heading 1 paragraphs, 9 Heading 2 paragraphs — matches the 10 sections +
  acknowledgement heading, and the 7+2 subsections)
- `allCaps` used (not literal case changes) everywhere a source label is
  displayed in small caps — 13 occurrences, confirmed via raw XML
  (`<w:caps/>`)
- Page size and margins confirmed (8.5"×11", 1in all sides)

As with other native `.docx` deliverables in this repo, no LibreOffice
preview was available in this environment to visually confirm rendering —
structural/content validation via `python-docx` and raw XML inspection was
used instead.
