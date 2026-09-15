# Contractor Combined Incident Report Log — Valletta Rebrand

Rebrand of `CIFSO_Contractor_Combined_Incident_Report_Log_09-10-2026.docx`
in the Valletta Industries design system (`../../DESIGN_SYSTEM.md`,
`../../tokens.json`). Visual rebrand only — every site, incident, case
number, date, and status/action line is transcribed unchanged from the
source table (all 18 data rows).

This document is a different kind of piece from the leadership-training
rebrands elsewhere in this repo: it's a working weekly security/facilities
incident log (a single 5-column table — Site / Type / Incident Description
/ Date / Status & Action Taken), not training material, and the source
carried no SOC branding or logo to begin with (blank header/footer, no
embedded images). So this is a fresh professional format built around the
Valletta system rather than a swap-out of someone else's branding.

One naming note: the source's document-properties metadata title reads
"reporting period 8/21-27/2026," but that's stale leftover metadata, not
visible content in the document body — every actual incident date in the
table falls between 9/4 and 9/10/2026 (matching the "09-10-2026" in the
filename). The rebrand's title block uses the real date range found in the
data (9/4 – 9/10/2026) rather than repeating the stale metadata string,
since there was no visible in-document title to preserve verbatim in the
first place.

Design:

- Landscape US Letter, black-on-white header band with the Valletta mark,
  document title, and reporting period — no separate cover page, since a
  full-bleed divider doesn't suit a working operational log the way it did
  the training decks
- Data table with a black header row, alternating row shading, and the
  case number set as a small steel-gray line under each incident
  description for quick scanning
- Status column leads with **OPEN** (red) or **CLOSED** (steel gray) pulled
  directly from each row's own text, so open items are visually easy to
  spot — a formatting emphasis, not an added judgment call, since "Open"
  and "Closed" are literally how the source itself labeled each row
- Repeating table header and running footer with page numbers across all
  pages

Rows were packed by measuring each row's real rendered height and filling
each landscape page as full as it reasonably goes. Result: 3 pages, no
overflow.

## A bug worth flagging

The first docx build had a real defect, not just a preview artifact: passing
`page.size` with landscape width/height directly (11in × 8.5in) alongside
`orientation: "landscape"` produced a page.xml with `w:w="12240" w:h="15840"
w:orient="landscape"` — portrait dimensions with a landscape flag, which
Word could render unpredictably. The `docx` package's `page.size` expects
the *portrait* base width/height when `orientation: LANDSCAPE` is set and
swaps them internally; passing already-landscape numbers double-swaps them.
Fixed by passing the portrait base dimensions (8.5in × 11in) and letting the
library perform the swap — confirmed in the raw XML afterward
(`w:w="15840" w:h="12240"`, i.e. 11in wide × 8.5in tall).

## Files

| File | Format |
|---|---|
| `valletta_incident_report_log.pdf` | Print-ready PDF, US Letter landscape, 3 pages |
| `valletta_incident_report_log.docx` | Editable Word document, US Letter landscape |
| `valletta_incident_report_log.html` | Self-contained source (fonts + logo embedded) |
| `generate_incident_log.py` | Regenerates the HTML/PDF from data (run from this folder) |
| `export_pdf.py` | Renders the HTML to PDF via Playwright |
| `build_docx.js` | Regenerates the .docx from data (`node build_docx.js`) |

Same note as the earlier rebrands: this sandbox can't run LibreOffice to
render a visual preview of the `.docx`, so it was verified structurally —
19 table rows (1 header + 18 data) confirmed, every site name and case
number confirmed present, page orientation and dimensions confirmed correct
in the raw XML after the fix above, zip integrity checked. Give it a look in
Word and flag anything off.
