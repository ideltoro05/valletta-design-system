# Physical Security Force Culture — Valletta Redesign

Redesign of `Potential_Culture_Slide.pdf` as a single impactful one-page
graphic in the Valletta Industries design system (`../DESIGN_SYSTEM.md`,
`../tokens.json`). All original text (titles, subheads, bullet points,
mindset quotes, values, closing banner) is unchanged — only the visual
system was replaced.

This is the third pass. The first kept the source PDF's circular wheel
layout (too cramped, wedge-divider lines crossed the text). The second
dropped the wheel for a long scrolling document (readable, but not the
"one pager" the client expects). This version is a single 2000x950
landscape graphic — no wheel, no scrolling — with the 5 pillars side by
side as clean columns:

- Masthead with the combined Valletta Industries + SOC logo lockup
  (extracted from Bryan Paarmann's email signature, saved at
  `../assets/logo/`)
- Full-bleed black core-purpose band
- 5 pillar columns: number, icon, title, subhead, bullets, mindset quote
- Values line and closing banner in the same black/red/white system

Palette: Operator Black / Field White / a single red accent. Type: Oswald
(headlines) + Inter (body/labels).

**Pending:** the user has newer, higher-quality logo files (a clean
Valletta wordmark, a standalone SOC logo with its "A Day & Zimmermann
Company" line, and an isolated mark) to swap in once provided as actual
file attachments — the masthead currently still uses the earlier
screenshot-cropped lockup.

## Files

| File | Format |
|---|---|
| `valletta_culture_slide.png` | High-res raster, 4000x1900 |
| `valletta_culture_slide.pdf` | Single-page PDF, 20.8x9.9in |
| `valletta_culture_slide.pptx` | PowerPoint, one 13.33x6.33in slide |
| `valletta_culture_slide.html` | Self-contained source (fonts + logo embedded) |
| `valletta_culture_slide_artifact.html` | Responsive version (same design, scales down to phone width) |
| `generate_slide.py` | Regenerates all HTML from data (run from this folder) |
| `fonts_embed.css` | Base64-embedded Oswald/Inter used by the HTML |
| `logo_b64.txt` | Base64 logo lockup embedded by the generator |
