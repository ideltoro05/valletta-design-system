# Valletta Industries — Design System
**Version 1.0 — built for use with Claude (presentations, docs, decks)**

> Source: extracted from vallettaindustries.com (public site content, live June 2026),
> plus real logo files and Mission Protect product screenshots supplied directly by
> Valletta and stored in `/assets`. Values pulled from those real assets are flagged
> **[confirmed]**; values still inferred from the public site alone are flagged
> **[extrapolated]**. Swap in more real values any time — see "How to Customize" at
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

**Headline typeface [confirmed from the real logo lockup, `/assets/logo/valletta-lockup.png`]:**
the actual wordmark is set in a refined, high-contrast **Didone-style serif** (thin
horizontal strokes, thick verticals — in the Bodoni/Didot family), regular weight, wide
letter-spacing, ALL CAPS — not a bold slab serif. This **supersedes the earlier
Bookman Old Style guess below**, which read far too heavy/blocky next to the real mark.

| Role | Font (PowerPoint-safe) | Notes |
|------|------------------------|-------|
| Headlines / Titles | **Cambria**, Regular (not bold), all-caps, wide tracking | Closest PowerPoint-safe match to the real Didone-style wordmark — moderate-contrast serif reads far closer than a slab serif. If you have real Adobe/Google font access, use **Bodoni** or **Didot** directly to match the logo exactly. |
| Section labels / eyebrows | **Arial**, Bold, all-caps, letter-spaced | Matches the site's small caps sub-labels (e.g. "ENGINEERING MANAGEMENT") **[extrapolated]** |
| Body copy | **Calibri** or **Arial**, Regular | Site body copy is a clean, unadorned sans-serif **[extrapolated]** |
| Captions / metadata | **Arial**, Regular, Steel Gray | Certification numbers, credential lines **[extrapolated]** |

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

**[confirmed — real files in `/assets/logo`]**

- **The mark is a stylized Maltese cross** (eight-pointed, built from four triangular
  wedges) in Valletta Red `#FF002B` — a deliberate nod to Valletta, the capital of Malta,
  and the Maltese cross as Malta's national symbol. This is the icon to use everywhere
  the brand needs a compact mark (favicons, badges, the corner of a slide).
- **Files:**
  - `assets/logo/valletta-mark.png` — icon only, transparent background, near-square
    (482×513). Use on **either** light or dark slide backgrounds — it's pure red on
    transparency, no light/dark variant needed.
  - `assets/logo/valletta-lockup.png` — full horizontal lockup (icon + "VALLETTA
    INDUSTRIES" wordmark in black). **Light backgrounds only** — the wordmark text is
    black with no transparent/white variant currently on file. On dark slides, pair
    `valletta-mark.png` with a separately typeset white wordmark (Cambria, see §3)
    until a white-text lockup file is provided.
  - `assets/logo/valletta-mark-wide.png` — the same icon on a wide (2000×420) canvas,
    useful when a lockup-shaped placeholder is needed but only the icon is available.
- Clear space: maintain minimum clear space equal to the height of the mark's capital
  letter on all sides.
- Do not recolor the mark outside of red/black/white.
- Do not place the red logo mark on busy photography without a solid-color safe area
  behind it.

### Sub-brand: Mission Protect

Mission Protect is Valletta's AI-enabled training/LMS product (course catalog, scenario
training modules, learner progress tracking). **[confirmed from product screenshots,
`/assets/mission-protect/`]** — its own product UI runs a **distinct accent identity**,
not the parent red/black/white system:

| Role | Value | Notes |
|---|---|---|
| Primary gradient | `#7C32DF` → `#0916DC` (purple → blue) | Primary CTA buttons ("Start Training"), progress accents |
| Wordmark | "MISSION PROTECT" | Black, bold, sans-serif, stacked two-line lockup with an angular "M" mark |
| Course-badge treatment | Navy `#1C1C61` shield/crest with gold border, red cross mark, "SECURITY — PROTECT SERVE LEAD" banner | Used as course-card art *inside* Mission Protect — a distinct badge style from the flat corporate mark, not a substitute for it |

**When representing Mission Protect inside a Valletta-branded deck:** keep the deck's
own black/red/white system for everything around it (headlines, layout, other slides),
but let an actual Mission Protect screenshot or its purple/blue gradient appear *within
its own callout/frame* — don't recolor Mission Protect's UI into Valletta red, and don't
bleed the purple into the rest of the deck. It stays visually subordinate to the parent
system by appearing only inside its own contained visual, exactly as a screenshot would.

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

font.headline           = Cambria, Regular, ALL CAPS, wide tracking (real mark is Bodoni/Didot-style)
font.label              = Arial, Bold, ALL CAPS, letter-spaced
font.body               = Calibri / Arial, Regular

logo.icon               = assets/logo/valletta-mark.png        (any background)
logo.lockup             = assets/logo/valletta-lockup.png       (light backgrounds only)
missionProtect.gradient = #7C32DF -> #0916DC (purple -> blue; Mission Protect's own UI only)
```

---

## 9. How to Customize This File

Real logo files and Mission Protect product screenshots are now in `/assets` (see §4) —
the headline typeface and logo/mark guidance above are confirmed from them. What's
still open:
1. **A white/light version of the full lockup** (`valletta-lockup.png` is black-text,
   light-background-only) — needed to put the full lockup, not just the icon, on dark
   slides. Drop it in `/assets/logo/` as `valletta-lockup-white.png` any time.
2. **Licensed Bodoni/Didot font files**, if available, would let decks match the
   headline typeface exactly instead of the Cambria substitute.
3. Section 2's neutral palette (Operator Black, Tactical Charcoal, Field White) is
   still **[extrapolated]** from the public site — upload an official style guide PDF
   if one exists and I'll reconcile it against these values.