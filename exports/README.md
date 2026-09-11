# Physical Security Force Culture — Valletta Redesign

Redesign of `Potential_Culture_Slide.pdf` as a clean editorial document in
the Valletta Industries design system (`../DESIGN_SYSTEM.md`,
`../tokens.json`). All original text (titles, subheads, bullet points,
mindset quotes, ring tagline, values, closing banner) is unchanged — only
the visual system was replaced.

This is the second pass: the first attempt kept the source PDF's circular
wheel layout, which forced very small type and had wedge-divider lines
crossing over text. This version drops the wheel entirely for a flowing,
generously-spaced page — full-size headlines, real body-copy type sizes,
and a clear top-to-bottom reading order — while still hitting every one of
the original's structural beats:

- Masthead with the combined Valletta Industries + SOC logo lockup
  (extracted from Bryan Paarmann's email signature, saved at
  `../assets/logo/`)
- Hero headline + core-purpose statement in a full-bleed black band
- Each of the 5 pillars as its own row: number, icon, title, subhead,
  bullets, and its mindset quote as a pull-quote
- Values line and closing banner in the same black/red/white system

Palette: Operator Black / Field White / a single red accent (never used as
a large fill). Type: Oswald (headlines) + Inter (body/labels), per the
system's Claude-Design font guidance.

## Files

| File | Format |
|---|---|
| `valletta_culture_slide.png` | High-res raster, full document (2000px wide) |
| `valletta_culture_slide.pdf` | Paginated print PDF, US Letter (4 pages) |
| `valletta_culture_slide.pptx` | PowerPoint — one continuous 10x28.15in slide matching the document layout (not a slide-per-section deck; ask if you need it split into a standard-size deck instead) |
| `valletta_culture_slide.html` | Self-contained source (fonts + logo embedded) |
| `valletta_culture_slide_artifact.html` | Responsive version (same design, scales to phone width) |
| `generate_slide.py` | Regenerates all HTML from data (run from this folder) |
| `fonts_embed.css` | Base64-embedded Oswald/Inter used by the HTML |
| `logo_b64.txt` | Base64 logo lockup embedded by the generator |
