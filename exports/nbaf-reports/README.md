# NBAF Security Services Reports — Valletta Rebrand

In-place branding update of three September 2026 NBAF (National Bio and
Agro-Defense Facility) reports in the Valletta Industries design system v2.0
(`../../DESIGN_SYSTEM.md`, `../../tokens.json`):

| Source | Output |
|---|---|
| `Valletta_NBAF_Completed_Training_Summary_September.docx` | `valletta_NBAF_Completed_Training_Summary_September.docx` |
| `Valletta_NBAF_Incident_Report_September.docx` | `valletta_NBAF_Incident_Report_September.docx` |
| `Valletta_NBAF_Monthly_Report_September.docx` | `valletta_NBAF_Monthly_Report_September.docx` |

**Branding only — content unchanged.** Every word of every report is
untouched. This wasn't rebuilt from scratch like the other documents in this
repo; it's an **in-place edit** of the original files, which made a strong
content-fidelity guarantee possible: `rebrand_nbaf.py` only ever rewrites
XML *attribute values* (hex color codes, a font-family name, the embedded
logo image, and its size) and never touches a `<w:t>` text node. Verified
afterward by extracting every text node from the source and the rebranded
file and diffing them — identical, in every one of the three documents.

## What changed

- **Logo**: the old Valletta-only mark (black shield, red cross, black
  wordmark) replaced with the combined Valletta + SOC lockup, resized to
  fit the header space the old logo already used (no margin changes
  needed).
- **Colors**: these reports used two legacy accent colors — a red
  (`#DC1E25`) and a navy (`#002451`) — in different places for essentially
  the same job (table header bands, heading/stat-number text, thin border
  accents). Remapped by role, not by blanket substitution:
  - Where either color was a **large background fill** (table header
    row bands) → **black** (`#0A0A0A`), matching the black-header-band
    convention used in every other document in this repo and the design
    system's rule that red/cobalt is an accent, never a large fill.
  - Where either color was **text or a thin border accent** (heading
    color, the big stat-tile numbers, cell-top accent stripes) →
    **Valletta Cobalt** (`#1B4FA0`), unifying what were two different ad
    hoc accent colors into the one official v2.0 accent.
  - A light neutral background tint (`#F3F5F8`, used behind the stat
    tiles) was left as-is — it's a neutral card background, not a brand
    color, and didn't need to change.
- **Typography**: the documents' theme font (Aptos/Aptos Display, Word's
  default) was swapped to this design system's Bookman Old Style
  (headings) / Calibri (body) at the theme and style level — this is a
  pure styling change (theme font-scheme + the `Normal` style's font
  reference), so it took effect without touching any paragraph's actual
  text.

## Verification

- Zip integrity confirmed for all three output files
- **Every `<w:t>` text node in `document.xml`, `header1.xml`, and
  `footer1.xml` extracted and diffed against the source — identical, zero
  mismatches, in all three documents**
- No residual instances of the old red, navy, or dark-gray fill colors, or
  the old font names, in any of the three
- Logo image confirmed byte-identical to the canonical
  `valletta-soc-lockup.png` asset in all three
- Header image extent updated correctly (old logo's aspect ratio was
  2.344:1; the combined lockup's is 1.302:1 — reusing the old extent
  without recalculating it would have stretched the new logo)

As with other native `.docx` deliverables in this repo, no LibreOffice
preview was available in this environment to visually confirm rendering —
the text-node-level content diff (a stronger guarantee for this particular
job, since the whole point was zero content drift) was used instead.

## Files

| File | Purpose |
|---|---|
| `rebrand_nbaf.py` | Reads each source docx, rewrites only the color/font/logo attribute values described above, writes the rebranded docx |
| `valletta-soc-lockup.png` | The combined logo asset swapped into each file |
| `valletta_NBAF_*.docx` | The three rebranded reports, US Letter |
