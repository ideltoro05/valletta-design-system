# Leadership Course Student Handout (V3 lineage) — Valletta Rebrand

Rebrand of `Leadership_Course_Student_Handout_-_Copy.docx` in the Valletta
Industries design system (`../../DESIGN_SYSTEM.md`, `../../tokens.json`).
Visual rebrand only — every word of the outline is unchanged.

This is the terse student-facing companion to `../leadership-outline-v3/`
(the "SOC Delaune V3" outline) — same lettered A.–F. structure, same
"Makes the team a priority" wording (not "Prioritizes the Team," which is
what the *other*, differently-lineaged student handout already in this
repo, `../leadership-handout/`, uses). The two student handouts in this
repo are genuinely different source files from different course revisions;
this one was transcribed from its own source, not reused from the other.

Word's own outline numbering in the source (`ilvl` on each list paragraph)
isn't literal text, so the visible "1./2./3." and "a./b./c." labels here are
a faithful reconstruction of what the list numbering would render as in
Word, not invented content — verified level-by-level against the source
document's paragraph formatting before transcribing.

One structural note worth flagging: Section B ("Examples of Effective
Leadership") lists the four leader types as a plain bulleted list with no
outline letters in the source (unlike Section A, whose items do carry
literal "a./b./c." prefixes in the text) — rendered here as plain red-square
bullets rather than force-fitting a lettered-outline look, to match what's
actually in the source.

The source was branded for SOC (gold/black geometric shapes, a gold
"OVERVIEW" banner, gold section rules, the SOC "A Day & Zimmermann Company"
logo). This version carries the same structure and depth in the Valletta
black/red/white system:

- Cover: black page, Valletta shield + wordmark, the same John Quincy Adams
  quote the source opens with
- Masthead: the Valletta mark + running title with a red rule, repeating on
  every content page
- Lettered section headings (A.–F., Oswald/Bookman Old Style, red letter,
  red rule beneath) replacing the gold banner/rule treatment
- Outline labels (1./2./3., a./b./c.) in red bold as the recurring accent,
  body text in charcoal — no color-coded backgrounds
- Pull-quotes (Jocko Willink, David Goggins, John Quincy Adams, the
  Followers passage) styled with a red left border, matching the
  mindset-quote treatment used across this repo's rebrands
- Additional Reading as a bulleted list with the red square marker

Pages were packed by measuring each block's real height and filling each
page as full as it reasonably goes, same approach as the other rebrands.
Result: 5 pages (plus cover) with no overflow on any page.

## Files

| File | Format |
|---|---|
| `valletta_student_handout_v3.pdf` | Print-ready PDF, US Letter, 5 pages |
| `valletta_student_handout_v3.docx` | Editable Word document, US Letter |
| `valletta_student_handout_v3.html` | Self-contained source (fonts + logo embedded) |
| `generate_handout_v3.py` | Regenerates the HTML/PDF from data (run from this folder) |
| `export_pdf.py` | Renders the HTML to PDF via Playwright |
| `build_docx.js` | Regenerates the .docx from data (`node build_docx.js`) |

Same note as the earlier rebrands: this sandbox can't run LibreOffice to
render a visual preview of the `.docx`, so it was verified structurally
(every section checked present, the "Makes the team a priority" wording
confirmed and the other document's "Prioritizes the Team" wording confirmed
absent, header/footer/page-numbering confirmed, zip integrity checked, both
logo images confirmed embedded) rather than by eye. Give it a look in Word
and flag anything off.
