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

def header():
    return f'''<div class="doc-header">
      <img src="data:image/png;base64,{LOGO_BLACK}" alt="Valletta Industries"/>
      <div class="doc-tag">Leadership Training Outline</div>
    </div>'''

def footer():
    return '<div class="doc-footer">Valletta Industries &nbsp;|&nbsp; Leadership Training Outline<span class="pagenum"></span></div>'

def sheet(inner, klass=""):
    return f'<section class="sheet {klass}">{inner}</section>'

def title(text):
    return f'<div class="h1-title">{text}</div>'

def subhead(text):
    return f'<div class="h2-sub">{text}</div>'

def sec(letter, text):
    return f'<div class="sec-heading"><span class="sec-label">{letter}.</span>{text}</div>'

def p(text):
    return f'<p class="body-p">{text}</p>'

def leadin(label, text):
    return f'<p class="body-p"><span class="lead-in">{label}</span> {text}</p>'

def note(tag, lines):
    body = "".join(f'<div class="note-line">{l}</div>' for l in lines)
    return f'<div class="note-box"><span class="note-tag">{tag}</span>{body}</div>'

def bio(text):
    return f'<p class="bio-aside">{text}</p>'

def quote(text, attribution=None, lead=None):
    lead_html = f'<span class="q-lead">{lead}</span> ' if lead else ""
    attr_html = f' &ndash; <span class="q-attr">{attribution}</span>' if attribution else ""
    return f'<div class="quote">{lead_html}<span class="q-mark">&ldquo;</span>{text}<span class="q-mark">&rdquo;</span>{attr_html}</div>'

def stat(text):
    return f'<li>{text}</li>'

def meta_row(label, value):
    return f'<div class="meta-row"><span class="meta-label">{label}</span><span class="meta-value">{value}</span></div>'

def item(label, text, level=0):
    return f'<div class="outline-item lvl-{level}"><span class="item-label">{label}</span>{text}</div>'

# ================= CONTENT BLOCKS =================
BLOCKS = []

COVER_HTML = sheet(f'''
  <div class="cover-tick tl"></div><div class="cover-tick br"></div>
  <img class="cover-logo" src="data:image/png;base64,{LOGO_WHITE}" alt="Valletta Industries"/>
  <div class="cover-eyebrow">Leadership Training</div>
  <div class="cover-title">Leadership Training<br/>Outline</div>
  <div class="cover-meta">Time: 4 Hours</div>
''', "cover")

# ---- Course metadata ----
meta_html = (
    '<div class="meta-box">'
    + meta_row("Time", "4 hours")
    + meta_row("Method of Instruction", "Classroom lecture, PowerPoint presentation, classroom discussion, and observation/review during practical exercises.")
    + meta_row("Description", "In this period of instruction, we will discuss the importance of leadership principles and the components it takes to be an effective leader.")
    + meta_row("Special Requirements", "Classroom, laptop computer, presentation pointer, projector, and PowerPoint presentation. (Can be conducted by lecture only from the outline)")
    + meta_row("Instructional Aides", "PowerPoint presentation, student outlines, handouts")
    + '</div>'
)
BLOCKS.append(("meta", meta_html))

# ---- Presentation / Introduction / Objective ----
presentation = (
    title("Presentation")
    + leadin("INTRODUCTION:", "Good morning/afternoon/evening, my name is __________. Your next period of instruction will be on becoming an effective leader. (Instructor Experience)")
    + leadin("OBJECTIVE:", "The objective of this course is to learn the fundamentals of being a leader. As a supervisor, manager, or task leader you will be around people from different backgrounds and with different past experiences, and each may require a different style of leadership. It is your responsibility to effectively lead and complete assigned tasks while dealing with different personalities. Your people (subordinates) will determine if you are an effective or ineffective leader, and this can be measured by performance of assigned tasks. Effective leadership begins with having the proper mindset and attitude.")
)
BLOCKS.append(("presentation", presentation))

video1 = note("VIDEO 1 — SGT. TRAVIS MILLS", ["https://www.youtube.com/watch?v=eSytAgtLqVw"]) + bio(
    "(Retired United States Army Staff Sergeant Travis Mills of the 82nd Airborne is a recalibrated warrior, "
    "motivational speaker, actor, author and an advocate for veterans and amputees. Travis’s New York Times "
    "bestselling memoir, Tough as They Come, is currently available on sale in bookstores everywhere. Despite "
    "losing portions of both arms and legs from an IED while on active duty in Afghanistan, Travis continues to "
    "overcome life’s challenges, breaking physical barriers and defying odds. Travis lives by his motto: "
    "“Never give up. Never quit.”)"
)
BLOCKS.append(("video1", video1))

goggins = (
    quote("The only thing more contagious than a good attitude is a bad one.", "David Goggins.", lead="Positive Attitude:")
    + bio(
        "(David Goggins is the Author of Can’t Hurt Me: Master Your Mind and Defy the Odds chronicles David "
        "Goggins’ incredible life from perpetual victim to active duty Navy SEAL to world class ultra-athlete "
        "and world record holder. Graduate of SEAL training, Ranger school, and Air Force Tactical Air Control)"
    )
)
BLOCKS.append(("goggins", goggins))

# ---- Statistics ----
stats = (
    title("Statistics")
    + p("For 30 years, MDA has helped many large corporations improve their financial and operating performance.")
    + bio('According to MDA Training “5 Workplace Leadership Statistics, You Shouldn’t Ignore.” MDA '
          'Training, 12 Feb. 2020, mdatraining.com/blog/workplace-leadership-statistics/.')
    + '<ul class="stat-list">'
    + stat("Employees supervised by highly engaged LEADERSHIP teams are 39% more likely to be engaged themselves.")
    + stat("32% of employees lack the confidence to put new ideas to employers")
    + stat("58% of Managers report that they never received any management training")
    + stat("82% of employees don’t trust their boss, to tell the truth,")
    + stat("79% of employees cite the “lack of appreciation” as a reason for quitting their job.")
    + '</ul>'
    + p("It is paramount that leaders in the workplace are consistently rewarding hard work and success. Without "
        "this, employees who excel within their roles will feel undervalued and ultimately unhappy at the "
        "business, despite their strong performance.")
    + p("So with these statistics in mind, what is a common denominator that can affect these results? What can we "
        "do as leaders to improve these numbers?")
    + quote(
        "The single biggest way to impact an organization is to focus on leadership development. There is almost "
        "no limit to the potential of an organization that recruits good people, raises them as leaders, and "
        "continually develops them.", "John Maxwell.")
    + bio(
        "(John Maxwell has written more than 100 books that have been translated into fifty languages. He has "
        "authored several New York Times bestselling books about leadership and was named #1 leadership expert in "
        "the world by Inc. Magazine in 2014)")
)
BLOCKS.append(("stats", stats))

# ---- Overview ----
overview = (
    '<div class="overview-band">Overview</div><ul class="overview-list">'
    + "".join(f'<li><span class="ov-letter">{l}.</span>{t}</li>' for l, t in [
        ("A", "Define Leadership"), ("B", "Examples of Effective Leadership"),
        ("C", "Describe components of being an effective leader."), ("D", "Ethical Characteristics for Leadership"),
        ("E", "Describe what motivational leadership is"), ("F", "Understand the basics of supervision and evaluating work performance."),
    ]) + '</ul>'
)
BLOCKS.append(("overview", overview))

# ---- A. Defining leadership ----
sec_a = (
    sec("A", "Defining Leadership")
    + note("VIDEO 2", ["We were soldiers, play the first 16 seconds about a leader going first", "https://www.youtube.com/watch?v=abFAhCtUyMM"])
    + item("a.", "Definition — The ability to influence others to accomplish a task by providing a purpose, a direction, and appropriate motivation. Explaining the mission to subordinates helps them focus on the importance of the objective and allows them to perform in a more efficient and disciplined manner.")
    + item("b.", "Although having a supervisory position provides the opportunity to be a leader; a position does not make you a leader. Being a leader is a choice that has nothing to do with your status on the organizational chart; once you decide to lead others, it will become easier to see where you can impact the mission the most.")
    + item("c.", "We have all heard the phrase “Leaders Lead,” but not all leaders are influential. Leaders must set an example for all to follow. Good leaders set the standard and can meet it/surpass it. Leading by example instills confidence and respect from subordinates and makes the leader more effective.")
    + item("d.", "Strive to be the best at your assignments and learn the positions above and below you. Understanding the tasks assigned to personnel on your team will build confidence in your leadership.")
    + item("e.", "A leader looks for ways to better those around them and the mission. A leader looks for more responsibility and accepts the outcome no matter the success of your actions.")
    + item("f.", "Make sound and timely decisions. A good leader makes a decision based on the immediately available information. As a leader being indecisive can result in problems getting worse rather than better. An immediate decision is still moving the team closer to completing the mission. If a decision does not get the desired result, discuss with subordinates and other leaders to learn from it.")
)
BLOCKS.append(("sec_a", sec_a))

# ---- B. Examples of effective leadership ----
sec_b_1 = (
    sec("B", "Examples of Effective Leadership")
    + p("Charismatic Leader — Charismatic leadership combines charm, interpersonal connection, and persuasive communication to motivate others. Some examples are Sir Winston Churchill, Malcolm X, and Nelson Mandela.")
    + p("Transformational Leader — Transformational leadership is when a leader’s behaviors influence followers and inspire them to perform beyond their perceived capabilities. Transformational leadership inspires people to achieve unexpected or remarkable results. Examples are Dr. Martin Luther King, Henry Ford, and Steve Jobs")
    + p("Servant Leader — Servant leadership occurs when the leader’s main goal and responsibility is to provide service to their people. Examples are Mahatma Gandhi and Mother Teresa.")
    + p("Quiet Leaders — Quiet leaders recognize they cannot ask someone to do a task they wouldn’t or haven’t done. They set the example for others to follow. Silent leaders hold themselves to the same (or higher) standard than they hold for others. Trust. Silent leaders do not micromanage or nag others. Examples are Albert Einstein, Sir Isaac Newton, Rosa Parks, Bill Gates, and Warren Buffett.")
)
BLOCKS.append(("sec_b_1", sec_b_1))
sec_b_2 = (
    note("VIDEO 3", ["We Were Soldier’s Leadership clip, different types of leaders.", "https://www.youtube.com/watch?v=0fpK9591u6M"])
    + note("DISCUSSION", ["Discussion on types of leadership in video and perceived traits. How does this impact a team, what does it make you feel?"])
)
BLOCKS.append(("sec_b_2", sec_b_2))

# ---- C. Describe the components of effective leadership ----
sec_c_traits = (
    sec("C", "Describe the Components of Effective Leadership")
    + subhead("Leadership Traits")
    + p("A good leader encourages their staff to participate in all assigned tasks with clear instructions and supervision.")
    + p("A good leader educates themselves to understand assigned tasks and mentor those below them. Learning the functions of their supervisors provide context for the direction of the mission and makes the leader a more valuable member of the team.")
    + p("A good leader knows their capabilities and has an honest opinion of their strengths and weaknesses. This information is discovered through honest evaluation by supervisors and subordinates during regular performance discussions.")
    + p("A good leader treats all team members with dignity and respect. Respect in its basic form shows that you are aware of someone’s rights, values, wishes, and other personal beliefs. To be aware of this information, a leader must regularly communicate to understand each team member’s individual needs. A leader always must respect subordinates to earn their respect.")
    + p("A leader must possess professional character traits such as ambition, creativity, compassion, courage, flexibility, honesty (integrity), humility, loyalty, patience, discipline, and curiosity.")
    + p("A leader understands how to manage stress and is capable of sharing those skills. Exercise, meditation, breathing exercises, and reading are all examples of stress-relieving activities. Also, honest discussions about specific topics can help relieve stress by providing clarity about the stressful issue.")
)
BLOCKS.append(("sec_c_traits", sec_c_traits))

sec_c_comm = (
    subhead("Communication")
    + p("Influential leaders must adapt their communication style to effectively communicate to their team.")
    + p("Each employee will have different motivations, so understanding how to communicate with each team member is essential.")
    + p("Effective leaders must be able to talk but also listen. It is essential to listen to your team and genuinely accept their input even if their suggestions are not part of the leader’s final instructions.")
    + p("An effective leader must be transparent about the team’s direction to continue building trust with subordinates. Honestly assessing performance and acknowledging if the leader has made a mistake will encourage employees that they are safe to share information with the leader.")
    + p("Effective leaders use communication tools to understand subordinate’s suggestions better. By asking open-ended questions like “tell me more” or “explain what you mean,” a leader can get more details and ensure they understand the information thoroughly.")
    + p("Communication is not only verbal but how you carry yourself. Practicing simple body language cues will help establish interest and rapport. Making eye contact is a simple way to start changing body language cues.")
    + p("A good leader will ask for feedback on their performance to subordinates, and understanding what subordinates need from the leader. The most important part of this is to implement change based on their input. The effort to implement change will continue to strengthen the trust of subordinates.")
)
BLOCKS.append(("sec_c_comm", sec_c_comm))

sec_c_followers = (
    subhead("Observing Effective Follower Traits (Knowing your People)")
    + quote(
        "Why would you want to be someone called a follower? A simple answer is people follow because they derive "
        "benefits. The psychological payback of following exceeds the psychological cost of following. Throughout "
        "our human history, most humans were in small, nomadic clusters. These tribes offered protection, food, "
        "and survival. The groups with the best leader and followers had a higher probability of survival than "
        "those poorly led that consisted of poor followers. The physical benefits for followers outweighed the "
        "psychological costs and so most likely they stayed connected to the tribe. If some followers were "
        "dissatisfied with the leader’s goals and agenda, they had a choice of either fighting for the top "
        "position, or leaving to join other groups.",
        "(Project Management Institute 2021)", lead="The Psychology of Followers")
    + p("Followers are an essential part of leadership, and being a follower is a straightforward concept. Following is the ability to take direction well, believe in a program, be part of a team, and deliver on your expectations. A follower can provide strength to the leader by contributing to the organization in areas that complement the leader’s position.")
    + p("A follower has good judgment and will take direction but not follow blindly. Good judgment is required and can be learned from good leadership.")
    + p("Good followers are good workers, and they need good direction to understand what is expected of them.")
    + p("Followers can be categorized into multiple groups, such as followers with positive attitudes who will be motivated on their own. Others will have minimal levels of independent thinking and need constant direction. Also, negative followers will be more capable of thinking independently but do not contribute positively to the team. We can break these groups down further, but for this course, it is only essential to understand that each follower will be different in the leadership style that will inspire them the most.")
    + p("To be effective, followers must be willing to share their ideas and opinions with leaders.")
)
BLOCKS.append(("sec_c_followers", sec_c_followers))

sec_c_mission = (
    subhead("Understanding the Mission or Task")
    + p("As a leader, you must have a purpose, and your drive will come from your mission.")
    + p("The mission will help the team share priorities, set performance goals, plan performance rewards, and give a shared vision for the team.")
    + p("The mission or task also gives an effective leader “vision.” Vision is the opportunity to see a path to success or failure and the future development of your team.")
    + p("An effective leader can create small tasks to create growth on their team. A leader can plan short team-building exercises or task-specific training to focus the team on an assigned task. Often an effective will be managing multiple tasks for each member on their team based on the team member’s ability.")
)
BLOCKS.append(("sec_c_mission", sec_c_mission))

sec_c_video4 = (
    note("VIDEO 4", ["The first 3:27 of — https://www.youtube.com/watch?v=jYK-drFNI6o", "Jocko Willink/Mulligan Brothers interview that describes timing and response"])
    + note("DISCUSSION", ["Focusing on the appropriate time to execute decisions. Picking the right time to action change."])
)
BLOCKS.append(("sec_c_video4", sec_c_video4))

sec_c_jocko_bio = (
    bio(
        "(Jocko Willink is a retired U.S. Navy SEAL officer, co-author of the #1 New York Times bestseller Extreme "
        "Ownership: How U.S. Navy SEALs Lead and Win, Dichotomy of Leadership, host of the top-rated Jocko "
        "Podcast, and co-founder of Echelon Front, where he serves as Chief Executive Officer, leadership "
        "instructor, speaker and strategic advisor. Jocko spent 20 years in the SEAL Teams, starting as an "
        "enlisted SEAL and rising through the ranks to become a SEAL officer. As commander of SEAL Team "
        "Three’s Task Unit Bruiser during the battle of Ramadi, he orchestrated SEAL operations that helped "
        "the “Ready First” Brigade of the U.S. Army’s First Armored Division bring stability to the "
        "violent, war-torn city. Task Unit Bruiser became the most highly decorated Special Operations Unit of the "
        "Iraq War.")
    + bio(
        "Jocko returned from Iraq to serve as Officer-in-Charge of training for all West Coast SEAL Teams. There, "
        "he spearheaded the development of leadership training and personally instructed and mentored the next "
        "generation of SEAL leaders who have continued to perform with great success on the battlefield. Jocko is "
        "the recipient of the Silver Star, the Bronze Star, and numerous other personal and unit awards.")
    + bio(
        "Upon retiring from the Navy, Jocko co-founded Echelon Front, a premier leadership consulting company, "
        "where he teaches the leadership principles he learned on the battlefield to help others lead and win. "
        "Jocko also authored the Discipline Equals Freedom Field Manual, a New York Times Bestseller, and the "
        "bestselling Way of the Warrior Kid children’s book series.)")
    + p("According to Simon Sinek, Leaders have always been told to learn to listen, He states that Good Leaders "
        "need to learn to listen and then speak last. He further states, “The skill that it takes to hold "
        "your opinion and comments until everyone has spoken, allows you to do two things, 1 It gives everyone the "
        "opportunity and feeling that they have been heard and that everyone has contributed, 2 it gives you the "
        "opportunity to hear everyone else’s input and feelings before you render your opinion.”")
)
BLOCKS.append(("sec_c_jocko_bio", sec_c_jocko_bio))

# ---- D. Ethical characteristics for leadership ----
sec_d = (
    sec("D", "Ethical Characteristics for Leadership")
    + p("<strong>Fair</strong> — An ethical leader is fair, and they treat everyone on their team equally with no bias. Team members will not perform to their best ability if they feel like decisions are unfair and made with any bias.")
    + p("<strong>Honest</strong> — Ethical leaders are honest and must always be transparent and fair. A good leader should give the unpopular truth to their team rather than a lie. Consistent honesty builds trust with your team and promotes the open sharing of information.")
    + p("<strong>Respect</strong> — Leaders who actively listen to subordinates and do not dismiss their concerns will have a team focused on achieving the same objective. Although you may be higher in a chain of command, your team should feel as though they are equally important to the mission.")
    + p("<strong>Value-Oriented</strong> — While each person has individual values, a good leader will make decisions based on the organization’s values. An ethical leader will share the organization’s values with the team and implement changes that adhere to those values.")
    + p("<strong>Leads by Example</strong> — Employees will mimic the action of their leader. A leader cannot expect his team to make ethical decisions if they are unwilling to make ethical choices. An ethical leader takes ownership of their actions without placing blame on anyone else.")
    + p("<strong>Makes the team a priority</strong> — Ethical leaders will promote team building and foster a sense of community. Ethical leaders will help each team member to achieve personal and professional goals through regular communication.")
    + quote(
        "When setting expectations, no matter what has been said or written, if substandard performance is "
        "accepted and no one is held accountable if there are no consequences, then poor or substandard "
        "performance becomes the new standard. Therefore, leaders must enforce standards.",
        "Jocko Willink.", lead="Expectations")
)
BLOCKS.append(("sec_d", sec_d))

# ---- E. Describe what motivational leadership is ----
sec_e = (
    sec("E", "Describe What Motivational Leadership Is")
    + quote(
        "A leader must lead, but also be ready to follow. They must be aggressive, but not overbearing. A leader "
        "must be calm, but not robotic. They must be confident, but never cocky. A leader must be brave, but not "
        "foolhardy. They must have a competitive spirit, but be a gracious loser.", "Jocko Willink")
    + p("A motivational leader can make decisions and set clear goals for their teams. Motivational leaders see "
        "the best in their team and inspire them to accomplish a goal. Sometimes these goals are shared by the "
        "team or individual goals to better a team member.")
    + p("What is the difference between Motivation and Inspiration?")
    + p("Inspiration is an external influence or pulling force that compels you to achieve something.")
    + p("Motivation is an internal influence or a driving force that you feel on the inside to achieve something.")
    + p("A good leader should try to inspire those around them. If the leader has a positive attitude and tries to "
        "help others succeed, it will encourage their team members to share those behaviors. An effective leader "
        "aims to inspire their team with knowledge, experience, and clear direction. Sometimes trying to "
        "“motivate” subordinates can feel fake. They may feel the leader isn’t experiencing the "
        "same doubts as them. When the leader focuses on inspiration as the goal, the subordinate will likely feel "
        "more connected to the leader. This thought process will continue to strengthen trust between the team.")
    + p("An effective leader will make logical decisions based on the immediate information available. If the "
        "decision was wrong, explain the rationale behind it or what led you to the conclusion and learn from it.")
    + note("OODA LOOP", ["Observe, Orient, Decide, and Act. A simple process to handle any situation."])
    + p("Know the strengths and weaknesses of subordinates and look out for their wellbeing.")
    + quote("If your actions inspire others to dream more, learn more, do more and become more, then you are a "
            "leader.", "John Quincy Adams.")
)
BLOCKS.append(("sec_e", sec_e))

# ---- F. Understand the basics of supervision ----
sec_f = (
    sec("F", "Understand the Basics of Supervision and Evaluating Work Performance")
    + p("An effective leader does not Micro-Manage. Micromanagers stifle initiative, breed resentment, and lower "
        "morale for everyone. When a leader micromanages subordinates its takes away their ambition and desire to "
        "succeed, so there is no natural desire to perform because someone else will tell them when and how to do "
        "everything.")
    + p("An effective leader is proactive and should avoid having a “hands-off” mentality. A "
        "“hands-off” leadership approach can lead to subordinates not having clear direction causing a "
        "lack of confidence in the chain of command. A lack of engagement can also cause team members to perceive "
        "that the leader doesn’t care about the team or the mission.")
    + p("A leader will delegate supervision, responsibility, and authority to capable subordinates. Delegating "
        "responsibility to subordinates will help them to understand the challenges faced by supervisors. Sharing "
        "the supervisor’s role also gives experience to other team members and provides the leader an "
        "opportunity to communicate performance.")
    + p("As a supervisor, you should ensure that all tasks are understood, supervised, and accomplished. This "
        "supervision must include clear instructions so your team can execute their jobs efficiently.")
    + p("A good supervisor can perform the tasks of his subordinates and is capable of improving their "
        "team’s performance through technical proficiency and guidance.")
    + p("A good leader will hold their team accountable with honest feedback on performance from each assigned "
        "task. Giving verbal performance evaluations should be done during the execution of assigned tasks and "
        "also with after-action discussions. Using regular written performance statements will reinforce the "
        "verbal directions during the performance of their assignments. Using a multiple approach system to "
        "performance evaluations will ensure all team members are aware of their performance in each area of "
        "their assigned task.")
)
BLOCKS.append(("sec_f", sec_f))

# ---- Conclusion ----
conclusion = (
    '<div class="conclusion-band">Conclusion</div>'
    + p("Today, we have reviewed ways to be an effective leader and the different factors that affect a team. We "
        "have discussed traits and tactics that you can adopt to build trust and understanding of your "
        "subordinates.")
)
BLOCKS.append(("conclusion", conclusion))

# ---- Additional Reading ----
reading_items = [
    "12 Rules for Life &ndash; Jordan B. Peterson",
    "Leadership and Training for the Fight &ndash; Paul Howe",
    "Extreme Ownership &ndash; Jocko Willink",
    "Can&rsquo;t Hurt Me: Master Your Mind and Defy the Odds &ndash; David Goggins",
    '<a href="https://www.johnmaxwell.com/my-purpose/">https://www.johnmaxwell.com/my-purpose/</a>',
    '<a href="https://echelonfront.com/jocko-willink/">https://echelonfront.com/jocko-willink/</a>',
    '<a href="https://www.travismills.org/">https://www.travismills.org/</a>',
]
reading = (title("Additional Reading")
           + '<p class="body-p">Several good books are recommended for follow on information:</p>'
           + '<ul class="ar-list">' + "".join(f'<li>{t}</li>' for t in reading_items) + '</ul>')
BLOCKS.append(("reading", reading))

# ---- measure each block's natural height, then greedily pack onto pages ----
MEASURE_CSS = f'''
{FONTS_CSS}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{FIELD_WHITE}; }}
.probe {{ width:700px; font-family:'Inter',sans-serif; color:{CHARCOAL}; position:absolute; left:0; top:0; }}
.meta-box {{ border:1px solid {LINE_GRAY}; padding:14px 16px; margin-bottom:10px; }}
.meta-row {{ display:flex; margin-bottom:8px; }}
.meta-row:last-child {{ margin-bottom:0; }}
.meta-label {{ flex:none; width:150px; font-family:'Inter'; font-weight:700; font-size:10.5px; letter-spacing:0.5px; color:{RED}; text-transform:uppercase; }}
.meta-value {{ font-size:11px; line-height:1.5; color:{CHARCOAL}; }}
.h1-title {{ font-family:'Oswald'; font-weight:700; font-size:16.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:18px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {RED}; }}
.h2-sub {{ font-family:'Inter'; font-weight:700; font-size:12.5px; letter-spacing:0.8px; color:{BLACK}; text-transform:uppercase; margin:14px 0 6px; }}
.sec-heading {{ font-family:'Oswald'; font-weight:700; font-size:16.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:18px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {RED}; }}
.sec-label {{ color:{RED}; margin-right:8px; }}
.body-p {{ font-size:11px; line-height:1.52; margin-bottom:8px; color:{CHARCOAL}; }}
.body-p strong {{ color:{BLACK}; }}
.lead-in {{ font-weight:700; color:{BLACK}; }}
.note-box {{ border-left:2px solid {RED}; background:#EFEFEC; padding:8px 12px; margin:10px 0; }}
.note-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:9px; letter-spacing:1.2px; color:{RED}; text-transform:uppercase; margin-bottom:3px; }}
.note-line {{ font-size:10.5px; line-height:1.42; color:{CHARCOAL}; }}
.bio-aside {{ font-size:9.7px; font-style:italic; line-height:1.45; color:{STEEL}; margin-bottom:8px; }}
.quote {{ border-left:2px solid {RED}; padding:6px 0 6px 16px; margin:10px 0; font-family:'Inter'; font-style:italic;
  font-size:11px; line-height:1.5; color:{STEEL}; }}
.q-lead {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.q-mark {{ color:{RED}; font-style:normal; }}
.q-attr {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.overview-band, .conclusion-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:13px;
  letter-spacing:1.6px; text-transform:uppercase; padding:8px 14px; margin-bottom:2px; }}
.overview-list {{ list-style:none; border:1px solid {LINE_GRAY}; border-top:none; padding:12px 16px 14px; margin-bottom:10px; }}
.overview-list li {{ font-size:11px; line-height:1.6; color:{CHARCOAL}; }}
.ov-letter {{ color:{RED}; font-weight:700; margin-right:6px; }}
.outline-item {{ font-size:11px; line-height:1.5; margin-bottom:7px; color:{CHARCOAL}; }}
.outline-item.lvl-1 {{ margin-left:22px; }}
.item-label {{ color:{RED}; font-weight:700; margin-right:6px; }}
.stat-list {{ list-style:none; margin:8px 0; }}
.stat-list li {{ position:relative; padding-left:15px; font-size:11px; line-height:1.5; margin-bottom:5px; color:{CHARCOAL}; }}
.stat-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}
.ar-list {{ list-style:none; }}
.ar-list li {{ position:relative; padding-left:15px; font-size:11px; line-height:1.55; margin-bottom:5px; color:{CHARCOAL}; }}
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
  padding:54px 58px 64px; font-family:'Inter',sans-serif; color:{CHARCOAL}; break-after:page; margin:0 auto;
  counter-increment:pagenum; }}
.sheet + .sheet {{ margin-top:2px; }}
.sheet .pagenum::before {{ content:" \\2013  Page " counter(pagenum) " of {len(PAGES)}"; }}

.doc-header {{ display:flex; align-items:center; justify-content:space-between; padding-bottom:12px;
  border-bottom:2px solid {RED}; margin-bottom:20px; }}
.doc-header img {{ height:30px; width:auto; display:block; }}
.doc-header .doc-tag {{ font-family:'Inter'; font-weight:700; font-size:9.5px; letter-spacing:1.4px; color:{STEEL}; text-transform:uppercase; }}
.doc-footer {{ position:absolute; left:0; right:0; bottom:26px; text-align:center; font-family:'Inter';
  font-weight:600; font-size:9px; letter-spacing:0.6px; color:{STEEL}; }}

.meta-box {{ border:1px solid {LINE_GRAY}; padding:14px 16px; margin-bottom:10px; }}
.meta-row {{ display:flex; margin-bottom:8px; }}
.meta-row:last-child {{ margin-bottom:0; }}
.meta-label {{ flex:none; width:150px; font-family:'Inter'; font-weight:700; font-size:10.5px; letter-spacing:0.5px; color:{RED}; text-transform:uppercase; }}
.meta-value {{ font-size:11px; line-height:1.5; color:{CHARCOAL}; }}

.h1-title {{ font-family:'Oswald'; font-weight:700; font-size:16.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:18px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {RED}; }}
.h2-sub {{ font-family:'Inter'; font-weight:700; font-size:12.5px; letter-spacing:0.8px; color:{BLACK}; text-transform:uppercase; margin:14px 0 6px; }}
.sec-heading {{ font-family:'Oswald'; font-weight:700; font-size:16.5px; letter-spacing:0.3px; text-transform:uppercase;
  color:{BLACK}; margin:18px 0 10px; padding-bottom:6px; border-bottom:1.5px solid {RED}; }}
.sec-label {{ color:{RED}; margin-right:8px; }}
.body-p {{ font-size:11px; line-height:1.52; margin-bottom:8px; color:{CHARCOAL}; }}
.body-p strong {{ color:{BLACK}; }}
.lead-in {{ font-weight:700; color:{BLACK}; }}

.note-box {{ border-left:2px solid {RED}; background:#EFEFEC; padding:8px 12px; margin:10px 0; }}
.note-tag {{ display:block; font-family:'Inter'; font-weight:700; font-size:9px; letter-spacing:1.2px; color:{RED}; text-transform:uppercase; margin-bottom:3px; }}
.note-line {{ font-size:10.5px; line-height:1.42; color:{CHARCOAL}; }}
.bio-aside {{ font-size:9.7px; font-style:italic; line-height:1.45; color:{STEEL}; margin-bottom:8px; }}

.quote {{ border-left:2px solid {RED}; padding:6px 0 6px 16px; margin:10px 0; font-family:'Inter'; font-style:italic;
  font-size:11px; line-height:1.5; color:{STEEL}; }}
.q-lead {{ font-weight:700; font-style:normal; color:{BLACK}; }}
.q-mark {{ color:{RED}; font-style:normal; }}
.q-attr {{ font-weight:700; font-style:normal; color:{BLACK}; }}

.overview-band, .conclusion-band {{ background:{BLACK}; color:{WHITE}; font-family:'Oswald'; font-weight:700; font-size:13px;
  letter-spacing:1.6px; text-transform:uppercase; padding:8px 14px; margin-bottom:2px; }}
.overview-list {{ list-style:none; border:1px solid {LINE_GRAY}; border-top:none; padding:12px 16px 14px; margin-bottom:10px; }}
.overview-list li {{ font-size:11px; line-height:1.6; color:{CHARCOAL}; }}
.ov-letter {{ color:{RED}; font-weight:700; margin-right:6px; }}

.outline-item {{ font-size:11px; line-height:1.5; margin-bottom:7px; color:{CHARCOAL}; }}
.outline-item.lvl-1 {{ margin-left:22px; }}
.item-label {{ color:{RED}; font-weight:700; margin-right:6px; }}

.stat-list {{ list-style:none; margin:8px 0; }}
.stat-list li {{ position:relative; padding-left:15px; font-size:11px; line-height:1.5; margin-bottom:5px; color:{CHARCOAL}; }}
.stat-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}

.ar-list {{ list-style:none; }}
.ar-list li {{ position:relative; padding-left:15px; font-size:11px; line-height:1.55; margin-bottom:5px; color:{CHARCOAL}; }}
.ar-list li::before {{ content:''; position:absolute; left:0; top:5px; width:6px; height:6px; background:{RED}; }}
.ar-list a {{ color:{CHARCOAL}; }}

.cover {{ background:{BLACK}; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:0 90px; }}
.cover-tick {{ position:absolute; width:26px; height:26px; border-color:{RED}; border-style:solid; }}
.cover-tick.tl {{ left:40px; top:40px; border-width:3px 0 0 3px; }}
.cover-tick.br {{ right:40px; bottom:40px; border-width:0 3px 3px 0; }}
.cover-logo {{ height:64px; width:auto; margin-bottom:44px; }}
.cover-eyebrow {{ font-family:'Inter'; font-weight:700; font-size:13px; letter-spacing:3px; color:{RED}; text-transform:uppercase; margin-bottom:14px; }}
.cover-title {{ font-family:'Oswald'; font-weight:700; font-size:40px; line-height:1.18; letter-spacing:0.3px;
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

with open(os.path.join(HERE, "valletta_leadership_outline_v3.html"), "w") as f:
    f.write(html)

print("written", len(PAGES), "pages")
