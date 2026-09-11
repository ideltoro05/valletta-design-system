# Physical Security Force Culture — Valletta Redesign

Redesign of `Potential_Culture_Slide.pdf` applying the Valletta Industries
design system (`../DESIGN_SYSTEM.md`, `../tokens.json`). All original text
(titles, subheads, bullet points, mindset quotes, ring tagline, values,
closing banner) is unchanged — only the visual system was replaced:

- Black / Field White / single red accent palette (no rainbow wedge colors)
- Oswald (headlines) + Inter (body/labels), per the system's Claude-Design
  font guidance
- Thin red "tick"/divider motif on wedge boundaries and corner accents
- Same composition as the original: one wheel with a curved title arc,
  5 numbered pillar wedges (badge + icon + title + subhead + bullets +
  mindset quote, directly in the wedge), a center "core purpose" medallion,
  an inner tagline ring, a curved values line, and a closing banner
- Combined Valletta Industries + SOC logo lockup (extracted from Bryan
  Paarmann's email signature, saved at `../assets/logo/`) placed above the
  wheel for brand attribution

## Files

| File | Format |
|---|---|
| `valletta_culture_slide.png` | High-res raster (3072x3760, 4x) |
| `valletta_culture_slide.pdf` | Vector PDF, 8x9.79in page |
| `valletta_culture_slide.pptx` | PowerPoint, one 8x9.79in slide |
| `valletta_culture_slide.html` | Self-contained source (fonts + logo embedded) |
| `generate_slide.py` | Regenerates the HTML from data (run from this folder) |
| `fonts_embed.css` | Base64-embedded Oswald/Inter used by the HTML |
| `logo_b64.txt` | Base64 logo lockup embedded by the generator |
