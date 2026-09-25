# Firearms Loading and Unloading SOP — Valletta Rebrand

Rebrand of `CIFSO_Weapons_SOP.docx` in the Valletta Industries design system
(`../../DESIGN_SYSTEM.md`, `../../tokens.json`). Visual rebrand only — every
section, procedure step, note, and acknowledgment form field is unchanged
from the source.

## Branding

The source header carried a combined "Valletta + SOC" lockup image — the
mid-rebrand co-branding visible across this project's source material,
confirming this is a branding change, not a content change. No text was
reworded; "SOC" only ever appeared as part of that logo image, not in the
body copy.

**2026-09-25 update (design system v2.0, per Sam's directive):** recolored
from Valletta Red to Valletta Cobalt (`#1B4FA0`), and switched from the
Valletta-only mark back to the combined Valletta + SOC lockup — co-branding
is standard again for this document package, reversing the Valletta-only
treatment this file used right after the initial rebrand. The combined
lockup carries its own black backdrop, so the same asset is used in both
the running header and on the black cover (previously two different mark
files, black-on-white and white-on-black). No content changed — verified
identical section/paragraph counts before and after. See
`../../COBALT_REBRAND_PLAN.md` for the full package this is part of.
Also confirmed against the source uploaded 2026-09-25
(`Weapons Loading_Unloading_Ammunition_Policy.docx`): word-for-word the
same content as this document (checked Section 1.1) — Sam's "Weapons and
Ammunition Policy" list item and this SOP are the same document, just
under a fuller title in the source header
("Weapons and Ammunition Loading and Unloading Policy" stacked with
"SOP – Firearms Loading and Unloading"). Title change pending confirmation
from Sam — not applied yet.

## Numbering reconstruction

The source uses Word's automatic multi-level list numbering
(`w:numPr`/`w:ilvl`/`w:numId`), not literal typed numbers, so the displayed
section numbers (1., 1.1, 3.3.1, 4.1.1, etc.) don't exist as text in the
document XML. They were reconstructed by reading `word/numbering.xml`:
each `w:abstractNum` defines a `w:lvl` per level with a `w:numFmt`
(`decimal` at all three levels used here) and a `w:lvlText` pattern
(`%1.`, `%1.%2.`, `%1.%2.%3.`). Walking the paragraphs in document order
while maintaining a per-level counter (resetting deeper levels whenever a
shallower one increments) reproduces the exact numbers Word would render.

This reconstruction was checked against an in-document self-reference: item
12.2 cites "Section 12.2" inside its own text. That's a genuine quirk of the
source (not something introduced here) — reproducing it verbatim confirmed
the numbering logic was correct rather than off by one.

## Structure

- Black cover with the Valletta mark, "Standard Operating Procedure" eyebrow,
  title, and a Document Number / Effective Date / Revision / Approved By
  meta block (fields left blank, matching the source template).
- 12 numbered sections (Purpose through Training and Compliance), each with
  red section numbers/rules and red bold item labels, matching the outline
  pattern used in every other document in this repo.
- One `NOTE` callout (red-left-border tinted box) under Section 7, covering
  press checks / magazine retention tests.
- Two acknowledgment forms (Armed Shift Supervisor, Armed Officer), each
  with employee-info field rows, an intro/lead-in/closing paragraph, a
  bulleted responsibilities list, and signature/date lines.

## Files

| File | Format |
|---|---|
| `valletta_weapons_sop.pdf` | Flattened PDF, US Letter, 6 pages |
| `valletta_weapons_sop.docx` | Native editable Word document, US Letter |
| `generate_sop.py` | Builds the HTML source (measurement-driven pagination) |
| `export_pdf.py` | Renders the HTML to PDF via Playwright |
| `build_docx.js` | Builds the native docx via the `docx` npm package |

## Verification

- HTML build: 0px overflow confirmed on all 6 pages via a Playwright
  `scrollHeight`/`clientHeight` check.
- All 6 pages visually reviewed via screenshot — cover, section numbering
  hierarchy (including the nested 3.3.1/3.3.2 and 4.1.1 levels), the NOTE
  callout, and both acknowledgment forms all render correctly.
- PDF export confirmed 6 pages at 612×792pt (US Letter portrait).
- docx validated programmatically: zip integrity OK, all 12 section
  headings present, all sampled numbered items (1.1, 3.3.1, 3.3.2, 4.1.1,
  7.6.1, 8.1.1, 12.5) present, both acknowledgment form titles present,
  page size 8.5"×11".

As with other native `.docx` deliverables in this repo, no LibreOffice
preview was available in this environment to visually confirm docx
rendering — structural validation via `python-docx` was used instead.
