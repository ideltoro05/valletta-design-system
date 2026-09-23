# Site Visit Assessment (Whiskey, Sep 2026) — Valletta Rebrand

Rebrand of `Whiskey_SVA_Sep_26.pdf` in the Valletta Industries design system
(`../../DESIGN_SYSTEM.md`, `../../tokens.json`). Visual rebrand only — every
field name, dropdown option, entered rating, entered comment, and the score
calculation are unchanged.

## Why this one was built differently

Every other rebrand in this repo started from a Word document and produced a
static PDF/HTML/docx. This source is different in a way that matters: it's
an **interactive PDF form** (an AcroForm), not flat content. It has 60 real
form fields — 5 visit-info text fields, 26 rating dropdowns with their own
option lists, 26 matching comment fields, 2 narrative text fields, and a
`total_score` field with an attached JavaScript calculation script that
re-scores the assessment live as ratings are picked. This particular copy is
also a **filled-in instance** (site Whiskey, visited 15 September 2026 by
Michael Flanagan/NTM, several questions already rated and commented on), not
a blank template.

Flattening this to an image-based PDF (the HTML+Playwright pipeline used
everywhere else in this repo) would have thrown away the thing that makes
this document useful — nobody could pick a rating or have the score
recalculate. So this rebrand was built with `PyMuPDF` instead, which can both
paint the branded page content (text, rules, section bands, the logo) *and*
create real AcroForm widgets — dropdowns, text fields, and a calculated
field — on top of it.

**Fidelity approach:** every field name, every dropdown's option list, every
currently-selected rating, every typed comment, and the `total_score`
calculation script were read out of the source PDF programmatically via
`pypdf` (`sva_data.py` holds the transcribed result) and then verified
against the source a second time in a separate pass — zero discrepancies on
all 60 fields, and the 26 question strings and 5 section headers were
confirmed to appear verbatim in the source's extracted text. The
`total_score` JavaScript itself is copied byte-for-byte from the source and
reattached to the field in the rebuilt PDF, so live score recalculation
behaves identically to the original.

## A real design-system violation, corrected

The source used solid **red-filled bands** for its five section headers.
This repo's own `../../DESIGN_SYSTEM.md` is explicit that Valletta Red is
"a precision accent, not a background color" and should cover roughly
5–10% of a layout, never a large fill. That's not a stylistic nitpick — it's
the documented rule this project has followed in every other rebrand here
(black bands for section dividers, red reserved for rules, labels, and small
accents). This rebrand corrects that: section bands are black with white
text, and red is used only for the title underline, field labels, sub-head
rules, and the question numbers — consistent with every other document in
this repo.

The source also carried a combined "Valletta + SOC" lockup image in its
header (the mid-rebrand co-branding visible across this whole project's
source material). This version uses the plain Valletta mark on its own,
matching the fully-rebranded logo treatment used everywhere else here.

## Fonts

PyMuPDF needs real font files, not the base64-embedded WOFF2 this repo's
HTML pipeline uses. `Inter` and `Oswald` here are variable fonts (a single
file with a `wght` axis), and PyMuPDF doesn't render variable-font weight
selection — so `fonts/` holds *static instances* pinned at specific weights
(Inter 400/600/700, Oswald 500/700), generated once from the same font data
as `../fonts_embed.css` via `fontTools.varLib.instancer`. Interactive
form-field *input* text (what you type into a field) uses the PDF base14
Helvetica (`Helv`) rather than the embedded fonts — form widget appearance
strings don't reliably carry custom embedded fonts across PDF viewers, and
the source used a plain sans for field input too, so this isn't a visible
regression.

## Files

| File | Format |
|---|---|
| `valletta_site_visit_assessment_whiskey.pdf` | Interactive fillable PDF, US Letter, 7 pages |
| `sva_data.py` | Transcribed field names, options, current values, and the calc script (verified against the source) |
| `generate_sva.py` | Builds the PDF via PyMuPDF — page content, section bands, and all 60 form widgets |
| `fonts/` | Static-weight Inter/Oswald instances used for the painted (non-field) text |

No `.docx` for this one — AcroForm interactivity (dropdowns, a live
calculated field) doesn't have a Word equivalent worth producing; a docx
export would just be a flat, non-functional copy.

## Verification

Since this needed to remain a *working* form, not just a good-looking one,
verification went beyond visual QA:

- All 60 field names, types, dropdown option lists, and current values
  diffed against the source with zero discrepancies
- All 26 question strings and 5 section headers confirmed present verbatim
  in the source's extracted text
- The `total_score` calculation script confirmed byte-for-byte identical to
  the source's and correctly re-attached to the field
- `NeedAppearances` set on the AcroForm (the source had it too), so viewers
  regenerate field appearances from current values rather than trusting a
  possibly-stale cached appearance stream
- Every page's widgets checked to confirm none crowd the footer or run off
  the page

One layout bug was caught and fixed during review: the first pass wrapped
question text without reserving space for the "NN." number prefix, so two
of the longer first lines (Q15, Q24) ran into the rating dropdown box.
Fixed by reserving a fixed indent for the prefix before wrapping.
