# Leadership Course Outline (SOC Delaune V3) — Valletta Rebrand

Rebrand of `Leadership_Course_OUTLINE_SOC_Delaune_V3_-_Copy.docx` in the
Valletta Industries design system (`../../DESIGN_SYSTEM.md`, `../../tokens.json`).
Visual rebrand only — every word is transcribed unchanged from this specific
source file.

This document is closely related to two other pieces already in this repo
(`../instructor-outline/`, the SOC "Instructor Outline" doc) but is a
genuinely different revision ("V3"), not a duplicate — it was rebranded from
its own source text rather than reused from the earlier file. Concrete
wording differences that were preserved exactly as this source has them,
not "corrected" to match the other document:

- The Charismatic Leader example list includes **Malcolm X** here (the
  earlier Instructor Outline's list does not)
- The sixth ethical characteristic is **"Makes the team a priority"** here,
  not "Prioritizes the Team" as in the other document
- The course meta box, Overview list, and top-level sections here use
  lettered outline markers (A.–F.) rather than the other document's
  unlettered section titles

Structurally, this is the flowing full-outline version (course meta box →
Presentation/Introduction/Objective → Statistics → lettered Overview →
sections A through F → Conclusion → Additional Reading), with videos cited
inline as plain "Video #N ... [url]" lines rather than the "NOTE: Show
Slide" cue format used in the separate Supporting Information lesson-plan
document also in this repo.

The source was branded for SOC (gold/black geometric cover, gold "OVERVIEW"
banner, the SOC "A Day & Zimmermann Company" logo). This version carries the
same structure and depth in the Valletta black/red/white system:

- Cover: black page, Valletta shield + wordmark, red corner-tick motif
- Masthead: the Valletta mark + running title with a red rule, repeating on
  every content page
- Course metadata as a bordered info box on page one
- Lettered section headings (A.–F.) in Oswald/Bookman Old Style with a red
  letter and a red rule beneath
- Video citations as tinted callout boxes with a red left border and a red
  "VIDEO N" tag; the one explicit discussion prompt in the source gets a
  "DISCUSSION" tag using the same treatment
- Speaker/author bios (Travis Mills, David Goggins, John Maxwell, Jocko
  Willink) set as small italic asides, matching the treatment used across
  this repo's other rebrands
- Pull-quotes styled with a red left border and decorative curly quote
  marks; the source's own straight quotation marks around each quote are
  not carried into the visual mark (they're a typographic replacement, not
  a wording change — the quoted words themselves are untouched)
- The gold "OVERVIEW" banner becomes a black band with the same six lettered
  items underneath; "CONCLUSION" gets the same band treatment
- Additional Reading as a bulleted list with the red square marker

Two minor formatting-artifact cleanups, not content changes: a stray
trailing en dash with nothing following it after the Video #1 citation, and
an orphaned closing bracket "]" after the Video #4 citation (its matching
opening bracket isn't present in the source) — both dropped as leftover
punctuation, the same way earlier rebrands in this repo de-hyphenated
line-wrap artifacts without touching the actual wording.

Pages were packed by measuring each block's real height and filling each
page as full as it reasonably goes, same approach as the other rebrands.
Result: 9 pages (plus cover) with no overflow on any page.

## Files

| File | Format |
|---|---|
| `valletta_leadership_outline_v3.pdf` | Print-ready PDF, US Letter, 9 pages |
| `valletta_leadership_outline_v3.docx` | Editable Word document, US Letter |
| `valletta_leadership_outline_v3.html` | Self-contained source (fonts + logo embedded) |
| `generate_v3_outline.py` | Regenerates the HTML/PDF from data (run from this folder) |
| `export_pdf.py` | Renders the HTML to PDF via Playwright |
| `build_docx.js` | Regenerates the .docx from data (`node build_docx.js`) |

Same note as the earlier rebrands: this sandbox can't run LibreOffice to
render a visual preview of the `.docx`, so it was verified structurally
(every section checked present, the two document-specific wording
differences confirmed present, header/footer/page-numbering confirmed, zip
integrity checked, both logo images confirmed embedded) rather than by eye.
Give it a look in Word and flag anything off.
