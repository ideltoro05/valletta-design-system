# Valletta Industries — Claude Design System

This repo contains a portable brand/design system for Valletta Industries, built for
use with Claude when generating presentations, one-pagers, or other client-facing
documents.

## Files

| File | Purpose |
|---|---|
| `DESIGN_SYSTEM.md` | Full human-readable brand system — colors, type, tone, layout rules, slide templates |
| `tokens.json` | Same system in machine-readable form (colors, type scale, credentials) for tools/scripts to consume |
| `assets/logo/` | Real Valletta logo files (icon + lockup) |
| `assets/mission-protect/` | Real Mission Protect product screenshots |
| `decks/` | Finished presentations (`.pptx`, plus `.pdf` where exported) and the screenshots each deck used |
| `CLAUDE.md` | Standing instructions Claude follows when it works in this folder (brand rules + the finish-a-deck checklist below) |

## Getting started on a new computer

1. **Install:** [GitHub Desktop](https://desktop.github.com), the [Claude desktop app](https://claude.ai/download),
   and [Google Drive for desktop](https://www.google.com/drive/download/).
2. **Clone this repo:** in GitHub Desktop choose **File › Clone repository › URL**, paste
   `https://github.com/ideltoro05/valletta-design-system.git`, and pick a local folder
   such as `Documents/valletta-design-system`. Keep it **outside** your Google Drive folder:
   Drive sync can corrupt a Git repo.
3. **Get the latest before you start:** click **Fetch origin**, then **Pull origin**.
4. **Work with Claude:** in the Claude desktop app open the **Code** tab, choose the cloned
   folder, and ask for what you need, e.g.
   > "Build a capabilities deck for [client] using the Valletta design system."

   Claude reads `CLAUDE.md` automatically, so it follows the brand rules and the finishing
   checklist below.

To push changes you need write access: ask Israel to add your GitHub account under the
repo's **Settings › Collaborators**.

## Finishing a presentation

Every finished deck goes to **both** places:

1. **GitHub:** save it in `decks/` (screenshots in `decks/<Deck_Name>_screenshots/`), then
   commit and push. In GitHub Desktop: write a short summary, click **Commit**, then **Push origin**.
2. **Google Drive:** copy the `.pptx` into the client's folder inside
   [Valletta Industries](https://drive.google.com/drive/folders/1rJkLz4tiAWmZFyTm9ni3WwqvPacGXpYa),
   e.g. `HHS Training/Presenation`. General capability decks go in `Biz Development`.

If you edit a deck later (in PowerPoint or Google Slides), put the updated file back in both places.

## What's real vs. extrapolated

Everything tagged **[confirmed]** in `DESIGN_SYSTEM.md` was pulled directly from the
live vallettaindustries.com site (the red `#FF002B` accent, credential/cert numbers,
service pillar names, site copy/tone). Everything tagged **[extrapolated]** — the exact
neutral palette, the typeface pairing — is a reasoned design system built to match the
site's visual character, since the public site doesn't expose a formal style guide.
Replace those with real values any time you have them (see "Improving Accuracy" below).

## Using this with Claude (without cloning)

**In Claude Design / a Claude Project:**
- Add `DESIGN_SYSTEM.md` (and `tokens.json`) to the Project's knowledge/files
- When asking Claude to build a deck, reference it directly, e.g.:
  > "Build a capabilities deck for [client] using the Valletta Industries design system —
  > dark mode, following the slide templates in section 6."

**Pulling from GitHub directly in a conversation:**
- Paste the raw GitHub URL (`https://raw.githubusercontent.com/ideltoro05/valletta-design-system/main/DESIGN_SYSTEM.md`)
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