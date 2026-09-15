# Contractor Combined Weekly Activity Report — Valletta Rebrand

Rebrand of `CIFSO_Contractor_Combined_Weekly_Activity_Report_09-10-2026.docx`
in the Valletta Industries design system (`../../DESIGN_SYSTEM.md`,
`../../tokens.json`). Visual rebrand only — every number, name, and label
across all 25 source tables is unchanged.

## Why this one was built differently

This is by far the largest and most data-dense document rebranded in this
repo so far: 25 tables (staffing, post hours, terminations, vehicle
inspections, truck entries, DEA cage entries, incident totals, notable
visitors, trainer hours, in-service and new-hire training, PFT results,
pending leave) spanning 30 section headings. With that much numeric data
across that many tables, hand-retyping it the way the earlier
narrative-style rebrands in this repo were built (typing the source text
directly into the generator) was too failure-prone — one transposed digit
in a 13-column table is easy to miss on review.

Instead, `extract_source.py` walks the source `.docx` body in document
order with `python-docx`, capturing every heading paragraph and every table
cell (normalizing non-breaking spaces and trimming stray whitespace, but
keeping each cell's internal line breaks intact) into `source_data.json`.
`generate_activity_report.py` and `build_docx.js` both render directly from
that JSON — so the rebrand is a faithful, programmatic copy of the source
table data rather than a manual transcription, and the same JSON drives
both the PDF and the docx builds.

Two content oddities in the source, both preserved verbatim rather than
"cleaned up," since this is a rebrand and not a copyedit:

- A standalone heading paragraph reading just **"S"** appears immediately
  before "SOW Required Weekly Training:" — almost certainly a leftover
  keystroke from editing, but not something to silently delete.
- **"OPERATIONS"** appears as a section heading twice in a row (before
  "# Vehicle Inspections and Visitors" and again before "Total Truck Entry
  by Type"), and **"Physical Fitness Test – Retest"** appears as two
  separate headings back to back (one over an empty N/A table, one over
  the actual populated retest data) — both exactly as the source has them.

Rows that were fully blank across every column (a handful of leftover
template rows, e.g. one at the end of the DEA Cage Entries table) were
dropped as empty template rows, not data — the same kind of formatting-noise
cleanup applied in earlier rebrands in this repo, never touching a cell
that actually held content.

## Design

- Landscape US Letter, the same title-block header treatment (Valletta
  mark + report title + reporting period) used in the sibling Incident
  Report Log rebrand, rather than a separate cover page — this is a working
  operational report, not training collateral
- Major section dividers (Cifso Contractor Staffing, Operations, Contract
  Incident Reports, Daily Activity Report – Executive Summary, Training
  Summary) as full-width black bands
- Each table's own caption as a smaller red-ruled sub-heading
- Data tables with a black header row, alternating row shading, and a
  tinted, bold "Total/Totals/Contract Totals" row where the source has one
- First column (Location/Type/Name) fixed wider than the rest; remaining
  columns share the page width evenly, since column counts range from 2 to
  13 across the 25 tables

Blocks (heading(s) + table) were packed by measuring each block's real
height and filling each landscape page as full as it reasonably goes, the
same approach used throughout this repo. Result: 10 pages, no overflow.

## A bug avoided (learned from the Incident Report Log rebrand)

The `docx` package's `page.size` expects the *portrait* base width/height
when `orientation` is set to landscape and swaps them internally — passing
already-landscape numbers double-swaps them into a mis-flagged page size.
That bug was caught and fixed in the Incident Report Log rebrand
(`../incident-log/`); this build uses the corrected pattern from the start
(portrait 8.5in × 11in base dimensions, `orientation: "landscape"`), and the
result was confirmed correct here too (11in × 8.5in landscape, `LANDSCAPE`
orientation flag).

## Files

| File | Format |
|---|---|
| `valletta_weekly_activity_report.pdf` | Print-ready PDF, US Letter landscape, 10 pages |
| `valletta_weekly_activity_report.docx` | Editable Word document, US Letter landscape |
| `valletta_weekly_activity_report.html` | Self-contained source (fonts + logo embedded) |
| `source_data.json` | Extracted source content (headings + full table data), drives both builds |
| `extract_source.py` | Re-extracts `source_data.json` from the original `.docx` |
| `generate_activity_report.py` | Regenerates the HTML/PDF from `source_data.json` |
| `export_pdf.py` | Renders the HTML to PDF via Playwright |
| `build_docx.js` | Regenerates the .docx from `source_data.json` (`node build_docx.js`) |

Same note as the earlier rebrands: this sandbox can't run LibreOffice to
render a visual preview of the `.docx`, so it was verified structurally —
all 25 tables and all 30 headings confirmed present in the correct order,
dozens of individual data points spot-checked against the source, landscape
page geometry confirmed correct in the raw XML, zip integrity checked. Give
it a look in Word and flag anything off.
