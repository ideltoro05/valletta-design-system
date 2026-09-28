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
| `valletta_site_visit_assessment_whiskey.docx` | Flattened native Word document, US Letter |
| `sva_data.py` | Transcribed field names, options, current values, and the calc script (verified against the source) |
| `generate_sva.py` | Builds the PDF via PyMuPDF — page content, section bands, and all 60 form widgets |
| `build_docx.js` | Builds the flattened docx via the `docx` npm package |
| `fonts/` | Static-weight Inter/Oswald instances used for the painted (non-field) text |

## About the .docx version

The PDF is the authoritative version of this document — it's the only format
that keeps the assessment interactive (working rating dropdowns and the live
`total_score` recalculation). AcroForm widgets don't have a Word equivalent,
so the docx is a **flattened snapshot**: every visit field, question,
current rating, and current comment is reproduced as static text, styled to
match the PDF (black section bands, red question numbers, bordered rating
and comment fields). Picking a different rating or editing a comment in Word
won't recalculate the total score — that only happens in the PDF. Unrated
questions ("Select...") show as an em dash rather than the literal
placeholder text, since a blank/dash reads more naturally in a static
document than a dropdown placeholder does.

The docx was validated with `python-docx`: zip integrity, all 26 question
numbers present in order, all 5 section headers, the visit-info fields, a
sample of the entered comments, and the total score value all confirmed
present and matching `sva_data.py`.

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

## 2026-09-28 update: split into two forms, cobalt v2.0, narrative-box bug fix

Per request: the single 26-question form was hard to use because whoever owns
Sections III–V (Training and Personnel Readiness, Equipment/Weapons/Emergency
Readiness, Overall Performance) received a copy where the first ~11 questions
(Sections I–II, someone else's job) showed as N/A — looked incomplete to the
client. Built via a new script, `generate_sva_split.py`, which produces two
independent interactive PDFs from the same `sva_data.py` source:

| File | Covers | Questions |
|---|---|---|
| `valletta_site_visit_assessment_whiskey_staffing_leadership.pdf` | Section I (Staffing and Post Operations), Section II (Leadership, Supervision and Management) | 1–11, unchanged from the original numbering |
| `valletta_site_visit_assessment_whiskey_training.pdf` | Original Section III renumbered to I (Training and Personnel Readiness), original IV renumbered to II (Equipment, Weapons and Emergency Readiness), original V renumbered to III (Overall Performance and Support Requirements) | 1–15, renumbered so the document reads as its own complete form |

**Only the visible section/question numbers and the internal field names
changed to match them** — every question's text, every dropdown's option
list, every currently-selected rating, and every typed comment is unchanged
from `sva_data.py`. Verified three ways: (1) every rating/comment/option-list
diffed field-by-field against the source with the correct renumbering
mapping applied — zero mismatches; (2) every question's text confirmed
verbatim (whitespace-normalized) in the rendered PDF's extracted text; (3)
full visual review of both documents' screenshots.

**Total score is now scoped per document.** The original calculation script
summed all 26 questions across 5 sections; reusing it as-is on a split
document would have silently ignored the questions that moved to the *other*
document (their fields no longer exist there) and produced a technically
different — and easily misread — number. Each split PDF gets its own
calculation script, built from the actual section/question ranges present in
that document, still scaled to a 0–500 total on the same formula as the
original. Cross-checked the static pre-filled score against the same math by
hand for both documents (Staffing & Leadership: 433/500; Training, Equipment
& Overall Performance: 411/500) — both correct.

**Narrative-box bug, root cause found and fixed.** The complaint was that the
narrative summary boxes only allowed about one line of typed text. The box
height and the multiline flag (`Ff` bit 4096) were already correct — the
actual cause was `/MaxLen 100`: PyMuPDF's `Widget.text_maxlen` defaults to
100 characters when left unset, and the original `add_text_widget` helper
never set it explicitly. That 100-character cap silently applied to *every*
text field in the document (comments too, not just the narrative boxes) —
it just wasn't noticed on the comment fields because none of the filled-in
comments happened to exceed 100 characters. Fixed by explicitly setting
`w.text_maxlen = 0` (no limit) on every text widget, confirmed at the raw
PDF level (`pypdf`) that the `/MaxLen` key is now absent entirely from both
narrative fields, not just reported as 0 by the wrapper API. Narrative boxes
were also made taller (70pt → 130pt) so there's visibly more room to write
into, per the request to "utilize the whole box."

**Rebrand:** same v2.0 system as the rest of the document package — Valletta
Cobalt (`#1B4FA0`) replacing red, and the combined Valletta + SOC lockup
(`valletta-soc-lockup.png`) in place of the Valletta-only mark used in the
first pass of this document.

Functionality preserved and re-verified on both split PDFs: all rating
dropdowns present with their exact original option lists, `NeedAppearances`
set, comment/narrative fields multiline with no length cap, and the
`total_score` field read-only with a working calculation script.
