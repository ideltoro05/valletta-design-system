# Door Security Training Package — Valletta Rebrand

Branding of five previously-unbranded Door Security Verification & Alarm
Response training documents in the Valletta Industries design system v2.0
(`../../DESIGN_SYSTEM.md`, `../../tokens.json`).

| Source | Output |
|---|---|
| `Door_Security_Curriculum_1.docx` | `valletta_Door_Security_Curriculum.docx` |
| `DoorSecurity_Module1_Training_Video_Transcript_1.docx` | `valletta_DoorSecurity_Module1_Training_Video_Transcript.docx` |
| `DoorSecurity_Module2_Training_Video_Transcript_1.docx` | `valletta_DoorSecurity_Module2_Training_Video_Transcript.docx` |
| `DoorSecurity_Module3_Training_Video_Transcript_1.docx` | `valletta_DoorSecurity_Module3_Training_Video_Transcript.docx` |
| `DoorSecurity_Module4_Training_Video_Transcript_1.docx` | `valletta_DoorSecurity_Module4_Training_Video_Transcript.docx` |

**Branding only — content unchanged.** Every word of every document is
untouched. Like the NBAF reports rebrand, this is an **in-place edit**:
`rebrand_door_security.py` only ever rewrites XML *attribute values* (hex
color codes, font-family name strings) or adds wholly new structural parts
(header, footer, their relationships, the logo image, and the
content-type/relationship declarations that wire them in) — it never
rewrites a `<w:t>` text node. Verified afterward by extracting every text
node from each source and its rebranded output and diffing them: identical,
zero mismatches, in all five documents.

Unlike the NBAF reports, these five documents had **no existing branding at
all** — no logo, no header, no footer, just Word-default styling (generic
Office heading colors, Arial/Times New Roman/Georgia). "Branding" here
means adding the standard Valletta identity from scratch, not swapping an
existing one.

## What changed

- **Header**: new header added to every document — the combined Valletta +
  SOC lockup logo, with a thin cobalt rule beneath it (the same template
  used in the NBAF reports header, reused as-is for consistency across this
  engagement).
- **Footer**: new footer added to every document — centered, muted gray
  text reading `Valletta Industries | <document title> | Page X of Y`,
  using real `PAGE`/`NUMPAGES` field codes so the page count stays correct
  if the document is edited later.
- **Colors**: these documents each used an ad hoc Word-default accent
  (navy `#2B2D6E` in the curriculum, "Automatic" blues `#2E74B5`/`#1F4D78`
  in the transcripts) for headings and table styling. Remapped by role, not
  blanket substitution:
  - **Large background fills** (the curriculum's table header-row bands) →
    **black** (`#0A0A0A`), matching the black-header-band convention used
    throughout this design system.
  - **Text and thin accents** (heading colors, the subtitle underline rule)
    → **Valletta Cobalt** (`#1B4FA0`), including on two heading styles
    (`Heading4`/`Heading5` in the curriculum, `Subtitle` in the
    transcripts) that exist in the stylesheet but aren't applied to any
    paragraph in these documents — updated anyway for consistency, at zero
    risk since nothing currently uses them.
  - Neutral, non-brand colors were left as-is: light table gridlines
    (`#BFC3D9`), the byline gray (`#666666`), ordinary black body text, and
    white text on dark fills (correct regardless of the fill's color).
- **Typography**: headings and body text swapped to this design system's
  Bookman Old Style (headings) / Calibri (body), replacing each
  document's own mix of Arial, Arial Unicode MS, Times New Roman, and
  Georgia.
  - The curriculum sets its body font via a literal `docDefaults` override
    (`Arial`), so it was replaced directly, along with a handful of direct
    per-run font overrides in the body text itself.
  - The four transcripts set no literal body-font override at all — their
    body text inherits from the *theme*, so only the theme's `minorFont`
    (`Cambria` → `Calibri`) needed to change; no document-body edits were
    necessary for these four files.
- **Logo**: the combined Valletta + SOC lockup (`valletta-soc-lockup.png`),
  sized `1130910×868680` EMU — the same size used in the NBAF reports,
  already correctly aspect-ratio-adjusted for this asset (694×533,
  1.302:1).

## Verification

- Zip integrity confirmed for all five output files
- **Every `<w:t>` text node in `document.xml` extracted and diffed against
  the source — identical, zero mismatches, in all five documents**
- No residual instances of the old accent colors or the old font names
  (Arial, Arial Unicode MS, Times New Roman, Georgia) anywhere they were
  supposed to be replaced
  - Two intentionally-untouched exceptions, both harmless: `word/fontTable.xml`
    is inert font-declaration metadata that doesn't drive rendering (not
    patched in the NBAF rebrand either, for the same reason), and
    `theme1.xml`'s non-Latin script-fallback typefaces (`a:font
    script="Arab"`/`"Hebr"`, used only if the document ever contained
    Arabic or Hebrew text) retain their Office-default values — neither is
    the Latin typeface that actually renders this English-language content
  - Fixed in a second pass after the first verification run caught them: a
    `w:cs`/`w:eastAsia` pair of "Arial Unicode MS" overrides in the
    curriculum's body, and the `Heading4`/`Heading5` and `Subtitle`
    styles' leftover accent color/font (unused by any paragraph, but
    corrected anyway)
- Logo image confirmed byte-identical to the canonical
  `valletta-soc-lockup.png` asset in all five
- `sectPr` confirmed to reference the new header/footer relationship IDs,
  and `document.xml.rels` / `[Content_Types].xml` confirmed well-formed
  with the new entries, in all five

As with every other native `.docx` deliverable in this repo, no
LibreOffice preview was available in this environment to visually confirm
rendering (confirmed broken again this session) — the text-node-level
content diff, plus structural XML verification, was used instead.

## Files

| File | Purpose |
|---|---|
| `rebrand_door_security.py` | Reads each source docx, rewrites the color/font attribute values described above, adds the new header/footer/logo parts, writes the branded docx |
| `valletta-soc-lockup.png` | The combined logo asset embedded in each file's header |
| `valletta_Door_Security_Curriculum.docx` | Branded course curriculum |
| `valletta_DoorSecurity_Module1-4_Training_Video_Transcript.docx` | Branded module transcripts |
