# Valletta Industries — Design System
**Version 2.0 — Cobalt directive (built for use with Claude: presentations, docs, decks)**

> Source: extracted from vallettaindustries.com (public site content, live June 2026).
> The site itself doesn't publish a formal brand book, so a few values below (exact hex
> supporting palette, typeface pairing) are reasonable extrapolations from the live site,
> flagged inline as **[extrapolated]**. Confirmed values (pulled directly from site code)
> are flagged **[confirmed]**. Swap in real values any time — see "How to Customize" at
> the bottom.

> **v2.0 changelog (2026-09-25) — directed by Sam, via email, for the government-client
> document package due 2026-10-04:**
> - **Cobalt Blue replaces Valletta Red as the primary document accent.** Red is no
>   longer used for rules, section bands, field labels, checkboxes, or callouts in new
>   work. It remains only inside the fixed Valletta shield mark itself (the logo asset
>   is not being redesigned) — see §2 and §4.
> - **Co-branding with SOC is standard again** for this document package: use the
>   combined Valletta Industries + SOC lockup (`/assets/logo/valletta-soc-lockup.png`),
>   not the Valletta-only mark, in headers/covers. This reverses the Valletta-only
>   treatment used on several documents built earlier in this project (site visit
>   assessment, weapons SOP, CIFSO certification forms, etc.) — those get re-branded to
>   match as part of this pass.
> - Two new cobalt hex values added in §2; everything else in this file (typography,
>   layout system, tone) is unchanged.

---

## 1. Brand Essence

**Company:** Valletta Industries
**Category:** Defense & security professional services — staffing, force-protection
training, and human performance support for military, SOF, corporate, hospitality, and
critical-infrastructure clients.
**Positioning line [confirmed]:** "Built By Operators"
**Status:** Service-Disabled Veteran-Owned Certified, GSA Schedule holder, SeaPort-NextGen
contractor, CMMC Level 1.

**Three service pillars [confirmed]:**
1. **Professional Services** — engineering management, program management, management
   support, data analytics, professional security staffing
2. **Scenario-Based Training** — tactical training, anti-terrorism/force protection,
   defensive & tactical driving, gear testing & evaluation, integrated training & role
   player support
3. **Human Performance** — warfighter performance, resilience, medical staffing support

**Voice & tone:**
- Direct, credential-forward, unembellished — reads like an operations order, not
  marketing copy
- Leads with capability and outcome ("Full lifecycle support for RDT&E programs...")
  rather than adjectives
- Government/defense register: acronyms used freely and correctly (RDT&E, TTPs, ATFP,
  MSC, MARAD), no exclamation points, no hype language
- Confidence is stated as fact, not sold ("Proven Track Record," "Mission-Focused
  Training") — short, declarative sub-heads, not taglines

**When writing copy in this system:** short declarative sentences, active voice, lead
with the deliverable/outcome, credentials and certifications stated plainly, avoid
consumer-marketing tone (no "unlock," "supercharge," "game-changing").

---

## 2. Color Palette

### Primary
| Role | Hex | Usage |
|------|-----|-------|
| **Valletta Cobalt** [v2.0 — directed by Sam, 2026-09-25] | `#1B4FA0` | The primary accent color. Replaces Valletta Red in this role: section bands, rules, field labels, checkboxes, callout borders, key stat callouts. Use the way red used to be used — sparingly, as a precision accent, not a background fill. |
| **Cobalt Navy** [v2.0 — sampled from Sam's reference image] | `#0B2C56` | An optional deep-blue dark background/cover treatment (matches the reference screenshot's title-slide background), for use alongside or instead of Operator Black on cover/title pages. Body documents keep Operator Black as their working dark background unless told otherwise. |
| **Operator Black** [extrapolated] | `#0A0A0A` | Primary dark background for title/section slides, headers, section bands |
| **Tactical Charcoal** [extrapolated] | `#1C1D21` | Secondary dark surface, card backgrounds on dark slides |
| **Field White** [extrapolated] | `#F5F5F3` | Primary light background for content slides (off-white, not stark white — keeps the tactical/paper feel) |

### Retired role
| Role | Hex | Usage |
|------|-----|-------|
| Valletta Red [confirmed — pulled from live site CSS] | `#FF002B` | **No longer used as a document accent as of v2.0.** Still appears inside the fixed Valletta shield mark's eight-point cross (the logo itself isn't being redesigned) — see §4. Do not introduce red anywhere else in new work. |

### Supporting neutrals
| Role | Hex | Usage |
|------|-----|-------|
| Steel Gray | `#5B5F66` | Secondary body text, captions, muted labels |
| Line Gray | `#D8D9DB` | Dividers, table gridlines, subtle borders |
| Pure White | `#FFFFFF` | Text on dark backgrounds |
| SOC Gold | `#B8801D` | SOC sub-lockup stripe accent only — see §4. Not part of the primary palette. |

### Usage ratio (per pptx skill guidance)
- **60–70%** Operator Black / Tactical Charcoal (dark) or Field White (light) — pick one
  mode per deck, don't mix randomly
- **20–30%** Steel Gray / Line Gray for structure and secondary text
- **5–10%** Valletta Cobalt — reserved for the single sharp accent (a stat, an icon
  circle, a key word in a headline, a section band). Never used as a large background
  fill in body documents; restraint is still the point, only the color changed.

### Do not
- Do not tint the cobalt down to a pastel/"corporate light blue" for backgrounds — keep
  it saturated and used only in small-to-medium doses (section bands are fine; full-page
  fills are not, outside of a cover/title treatment using Cobalt Navy)
- Do not use Valletta Red anywhere outside the fixed logo mark itself as of v2.0

---

## 3. Typography

**[extrapolated — no webfont was exposed in the page source]**

| Role | Font (PowerPoint-safe) | Notes |
|------|------------------------|-------|
| Headlines / Titles | **Bookman Old Style**, Bold, all-caps, tight tracking | Site headers render as bold sans caps; Bookman Old Style bold-caps gives a similar authoritative block-letter feel while staying in the PowerPoint safe-font list |
| Section labels / eyebrows | **Arial**, Bold, all-caps, letter-spaced | Matches the site's small caps sub-labels (e.g. "ENGINEERING MANAGEMENT") |
| Body copy | **Calibri** or **Arial**, Regular | Site body copy is a clean, unadorned sans-serif |
| Captions / metadata | **Arial**, Regular, Steel Gray | Certification numbers, credential lines |

If you have Anthropic/Claude Design access to real Adobe/Google fonts (not just
PowerPoint-safe), a closer match to the live site's condensed bold headline style would
be **Oswald** or **Barlow Condensed** (headlines) paired with **Inter** or **Source Sans
Pro** (body).

### Type scale for decks
| Element | Size | Weight | Case |
|---|---|---|---|
| Title slide headline | 44–54pt | Bold | ALL CAPS |
| Section header | 28–32pt | Bold | ALL CAPS |
| Slide title | 32–36pt | Bold | Title Case or ALL CAPS |
| Sub-head / eyebrow | 12–14pt | Bold, letter-spaced | ALL CAPS |
| Body | 14–16pt | Regular | Sentence case |
| Caption / credential line | 10–11pt | Regular | Sentence case |

---

## 4. Logo & Marks

- Primary lockup **[confirmed — extracted from Bryan Paarmann's email signature,
  `/assets/logo/valletta-soc-lockup.png`]**: white shield outline containing a red
  eight-point cross mark, paired with the "VALLETTA INDUSTRIES" wordmark in a serif
  display face (bold, wide capital letterforms — closer to a classical serif like
  Cinzel/Trajan than the PowerPoint-safe Bookman Old Style substitute below; use the
  real lockup image rather than re-setting the wordmark whenever possible). Logo
  background is black (`#000000`, i.e. Operator Black). **The red in the shield's
  cross mark is part of this fixed asset and is not being redesigned or recolored —
  it's the one place red still legitimately appears post-v2.0.**
- Sub-brand: **SOC** — carries its own lockup (angled gold/bronze stripes + bold
  condensed "SOC" wordmark in a rounded-rectangle frame) **[confirmed, same source]**.
  Combined "Valletta Industries + SOC" lockup is the standard signature/letterhead
  mark — divided by a thin vertical white rule, shield+wordmark on the left, SOC mark
  on the right.
  - **[v2.0]** Use the **combined lockup** (not the Valletta-only shield/wordmark) as
    the default for this document package — Sam's guidance is to co-brand with SOC
    across the board, not only where SOC is the specifically relevant business line.
    Documents in this repo built before 2026-09-25 that used the Valletta-only mark
    (site visit assessment, weapons SOP, CIFSO certification forms, incident log,
    weekly activity report, etc.) are being brought back in line with this as they're
    revisited.
  - Standalone `valletta-mark-black.png` / `valletta-mark-white.png` (Valletta shield
    + wordmark, no SOC) remain available for contexts where SOC genuinely isn't
    relevant, but default to the combined lockup unless told otherwise.
  - **SOC Gold** [confirmed]: `#B8801D` — used only within the SOC sub-lockup's stripe
    accent; not part of the primary Valletta palette, do not use elsewhere.
  - Previously listed sub-brand "Mission Protect" (Active Shooter LMS) has not been
    confirmed against real assets — treat as unconfirmed until a real lockup is supplied.
- Clear space: maintain minimum clear space equal to the height of the mark's capital
  letter on all sides
- Do not recolor the mark outside of red/black/white (or gold, within the SOC stripe only)
- Do not place the red logo mark on busy photography without a solid-color safe area
  behind it
- On decks/slides: place the combined lockup small and unobtrusive (a corner mark in a
  title bar or footer), not as a dominant element — it credits the brand without
  competing with slide content.

---

## 5. Imagery Style

Based on the site's photography direction:
- Real operational/tactical photography: security personnel, tactical training
  environments, maritime/waterborne security, gear, dining/hospitality environments
  (per site categories) — not stock-generic corporate photos
- Desaturated or naturally toned (no heavy filters); let the red accent be the only
  saturated color in a composition
- Environments over posed portraits — the photography documents capability in context
  (training grounds, facilities, equipment)
- Avoid overtly graphic/violent imagery in client-facing decks; the brand communicates
  capability and professionalism, not aggression

---

## 6. Layout System for Presentations

### Slide modes
Pick **one** mode as the deck's baseline and use the other only for contrast on
title/section-break slides ("sandwich" structure per pptx skill guidance):
- **Dark mode (primary for title/executive decks):** Operator Black (or Cobalt Navy for
  a cover/title treatment) background, white headlines, Steel Gray body text, cobalt
  accent used for exactly one element per slide
- **Light mode (primary for detailed/technical content decks):** Field White background,
  Operator Black headlines, Steel Gray body text, cobalt accent for callouts/icons

### Motif
Use **one** repeating visual device across the deck — recommended: a thin cobalt
"tick mark" or right-angle bracket (⌐) at the corner of image frames and stat callouts,
echoing tactical/targeting reticle language without literally using a crosshair.
Do not use a full-width color bar or side stripe (reads as generic AI-deck filler).

### Slide templates
1. **Title slide:** Operator Black or Cobalt Navy background, all-caps bold headline
   (white), one-line cobalt-accented sub-head, credential/cert logos small and
   bottom-aligned
2. **Section break:** Operator Black background, large section number + all-caps title,
   minimal supporting text
3. **Capability/service slide:** Field White background, bold all-caps section label top
   left, 1–2 sentence description, supporting photography right-aligned or full-bleed
   half-slide
4. **Stat/proof slide:** Dark background, large cobalt or white numerals (60–72pt) with
   small caption labels beneath — for readiness metrics, years of experience, personnel
   trained, etc.
5. **Credentials/footer slide:** Field White, small-caps credential list (UEI, DUNS,
   CAGE, CMMC level) — mirror the site's footer block for closing/contact slides

### Spacing
- 0.5" minimum slide margins
- 0.3–0.5" between content blocks, applied consistently
- Generous negative space — this is a confident, uncluttered brand; avoid packing
  slides

---

## 7. Certifications & Credential Block (reuse verbatim)

For closing/contact slides, reuse this block **[confirmed from site footer]**:

```
UEI Number: CKXMD3HBP1P7
DUNS Number: 118055280
Cage Code: 92SX6
CMMC LEVEL-1
UID Number: S100027899

403 Columbia Street #9, Covington, LA 70433
```

Also reference where relevant: Service-Disabled Veteran-Owned Certified, GSA Schedule,
SeaPort-NextGen.

---

## 8. Quick-Reference Token Summary

```
color.primary.cobalt    = #1B4FA0   (v2.0 — replaces red as the document accent)
color.bg.dark.cobaltNavy = #0B2C56  (v2.0 — optional cover/title dark background)
color.primary.red       = #FF002B   (retired as an accent — logo mark only, see §4)
color.bg.dark           = #0A0A0A
color.bg.dark.secondary = #1C1D21
color.bg.light          = #F5F5F3
color.text.muted        = #5B5F66
color.border            = #D8D9DB
color.text.onDark       = #FFFFFF
color.subBrand.socGold  = #B8801D

font.headline           = Bookman Old Style, Bold, ALL CAPS
font.label              = Arial, Bold, ALL CAPS, letter-spaced
font.body               = Calibri / Arial, Regular

logo.default             = /assets/logo/valletta-soc-lockup.png  (v2.0 — combined Valletta+SOC lockup is now the default)
```

---

## 9. How to Customize This File

This system was built from public site content only — it does **not** include your
actual logo files, exact PMS/hex brand colors from a style guide, or licensed fonts if
you have them. To make it fully accurate:
1. Drop your real logo files (SVG/PNG/EPS) into `/assets/logo/` in this repo
2. If you have an actual brand guide PDF, upload it and I can extract exact hex values,
   type specs, and usage rules to replace the "[extrapolated]" entries above
3. Update section 2/3 hex and font values directly in this file — everything else
   (layout system, slide templates, tone) will still apply