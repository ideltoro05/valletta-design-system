# Valletta Industries — Design System
**Version 1.0 — built for use with Claude (presentations, docs, decks)**

> Source: extracted from vallettaindustries.com (public site content, live June 2026).
> The site itself doesn't publish a formal brand book, so a few values below (exact hex
> supporting palette, typeface pairing) are reasonable extrapolations from the live site,
> flagged inline as **[extrapolated]**. Confirmed values (pulled directly from site code)
> are flagged **[confirmed]**. Swap in real values any time — see "How to Customize" at
> the bottom.

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
| **Valletta Red** [confirmed — pulled from live site CSS] | `#FF002B` | Logo mark, single accent color, key stat callouts, CTA elements. Use sparingly — it is a precision accent, not a background color. |
| **Operator Black** [extrapolated] | `#0A0A0A` | Primary dark background for title/section slides, headers |
| **Tactical Charcoal** [extrapolated] | `#1C1D21` | Secondary dark surface, card backgrounds on dark slides |
| **Field White** [extrapolated] | `#F5F5F3` | Primary light background for content slides (off-white, not stark white — keeps the tactical/paper feel) |

### Supporting neutrals
| Role | Hex | Usage |
|------|-----|-------|
| Steel Gray | `#5B5F66` | Secondary body text, captions, muted labels |
| Line Gray | `#D8D9DB` | Dividers, table gridlines, subtle borders |
| Pure White | `#FFFFFF` | Text on dark backgrounds |

### Usage ratio (per pptx skill guidance)
- **60–70%** Operator Black / Tactical Charcoal (dark) or Field White (light) — pick one
  mode per deck, don't mix randomly
- **20–30%** Steel Gray / Line Gray for structure and secondary text
- **5–10%** Valletta Red — reserved for the single sharp accent (a stat, an icon circle,
  a key word in a headline). Never used as a large background fill; it reads as a
  warning color at scale, and its power in this brand comes from restraint.

### Do not
- Do not tint the red down to a "brand pink" for backgrounds — keep it saturated and
  used only in small doses
- Do not introduce blue as a default (common AI-deck default) — this is a black/red/
  white system, not navy corporate

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

- Primary wordmark: "Valletta Industries" — used in nav/header, typically paired with
  the red accent mark **[confirmed: red = `#FF002B`]**
- Sub-brand: **Mission Protect** — an Active Shooter Learning Management System product
  line; carries its own logo lockup (MP mark) but should stay visually subordinate to
  the parent Valletta system when used together
- Clear space: maintain minimum clear space equal to the height of the mark's capital
  letter on all sides
- Do not recolor the mark outside of red/black/white
- Do not place the red logo mark on busy photography without a solid-color safe area
  behind it

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
- **Dark mode (primary for title/executive decks):** Operator Black background, white
  headlines, Steel Gray body text, red accent used for exactly one element per slide
- **Light mode (primary for detailed/technical content decks):** Field White background,
  Operator Black headlines, Steel Gray body text, red accent for callouts/icons

### Motif
Use **one** repeating visual device across the deck — recommended: a thin red
"tick mark" or right-angle bracket (⌐) at the corner of image frames and stat callouts,
echoing tactical/targeting reticle language without literally using a crosshair.
Do not use a full-width color bar or side stripe (reads as generic AI-deck filler).

### Slide templates
1. **Title slide:** Operator Black background, all-caps bold headline (white), one-line
   red-accented sub-head, credential/cert logos small and bottom-aligned
2. **Section break:** Operator Black background, large section number + all-caps title,
   minimal supporting text
3. **Capability/service slide:** Field White background, bold all-caps section label top
   left, 1–2 sentence description, supporting photography right-aligned or full-bleed
   half-slide
4. **Stat/proof slide:** Dark background, large red or white numerals (60–72pt) with
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
color.primary.red      = #FF002B
color.bg.dark           = #0A0A0A
color.bg.dark.secondary = #1C1D21
color.bg.light          = #F5F5F3
color.text.muted        = #5B5F66
color.border            = #D8D9DB
color.text.onDark       = #FFFFFF

font.headline           = Bookman Old Style, Bold, ALL CAPS
font.label              = Arial, Bold, ALL CAPS, letter-spaced
font.body               = Calibri / Arial, Regular
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