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

## Files

| File | Format |
|---|---|
| `valletta_benefits_guide.pdf` | Print-ready PDF, US Letter, 11 pages |
| `valletta_benefits_guide.html` | Self-contained source (fonts + images embedded) |
| `generate_guide.py` | Regenerates the HTML from data (run from this folder) |
| `goodrx.png`, `tresapp.png` | Third-party graphics carried over from the source PDF |
| `*.b64` | Base64 copies of the images/logo embedded by the generator |

Let me know if you'd also like this as an editable .docx for HR to maintain directly in Word.
