import math

CX, CY = 384, 404
R_CENTER = 78
R_WEDGE_IN = 82
R_WEDGE_OUT = 176
R_RING_IN = 176
R_RING_OUT = 192
R_TAGLINE = 96

BLACK = "#0A0A0A"
CHARCOAL = "#1C1D21"
FIELD_WHITE = "#F5F5F3"
RED = "#FF002B"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"
MUTED_ON_DARK = "#A6A9AE"

def pol(r, deg):
    rad = math.radians(deg)
    x = CX + r * math.sin(rad)
    y = CY - r * math.cos(rad)
    return x, y

def wedge_path(r_in, r_out, a_start, a_end, pad=0.8):
    a0 = a_start + pad
    a1 = a_end - pad
    x1,y1 = pol(r_out, a0)
    x2,y2 = pol(r_out, a1)
    x3,y3 = pol(r_in, a1)
    x4,y4 = pol(r_in, a0)
    large = 1 if (a1-a0) > 180 else 0
    return f"M {x1:.2f},{y1:.2f} A {r_out:.2f},{r_out:.2f} 0 {large} 1 {x2:.2f},{y2:.2f} L {x3:.2f},{y3:.2f} A {r_in:.2f},{r_in:.2f} 0 {large} 0 {x4:.2f},{y4:.2f} Z"

ICONS = {
 "people": '<path d="M-13,4 a6.2,6.2 0 1,1 0.01,0 M13,4 a5.4,5.4 0 1,1 0.01,0 M0,-8.5 a7,7 0 1,1 0.01,0" fill="none" stroke="currentColor" stroke-width="2.1"/><path d="M-20,18 c0,-8 5,-12.5 7,-12.5 M20,18 c0,-8 -5,-12.5 -7,-12.5 M-10,18 c0,-9.5 7,-15 10,-15 c3,0 10,5.5 10,15" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/>',
 "shield": '<path d="M0,-17 L14,-10.5 V3.5 C14,13 7,18.5 0,21 C-7,18.5 -14,13 -14,3.5 V-10.5 Z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/><path d="M-6,1.5 L-1.5,7 L8,-5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>',
 "action": '<path d="M-2,-19 L-15,3 L-3,3 L-6,19 L16,-5 L2,-5 Z" fill="currentColor" stroke="none"/>',
 "speech": '<path d="M-17,-11.5 h34 a3.5,3.5 0 0 1 3.5,3.5 v14 a3.5,3.5 0 0 1 -3.5,3.5 h-19.5 l-8,7 v-7 h-6 a3.5,3.5 0 0 1 -3.5,-3.5 v-14 a3.5,3.5 0 0 1 3.5,-3.5 Z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/><circle cx="-7" cy="-1" r="1.6" fill="currentColor" stroke="none"/><circle cx="0" cy="-1" r="1.6" fill="currentColor" stroke="none"/><circle cx="7" cy="-1" r="1.6" fill="currentColor" stroke="none"/>',
 "handshake": '<path d="M-15,-14 A15,15 0 0,1 14,-4" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/><path d="M14,-4 L14,-11 M14,-4 L7,-5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/><path d="M15,14 A15,15 0 0,1 -14,4" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/><path d="M-14,4 L-14,11 M-14,4 L-7,5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>',
}

def icon_svg(name, size=24, color=RED):
    return f'<svg width="{size}" height="{size}" viewBox="-21 -21 42 42" color="{color}">{ICONS[name]}</svg>'

PILLARS = [
    {"num":1,"angle":0,"fill":BLACK,
     "title":"YOU MATTER","sub":"PEOPLE FIRST CULTURE",
     "bullets":["Treat everyone with dignity and respect.",
                "Prioritize safety and wellbeing.",
                "Look out for one another.",
                "Develop and mentor teammates.",
                "Recognize contributions and successes."],
     "mindset":"Every person deserves to go home safe and know they are valued.",
     "icon":"people"},
    {"num":2,"angle":72,"fill":CHARCOAL,
     "title":"PROFESSIONAL AND CONSISTENT","sub":"TRUSTED THROUGH EXCELLENCE",
     "bullets":["Follow standards and procedures.",
                "Maintain appearance and readiness.",
                "Demonstrate discipline and accountability.",
                "Treat every situation objectively.",
                "Deliver the same level of service every shift, every day."],
     "mindset":"Our reputation is earned through consistency.",
     "icon":"shield"},
    {"num":5,"angle":144,"fill":BLACK,
     "title":"ACTION ORIENTED","sub":"DECISIVE WHEN IT MATTERS",
     "bullets":["Respond promptly.",
                "Take initiative.",
                "Solve problems at the lowest level possible.",
                "Adapt to changing circumstances.",
                "Drive issues to resolution."],
     "mindset":"When action is required, we lead.",
     "icon":"action"},
    {"num":4,"angle":216,"fill":CHARCOAL,
     "title":"SAY SOMETHING","sub":"SEE IT. OWN IT. REPORT IT.",
     "bullets":["Report concerns immediately.",
                "Escalate issues without hesitation.",
                "Challenge unsafe conditions respectfully.",
                "Encourage open communication.",
                "Learn from incidents and near misses."],
     "mindset":"Silence creates risk. Speaking up creates safety.",
     "icon":"speech"},
    {"num":3,"angle":288,"fill":BLACK,
     "title":"COLLABORATE AND WIN","sub":"ONE TEAM, ONE MISSION",
     "bullets":["Share information proactively.",
                "Support fellow officers and business partners.",
                "Build relationships across departments.",
                "Seek solutions, not blame.",
                "Celebrate team achievements."],
     "mindset":"We are stronger together than we are individually.",
     "icon":"handshake"},
]

# card layout: pillar num -> card box + leader anchor on hub
CARD_LAYOUT = {
    1: dict(left=218, top=54,  width=332, height=140, cols=2),
    2: dict(left=560, top=50,  width=200, height=205, cols=1),
    5: dict(left=520, top=550, width=236, height=145, cols=1),
    4: dict(left=12,  top=550, width=236, height=145, cols=1),
    3: dict(left=8,   top=50,  width=200, height=205, cols=1),
}

wedge_svgs, divider_svgs, badge_svgs = [], [], []
for w in PILLARS:
    a0, a1 = w["angle"] - 36, w["angle"] + 36
    wedge_svgs.append(f'<path d="{wedge_path(R_WEDGE_IN, R_WEDGE_OUT, a0, a1)}" fill="{w["fill"]}"/>')
    x1,y1 = pol(R_WEDGE_IN-4, a0)
    x2,y2 = pol(R_WEDGE_OUT+4, a0)
    divider_svgs.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{RED}" stroke-width="1.4"/>')
    bx, by = pol(R_WEDGE_OUT - 30, w["angle"])
    badge_svgs.append(f'''<circle cx="{bx:.2f}" cy="{by:.2f}" r="14" fill="{RED}"/>
    <text x="{bx:.2f}" y="{by+5:.2f}" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="14" fill="{WHITE}">{w["num"]}</text>''')
    ix, iy = pol((R_WEDGE_OUT + R_WEDGE_IN) / 2 - 6, w["angle"])
    scale = 30/42
    wedge_svgs.append(f'<g transform="translate({ix:.2f},{iy:.2f}) scale({scale:.3f})" color="{WHITE}">{ICONS[w["icon"]]}</g>')

def arc_path(r, a_start, a_end, pid):
    x1,y1 = pol(r, a_start)
    x2,y2 = pol(r, a_end)
    large = 1 if (a_end - a_start) > 180 else 0
    return f'<path id="{pid}" d="M {x1:.2f},{y1:.2f} A {r:.2f},{r:.2f} 0 {large} 1 {x2:.2f},{y2:.2f}" fill="none"/>'

inner_ring = arc_path(R_TAGLINE, 0.1, 360, "innerRing")

# leader lines from hub badge to nearest card edge
leader_svgs = []
for w in PILLARS:
    L = CARD_LAYOUT[w["num"]]
    bx, by = pol(R_WEDGE_OUT - 30, w["angle"])
    cx_ = L["left"] + L["width"]/2
    cy_ = L["top"] + L["height"]/2
    # connect to nearest edge midpoint of the card instead of center
    if L["left"] > CX:  # card to the right
        ex, ey = L["left"], L["top"] + 26
    elif L["left"]+L["width"] < CX:  # card to the left
        ex, ey = L["left"]+L["width"], L["top"] + 26
    else:  # top wide card
        ex, ey = cx_, L["top"] + L["height"]
    leader_svgs.append(f'<line x1="{bx:.2f}" y1="{by:.2f}" x2="{ex:.2f}" y2="{ey:.2f}" stroke="{RED}" stroke-width="1.2" stroke-dasharray="2,2"/>')

card_html = []
for w in PILLARS:
    L = CARD_LAYOUT[w["num"]]
    bullets_html = "".join(f'<li>{b}</li>' for b in w["bullets"])
    cols_class = "cols2" if L["cols"] == 2 else "cols1"
    block = f'''
    <div class="card {cols_class}" style="left:{L["left"]}px; top:{L["top"]}px; width:{L["width"]}px; height:{L["height"]}px;">
      <div class="c-head">
        <span class="c-badge">{w["num"]}</span>
        <span class="c-icon">{icon_svg(w["icon"])}</span>
        <div class="c-headtext">
          <div class="c-title">{w["title"]}</div>
          <div class="c-sub">{w["sub"]}</div>
        </div>
      </div>
      <ul class="c-bullets">{bullets_html}</ul>
      <div class="c-rule"></div>
      <div class="c-mindset"><span class="label">MINDSET</span> &ldquo;{w["mindset"]}&rdquo;</div>
    </div>'''
    card_html.append(block)

import os
HERE = os.path.dirname(os.path.abspath(__file__))
fonts_css = open(os.path.join(HERE, "fonts_embed.css")).read()

html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>
{fonts_css}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ width:768px; height:768px; background:{FIELD_WHITE}; }}
.stage {{ position:relative; width:768px; height:768px; font-family:'Inter',sans-serif; overflow:hidden; }}
svg.base {{ position:absolute; inset:0; }}

.titlebar {{ position:absolute; left:0; top:0; width:768px; height:34px; background:{BLACK}; display:flex; align-items:center; justify-content:center; }}
.titlebar .t {{ font-family:'Oswald'; font-weight:700; font-size:15px; letter-spacing:3px; color:{WHITE}; }}
.titlebar .t span {{ color:{RED}; }}

.card {{ position:absolute; background:{BLACK}; border:1px solid #2A2C30; color:{WHITE}; padding:10px 12px; }}
.card:nth-of-type(odd) {{ background:{BLACK}; }}
.c-head {{ display:flex; align-items:flex-start; gap:6px; margin-bottom:6px; }}
.c-badge {{ display:inline-flex; align-items:center; justify-content:center; width:20px; height:20px; border-radius:50%; background:{RED}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:11px; flex:none; margin-top:1px; }}
.c-icon svg {{ display:block; flex:none; }}
.c-headtext {{ flex:1; min-width:0; }}
.c-title {{ font-family:'Oswald'; font-weight:700; font-size:13.5px; letter-spacing:0.2px; line-height:1.1; text-transform:uppercase; }}
.c-sub {{ font-family:'Inter'; font-weight:700; font-size:7.6px; letter-spacing:0.6px; text-transform:uppercase; color:{RED}; margin-top:2px; }}
.c-bullets {{ list-style:none; }}
.cols1 .c-bullets {{ column-count:1; }}
.cols2 .c-bullets {{ column-count:2; column-gap:18px; }}
.c-bullets li {{ font-size:7.9px; line-height:1.32; color:#E7E7E5; position:relative; padding-left:8px; margin-bottom:2px; break-inside:avoid; }}
.c-bullets li::before {{ content:''; position:absolute; left:0; top:4px; width:3.2px; height:3.2px; background:{RED}; }}
.c-rule {{ height:1px; background:#3C3E42; margin:6px 0 4px 0; width:100%; }}
.c-mindset {{ font-size:7.4px; font-style:italic; color:{MUTED_ON_DARK}; line-height:1.3; }}
.c-mindset .label {{ font-style:normal; font-weight:700; color:{WHITE}; letter-spacing:0.5px; font-size:6.9px; }}

.center-wrap {{ position:absolute; left:{CX-R_CENTER}px; top:{CY-R_CENTER}px; width:{2*R_CENTER}px; height:{2*R_CENTER}px; border-radius:50%; background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:10px; }}
.core-shield {{ margin-bottom:5px; }}
.core-eyebrow {{ font-family:'Inter'; font-weight:700; font-size:7.5px; letter-spacing:1.6px; color:{RED}; margin-bottom:4px; }}
.core-line {{ font-family:'Oswald'; font-weight:700; font-size:13.5px; letter-spacing:0.2px; line-height:1.16; text-transform:uppercase; color:{WHITE}; }}
.core-line.accent {{ color:{RED}; }}

.values-line {{ position:absolute; left:0; top:706px; width:768px; text-align:center; font-family:'Inter'; font-weight:700; font-size:10.5px; letter-spacing:2.2px; color:{BLACK}; }}
.values-line span {{ color:{RED}; }}
.banner {{ position:absolute; left:96px; top:730px; width:576px; height:34px; background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center; }}
.banner .l1 {{ font-family:'Oswald'; font-weight:700; font-size:12.5px; letter-spacing:1px; color:{WHITE}; }}
.banner .l2 {{ font-family:'Inter'; font-weight:700; font-size:7.6px; letter-spacing:1.2px; color:{RED}; margin-top:2px; }}
.tick {{ position:absolute; width:11px; height:11px; }}
.tick.tl {{ left:96px; top:730px; border-top:2px solid {RED}; border-left:2px solid {RED}; }}
.tick.tr {{ left:661px; top:730px; border-top:2px solid {RED}; border-right:2px solid {RED}; }}
.tick.bl {{ left:96px; top:753px; border-bottom:2px solid {RED}; border-left:2px solid {RED}; }}
.tick.br {{ left:661px; top:753px; border-bottom:2px solid {RED}; border-right:2px solid {RED}; }}
</style>
</head>
<body>
<div class="stage">
  <div class="titlebar"><div class="t">PHYSICAL SECURITY <span>FORCE</span> CULTURE</div></div>

  <svg class="base" width="768" height="768" viewBox="0 0 768 768">
    <defs>{inner_ring}</defs>
    {''.join(leader_svgs)}
    <circle cx="{CX}" cy="{CY}" r="{R_RING_OUT}" fill="{BLACK}"/>
    {''.join(wedge_svgs)}
    {''.join(divider_svgs)}
    <circle cx="{CX}" cy="{CY}" r="{R_WEDGE_OUT}" fill="none" stroke="{RED}" stroke-width="2"/>
    <circle cx="{CX}" cy="{CY}" r="{R_WEDGE_IN}" fill="none" stroke="{RED}" stroke-width="1.4"/>
    <text font-family="Inter" font-weight="600" font-size="7.6" letter-spacing="0.8" fill="{WHITE}">
      <textPath href="#innerRing" startOffset="50%" text-anchor="middle">EVERY ACTION, DECISION, AND INTERACTION SUPPORTS THE SAFETY, SECURITY, AND SUCCESS OF THE ORGANIZATION</textPath>
    </text>
    {''.join(badge_svgs)}
  </svg>

  {''.join(card_html)}

  <div class="center-wrap">
    <svg class="core-shield" width="28" height="28" viewBox="-20 -20 40 40">
      <path d="M0,-17 L14,-10.5 V3.5 C14,13 7,18.5 0,21 C-7,18.5 -14,13 -14,3.5 V-10.5 Z" fill="none" stroke="{RED}" stroke-width="2"/>
      <path d="M0,-11 L4.5,7 M-4,-2 h8" fill="none" stroke="{WHITE}" stroke-width="1.3"/>
      <rect x="-3.4" y="2.5" width="6.8" height="5.5" rx="1" fill="none" stroke="{WHITE}" stroke-width="1.3"/>
    </svg>
    <div class="core-eyebrow">CORE PURPOSE</div>
    <div class="core-line">Protect People.</div>
    <div class="core-line accent">Secure Assets.</div>
    <div class="core-line">Enable Operations.</div>
  </div>

  <div class="values-line">VIGILANCE <span>&#8226;</span> INTEGRITY <span>&#8226;</span> RESPECT <span>&#8226;</span> ACCOUNTABILITY <span>&#8226;</span> SERVICE</div>
  <div class="tick tl"></div><div class="tick tr"></div><div class="tick bl"></div><div class="tick br"></div>
  <div class="banner">
    <div class="l1">ONE TEAM. ONE STANDARD. ONE MISSION.</div>
    <div class="l2">PROTECTING TODAY. ENABLING TOMORROW.</div>
  </div>
</div>
</body></html>'''

with open(os.path.join(HERE, "valletta_culture_slide.html"),"w") as f:
    f.write(html)
print("written")
