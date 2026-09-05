# Physical Security Force Culture — Valletta Redesign

Redesign of `Potential_Culture_Slide.pdf` applying the Valletta Industries
design system (`../DESIGN_SYSTEM.md`, `../tokens.json`). All original text
(titles, subheads, bullet points, mindset quotes, ring tagline, values,
closing banner) is unchanged — only the visual system was replaced:

- Black / Field White / single red accent palette (no rainbow wedge colors)
- Oswald (headlines) + Inter (body/labels), per the system's Claude-Design
  font guidance
- Thin red "tick" motif on corner accents and leader lines
- Hub-and-spoke layout: a compact wheel (core purpose + 5 numbered pillars)
  with each pillar's full bullet detail in a surrounding card, so all
  original copy stays fully legible at presentation size

## Files

| File | Format |
|---|---|
| `valletta_culture_slide.png` | High-res raster (3072x3072) |
| `valletta_culture_slide.pdf` | Vector PDF, 8x8in page |
| `valletta_culture_slide.pptx` | PowerPoint, one 8x8in slide |
| `valletta_culture_slide.html` | Self-contained source (fonts embedded) |
| `generate_slide.py` | Regenerates the HTML from data (run from this folder) |
| `fonts_embed.css` | Base64-embedded Oswald/Inter used by the HTML |
