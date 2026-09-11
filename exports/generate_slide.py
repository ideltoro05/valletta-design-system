import os

BLACK = "#0A0A0A"
CHARCOAL = "#1C1D21"
FIELD_WHITE = "#F5F5F3"
RED = "#FF002B"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"
INK = "#17181A"

ICONS = {
 "people": '<path d="M-13,4 a6.2,6.2 0 1,1 0.01,0 M13,4 a5.4,5.4 0 1,1 0.01,0 M0,-8.5 a7,7 0 1,1 0.01,0" fill="none" stroke="currentColor" stroke-width="2.1"/><path d="M-20,18 c0,-8 5,-12.5 7,-12.5 M20,18 c0,-8 -5,-12.5 -7,-12.5 M-10,18 c0,-9.5 7,-15 10,-15 c3,0 10,5.5 10,15" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/>',
 "shield": '<path d="M0,-17 L14,-10.5 V3.5 C14,13 7,18.5 0,21 C-7,18.5 -14,13 -14,3.5 V-10.5 Z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/><path d="M-6,1.5 L-1.5,7 L8,-5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>',
 "action": '<path d="M-2,-19 L-15,3 L-3,3 L-6,19 L16,-5 L2,-5 Z" fill="currentColor" stroke="none"/>',
 "speech": '<path d="M-17,-11.5 h34 a3.5,3.5 0 0 1 3.5,3.5 v14 a3.5,3.5 0 0 1 -3.5,3.5 h-19.5 l-8,7 v-7 h-6 a3.5,3.5 0 0 1 -3.5,-3.5 v-14 a3.5,3.5 0 0 1 3.5,-3.5 Z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/><circle cx="-7" cy="-1" r="1.6" fill="currentColor" stroke="none"/><circle cx="0" cy="-1" r="1.6" fill="currentColor" stroke="none"/><circle cx="7" cy="-1" r="1.6" fill="currentColor" stroke="none"/>',
 "handshake": '<path d="M-15,-14 A15,15 0 0,1 14,-4" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/><path d="M14,-4 L14,-11 M14,-4 L7,-5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/><path d="M15,14 A15,15 0 0,1 -14,4" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/><path d="M-14,4 L-14,11 M-14,4 L-7,5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>',
}

def icon_svg(name, size=34, color=RED):
    return f'<svg width="{size}" height="{size}" viewBox="-21 -21 42 42" color="{color}">{ICONS[name]}</svg>'

PILLARS = [
    {"num":1,"title":"You Matter","sub":"PEOPLE FIRST CULTURE",
     "bullets":["Treat everyone with dignity and respect.",
                "Prioritize safety and wellbeing.",
                "Look out for one another.",
                "Develop and mentor teammates.",
                "Recognize contributions and successes."],
     "mindset":"Every person deserves to go home safe and know they are valued.",
     "icon":"people"},
    {"num":2,"title":"Professional and Consistent","sub":"TRUSTED THROUGH EXCELLENCE",
     "bullets":["Follow standards and procedures.",
                "Maintain appearance and readiness.",
                "Demonstrate discipline and accountability.",
                "Treat every situation objectively.",
                "Deliver the same level of service every shift, every day."],
     "mindset":"Our reputation is earned through consistency.",
     "icon":"shield"},
    {"num":3,"title":"Collaborate and Win","sub":"ONE TEAM, ONE MISSION",
     "bullets":["Share information proactively.",
                "Support fellow officers and business partners.",
                "Build relationships across departments.",
                "Seek solutions, not blame.",
                "Celebrate team achievements."],
     "mindset":"We are stronger together than we are individually.",
     "icon":"handshake"},
    {"num":4,"title":"Say Something","sub":"SEE IT. OWN IT. REPORT IT.",
     "bullets":["Report concerns immediately.",
                "Escalate issues without hesitation.",
                "Challenge unsafe conditions respectfully.",
                "Encourage open communication.",
                "Learn from incidents and near misses."],
     "mindset":"Silence creates risk. Speaking up creates safety.",
     "icon":"speech"},
    {"num":5,"title":"Action Oriented","sub":"DECISIVE WHEN IT MATTERS",
     "bullets":["Respond promptly.",
                "Take initiative.",
                "Solve problems at the lowest level possible.",
                "Adapt to changing circumstances.",
                "Drive issues to resolution."],
     "mindset":"When action is required, we lead.",
     "icon":"action"},
]

pillar_blocks = []
for i, p in enumerate(PILLARS):
    bullets_html = "".join(f'<li>{b}</li>' for b in p["bullets"])
    divider = '<div class="pillar-divider"></div>' if i > 0 else ''
    pillar_blocks.append(f'''
    {divider}
    <article class="pillar">
      <div class="pillar-num">{p["num"]:02d}</div>
      <div class="pillar-body">
        <div class="pillar-head">
          <span class="pillar-icon">{icon_svg(p["icon"])}</span>
          <div class="pillar-headtext">
            <h2>{p["title"]}</h2>
            <div class="pillar-sub">{p["sub"]}</div>
          </div>
        </div>
        <ul class="pillar-bullets">{bullets_html}</ul>
      </div>
      <blockquote class="pillar-mindset">
        <p>{p["mindset"]}</p>
        <footer>Mindset</footer>
      </blockquote>
    </article>''')

HERE = os.path.dirname(os.path.abspath(__file__))
fonts_css = open(os.path.join(HERE, "fonts_embed.css")).read()
logo_b64 = open(os.path.join(HERE, "logo_b64.txt")).read().strip()

inner_style = f'''
{fonts_css}
.doc {{ max-width:920px; margin:0 auto; font-family:'Inter',sans-serif; color:{INK}; }}

.masthead {{ display:flex; align-items:center; justify-content:space-between; padding:44px 0 36px; border-bottom:1px solid {LINE_GRAY}; }}
.masthead img {{ height:52px; width:auto; display:block; }}
.masthead .doctype {{ font-family:'Inter'; font-weight:700; font-size:11px; letter-spacing:2.2px; color:{STEEL}; text-align:right; text-transform:uppercase; }}

.hero {{ padding:64px 0 56px; }}
.eyebrow {{ font-family:'Inter'; font-weight:700; font-size:12px; letter-spacing:3px; color:{RED}; text-transform:uppercase; margin-bottom:14px; }}
.hero h1 {{ font-family:'Oswald'; font-weight:700; font-size:clamp(40px,7vw,68px); line-height:1.03; letter-spacing:0.2px; text-transform:uppercase; color:{BLACK}; text-wrap:balance; }}
.hero h1 .accent {{ color:{RED}; }}
.hero .dek {{ margin-top:20px; font-size:17px; line-height:1.6; color:{STEEL}; max-width:62ch; }}

.core-purpose {{ background:{BLACK}; color:{WHITE}; padding:56px 48px; margin:0 -48px 72px; border-radius:2px; position:relative; }}
.core-purpose::before, .core-purpose::after {{ content:''; position:absolute; width:22px; height:22px; border-color:{RED}; border-style:solid; }}
.core-purpose::before {{ left:20px; top:20px; border-width:2px 0 0 2px; }}
.core-purpose::after {{ right:20px; bottom:20px; border-width:0 2px 2px 0; }}
.core-purpose .eyebrow {{ text-align:center; color:{RED}; }}
.core-statement {{ font-family:'Oswald'; font-weight:700; font-size:clamp(26px,4.2vw,40px); line-height:1.18; text-align:center; text-transform:uppercase; letter-spacing:0.2px; }}
.core-statement .accent {{ color:{RED}; }}
.core-tagline {{ text-align:center; margin-top:22px; font-size:15px; color:#B9BBBE; max-width:56ch; margin-left:auto; margin-right:auto; line-height:1.6; }}

.pillars {{ padding-bottom:8px; }}
.pillar-divider {{ height:1px; background:{LINE_GRAY}; margin:0; }}
.pillar {{ display:grid; grid-template-columns:88px 1fr 280px; column-gap:36px; padding:52px 0; align-items:start; }}
.pillar-num {{ font-family:'Oswald'; font-weight:700; font-size:40px; color:{RED}; line-height:1; }}
.pillar-head {{ display:flex; align-items:flex-start; gap:18px; margin-bottom:20px; }}
.pillar-icon {{ flex:none; width:40px; height:40px; display:flex; align-items:center; justify-content:center; border:1.5px solid {RED}; border-radius:50%; }}
.pillar-icon svg {{ display:block; }}
.pillar h2 {{ font-family:'Oswald'; font-weight:700; font-size:27px; letter-spacing:0.2px; text-transform:uppercase; color:{BLACK}; line-height:1.12; }}
.pillar-sub {{ font-family:'Inter'; font-weight:700; font-size:12px; letter-spacing:1.4px; color:{RED}; text-transform:uppercase; margin-top:6px; }}
.pillar-bullets {{ list-style:none; max-width:56ch; }}
.pillar-bullets li {{ position:relative; padding-left:20px; font-size:15.5px; line-height:1.55; color:{INK}; margin-bottom:9px; }}
.pillar-bullets li::before {{ content:''; position:absolute; left:0; top:9px; width:7px; height:7px; background:{RED}; }}
.pillar-mindset {{ border-left:2px solid {RED}; padding-left:20px; margin:0; }}
.pillar-mindset p {{ font-family:'Inter'; font-style:italic; font-size:17px; line-height:1.5; color:{CHARCOAL}; }}
.pillar-mindset p::before {{ content:'\\201C'; }}
.pillar-mindset p::after {{ content:'\\201D'; }}
.pillar-mindset footer {{ margin-top:10px; font-family:'Inter'; font-weight:700; font-size:11px; letter-spacing:1.6px; color:{STEEL}; text-transform:uppercase; }}

.values-band {{ background:{BLACK}; color:{WHITE}; margin:56px -48px 0; padding:26px 48px; text-align:center; font-family:'Inter'; font-weight:700; font-size:14px; letter-spacing:2.6px; text-transform:uppercase; }}
.values-band span {{ color:{RED}; padding:0 4px; }}

.closing-banner {{ background:{BLACK}; color:{WHITE}; margin:0 -48px; padding:34px 48px 46px; text-align:center; }}
.closing-banner .l1 {{ font-family:'Oswald'; font-weight:700; font-size:19px; letter-spacing:1.2px; }}
.closing-banner .l2 {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:1.8px; color:{RED}; margin-top:8px; text-transform:uppercase; }}

@media (max-width:760px) {{
  .pillar {{ grid-template-columns:1fr; row-gap:18px; }}
  .pillar-num {{ font-size:30px; }}
  .pillar-mindset {{ margin-top:4px; }}
}}

@media print {{
  .pillar, .core-purpose, .masthead, .hero {{ break-inside:avoid; }}
  .values-band, .closing-banner {{ break-before:avoid; }}
}}
'''

inner_body = f'''
<div class="doc">
  <header class="masthead">
    <img src="data:image/png;base64,{logo_b64}" alt="Valletta Industries / SOC"/>
    <div class="doctype">Culture Framework</div>
  </header>

  <section class="hero">
    <div class="eyebrow">Physical Security Division</div>
    <h1>Physical Security<br><span class="accent">Force</span> Culture</h1>
    <p class="dek">The behaviors and mindsets that define how every officer shows up, every shift.</p>
  </section>

  <section class="core-purpose">
    <div class="eyebrow">Core Purpose</div>
    <p class="core-statement">Protect people. <span class="accent">Secure assets.</span> Enable operations.</p>
    <p class="core-tagline">Every action, decision, and interaction supports the safety, security, and success of the organization.</p>
  </section>

  <section class="pillars">
    {''.join(pillar_blocks)}
  </section>

  <div class="values-band">Vigilance <span>&#8226;</span> Integrity <span>&#8226;</span> Respect <span>&#8226;</span> Accountability <span>&#8226;</span> Service</div>

  <footer class="closing-banner">
    <div class="l1">ONE TEAM. ONE STANDARD. ONE MISSION.</div>
    <div class="l2">Protecting Today. Enabling Tomorrow.</div>
  </footer>
</div>
'''

standalone_html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; padding:0 48px; }}
{inner_style}
</style>
</head>
<body>{inner_body}</body></html>'''

with open(os.path.join(HERE, "valletta_culture_slide.html"),"w") as f:
    f.write(standalone_html)

artifact_html = f'''<title>Physical Security Force Culture</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; padding-inline:48px; padding-block:0; }}
{inner_style}
@media (max-width:600px) {{ body {{ padding-inline:20px; }} .core-purpose,.values-band,.closing-banner {{ margin-left:-20px; margin-right:-20px; padding-left:20px; padding-right:20px; }} }}
</style>
{inner_body}'''

with open(os.path.join(HERE, "valletta_culture_slide_artifact.html"),"w") as f:
    f.write(artifact_html)

print("written")
