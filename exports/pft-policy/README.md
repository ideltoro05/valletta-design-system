# PFT Policy and Administration Plan — Valletta Redesign

Visual redesign of `PFT_v1.docx` (Physical Fitness Test Policy and Administration
Plan, HHS/ASPR Strategic National Stockpile Protective Services, Task Order
75A50326F80009 Appendix D) in the Valletta Industries design system v2.0
(`../../DESIGN_SYSTEM.md`, `../../tokens.json`, `../../COBALT_REBRAND_PLAN.md`).

**Redesign only — content is unchanged.** Per the request, no title, section number,
paragraph, bullet, or table value was reworded, reordered, or altered. Every word and
number in this document (including the 10 government fitness-standard tables and the
verbatim test-administrator read-out scripts) is byte-identical to the source.

## How content fidelity was verified

The source docx was read via `python-docx` walking the document body in true element
order (paragraphs and tables interleaved as they actually appear — not python-docx's
separate `.paragraphs`/`.tables` lists, which lose that order) and saved to
`pft_data.json`: 81 items, 68 paragraphs and 13 tables. `build_docx.js` renders
**from that JSON**, not from retyped text, which removes transcription risk entirely
(the same approach used for `sva_data.py` and `source_data.json` elsewhere in this
repo). After building, the output docx was walked the same way and diffed
item-by-item against `pft_data.json` — **zero mismatches** across all 81 items.

One subtlety this caught: several labels (table headers, section sub-heads, the four
event names) are styled in small-caps/all-caps for visual consistency with the rest of
this design system. The first pass did this by calling `.toUpperCase()` on the actual
source text, which — though it looks identical on the page — silently changes the
underlying document content ("Push-Ups" becomes "PUSH-UPS" as stored text, not just
as a display effect). Caught by the verification diff and fixed by switching to
Word's `allCaps` character property (`w:caps`) instead, which displays the text in
capitals without altering the stored text at all. The diff came back clean only
after that fix.

## Design treatment

Same v2.0 system as the rest of this document package: Valletta Cobalt (`#1B4FA0`)
accents, the combined Valletta + SOC lockup in the header, Bookman Old Style section
headings, 1in margins. The document is unusually table-heavy (13 tables — a document
control block, two summary tables, and ten age/gender fitness-standard tables), so
its table styling reuses the black-header-row / zebra-striped-body convention
established for `../incident-log/` rather than inventing a new one, since that's
already this repo's precedent for a dense data table.

One inconsistency in the source was smoothed over as a matter of visual
formatting, not content: section "11. STANDARDIZED PFT EVENT READ-OUTS" was styled
as plain body text in the source Word doc while sections 1–10 used its Heading 1
style — clearly a numbered section by its own text, just inconsistently tagged. It's
rendered here with the same section-heading treatment as 1–10. The text itself is
unchanged.

A stray backtick character at the end of the Section 3 paragraph
("...unless otherwise directed by the COR/designee.`") appears to be a source typo,
but per the redesign-only instruction it was left exactly as-is rather than corrected.

## Files

| File | Purpose |
|---|---|
| `valletta_pft_policy.docx` | The redesigned document, US Letter |
| `pft_data.json` | Source content extracted in true document order (81 items), used to drive the build and to verify the output |
| `build_docx.js` | Builds the docx from `pft_data.json` |

Delivered as docx only (the source was docx), per the package's format rule.
