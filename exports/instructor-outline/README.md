# Leadership Course Instructor Outline — Valletta Rebrand

Rebrand of `Leadership_Course_Instructor_Outline_FINAL_V2_-_Copy.docx` in the
Valletta Industries design system (`../../DESIGN_SYSTEM.md`, `../../tokens.json`).
Visual rebrand only — every paragraph of instructor script, every video/discussion
cue, every speaker bio, every quote and attribution, the statistics list, the
overview list, and the Additional Reading list are transcribed unchanged from
the source (all 358 source paragraphs accounted for). Two things carried over
faithfully as genuine quirks of the source rather than "fixed": the sentence
"Often an effective will be managing multiple tasks..." (a dropped word in the
original), and this instructor version's Additional Reading list, which is
missing "Leaders Eat Last – Simon Sinek" compared to the student handout —
that's a real difference between the two source documents, not an omission
introduced here.

The source was branded for SOC (gold/black geometric cover template, a running
"Leadership Instructor Outline" header banner, the SOC "A Day & Zimmermann
Company" logo). This version carries the same content and structure in the
Valletta black/red/white system:

- Cover: black page, Valletta shield + wordmark, "Instructor Outline" eyebrow,
  same treatment as the other rebranded covers in this repo
- Masthead: the Valletta mark + running "Leadership Instructor Outline" title
  with a red rule, repeating on every content page
- Course metadata (Time / Method of Instruction / Description / Special
  Requirements / Instructional Aides) as a bordered info box on page one
- Section headings in Oswald/Bookman Old Style with a red rule beneath
- Video and Discussion cues as tinted callout boxes with a red left border
  and a red uppercase tag (VIDEO 1–4, DISCUSSION, SCRIPT, OODA LOOP)
- Speaker/author bios (Travis Mills, David Goggins, John Maxwell, Jocko
  Willink) set as small italic asides, distinct from the main instructor
  script
- Pull-quotes styled with a red left border, matching the mindset-quote
  treatment used across the other rebranded pieces
- The gold "OVERVIEW" banner becomes a black band with the same list
  underneath; "CONCLUSION" gets the same band treatment
- Additional Reading as a bulleted list with the red square marker

Pages were packed by measuring each content block's real height and filling
each page as full as it reasonably goes, same approach as the benefits guide
and student handout. A few of the longer sections (Observing Effective
Follower Traits, Understanding the Mission or Task, Describe Motivational
Leadership) were split into finer packing units — title+lead-in as one unit,
supporting paragraphs/bios as another — purely so the algorithm could use
leftover space on a page instead of stranding a short section alone on an
otherwise-empty page. This is a packing-granularity change only; it does not
reorder or alter any content. The result is 9 pages (plus cover) with no
overflow on any page, down from an initial 10-page pass with two pages sitting
under 50% full.

## Files

| File | Format |
|---|---|
| `valletta_instructor_outline.pdf` | Print-ready PDF, US Letter, 9 pages |
| `valletta_instructor_outline.docx` | Editable Word document, US Letter |
| `valletta_instructor_outline.html` | Self-contained source (fonts + logo embedded) |
| `generate_outline.py` | Regenerates the HTML/PDF from data (run from this folder) |
| `export_pdf.py` | Renders the HTML to PDF via Playwright |
| `build_docx.js` | Regenerates the .docx from data (`node build_docx.js`) |

Same note as the earlier rebrands: this sandbox can't run LibreOffice to
render a visual preview of the `.docx`, so it was verified structurally
(every section checked present, header/footer/page-numbering confirmed, zip
integrity checked, both logo images confirmed embedded) rather than by eye.
Give it a look in Word and flag anything off.
