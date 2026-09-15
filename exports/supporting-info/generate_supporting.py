import os, re

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

def esc(t):
    return t  # source strings are already HTML-safe (no raw &, <, > outside our own markup)

def header():
    return f'''<div class="doc-header">
      <img src="data:image/png;base64,{LOGO_BLACK}" alt="Valletta Industries"/>
      <div class="doc-tag">Effective Motivational Leadership &ndash; Supporting Information</div>
    </div>'''

def footer():
    return '<div class="doc-footer">Valletta Industries &nbsp;|&nbsp; Effective Motivational Leadership &ndash; Supporting Information<span class="pagenum"></span></div>'

def sheet(inner, klass=""):
    return f'<section class="sheet {klass}">{inner}</section>'

def roman(numeral, text):
    return f'<div class="roman-band"><span class="roman-num">{numeral}</span>{text}</div>'

def epo(label, text):
    return f'<div class="epo-heading"><span class="epo-label">{label}</span>{text}</div>'

def subhead(text):
    return f'<div class="h2-sub">{text}</div>'

def p(text):
    return f'<p class="body-p">{text}</p>'

def leadin(label, text):
    return f'<p class="body-p"><span class="lead-in">{label}</span> {text}</p>'

def note(tag, lines):
    body = "".join(f'<div class="note-line">{l}</div>' for l in lines)
    return f'<div class="note-box"><span class="note-tag">{tag}</span>{body}</div>'

def quote(text, attribution=None, lead=None):
    lead_html = f'<span class="q-lead">{lead}</span> ' if lead else ""
    attr_html = f' &ndash; <span class="q-attr">{attribution}</span>' if attribution else ""
    return f'<div class="quote">{lead_html}<span class="q-mark">&ldquo;</span>{text}<span class="q-mark">&rdquo;</span>{attr_html}</div>'

IND = [0, 20, 40]
def item(label, text, level=0):
    return f'<div class="outline-item lvl-{level}"><span class="item-label">{label}</span>{text}</div>'

def stat(text):
    return f'<li>{text}</li>'

def refs(items):
    body = "".join(f'<div class="ref-link">{t}</div>' for t in items)
    return f'<div class="ref-block"><span class="ref-tag">References</span>{body}</div>'

# ================= CONTENT BLOCKS =================
BLOCKS = []  # list of (name, html)

COVER_HTML = sheet(f'''
  <div class="cover-tick tl"></div><div class="cover-tick br"></div>
  <img class="cover-logo" src="data:image/png;base64,{LOGO_WHITE}" alt="Valletta Industries"/>
  <div class="cover-eyebrow">Supporting Information</div>
  <div class="cover-title">Effective Motivational<br/>Leadership</div>
  <div class="cover-meta">Leadership Training</div>
''', "cover")

# ---- References (no heading in source; labeled per the same convention used for
# the unlabeled instructor script in the earlier Instructor Outline rebrand) ----
BLOCKS.append(("references", refs([
    "https://www.projectmanagement.com/contentPages/article.cfm?ID=570414&thisPageURL=/articles/570414/Leading-in-High-Stress-Environments#_=_",
    "https://www.360training.com/blog/8-characteristics-ethical-leader",
    "https://www.pmi.org/learning/library/importance-of-effective-followers-5887",
])))

# ---- II. PRESENTATION : opening ----
pres_open = (
    roman("II.", "Presentation")
    + note("NOTE", ["Show Slide “Effective Motivational Leadership” — Introduce yourself to the class."])
    + leadin("INTRODUCTION:", "Good morning/afternoon/evening, my name is __________. Your next period of instruction will be on Effective Motivational Leadership.")
    + note("NOTE", ["Show Slide “Why are you here?” — Solicit feedback from students and get them talking about why they are sitting in the course."])
)
BLOCKS.append(("pres_open", pres_open))

gain_attention = (
    leadin("GAIN ATTENTION:", "Being a manager/leader on any SOC contract you will be around people all from different backgrounds and with different past experiences and it is your responsibility to effectively lead and complete assigned tasks all while dealing with different personalities. Your people (subordinates) will determine if you are an effective or in-effective leader. Effective leadership begins with having the proper mindset and attitude.")
)
BLOCKS.append(("gain_attention", gain_attention))

video1 = (
    note("VIDEO 1 — SGT. TRAVIS MILLS", ["06:14 — https://www.youtube.com/watch?v=eSytAgtLqVw", "Talk about the video as it pertains to a positive attitude"])
    + quote("The only thing more contagious than a good attitude is a bad one.", "David Goggins")
)
BLOCKS.append(("video1", video1))

# ---- Statistics ----
stats = (
    note("NOTE", ["Show Slide “Statistics” — Discuss each and solicit feedback. Continue with “Statistics Continued” slide."])
    + subhead("Statistics")
    + p("According to MDA Training “5 Workplace Leadership Statistics You Shouldn't Ignore.” MDA Training, 12 Feb. 2020, mdatraining.com/blog/workplace-leadership-statistics/.")
    + '<ul class="stat-list">'
    + stat("Employees who are supervised by highly engaged LEADERSHIP teams are 39% more likely to be engaged themselves.")
    + stat("32% of employees lack the confidence to put new ideas to employers")
    + stat("58% of Managers report that they never received any management training")
    + stat("82% of employees don’t trust their boss to tell the truth")
    + stat("79% of employees cite the “lack of appreciation” as a reason for quitting their job.")
    + '</ul>'
    + p("So with these numbers in mind, what is the one common denominator that I/You/We can do to change these numbers? We can be better examples of the leader we want above us.")
)
BLOCKS.append(("stats", stats))

maxwell = (
    note("NOTE", ["Show Slide — John Maxwell Quote"])
    + quote("The single biggest way to impact an organization is to focus on leadership development. There is almost no limit to the potential of an organization that recruits good people, raises them up as leaders and continually develops them.", "John Maxwell")
)
BLOCKS.append(("maxwell", maxwell))

# ---- Performance Objectives ----
objectives = (
    note("NOTE", ["Show Slide “Terminal Performance Objective”"])
    + subhead("Introduction of Performance Objectives")
    + '<p class="body-p"><strong>Terminal Performance Objective (TPO)(s):</strong></p>'
    + item("TPO 1:", "Students will be able to properly define and identify leadership styles and be able to motivate subordinates and effectively lead.")
    + note("NOTE", ["Show Slide “Enabling Performance Objectives”"])
    + '<p class="body-p"><strong>Enabling Performance Objective (EPO)(s):</strong></p>'
    + item("EPO 1:", "Define Leadership")
    + item("EPO 2:", "Identify and discuss examples of effective and in-effective leadership.")
    + item("EPO 3:", "List and describe in detail the four (4) components of effective leadership.")
    + item("EPO 4:", "List four (4) Ethics qualities found in a professional work environment.")
    + item("EPO 5:", "Describe what motivational leadership is.")
    + item("EPO 6:", "Understand the basics of supervision and evaluating work performance.")
)
BLOCKS.append(("objectives", objectives))

video2 = note("VIDEO 2 — “WE WERE SOLDIERS”", ["00:16 — https://www.youtube.com/watch?v=abFAhCtUyMM", "Solicit feedback"])
BLOCKS.append(("video2", video2))

# ---- EPO 1: Define Leadership ----
epo1_a = (
    epo("EPO 1:", "Define leadership.")
    + note("NOTE", ["Show Slide “Leadership” and “Leadership Continued”"])
    + subhead("Leadership")
    + item("a.", "Definition — The ability to influence others to accomplish a task by proviing a purpose, a direction and appropriate motivation. Explaining the mission to subordinates helps them keep the importance of the objective up front and allows them to perform in a more efficient and disciplined manner.")
    + item("b.", "Leadership is not a rank, leadership is not a position, leadership is a choice. It has nothing to do with your position on the organizational chart, once you make a conscious decision to look after the person on your left and your right you have become a leader.")
    + item("c.", "We have all heard the phrase “Leaders Lead” well do they? Leaders must set the example for all to follow. Good leaders set the standard and can meet it/surpass it. Leading by example instills confidence and respect in their leaders and in turn makes them more effective.")
)
BLOCKS.append(("epo1_a", epo1_a))
epo1_b = (
    item("d.", "Be technically proficient, give off a good/positive vibe not a negative one")
    + item("e.", "Seek responsibility and always take responsibility for your actions, good or bad")
    + item("f.", "Make sound and timely decisions. A good leader makes a decision, right wrong or indifferent make a decision, indecision or no decision is wrong every time and can result in an adverse action. If the decision was the wrong one, explain the rationale behind it or what led you to the decision and learn from it.")
)
BLOCKS.append(("epo1_b", epo1_b))

# ---- EPO 2: Examples of effective / in-effective leadership ----
epo2_a = (
    epo("EPO 2:", "Identify and discuss examples of effective and in-effective leadership.")
    + note("NOTE", ["Show Slide “Charismatic Leader” — There will be examples and photos of each, discuss and solicit feedback."])
    + item("a.", "Sir Winston Churchill — Charismatic Leader, led with passion, used charm to gain followers and put other people before himself. Other examples, Fidel Castro, Malcolm X and Nelson Mandela.")
)
BLOCKS.append(("epo2_a", epo2_a))
epo2_b = (
    note("NOTE", ["Show Slide “Transformational Leader” — There will be examples and photos of each, discuss and solicit feedback."])
    + item("b.", "Dr. Martin Luther King — Transformational Leader, showed other people their visions, very passionate about his own visions and people followed him because he was honest. Some other examples Henry Ford, Steve Jobs and Adolf Hitler.")
)
BLOCKS.append(("epo2_b", epo2_b))
epo2_c = (
    note("NOTE", ["Show Slide “Servant Leader” — There will be examples and photos of each, discuss and solicit feedback."])
    + item("c.", "Mahatma Ghandi — Servant Leader — took care of everyone before he gave followers what they want. Another example is Mother Teresa.")
)
BLOCKS.append(("epo2_c", epo2_c))
epo2_d = (
    note("NOTE", ["Show Slide “Quiet Leaders” — There will be examples and photos of each, discuss and solicit feedback."])
    + item("d.", "Rosa Parks — Quiet Leaders are actually Introverts — Don’t try to be a leader, just comes natural and when they think of something that needs to be done, they do it and don’t rely on someone else. Other examples President Barrack Obama, Bill Gates and Warren Buffett.")
)
BLOCKS.append(("epo2_d", epo2_d))
epo2_e = (
    note("NOTE", ["Show Slide “Effective vs. In-Effective” — Examples of 3 controversial leaders are presented. Discuss each and how their methods made them a good or bad leader."])
    + item("e.", "Examples of In-Effective Leadership — [Solicit feedback from the class and discuss names that come up] David Koresh, Osama Bin Laden, Saddam Hussein, etc. Were they ineffective leaders or were they good leaders with bad intentions?")
    + note("VIDEO 3 — “WE WERE SOLDIERS”", ["01:06 — https://www.youtube.com/watch?v=0fpK9591u6M", "Solicit feedback"])
    + note("NOTE", ["Show Slide “What type of leaders were depicted in the two clips” “What type of leader, are you?”"])
)
BLOCKS.append(("epo2_e", epo2_e))

# ---- EPO 3: Four components of effective leadership ----
epo3_open = (
    epo("EPO 3:", "List and describe in detail the four (4) components of effective leadership.")
    + note("NOTE", ["Show Slide “4 Components of Effective Leadership”"])
    + subhead("1. Leader")
    + item("a.", "A good leader encourages his/her staff to participate in all assigned tasks")
    + item("b.", "A good leader educates his/herself to understand and mentor those below them and also support those above")
    + item("c.", "A good leader knows his/her capabilities to include strengths/weaknesses and limitations")
    + item("d.", "A good leader knows his/her staffs strengths, weaknesses and looks out for their well being")
    + item("e.", "A good leader is disciplined and leads effectively and treats all members with dignity and respect")
    + item("f.", "A good leader must possess professional character traits")
    + item("g.", "A good leader must manage stress and avoid burnout")
    + quote("A leader must lead, but also be ready to follow. They must be aggressive, but not overbearing. A leader must be calm, but not robotic. They must be confident, but never cocky. A leader must be brave, but not foolhardy. They must have a competitive spirit, but be a gracious loser.", "Jocko Willink")
)
BLOCKS.append(("epo3_open", epo3_open))

epo3_follower = (
    note("NOTE", ["Show Slide “Follower”"])
    + subhead("2. Follower")
    + item("a.", "Followers need encouragement")
    + item("b.", "Deserves praise when earned")
    + item("c.", "Constantly evaluated and may need to be reprimanded and/or punished")
    + item("d.", "A follower will develop their mutual trust, respect and confidence from a good leader leading by example, being respectful and keeping them informed")
    + item("e.", "Followers volunteer to help")
)
BLOCKS.append(("epo3_follower", epo3_follower))

epo3_situation = (
    note("NOTE", ["Show Slide “Situation”"])
    + subhead("3. Situation")
    + item("a.", "Understanding the situation is very important. One leadership style may not work in all situations. Leadership styles need to be fluid")
    + item("b.", "Consider all available resources and factors during any given situation")
    + item("c.", "Consider the followers competence, motivation and commitment to job performance")
    + item("d.", "Timing of actions and/or reactions may also be important.")
)
BLOCKS.append(("epo3_situation", epo3_situation))

video4 = note("VIDEO 4 — JOCKO WILLINK / MULLIGAN BROTHERS INTERVIEW", ["3:27 — https://www.youtube.com/watch?v=jYK-drFNI6o&pbjreload=10", "The interview discusses proper timing and response"])
BLOCKS.append(("video4", video4))

epo3_comm = (
    note("NOTE", ["Show Slide “Communications”"])
    + subhead("4. Communications")
    + item("a.", "Exchange information, ideas and insure you are precisely understood and you understand your staff")
    + item("b.", "The proper method of communication may vary and is situational dependent")
    + item("c.", "Effective communication is demonstrated in the completion of assigned tasks in a timely manner")
    + item("d.", "Understanding that there is more than one way to get to a desired result")
    + item("e.", "Communication must travel upward and downward")
)
BLOCKS.append(("epo3_comm", epo3_comm))

sinek = (
    note("NOTE", ["Show Slide “According to Simon Sinek”"])
    + p("According to Simon Sinek, Leaders have always been told to learn to listen, He states that Good Leaders need to learn to listen and then speak last. He further states “The skill that it takes to hold your opinion and comments until everyone has spoken, allows you to do two things, 1 It gives everyone the opportunity and feeling that they have been heard and that everyone has contributed, 2 it gives you the opportunity to hear everyone else’s input and feelings before you render your opinion”")
)
BLOCKS.append(("sinek", sinek))

# ---- EPO 4: Ethics ----
epo4 = (
    epo("EPO 4:", "List four (4) Ethics qualities found in a professional work environment.")
    + note("NOTE", ["Show Slide “Ethics”"])
    + item("1.", "Loyalty — Support and defend the group/organization")
    + item("2.", "Duty — Accomplish all assigned tasks to the best of your ability")
    + item("a.", "Self-Reflection — This is the process of understanding your own strengths, and weaknesses, and grow the understanding of who you are. Being realistic about your values, and what makes you act the way you do. It is a constant evaluation of who you are, and what you want to become.", 1)
    + item("3.", "Selfless Service — Put self-interest, personal advantage and self-gain aside and do what is best for the group/organization")
    + item("4.", "Integrity — Be honest, upright, avoid deception and live with respectful values")
    + item("a.", "Ownership — Taking ownership includes solving problems, being decisive, not placing blame, and taking responsibility for actions. Morale of subordinates can be damaged if a leader is not accountable for their own actions. Also holding subordinates accountable is very important, because it teaches them to have ownership over their performance.", 1)
)
BLOCKS.append(("epo4", epo4))

expectations = (
    note("NOTE", ["Show Slide “Expectations” — Jocko Willink Quote"])
    + item("b.", "Expectations — “When setting expectations, no matter what has been said or written, if substandard performance is accepted and no one is held accountable, if there are no consequences, then poor or substandard performance becomes the new standard. Therefore, leaders must enforce standards.” – Jocko Willink.", 1)
    + note("NOTE", ["Show Slide “Questions”"])
    + p("How does a leader maintain these qualities and how does this relate to what we do in training and our job performance every day?")
)
BLOCKS.append(("expectations", expectations))

# ---- EPO 5: Motivational Leadership ----
epo5_a = (
    epo("EPO 5:", "Describe what motivational leadership is.")
    + note("NOTE", ["Show Slide “What is Motivational Leadership?” — Solicit feedback"])
    + note("NOTE", ["Show Slide “Motivational Leadership”"])
    + item("a.", "Motivation good or bad should be displayed; disciplined when they fail to meet a required task but also be prepared to compliment when they meet or exceed a task.")
    + item("b.", "What is the difference between Motivation and Inspiration?")
    + item("–", "Motivation is an external influence or driving force", 1)
    + item("–", "Inspiration is an internal influence or pulling force.", 1)
    + item("c.", "As a leader we need to try and inspire those around us. If we stay motivated and positive, we should hope those around us will also choose to be motivated and in turn be motivated in a positive direction. It’s a little thing, but if we try to inspire people it will feel more natural and if you try to “motivate” people it can seem fake.")
)
BLOCKS.append(("epo5_a", epo5_a))

video5 = note("VIDEO 5 — UNDERSTANDING MOTIVATION AND INSPIRATION", ["3:16 — https://www.youtube.com/watch?v=kr725Lm7bfM"])
BLOCKS.append(("video5", video5))

epo5_b = (
    note("NOTE", ["Show Slide “Motivation Leadership Continued”"])
    + item("f.", "Make sound and timely decisions. A good leader makes a decision, right wrong or indifferent make a decision, indecision or no decision is wrong every time and can result in an adverse action. If the decision was the wrong one, explain the rationale behind it or what led you to the decision and learn from it. OODA LOOP — Explain the process to Observe, Orient, Decide, and Act. A simple process to handle any situation.")
    + item("g.", "Know the strengths and weaknesses of subordinates, and look out for their wellbeing.")
    + quote("If your actions inspire others to dream more, learn more, do more and become more then you are a leader.", "John Quincy Adams")
)
BLOCKS.append(("epo5_b", epo5_b))

# ---- EPO 6: Supervision ----
epo6_a = (
    epo("EPO 6:", "Understand the basics of supervision and evaluating work performance.")
    + '<p class="body-p"><strong>Considerations</strong></p>'
    + note("NOTE", ["Show Slide “Basics of Supervision and Evaluation”"])
    + item("a.", "Don’t over supervise — These are referred to as Micro Managers. Micro Managers stifle initiative, breed resentment and lower morale for everyone. It’s like the common cold, and highly contagious.")
    + item("b.", "Issue tasks, and let your subordinate work the task. Let the task mature, and offer feedback on current progress. Don’t get stuck telling your subordinate exactly how to accomplish a task.")
)
BLOCKS.append(("epo6_a", epo6_a))
epo6_b = (
    item("c.", "Don’t under supervise — This can lead to miscommunications, lack of confidence in the chain of command, and the perception that you as the leader do not care about the team and/or the mission")
    + item("d.", "Don’t be afraid to delegate leadership, responsibility, and authority. This will make sure subordinates understand what goes into making decisions and have a better understanding of the end task. This also helps start building a better leader by challenging them to be successful.")
    + item("e.", "Ensure that all tasks are understood, supervised, and accomplished. This can be done through clear and concise instructions. These instructions should be supervised, and then feedback provided to the subordinate about performance")
    + item("f.", "Practice what you preach. Subordinates should want to learn from a good leader, the same is true that a bad leader can instill bad habits in good people. Perform as if everyone knows each choice you make, and will be critical of all of your decisions.")
    + note("VIDEO 6 — “5 SIGNS YOU ARE A MICRO MANAGER”", ["5:30 — https://www.youtube.com/watch?v=mehkUPN8u6E — Hans Fenzel"])
)
BLOCKS.append(("epo6_b", epo6_b))

# ---- III. REVIEW ----
review_a = (
    roman("III.", "Review")
    + subhead("Conclusion")
    + note("NOTE", ["Show Slide “Conclusion”"])
    + p("Today, we have discussed both effective and in-effective leadership styles. We have discussed traits that you can adopt to make you a better leader in the work place.")
    + '<ul class="ar-list">'
    + "".join(f'<li>{t}</li>' for t in [
        "Define Leadership", "List examples of Effective Leadership", "4 Components of Effective Leadership",
        "4 Ethics Qualities", "What is Motivational Leadership", "Basics of Supervising and Evaluating Work Performance",
    ]) + '</ul>'
)
BLOCKS.append(("review_a", review_a))
review_b = (
    note("NOTE", ["Show Slide “Questions”"])
    + p("At this time, are there any questions on what we have discussed today?")
)
BLOCKS.append(("review_b", review_b))

# ---- IV. FOLLOW ON ASSIGNMENT ----
followon = (
    roman("IV.", "Follow On Assignment")
    + note("NOTE", ["Show Slide “Follow on Reading Suggestions”"])
    + p("There are several good books that are recommended for follow on information:")
    + '<ul class="ar-list">'
    + "".join(f'<li>{t}</li>' for t in [
        "Leadership and Training for the Fight – Paul Howe",
        "Extreme Ownership – Jocko Willink",
        "Can’t Hurt Me: Master Your Mind and Defy the Odds – David Goggins",
    ]) + '</ul>'
    + note("NOTE", ["Show Slide “Credits”"])
    + note("NOTE", ["Show Slide “Eric DeLaune Contact Information”"])
)
BLOCKS.append(("followon", followon))

# ---- V. STUDENT SIGN-IN SHEET ----
signin = (
    roman("V.", "Student Sign-In Sheet")
    + p("All students must complete the student sign-in sheet for EVERY period of instruction.")
)
BLOCKS.append(("signin", signin))

# ---- measure each block's natural height, then greedily pack onto pages ----
MEASURE_CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; }}
.probe {{ width:700px; font-family:'Inter',sans-serif; color:{CHARCOAL}; position:absolute; left:0; top:0; }}
.ref-block {{ border:1px solid {LINE_GRAY}; padding:10px 14px; margin-bottom:14px; }}
.ref-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.4px; color:{RED}; text-transform:uppercase; margin-bottom:6px; }}
.ref-link {{ font-size:9.5px; line-height:1.5; color:{STEEL}; word-break:break-all; margin-bottom:3px; }}
.roman-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:15px;
  letter-spacing:1.6px; text-transform:uppercase; padding:9px 14px; margin:16px 0 12px; }}
.roman-num {{ color:{RED}; margin-right:10px; }}
.epo-heading {{ font-family:'Oswald'; font-weight:700; font-size:14px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:16px 0 8px; padding-bottom:5px; border-bottom:1.5px solid {RED}; }}
.epo-label {{ color:{RED}; margin-right:8px; }}
.h2-sub {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:0.7px; color:{BLACK}; text-transform:uppercase; margin:12px 0 6px; }}
.body-p {{ font-size:10.7px; line-height:1.5; margin-bottom:7px; color:{CHARCOAL}; }}
.body-p strong {{ color:{BLACK}; }}
.lead-in {{ font-weight:700; color:{BLACK}; }}
.note-box {{ border-left:2px solid {RED}; background:#EFEFEC; padding:7px 11px; margin:9px 0; }}
.note-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:8.5px; letter-spacing:1.1px; color:{RED}; text-transform:uppercase; margin-bottom:3px; }}
.note-line {{ font-size:10px; line-height:1.4; color:{CHARCOAL}; }}
.quote {{ border-left:2px solid {RED}; padding:6px 0 6px 15px; margin:9px 0; font-family:'Inter'; font-style:italic;
  font-size:10.5px; line-height:1.48; color:{STEEL}; }}
.q-lead {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.q-mark {{ color:{RED}; font-style:normal; }}
.q-attr {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.outline-item {{ font-size:10.7px; line-height:1.48; margin-bottom:5px; color:{CHARCOAL}; }}
.outline-item.lvl-1 {{ margin-left:22px; }}
.item-label {{ color:{RED}; font-weight:700; margin-right:6px; }}
.stat-list {{ list-style:none; margin:7px 0; }}
.stat-list li {{ position:relative; padding-left:14px; font-size:10.7px; line-height:1.46; margin-bottom:4px; color:{CHARCOAL}; }}
.stat-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}
.ar-list {{ list-style:none; margin:6px 0; }}
.ar-list li {{ position:relative; padding-left:14px; font-size:10.7px; line-height:1.5; margin-bottom:4px; color:{CHARCOAL}; }}
.ar-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}
'''
MEASURE_HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>{MEASURE_CSS}</style></head>
<body>{"".join(f'<div class="probe" id="probe-{i}">{html_}</div>' for i, (name, html_) in enumerate(BLOCKS))}</body></html>'''
measure_path = os.path.join(HERE, "_measure.html")
with open(measure_path, "w") as f:
    f.write(MEASURE_HTML)

from playwright.sync_api import sync_playwright
heights = {}
with sync_playwright() as p_:
    browser = p_.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    page = browser.new_page(viewport={"width": 900, "height": 400})
    page.goto("file://" + measure_path)
    page.wait_for_timeout(200)
    for i, (name, _) in enumerate(BLOCKS):
        h = page.evaluate(f'document.getElementById("probe-{i}").getBoundingClientRect().height')
        heights[name] = h
    browser.close()
os.remove(measure_path)

PAGE_BUDGET = 862
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
  padding:50px 56px 60px; font-family:'Inter',sans-serif; color:{CHARCOAL}; break-after:page; margin:0 auto;
  counter-increment:pagenum; }}
.sheet + .sheet {{ margin-top:2px; }}
.sheet .pagenum::before {{ content:" \\2013  Page " counter(pagenum) " of {len(PAGES)}"; }}

.doc-header {{ display:flex; align-items:center; justify-content:space-between; padding-bottom:11px;
  border-bottom:2px solid {RED}; margin-bottom:16px; }}
.doc-header img {{ height:28px; width:auto; display:block; }}
.doc-header .doc-tag {{ font-family:'Inter'; font-weight:700; font-size:8.5px; letter-spacing:1px; color:{STEEL}; text-transform:uppercase; }}
.doc-footer {{ position:absolute; left:0; right:0; bottom:24px; text-align:center; font-family:'Inter';
  font-weight:600; font-size:8px; letter-spacing:0.5px; color:{STEEL}; }}

.ref-block {{ border:1px solid {LINE_GRAY}; padding:10px 14px; margin-bottom:14px; }}
.ref-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.4px; color:{RED}; text-transform:uppercase; margin-bottom:6px; }}
.ref-link {{ font-size:9.5px; line-height:1.5; color:{STEEL}; word-break:break-all; margin-bottom:3px; }}

.roman-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:15px;
  letter-spacing:1.6px; text-transform:uppercase; padding:9px 14px; margin:16px 0 12px; }}
.roman-num {{ color:{RED}; margin-right:10px; }}

.epo-heading {{ font-family:'Oswald'; font-weight:700; font-size:14px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:16px 0 8px; padding-bottom:5px; border-bottom:1.5px solid {RED}; }}
.epo-label {{ color:{RED}; margin-right:8px; }}

.h2-sub {{ font-family:'Inter'; font-weight:700; font-size:11.5px; letter-spacing:0.7px; color:{BLACK}; text-transform:uppercase; margin:12px 0 6px; }}
.body-p {{ font-size:10.7px; line-height:1.5; margin-bottom:7px; color:{CHARCOAL}; }}
.body-p strong {{ color:{BLACK}; }}
.lead-in {{ font-weight:700; color:{BLACK}; }}

.note-box {{ border-left:2px solid {RED}; background:#EFEFEC; padding:7px 11px; margin:9px 0; }}
.note-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:8.5px; letter-spacing:1.1px; color:{RED}; text-transform:uppercase; margin-bottom:3px; }}
.note-line {{ font-size:10px; line-height:1.4; color:{CHARCOAL}; }}

.quote {{ border-left:2px solid {RED}; padding:6px 0 6px 15px; margin:9px 0; font-family:'Inter'; font-style:italic;
  font-size:10.5px; line-height:1.48; color:{STEEL}; }}
.q-lead {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.q-mark {{ color:{RED}; font-style:normal; }}
.q-attr {{ font-weight:700; font-style:normal; color:{BLACK}; }}

.outline-item {{ font-size:10.7px; line-height:1.48; margin-bottom:5px; color:{CHARCOAL}; }}
.outline-item.lvl-1 {{ margin-left:22px; }}
.item-label {{ color:{RED}; font-weight:700; margin-right:6px; }}

.stat-list {{ list-style:none; margin:7px 0; }}
.stat-list li {{ position:relative; padding-left:14px; font-size:10.7px; line-height:1.46; margin-bottom:4px; color:{CHARCOAL}; }}
.stat-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}

.ar-list {{ list-style:none; margin:6px 0; }}
.ar-list li {{ position:relative; padding-left:14px; font-size:10.7px; line-height:1.5; margin-bottom:4px; color:{CHARCOAL}; }}
.ar-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}

.cover {{ background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:0 90px; }}
.cover-tick {{ position:absolute; width:26px; height:26px; border-color:{RED}; border-style:solid; }}
.cover-tick.tl {{ left:40px; top:40px; border-width:3px 0 0 3px; }}
.cover-tick.br {{ right:40px; bottom:40px; border-width:0 3px 3px 0; }}
.cover-logo {{ height:64px; width:auto; margin-bottom:44px; }}
.cover-eyebrow {{ font-family:'Inter'; font-weight:700; font-size:13px; letter-spacing:3px; color:{RED}; text-transform:uppercase; margin-bottom:14px; }}
.cover-title {{ font-family:'Oswald'; font-weight:700; font-size:38px; line-height:1.2; letter-spacing:0.3px;
  text-transform:uppercase; color:{WHITE}; }}
.cover-meta {{ margin-top:36px; font-family:'Inter'; font-weight:700; font-size:13px; letter-spacing:1px; color:#B9BBBE; text-transform:uppercase; }}
'''

html = f'''<!doctype html>
<html><head><meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{"".join(PAGES)}
</body></html>'''

with open(os.path.join(HERE, "valletta_supporting_information.html"), "w") as f:
    f.write(html)

print("written", len(PAGES), "pages")
