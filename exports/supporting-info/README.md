# Leadership Course Supporting Information — Valletta Rebrand

Rebrand of `Leadership_Course_supporting_information_-_Copy.docx` in the
Valletta Industries design system (`../../DESIGN_SYSTEM.md`, `../../tokens.json`).
Visual rebrand only — this is the full instructor lesson-plan script (285
source paragraphs): every "Show Slide" cue, every instructor script line
(Introduction / Gain Attention / Conclusion), every EPO/TPO objective, every
lettered and numbered outline point, every quote and attribution, the
statistics list, and the follow-on reading list are transcribed unchanged.
Source typos are preserved as-is rather than silently corrected ("proviing"
for "providing", "Soilders" for "Soldiers" in two video slide titles,
"Ghandi" for "Gandhi") — this is a rebrand, not a copyedit, and the previous
two rebrands in this repo followed the same rule. The three bare reference
links at the top of the source have no heading of their own; they're labeled
"References" here for legibility, the same convention used for the unlabeled
instructor script in the earlier Instructor Outline rebrand.

This document is structurally different from the other two Leadership
Training pieces already in this repo — it's the detailed lesson-plan/script
version (roman-numeral top sections II–V: Presentation, Review, Follow On
Assignment, Student Sign-In Sheet; no "I." section exists in the source),
built around six Enabling Performance Objectives rather than a numbered
outline. The source was branded for SOC (gold/black cover template, the SOC
"A Day & Zimmermann Company" header logo). This version carries the same
content and structure in the Valletta black/red/white system:

- Cover: black page, Valletta shield + wordmark, "Supporting Information"
  eyebrow, title taken from the course's own stated subject ("Effective
  Motivational Leadership") — matching the cover treatment used across the
  other rebranded pieces
- Masthead: the Valletta mark + running title with a red rule, repeating on
  every content page
- Roman-numeral major sections (II–V) as full-width black bands with a red
  numeral, replacing the source's plain "II. PRESENTATION" text headings
- EPO headings (EPO 1–6) as red-numbered, red-ruled section heads — visually
  distinct from the roman-numeral bands one level up
- "NOTE: Show Slide ..." cues, and the six embedded video cues (VIDEO 1–6),
  as tinted callout boxes with a red left border, matching the note-box
  treatment from the Instructor Outline rebrand
- Lettered/numbered outline points (a./b./c., 1./2./3.) in red bold labels
  with indentation for nested sub-points (e.g., "a. Self-Reflection" and
  "b. Expectations" nested under "4. Integrity")
- Pull-quotes (David Goggins, John Maxwell, Jocko Willink, John Quincy Adams)
  styled with a red left border, the same treatment used throughout this
  repo's rebrands
- Instructor script lead-ins (INTRODUCTION:, GAIN ATTENTION:) as bold black
  labels inline with their paragraph, matching how the source visually
  distinguished them from surrounding text

One ordering correction made during transcription, not a content change:
the Jocko Willink "ready to follow" quote sits after EPO 3's "1. Leader"
list (item g) in the source, not after EPO 1's list — an easy place to
mis-attach given how similar the two "Leader"-themed lists read. Verified
against the source paragraph-by-paragraph and placed correctly.

Pages were packed by measuring each block's real height and filling each
page as full as it reasonably goes, the same approach used for the other two
rebrands. The result is 9 pages (plus cover) with no overflow on any page;
the final two pages (Review/Follow-On/Sign-In) run lighter than the rest
since those source sections are short and came last — left as-is rather than
forcing them to interleave earlier content out of order.

## Files

| File | Format |
|---|---|
| `valletta_supporting_information.pdf` | Print-ready PDF, US Letter, 9 pages |
| `valletta_supporting_information.docx` | Editable Word document, US Letter |
| `valletta_supporting_information.html` | Self-contained source (fonts + logo embedded) |
| `generate_supporting.py` | Regenerates the HTML/PDF from data (run from this folder) |
| `export_pdf.py` | Renders the HTML to PDF via Playwright |
| `build_docx.js` | Regenerates the .docx from data (`node build_docx.js`) |

Same note as the earlier rebrands: this sandbox can't run LibreOffice to
render a visual preview of the `.docx`, so it was verified structurally
(every section checked present, header/footer/page-numbering confirmed, zip
integrity checked, both logo images confirmed embedded) rather than by eye.
Give it a look in Word and flag anything off.
