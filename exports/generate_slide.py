import os

BLACK = "#0A0A0A"
CHARCOAL = "#1C1D21"
FIELD_WHITE = "#F5F5F3"
RED = "#FF002B"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"
MUTED_ON_DARK = "#A6A9AE"

CANVAS_W, CANVAS_H = 2000, 950

ICONS = {
 "people": '<path d="M-13,4 a6.2,6.2 0 1,1 0.01,0 M13,4 a5.4,5.4 0 1,1 0.01,0 M0,-8.5 a7,7 0 1,1 0.01,0" fill="none" stroke="currentColor" stroke-width="2.1"/><path d="M-20,18 c0,-8 5,-12.5 7,-12.5 M20,18 c0,-8 -5,-12.5 -7,-12.5 M-10,18 c0,-9.5 7,-15 10,-15 c3,0 10,5.5 10,15" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/>',
 "shield": '<path d="M0,-17 L14,-10.5 V3.5 C14,13 7,18.5 0,21 C-7,18.5 -14,13 -14,3.5 V-10.5 Z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/><path d="M-6,1.5 L-1.5,7 L8,-5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>',
 "action": '<path d="M-2,-19 L-15,3 L-3,3 L-6,19 L16,-5 L2,-5 Z" fill="currentColor" stroke="none"/>',
 "speech": '<path d="M-17,-11.5 h34 a3.5,3.5 0 0 1 3.5,3.5 v14 a3.5,3.5 0 0 1 -3.5,3.5 h-19.5 l-8,7 v-7 h-6 a3.5,3.5 0 0 1 -3.5,-3.5 v-14 a3.5,3.5 0 0 1 3.5,-3.5 Z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/><circle cx="-7" cy="-1" r="1.6" fill="currentColor" stroke="none"/><circle cx="0" cy="-1" r="1.6" fill="currentColor" stroke="none"/><circle cx="7" cy="-1" r="1.6" fill="currentColor" stroke="none"/>',
 "handshake": '<path d="M-15,-14 A15,15 0 0,1 14,-4" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/><path d="M14,-4 L14,-11 M14,-4 L7,-5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/><path d="M15,14 A15,15 0 0,1 -14,4" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/><path d="M-14,4 L-14,11 M-14,4 L-7,5.5" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>',
}

def icon_svg(name, size=30, color=RED):
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

col_blocks = []
for i, p in enumerate(PILLARS):
    bullets_html = "".join(f'<li>{b}</li>' for b in p["bullets"])
    sep = '<div class="col-sep"></div>' if i > 0 else ''
    col_blocks.append(f'''
    {sep}
    <div class="col">
      <div class="col-top">
        <span class="col-num">{p["num"]:02d}</span>
        <span class="col-icon">{icon_svg(p["icon"])}</span>
      </div>
      <h2>{p["title"]}</h2>
      <div class="col-sub">{p["sub"]}</div>
      <ul class="col-bullets">{bullets_html}</ul>
      <div class="col-mindset"><p>{p["mindset"]}</p><span>Mindset</span></div>
    </div>''')

HERE = os.path.dirname(os.path.abspath(__file__))
fonts_css = open(os.path.join(HERE, "fonts_embed.css")).read()
logo_b64 = open(os.path.join(HERE, "logo_b64.txt")).read().strip()

inner_style = f'''
{fonts_css}
.page {{ width:{CANVAS_W}px; height:{CANVAS_H}px; background:{FIELD_WHITE}; font-family:'Inter',sans-serif; position:relative; overflow:hidden; }}

.masthead {{ height:118px; display:flex; align-items:center; justify-content:space-between; padding:0 56px; }}
.masthead img {{ height:58px; width:auto; display:block; }}
.masthead .title-block {{ text-align:right; }}
.masthead .eyebrow {{ font-family:'Inter'; font-weight:700; font-size:12px; letter-spacing:2.6px; color:{RED}; text-transform:uppercase; }}
.masthead h1 {{ font-family:'Oswald'; font-weight:700; font-size:34px; letter-spacing:0.3px; text-transform:uppercase; color:{BLACK}; line-height:1.05; margin-top:4px; }}

.core {{ height:172px; background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; position:relative; padding:0 60px; }}
.core::before, .core::after {{ content:''; position:absolute; width:20px; height:20px; border-color:{RED}; border-style:solid; }}
.core::before {{ left:22px; top:18px; border-width:2px 0 0 2px; }}
.core::after {{ right:22px; bottom:18px; border-width:0 2px 2px 0; }}
.core .eyebrow {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:2.4px; color:{RED}; text-transform:uppercase; margin-bottom:10px; }}
.core .statement {{ font-family:'Oswald'; font-weight:700; font-size:33px; letter-spacing:0.2px; text-transform:uppercase; color:{WHITE}; line-height:1.15; }}
.core .statement .accent {{ color:{RED}; }}
.core .tagline {{ margin-top:10px; font-size:13.5px; color:#B9BBBE; max-width:80ch; line-height:1.5; }}

.cols {{ height:430px; display:flex; padding:0 40px; }}
.col {{ flex:1; min-width:0; padding:26px 22px 0; display:flex; flex-direction:column; }}
.col-sep {{ width:1px; background:{LINE_GRAY}; margin:26px 0 30px; }}
.col-top {{ display:flex; align-items:center; gap:10px; margin-bottom:14px; }}
.col-num {{ font-family:'Oswald'; font-weight:700; font-size:26px; color:{RED}; }}
.col-icon {{ width:38px; height:38px; border:1.5px solid {RED}; border-radius:50%; display:flex; align-items:center; justify-content:center; flex:none; }}
.col h2 {{ font-family:'Oswald'; font-weight:700; font-size:19.5px; letter-spacing:0.2px; text-transform:uppercase; color:{BLACK}; line-height:1.14; min-height:46px; }}
.col-sub {{ font-family:'Inter'; font-weight:700; font-size:10.5px; letter-spacing:1px; color:{RED}; text-transform:uppercase; margin-top:5px; margin-bottom:14px; }}
.col-bullets {{ list-style:none; flex:none; }}
.col-bullets li {{ position:relative; padding-left:15px; font-size:13.3px; line-height:1.48; color:{CHARCOAL}; margin-bottom:8px; }}
.col-bullets li::before {{ content:''; position:absolute; left:0; top:6px; width:5px; height:5px; background:{RED}; }}
.col-mindset {{ margin-top:20px; padding-top:16px; border-top:1px solid {LINE_GRAY}; }}
.col-mindset p {{ font-family:'Inter'; font-style:italic; font-size:13px; line-height:1.42; color:{STEEL}; }}
.col-mindset p::before {{ content:'\\201C'; }}
.col-mindset p::after {{ content:'\\201D'; }}
.col-mindset span {{ display:block; margin-top:7px; font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.4px; color:{BLACK}; text-transform:uppercase; }}

.values {{ height:60px; background:{BLACK}; color:{WHITE}; display:flex; align-items:center; justify-content:center; font-family:'Inter'; font-weight:700; font-size:13px; letter-spacing:2.4px; text-transform:uppercase; border-top:1px solid #2A2C30; }}
.values span {{ color:{RED}; padding:0 5px; }}
.banner {{ height:110px; background:{BLACK}; color:{WHITE}; display:flex; flex-direction:column; align-items:center; justify-content:center; }}
.banner .l1 {{ font-family:'Oswald'; font-weight:700; font-size:20px; letter-spacing:1.2px; }}
.banner .l2 {{ font-family:'Inter'; font-weight:700; font-size:12px; letter-spacing:1.8px; color:{RED}; margin-top:7px; text-transform:uppercase; }}
'''

inner_body = f'''
<div class="page">
  <div class="masthead">
    <img src="data:image/png;base64,{logo_b64}" alt="Valletta Industries / SOC"/>
    <div class="title-block">
      <div class="eyebrow">Physical Security Division</div>
      <h1>Physical Security Force Culture</h1>
    </div>
  </div>

  <div class="core">
    <div class="eyebrow">Core Purpose</div>
    <div class="statement">Protect People. <span class="accent">Secure Assets.</span> Enable Operations.</div>
    <div class="tagline">Every action, decision, and interaction supports the safety, security, and success of the organization.</div>
  </div>

  <div class="cols">
    {''.join(col_blocks)}
  </div>

  <div class="values">Vigilance <span>&#8226;</span> Integrity <span>&#8226;</span> Respect <span>&#8226;</span> Accountability <span>&#8226;</span> Service</div>
  <div class="banner">
    <div class="l1">ONE TEAM. ONE STANDARD. ONE MISSION.</div>
    <div class="l2">Protecting Today. Enabling Tomorrow.</div>
  </div>
</div>
'''

standalone_html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; }}
{inner_style}
</style>
</head>
<body>{inner_body}</body></html>'''

with open(os.path.join(HERE, "valletta_culture_slide.html"),"w") as f:
    f.write(standalone_html)

artifact_html = f'''<title>Physical Security Force Culture</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; padding-block:24px; padding-inline:16px; }}
.scale-wrap {{ width:100%; max-width:{CANVAS_W}px; margin:0 auto; aspect-ratio:{CANVAS_W}/{CANVAS_H}; position:relative; }}
{inner_style}
.page {{ position:absolute; left:0; top:0; transform-origin:top left; }}
</style>
<div class="scale-wrap" id="scaleWrap">{inner_body}</div>
<script>
(function(){{
  var wrap = document.getElementById('scaleWrap');
  var page = wrap.querySelector('.page');
  function fit(){{
    var w = wrap.getBoundingClientRect().width;
    var s = w / {CANVAS_W};
    page.style.transform = 'scale(' + s + ')';
  }}
  new ResizeObserver(fit).observe(wrap);
  fit();
}})();
</script>'''

with open(os.path.join(HERE, "valletta_culture_slide_artifact.html"),"w") as f:
    f.write(artifact_html)

print("written", CANVAS_W, CANVAS_H)
