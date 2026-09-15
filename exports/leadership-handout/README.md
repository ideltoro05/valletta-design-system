# Leadership Training Student Handout — Valletta Rebrand

Rebrand of `Leadership_Student_Handout_FINAL_-_Copy_1.pdf` in the Valletta
Industries design system (`../../DESIGN_SYSTEM.md`, `../../tokens.json`).
Visual rebrand only — every word of the outline (all six numbered
sections, every lettered/numbered/lettered sub-point, every quote and
attribution, and the Additional Reading list) is unchanged.

The source was branded for SOC (gold/black/gray geometric shapes, a gold
"OVERVIEW" banner, gold section rules, the SOC "A Day & Zimmermann
Company" logo). This version carries the same outline structure and
depth (1 → A → 1 → a) but in the Valletta black/red/white system:

- Cover: black page, Valletta shield + wordmark, red corner-tick motif
  (same treatment as the culture one-pager and benefits guide covers)
- Masthead: the Valletta mark + running title with a red rule, repeating
  on every content page
- Numbered section headings (Oswald/Bookman Old Style, red number, red
  rule beneath) replace the gold banner/rule treatment
- Outline labels (A./1./a.) set in red bold as the one recurring accent,
  body text in charcoal — no color-coded backgrounds
- Pull-quotes (Jocko Willink, David Goggins, John Quincy Adams, the
  Followers passage) styled with a red left border, matching the
  mindset-quote treatment used in the culture one-pager
- Additional Reading as a bulleted list with the red square marker

Pages were packed by measuring each block's real height and filling each
page as full as it reasonably goes (same approach as the benefits guide),
rather than one section per page — the source's 5 pages became 5 pages
here too, just distributed differently since section breaks don't land
on the same spots once the type and spacing change.

## Files

| File | Format |
|---|---|
| `valletta_leadership_handout.pdf` | Print-ready PDF, US Letter, 5 pages |
| `valletta_leadership_handout.docx` | Editable Word document, US Letter |
| `valletta_leadership_handout.html` | Self-contained source (fonts + logo embedded) |
| `generate_handout.py` | Regenerates the HTML/PDF from data (run from this folder) |
| `build_docx.js` | Regenerates the .docx from data (`node build_docx.js`) |

Same note as the benefits guide: this sandbox can't run LibreOffice to
render a visual preview of the `.docx`, so it was verified structurally
(every paragraph checked against the source, header/footer/page-numbering
confirmed) rather than by eye. Give it a look in Word and flag anything
off.
