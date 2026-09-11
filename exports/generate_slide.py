import math, os

CANVAS_W, CANVAS_H = 768, 940
CX, CY = 384, 460

R_CENTER = 80
R_WEDGE_IN = 86
R_WEDGE_OUT = 330
R_RING_IN = 330
R_RING_OUT = 352
R_TAGLINE = 100

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

def icon_svg(name, size=22, color=RED):
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

# left/top/width/align per pillar, verified to stay within R_WEDGE_OUT via corner-distance math
LAYOUT = {
    1: dict(left=276, top=182, width=216, height=174, align="center"),
    2: dict(left=496, top=282, width=155, height=178, align="left"),
    5: dict(left=496, top=460, width=155, height=178, align="left"),
    4: dict(left=117, top=460, width=155, height=178, align="right"),
    3: dict(left=117, top=282, width=155, height=178, align="right"),
}

wedge_svgs, divider_svgs, badge_svgs = [], [], []
for w in PILLARS:
    a0, a1 = w["angle"] - 36, w["angle"] + 36
    wedge_svgs.append(f'<path d="{wedge_path(R_WEDGE_IN, R_WEDGE_OUT, a0, a1)}" fill="{w["fill"]}"/>')
    x1,y1 = pol(R_WEDGE_IN-4, a0)
    x2,y2 = pol(R_WEDGE_OUT+4, a0)
    divider_svgs.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{RED}" stroke-width="1.4"/>')

def arc_path(r, a_start, a_end, pid, sweep=1):
    x1,y1 = pol(r, a_start)
    x2,y2 = pol(r, a_end)
    large = 1 if abs(a_end - a_start) > 180 else 0
    return f'<path id="{pid}" d="M {x1:.2f},{y1:.2f} A {r:.2f},{r:.2f} 0 {large} {sweep} {x2:.2f},{y2:.2f}" fill="none"/>'

R_TITLE = (R_RING_IN + R_RING_OUT) / 2
top_arc = arc_path(R_TITLE, -95, 95, "topArc", sweep=1)
values_arc = arc_path(R_TITLE, 180+70, 180-70, "valuesArc", sweep=0)
inner_ring = arc_path(R_TAGLINE, 0.1, 360, "innerRing")

blocks = []
for w in PILLARS:
    L = LAYOUT[w["num"]]
    bullets_html = "".join(f'<li>{b}</li>' for b in w["bullets"])
    head_justify = {"center":"center","left":"flex-start","right":"flex-end"}[L["align"]]
    block = f'''
    <div class="wedge-text align-{L["align"]}" style="left:{L["left"]}px; top:{L["top"]}px; width:{L["width"]}px; height:{L["height"]}px; text-align:{L["align"]};">
      <div class="w-head" style="justify-content:{head_justify};">
        <span class="w-badge">{w["num"]}</span>
        <span class="w-icon">{icon_svg(w["icon"])}</span>
      </div>
      <div class="w-title">{w["title"]}</div>
      <div class="w-sub">{w["sub"]}</div>
      <ul class="w-bullets">{bullets_html}</ul>
      <div class="w-rule"></div>
      <div class="w-mindset"><span class="label">MINDSET</span> &ldquo;{w["mindset"]}&rdquo;</div>
    </div>'''
    blocks.append(block)

HERE = os.path.dirname(os.path.abspath(__file__))
fonts_css = open(os.path.join(HERE, "fonts_embed.css")).read()
logo_b64 = open(os.path.join(HERE, "logo_b64.txt")).read().strip()

inner_style = f'''
{fonts_css}
.vw-scale-wrap {{ width:100%; max-width:{CANVAS_W}px; margin:0 auto; aspect-ratio:{CANVAS_W}/{CANVAS_H}; position:relative; }}
.stage {{ position:absolute; left:0; top:0; width:{CANVAS_W}px; height:{CANVAS_H}px; font-family:'Inter',sans-serif; overflow:hidden; transform-origin:top left; background:{FIELD_WHITE}; }}
svg.base {{ position:absolute; inset:0; }}

.brandmark {{ position:absolute; left:0; top:16px; width:{CANVAS_W}px; display:flex; align-items:center; justify-content:center; }}
.brandmark img {{ height:46px; width:auto; display:block; }}

.wedge-text {{ position:absolute; color:{WHITE}; overflow:hidden; }}
.w-head {{ display:flex; align-items:center; gap:6px; margin-bottom:5px; }}
.w-badge {{ display:inline-flex; align-items:center; justify-content:center; width:21px; height:21px; border-radius:50%; background:{RED}; color:{WHITE}; font-family:'Oswald',sans-serif; font-weight:700; font-size:11.5px; flex:none; }}
.w-icon svg {{ display:block; }}
.w-title {{ font-family:'Oswald',sans-serif; font-weight:700; font-size:15px; letter-spacing:0.2px; line-height:1.08; text-transform:uppercase; }}
.w-sub {{ font-family:'Inter',sans-serif; font-weight:700; font-size:8px; letter-spacing:0.6px; text-transform:uppercase; color:{RED}; margin-top:3px; }}
.w-bullets {{ list-style:none; margin-top:5px; padding:0; }}
.w-bullets li {{ font-size:7.6px; line-height:1.28; color:#E7E7E5; position:relative; padding-left:8px; margin-bottom:1.5px; }}
.align-right .w-bullets li {{ padding-left:0; padding-right:8px; }}
.w-bullets li::before {{ content:''; position:absolute; left:0; top:4px; width:3px; height:3px; background:{RED}; }}
.align-right .w-bullets li::before {{ left:auto; right:0; }}
.w-rule {{ height:1px; background:#3C3E42; margin:4px 0 3px 0; width:100%; }}
.w-mindset {{ font-size:7.2px; font-style:italic; color:{MUTED_ON_DARK}; line-height:1.28; }}
.w-mindset .label {{ font-style:normal; font-weight:700; color:{WHITE}; letter-spacing:0.5px; font-size:6.8px; }}

.center-wrap {{ position:absolute; left:{CX-R_CENTER}px; top:{CY-R_CENTER}px; width:{2*R_CENTER}px; height:{2*R_CENTER}px; border-radius:50%; background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:10px; }}
.core-shield {{ margin-bottom:5px; }}
.core-eyebrow {{ font-family:'Inter'; font-weight:700; font-size:7.6px; letter-spacing:1.6px; color:{RED}; margin-bottom:4px; }}
.core-line {{ font-family:'Oswald'; font-weight:700; font-size:13.8px; letter-spacing:0.2px; line-height:1.16; text-transform:uppercase; color:{WHITE}; }}
.core-line.accent {{ color:{RED}; }}

.banner {{ position:absolute; left:0; top:{CY+R_RING_OUT+18}px; width:{CANVAS_W}px; height:56px; background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center; }}
.banner .l1 {{ font-family:'Oswald'; font-weight:700; font-size:15px; letter-spacing:1px; color:{WHITE}; }}
.banner .l2 {{ font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.3px; color:{RED}; margin-top:4px; }}
.tick {{ position:absolute; width:12px; height:12px; }}
.tick.tl {{ left:0px; top:0px; border-top:2px solid {RED}; border-left:2px solid {RED}; }}
.tick.tr {{ right:0px; top:0px; border-top:2px solid {RED}; border-right:2px solid {RED}; }}
.tick.bl {{ left:0px; bottom:0px; border-bottom:2px solid {RED}; border-left:2px solid {RED}; }}
.tick.br {{ right:0px; bottom:0px; border-bottom:2px solid {RED}; border-right:2px solid {RED}; }}
.banner-wrap {{ position:absolute; left:96px; top:{CY+R_RING_OUT+18}px; width:{CANVAS_W-192}px; height:56px; }}
'''

inner_body = f'''
<div class="stage">
  <div class="brandmark"><img src="data:image/png;base64,{logo_b64}" alt="Valletta Industries / SOC"/></div>

  <svg class="base" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">
    <defs>{top_arc}{values_arc}{inner_ring}</defs>
    <circle cx="{CX}" cy="{CY}" r="{R_RING_OUT}" fill="{BLACK}"/>
    {''.join(wedge_svgs)}
    {''.join(divider_svgs)}
    <circle cx="{CX}" cy="{CY}" r="{R_WEDGE_OUT}" fill="none" stroke="{RED}" stroke-width="2"/>
    <circle cx="{CX}" cy="{CY}" r="{R_WEDGE_IN}" fill="none" stroke="{RED}" stroke-width="1.4"/>
    <text font-family="Inter" font-weight="600" font-size="7.4" letter-spacing="0.8" fill="{WHITE}">
      <textPath href="#innerRing" startOffset="50%" text-anchor="middle">EVERY ACTION, DECISION, AND INTERACTION SUPPORTS THE SAFETY, SECURITY, AND SUCCESS OF THE ORGANIZATION</textPath>
    </text>
    <text font-family="Oswald" font-weight="700" font-size="17" letter-spacing="2.4" fill="{WHITE}">
      <textPath href="#topArc" startOffset="50%" text-anchor="middle">PHYSICAL SECURITY FORCE CULTURE</textPath>
    </text>
    <text font-family="Inter" font-weight="700" font-size="11" letter-spacing="2.2" fill="{WHITE}">
      <textPath href="#valuesArc" startOffset="50%" text-anchor="middle">VIGILANCE &#8226; INTEGRITY &#8226; RESPECT &#8226; ACCOUNTABILITY &#8226; SERVICE</textPath>
    </text>
  </svg>

  {''.join(blocks)}

  <div class="center-wrap">
    <svg class="core-shield" width="26" height="26" viewBox="-20 -20 40 40">
      <path d="M0,-17 L14,-10.5 V3.5 C14,13 7,18.5 0,21 C-7,18.5 -14,13 -14,3.5 V-10.5 Z" fill="none" stroke="{RED}" stroke-width="2"/>
      <path d="M0,-11 L4.5,7 M-4,-2 h8" fill="none" stroke="{WHITE}" stroke-width="1.3"/>
      <rect x="-3.4" y="2.5" width="6.8" height="5.5" rx="1" fill="none" stroke="{WHITE}" stroke-width="1.3"/>
    </svg>
    <div class="core-eyebrow">CORE PURPOSE</div>
    <div class="core-line">Protect People.</div>
    <div class="core-line accent">Secure Assets.</div>
    <div class="core-line">Enable Operations.</div>
  </div>

  <div class="banner-wrap">
    <div class="tick tl"></div><div class="tick tr"></div><div class="tick bl"></div><div class="tick br"></div>
  </div>
  <div class="banner">
    <div class="l1">ONE TEAM. ONE STANDARD. ONE MISSION.</div>
    <div class="l2">PROTECTING TODAY. ENABLING TOMORROW.</div>
  </div>
</div>
'''

standalone_html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ width:{CANVAS_W}px; height:{CANVAS_H}px; background:{FIELD_WHITE}; }}
{inner_style}
.vw-scale-wrap {{ max-width:none; width:{CANVAS_W}px; height:{CANVAS_H}px; aspect-ratio:auto; }}
.stage {{ position:relative; }}
</style>
</head>
<body>
<div class="vw-scale-wrap">{inner_body}</div>
</body></html>'''

with open(os.path.join(HERE, "valletta_culture_slide.html"),"w") as f:
    f.write(standalone_html)

artifact_html = f'''<title>Physical Security Force Culture</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; padding-block:24px; padding-inline:16px; }}
{inner_style}
</style>
<div class="vw-scale-wrap" id="scaleWrap">{inner_body}</div>
<script>
(function(){{
  var wrap = document.getElementById('scaleWrap');
  var stage = wrap.querySelector('.stage');
  function fit(){{
    var w = wrap.getBoundingClientRect().width;
    var s = w / {CANVAS_W};
    stage.style.transform = 'scale(' + s + ')';
  }}
  new ResizeObserver(fit).observe(wrap);
  fit();
}})();
</script>'''

with open(os.path.join(HERE, "valletta_culture_slide_artifact.html"),"w") as f:
    f.write(artifact_html)
print("written")
