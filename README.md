# Valletta Industries — Claude Design System

This repo contains a portable brand/design system for Valletta Industries, built for
use with Claude when generating presentations, one-pagers, or other client-facing
documents.

## Files

| File | Purpose |
|---|---|
| `DESIGN_SYSTEM.md` | Full human-readable brand system — colors, type, tone, layout rules, slide templates |
| `tokens.json` | Same system in machine-readable form (colors, type scale, credentials) for tools/scripts to consume |
| `assets/` | Drop real logo files and any official brand assets here (empty by default — see below) |

## What's real vs. extrapolated

Everything tagged **[confirmed]** in `DESIGN_SYSTEM.md` was pulled directly from the
live vallettaindustries.com site (the red `#FF002B` accent, credential/cert numbers,
service pillar names, site copy/tone). Everything tagged **[extrapolated]** — the exact
neutral palette, the typeface pairing — is a reasoned design system built to match the
site's visual character, since the public site doesn't expose a formal style guide.
Replace those with real values any time you have them (see "Improving Accuracy" below).

## Uploading to GitHub

1. Create a new repo (e.g. `valletta-design-system`) — private is recommended since this
   includes company identifiers (UEI/DUNS/CAGE codes)
2. Upload these three files (and an `assets/` folder if you add logo files) to the repo root
3. Commit

```bash
git init
git add .
git commit -m "Valletta Industries design system v1.0"
git branch -M main
git remote add origin https://github.com/<your-org>/valletta-design-system.git
git push -u origin main
```

## Using this with Claude

**In Claude Design / a Claude Project:**
- Add `DESIGN_SYSTEM.md` (and `tokens.json`) to the Project's knowledge/files
- When asking Claude to build a deck, reference it directly, e.g.:
  > "Build a capabilities deck for [client] using the Valletta Industries design system —
  > dark mode, following the slide templates in section 6."

**Pulling from GitHub directly in a conversation:**
- Paste the raw GitHub URL (e.g. `https://raw.githubusercontent.com/<org>/valletta-design-system/main/DESIGN_SYSTEM.md`)
  and ask Claude to fetch and apply it
- Or connect the GitHub connector/MCP if you have one enabled, and ask Claude to read the
  file from the repo directly

## Improving Accuracy

To upgrade this from "extrapolated from the public site" to "your actual brand guide":
1. Upload your real logo files (SVG/EPS/PNG, all lockups and color variants)
2. Upload an existing brand guide PDF if one exists internally — Claude can extract exact
   hex/PMS values, licensed fonts, and usage rules and merge them into `DESIGN_SYSTEM.md`
3. Confirm or correct the typeface pairing in section 3 — the current picks are
   PowerPoint-safe substitutes chosen to visually match the site, not confirmed brand fonts