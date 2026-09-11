# Employee Benefits Guide — Valletta Rebrand

Rebrand of `Valletta_Industries_Combined_Benefits_Guide_20262027.pdf` in the
Valletta Industries design system (`../../DESIGN_SYSTEM.md`,
`../../tokens.json`). This is a visual rebrand only — every word, number,
table value, contact detail, and disclaimer from the source document is
unchanged. Two elements are third-party graphics from the source PDF
(the GoodRx explainer and the Tres Health app screenshot) and are carried
over unedited, since they are content, not styling.

The original used a plain black-on-white Word-style layout with a red
logo box repeated on every page, red-filled table headers, and a pink
row tint. The rebrand replaces that with the actual Valletta system:

- Masthead: the real shield + serif wordmark (extracted from the source
  PDF's own logo image, re-colored for a light background and saved to
  `../../assets/logo/valletta-mark-black.png` — plus a white version for
  the dark cover, `valletta-mark-white.png`) with a thin red rule
- Oswald (page titles) + Inter (body, table type, labels)
- Tables: black header row / white type, a neutral light-gray zebra
  stripe (the original's red header fill and pink stripe were dropped —
  red is reserved as a small accent, not a large fill, per the design
  system)
- Red used only for sub-heading labels, bullet markers, and thin rules
- A black cover page with the red corner-tick motif used elsewhere in
  this project

The source PDF fit some dense sections (the full medical comparison
table + cost table on one page; Dental + Vision on one page) at a much
smaller, tighter type size. To keep body and table text at a comfortably
readable size, those two sections were each split across two pages, so
this version runs 11 pages instead of 9. No content was shortened to
make it fit — only where it breaks changed.

The `.docx` is a separate, independent build (not a conversion of the PDF)
using the same content and the same table/heading/bullet treatment, so HR
can edit it directly in Word — headers/footers repeat automatically, page
numbers are live fields ("Page X of Y"), and bullets/table shading are
native Word formatting, not images.

## Files

| File | Format |
|---|---|
| `valletta_benefits_guide.pdf` | Print-ready PDF, US Letter, 11 pages |
| `valletta_benefits_guide.docx` | Editable Word document, US Letter |
| `valletta_benefits_guide.html` | Self-contained source (fonts + images embedded) |
| `generate_guide.py` | Regenerates the HTML/PDF from data (run from this folder) |
| `build_docx.js` | Regenerates the .docx from data (`node build_docx.js`, run from this folder) |
| `goodrx.png`, `tresapp.png` | Third-party graphics carried over from the source PDF |
| `*.b64` | Base64 copies of the images/logo embedded by the HTML generator |

Note: this environment's sandbox couldn't run LibreOffice to render a visual
preview of the .docx (a pre-existing limitation, unrelated to this file) —
its content and structure were verified directly instead (every paragraph,
all 8 tables, headers/footers, and page numbering checked against the
source). Please sanity-check the visual layout once in Word/Google Docs;
flag anything off and I'll fix it.
