import os

BLACK = "#0A0A0A"
CHARCOAL = "#26282B"
FIELD_WHITE = "#F5F5F3"
RED = "#FF002B"
STEEL = "#5B5F66"
LINE_GRAY = "#D8D9DB"
WHITE = "#FFFFFF"

HERE = os.path.dirname(os.path.abspath(__file__))
def b64(name):
    return open(os.path.join(HERE, name)).read().strip()

LOGO_BLACK = b64("valletta-mark-black.png.b64")
LOGO_WHITE = b64("valletta-mark-white.png.b64")
FONTS_CSS = open(os.path.join(HERE, "..", "fonts_embed.css")).read()

def header():
    return f'''<div class="doc-header">
      <img src="data:image/png;base64,{LOGO_BLACK}" alt="Valletta Industries"/>
      <div class="doc-tag">Leadership Training Student Handout</div>
    </div>'''

def footer():
    return '<div class="doc-footer">Valletta Industries &nbsp;|&nbsp; Leadership Training Student Handout<span class="pagenum"></span></div>'

def sheet(inner, klass=""):
    return f'<section class="sheet {klass}">{inner}</section>'

# ---- outline item helper ----
def item(label, text, level=1, bold=False, children=""):
    cls = f"ol-lvl{level}" + (" ol-bold" if bold else "")
    lbl = f'<span class="ol-label">{label}</span>' if label else ""
    return f'<div class="{cls}">{lbl}<span class="ol-text">{text}</span></div>{children}'

def quote(text, attribution, lead=""):
    lead_html = f'<span class="q-lead">{lead}</span> ' if lead else ""
    return f'<div class="quote">{lead_html}<span class="q-mark">&ldquo;</span>{text}<span class="q-mark">&rdquo;</span> &ndash; <span class="q-attr">{attribution}</span></div>'

def sec_title(num, title):
    return f'<div class="sec-title"><span class="sec-num">{num}.</span> {title}</div>'

def overview():
    items = [
        "Define Leadership",
        "Examples of Effective Leadership",
        "Describe Components of Being an Effective Leader",
        "Ethical Characteristics for Leadership",
        "Describe Motivational Leadership",
        "Understand the Basics of Supervision and Evaluating Work Performance",
    ]
    lis = "".join(f'<li><span class="ov-num">{i+1}.</span> {t}</li>' for i, t in enumerate(items))
    return f'<div class="overview-band">Overview</div><ul class="overview-list">{lis}</ul>'

# ================= CONTENT BLOCKS (packed onto pages by measured height) =================
COVER_HTML = sheet(f'''
  <div class="cover-tick tl"></div><div class="cover-tick br"></div>
  <img class="cover-logo" src="data:image/png;base64,{LOGO_WHITE}" alt="Valletta Industries"/>
  <div class="cover-title">Leadership Training<br/>Student Handout</div>
  <div class="cover-quote">&ldquo;If your actions inspire others to dream more, learn more, do more<br/>
  and become more, then you are a leader.&rdquo;</div>
  <div class="cover-attr">&ndash; John Quincy Adams</div>
''', "cover")

BLOCKS = []  # list of (name, html) — packed greedily onto pages by measured height

sec1 = sec_title(1, "Defining Leadership") + "".join([
  item("A.", "Definition &mdash; The ability to influence others to accomplish a task by providing a purpose, a direction, and appropriate motivation.", 1),
  item("B.", "Being a supervisor doesn&rsquo;t make you a leader", 1),
  item("C.", "Lead by Example", 1),
  item("D.", "Strive to be the best", 1),
  item("E.", "Make those around you better", 1),
  item("F.", "Make sound and timely decisions.", 1),
])
sec2 = sec_title(2, "Examples of Effective Leadership") + "".join([
  item("A.", "Charismatic Leader", 1),
  item("B.", "Transformational Leader", 1),
  item("C.", "Servant Leader", 1),
  item("D.", "Quiet Leaders", 1),
])

BLOCKS.append(("overview", overview()))
BLOCKS.append(("sec1", sec1))
BLOCKS.append(("sec2", sec2))

sec3_a = sec_title(3, "Describe the Components of Effective Leadership") + item("A.", "Leadership Traits", 1, bold=True) + "".join([
  item("1.", "A good leader encourages their people", 2),
  item("2.", "A good leader knows the position above and below them", 2),
  item("3.", "A good leader is honest about their capabilities", 2),
  item("4.", "A good leader treats all team members with dignity and respect", 2),
  item("5.", "A good leader must possess professional character traits such as", 2),
  item("a.", "ambition", 3), item("b.", "creativity", 3), item("c.", "compassion", 3),
  item("d.", "courage", 3), item("e.", "flexibility", 3), item("f.", "honesty (integrity)", 3),
  item("g.", "humility", 3), item("h.", "loyalty", 3), item("i.", "patience", 3),
  item("j.", "discipline", 3), item("k.", "curiosity", 3),
  item("6.", "A good leader understands how to manage stress", 2),
  item("a.", "Exercise", 3), item("b.", "Meditation", 3),
  item("c.", "Discussing with peers, friends, or professional therapy", 3),
  item("d.", "Eat healthy", 3), item("e.", "Regular Breaks", 3), item("f.", "Breathing Drills", 3),
])
BLOCKS.append(("sec3a", sec3_a))

sec3_b = item("B.", "Communication", 1, bold=True) + "".join([
  item("1.", "Understand your people and what they need", 2),
  item("2.", "You must be able to listen", 2),
  item("3.", "Be honest about your performance and your team&rsquo;s performance", 2),
  item("4.", "Ask questions like &ldquo;tell me more&rdquo; or &ldquo;explain what you mean&rdquo;", 2),
  item("5.", "Communication with body language", 2),
  item("6.", "Seek feedback from your team", 2),
])
sec3_c_head = item("C.", "Observing Effective Follower Traits (Knowing your People)", 1, bold=True)
followers_quote = quote(
  "Why would you want to be someone called a follower? A simple answer is people follow because they derive "
  "benefits. The psychological payback of following exceeds the psychological cost of following. Throughout our "
  "human history, most humans were in small, nomadic clusters. These tribes offered protection, food, and "
  "survival. The groups with the best leader and followers had a higher probability of survival than those "
  "poorly led that consisted of poor followers. The physical benefits for followers outweighed the psychological "
  "costs and so most likely they stayed connected to the tribe. If some followers were dissatisfied with the "
  "leader&rsquo;s goals and agenda, they had a choice of either fighting for the top position, or leaving to join "
  "other groups.",
  "(Project Management Institute 2021)", lead="The Psychology of Followers:")
sec3_c_rest = "".join([
  item("1.", "Followers are an essential", 2),
  item("2.", "Types of followers", 2),
  item("a.", "Passive/sheep", 3), item("b.", "Conformist/Yes People", 3),
  item("c.", "Alienated", 3), item("d.", "Effective", 3),
  item("3.", "A follower has good judgment", 2),
  item("4.", "Good followers are good workers", 2),
  item("5.", "To be effective, followers must be willing to share their ideas and opinions with leaders.", 2),
])
sec3_d = item("D.", "Understanding the Mission or Task", 1, bold=True) + "".join([
  item("1.", "Identify the mission", 2),
  item("2.", "Have a shared vision to accomplish a task", 2),
  item("3.", "Regularly create team tasks", 2),
])
BLOCKS.append(("sec3b", sec3_b))
BLOCKS.append(("sec3c", sec3_c_head + followers_quote + sec3_c_rest))
BLOCKS.append(("sec3d", sec3_d))

sec4 = sec_title(4, "Ethical Characteristics for Leadership") + "".join([
  item("A.", "<strong>Fair</strong> &mdash; An ethical leader is fair, and they treat everyone on their team equally with no bias.", 1),
  item("B.", "<strong>Honest</strong> &mdash; Ethical leaders are honest and must always be transparent and fair.", 1),
  item("C.", "<strong>Respect</strong> &mdash; Listening to subordinate and valuing opinions of the team.", 1),
  item("D.", "<strong>Value-Oriented</strong> &mdash; A good leader will make decisions based on the organization&rsquo;s values, and the values of the mission.", 1),
  item("E.", "<strong>Leads by Example</strong> &mdash; Employees will mimic the action of their leader.", 1),
  item("F.", "<strong>Prioritizes the Team</strong> &mdash; Ethical leaders will promote team building and foster a sense of community.", 1),
]) + quote(
  "When setting expectations, no matter what has been said or written, if substandard performance is accepted "
  "and no one is held accountable if there are no consequences, then poor or substandard performance becomes "
  "the new standard. Therefore, leaders must enforce standards.",
  "Jocko Willink", lead="Expectations:")

sec5 = sec_title(5, "Describe Motivational Leadership") + quote(
  "The only thing more contagious than a good attitude is a bad one.", "David Goggins") + "".join([
  item("A.", "A motivational leader can make decisions and set clear goals for their teams.", 1),
  item("B.", "What is the difference between Motivation and Inspiration?", 1),
  item("1.", "Inspiration is an external influence or pulling force that compels you to achieve something.", 2),
  item("2.", "Motivation is an internal influence or a driving force that you feel on the inside to achieve something.", 2),
  item("C.", "A good leader should try to inspire those around them.", 1),
  item("D.", "An effective leader will make logical decisions based on the immediate information available. If the decision was wrong, explain the rationale behind it or what led you to the conclusion and learn from it.", 1),
  item("&ndash;", "<strong>OODA Loop:</strong> Observe, Orient, Decide, and Act", 2),
  item("1.", "Know the strengths and weaknesses of subordinates and look out for their wellbeing.", 2),
]) + quote(
  "A leader must lead, but also be ready to follow. They must be aggressive, but not overbearing. A leader must "
  "be calm, but not robotic. They must be confident, but never cocky. A leader must be brave, but not foolhardy. "
  "They must have a competitive spirit, but be a gracious loser.",
  "Jocko Willink")

BLOCKS.append(("sec4", sec4))
BLOCKS.append(("sec5", sec5))

sec6 = sec_title(6, "Understand the Basics of Supervision and Evaluating Work Performance") + "".join([
  item("A.", "An effective leader does not Micro-Manage.", 1),
  item("B.", "An effective leader is proactive and should avoid having a &ldquo;hands-off&rdquo; mentality.", 1),
  item("C.", "A leader will delegate supervision, responsibility, and authority to capable subordinates.", 1),
  item("D.", "A leader should ensure that all tasks are understood, supervised, and accomplished.", 1),
  item("E.", "A good supervisor can perform the tasks of his subordinates", 1),
  item("F.", "A good leader will hold their team accountable with honest feedback on performance from each assigned task.", 1),
])

reading_items = [
  "12 Rules for Life &ndash; Jordan B. Peterson",
  "Leaders eat last &ndash; Simon Sinek",
  "Leadership and Training for the Fight - Paul Howe",
  "Extreme Ownership &ndash; Jocko Willink",
  "Can&rsquo;t Hurt Me: Master Your Mind and Defy the Odds &ndash; David Goggins",
  '<a href="https://www.johnmaxwell.com/my-purpose/">https://www.johnmaxwell.com/my-purpose/</a>',
  '<a href="https://echelonfront.com/jocko-willink/">https://echelonfront.com/jocko-willink/</a>',
  '<a href="https://www.travismills.org/">https://www.travismills.org/</a>',
]
reading = ('<div class="sec-title">Additional Reading</div>'
           '<p class="ar-lead">Several good books are recommended for follow-on information:</p>'
           '<ul class="ar-list">' + "".join(f'<li>{t}</li>' for t in reading_items) + '</ul>')

BLOCKS.append(("sec6", sec6))
BLOCKS.append(("reading", reading))

# ---- measure each block's natural height, then greedily pack onto pages ----
MEASURE_CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; }}
.probe {{ width:700px; font-family:'Inter',sans-serif; color:{CHARCOAL}; position:absolute; left:0; top:0; }}
.overview-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:13px;
  letter-spacing:1.6px; text-transform:uppercase; padding:8px 14px; margin-bottom:2px; }}
.overview-list {{ list-style:none; border:1px solid {LINE_GRAY}; border-top:none; padding:12px 16px 14px; margin-bottom:22px; }}
.overview-list li {{ font-size:11.3px; line-height:1.7; color:{CHARCOAL}; }}
.ov-num {{ color:{RED}; font-weight:700; margin-right:5px; }}
.sec-title {{ font-family:'Oswald'; font-weight:700; font-size:15.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:20px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {RED}; }}
.sec-num {{ color:{RED}; }}
.ol-lvl1, .ol-lvl2, .ol-lvl3 {{ font-size:11px; line-height:1.48; margin-bottom:6px; color:{CHARCOAL}; }}
.ol-lvl1 {{ padding-left:4px; }}
.ol-lvl2 {{ padding-left:30px; }}
.ol-lvl3 {{ padding-left:56px; }}
.ol-bold > .ol-text {{ font-weight:700; color:{BLACK}; }}
.ol-label {{ color:{RED}; font-weight:700; display:inline-block; min-width:20px; }}
.quote {{ border-left:2px solid {RED}; padding:6px 0 6px 16px; margin:12px 0; font-family:'Inter'; font-style:italic;
  font-size:11px; line-height:1.55; color:{STEEL}; }}
.q-lead {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.q-mark {{ color:{RED}; font-style:normal; }}
.q-attr {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.ar-lead {{ font-size:11.3px; margin-bottom:8px; }}
.ar-list {{ list-style:none; }}
.ar-list li {{ position:relative; padding-left:15px; font-size:11.3px; line-height:1.55; margin-bottom:5px; }}
.ar-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}
.ar-list a {{ color:{CHARCOAL}; }}
'''
MEASURE_HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>{MEASURE_CSS}</style></head>
<body>{"".join(f'<div class="probe" id="probe-{i}">{html_}</div>' for i, (name, html_) in enumerate(BLOCKS))}</body></html>'''
measure_path = os.path.join(HERE, "_measure.html")
with open(measure_path, "w") as f:
    f.write(MEASURE_HTML)

from playwright.sync_api import sync_playwright
heights = {}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    page = browser.new_page(viewport={"width": 900, "height": 400})
    page.goto("file://" + measure_path)
    page.wait_for_timeout(200)
    for i, (name, _) in enumerate(BLOCKS):
        h = page.evaluate(f'document.getElementById("probe-{i}").getBoundingClientRect().height')
        heights[name] = h
    browser.close()
os.remove(measure_path)

PAGE_BUDGET = 860  # usable content height per page below the header
groups = []
cur, cur_h = [], 0
for name, html_ in BLOCKS:
    h = heights[name]
    if cur and cur_h + h > PAGE_BUDGET:
        groups.append(cur)
        cur, cur_h = [], 0
    cur.append(html_)
    cur_h += h
if cur:
    groups.append(cur)

PAGES = [COVER_HTML] + [sheet(header() + "".join(g) + footer()) for g in groups]

CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#CBCCCA; counter-reset:pagenum; }}
.sheet {{ width:816px; height:1056px; background:{FIELD_WHITE}; position:relative; overflow:hidden;
  padding:54px 58px 64px; font-family:'Inter',sans-serif; color:{CHARCOAL}; break-after:page; margin:0 auto;
  counter-increment:pagenum; }}
.sheet + .sheet {{ margin-top:2px; }}
.sheet .pagenum::before {{ content:" \\2013  Page " counter(pagenum) " of {len(PAGES)}"; }}

.doc-header {{ display:flex; align-items:center; justify-content:space-between; padding-bottom:12px;
  border-bottom:2px solid {RED}; margin-bottom:22px; }}
.doc-header img {{ height:30px; width:auto; display:block; }}
.doc-header .doc-tag {{ font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.4px; color:{STEEL}; text-transform:uppercase; }}
.doc-footer {{ position:absolute; left:0; right:0; bottom:26px; text-align:center; font-family:'Inter';
  font-weight:600; font-size:9px; letter-spacing:0.6px; color:{STEEL}; }}

.overview-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:13px;
  letter-spacing:1.6px; text-transform:uppercase; padding:8px 14px; margin-bottom:2px; }}
.overview-list {{ list-style:none; border:1px solid {LINE_GRAY}; border-top:none; padding:12px 16px 14px; margin-bottom:22px; }}
.overview-list li {{ font-size:11.3px; line-height:1.7; color:{CHARCOAL}; }}
.ov-num {{ color:{RED}; font-weight:700; margin-right:5px; }}

.sec-title {{ font-family:'Oswald'; font-weight:700; font-size:15.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:20px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {RED}; }}
.sec-num {{ color:{RED}; }}

.ol-lvl1, .ol-lvl2, .ol-lvl3 {{ font-size:11px; line-height:1.48; margin-bottom:6px; color:{CHARCOAL}; }}
.ol-lvl1 {{ padding-left:4px; }}
.ol-lvl2 {{ padding-left:30px; }}
.ol-lvl3 {{ padding-left:56px; }}
.ol-bold > .ol-text {{ font-weight:700; color:{BLACK}; }}
.ol-label {{ color:{RED}; font-weight:700; display:inline-block; min-width:20px; }}

.quote {{ border-left:2px solid {RED}; padding:6px 0 6px 16px; margin:12px 0; font-family:'Inter'; font-style:italic;
  font-size:11px; line-height:1.55; color:{STEEL}; }}
.q-lead {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.q-mark {{ color:{RED}; font-style:normal; }}
.q-attr {{ font-weight:700; font-style:normal; color:{BLACK}; }}

.ar-lead {{ font-size:11.3px; margin-bottom:8px; }}
.ar-list {{ list-style:none; }}
.ar-list li {{ position:relative; padding-left:15px; font-size:11.3px; line-height:1.55; margin-bottom:5px; }}
.ar-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}
.ar-list a {{ color:{CHARCOAL}; }}

.cover {{ background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:0 90px; }}
.cover-tick {{ position:absolute; width:26px; height:26px; border-color:{RED}; border-style:solid; }}
.cover-tick.tl {{ left:40px; top:40px; border-width:3px 0 0 3px; }}
.cover-tick.br {{ right:40px; bottom:40px; border-width:0 3px 3px 0; }}
.cover-logo {{ height:64px; width:auto; margin-bottom:56px; }}
.cover-title {{ font-family:'Oswald'; font-weight:700; font-size:40px; line-height:1.18; letter-spacing:0.3px;
  text-transform:uppercase; color:{WHITE}; }}
.cover-quote {{ margin-top:44px; font-family:'Inter'; font-style:italic; font-size:16px; line-height:1.6; color:#D8D9DB; }}
.cover-attr {{ margin-top:16px; font-family:'Inter'; font-weight:700; font-size:13px; letter-spacing:1px; color:{RED}; }}
'''

html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{"".join(PAGES)}
</body></html>'''

with open(os.path.join(HERE, "valletta_leadership_handout.html"), "w") as f:
    f.write(html)

print("written", len(PAGES), "pages")
