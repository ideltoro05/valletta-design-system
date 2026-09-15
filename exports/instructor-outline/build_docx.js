const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, PageBreak,
  convertInchesToTwip, LevelFormat, ExternalHyperlink,
} = require("docx");

const HERE = __dirname;
const img = (name) => fs.readFileSync(path.join(HERE, name));

const BLACK = "0A0A0A";
const CHARCOAL = "26282B";
const RED = "FF002B";
const STEEL = "5B5F66";
const LINE_GRAY = "D8D9DB";
const WHITE = "FFFFFF";

const F_HEAD = "Bookman Old Style";
const F_LABEL = "Arial";
const F_BODY = "Calibri";

const PAGE_W = 12240, PAGE_H = 15840;
const MARGIN = convertInchesToTwip(0.9);
const CONTENT_W = PAGE_W - 2 * MARGIN;

// ---- inline <strong> parsing for body paragraphs ----
function parseInline(text, opts = {}) {
  const size = opts.size ?? 21;
  const color = opts.color ?? CHARCOAL;
  const parts = text.split(/(<strong>.*?<\/strong>)/g).filter(Boolean);
  return parts.map((part) => {
    const m = part.match(/^<strong>(.*)<\/strong>$/);
    if (m) return new TextRun({ text: m[1], font: F_BODY, size, bold: true, color: BLACK });
    return new TextRun({ text: part, font: F_BODY, size, color });
  });
}

function sectionTitle(text) {
  return new Paragraph({
    spacing: { before: 260, after: 140 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 10 } },
    children: [new TextRun({ text: text.toUpperCase(), font: F_HEAD, bold: true, size: 25, color: BLACK })],
  });
}

function subHeading(text) {
  return new Paragraph({
    spacing: { before: 200, after: 90 },
    children: [new TextRun({ text: text.toUpperCase(), font: F_LABEL, bold: true, size: 19, color: BLACK, characterSpacing: 6 })],
  });
}

function bodyPara(text) {
  return new Paragraph({
    spacing: { after: 130, line: 270 },
    children: parseInline(text),
  });
}

function note(tag, lines) {
  const paras = [];
  paras.push(new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: "EFEFEC" },
    border: { left: { color: RED, space: 10, style: BorderStyle.SINGLE, size: 16 } },
    spacing: { before: 100, after: 20 },
    children: [new TextRun({ text: tag, font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 8 })],
  }));
  lines.forEach((l, i) => {
    paras.push(new Paragraph({
      shading: { type: ShadingType.CLEAR, color: "auto", fill: "EFEFEC" },
      border: { left: { color: RED, space: 10, style: BorderStyle.SINGLE, size: 16 } },
      spacing: { after: i === lines.length - 1 ? 100 : 20 },
      children: [new TextRun({ text: l, font: F_BODY, size: 19, color: CHARCOAL })],
    }));
  });
  return paras;
}

function bio(text) {
  return new Paragraph({
    spacing: { after: 110, line: 250 },
    children: [new TextRun({ text, font: F_BODY, italics: true, size: 18, color: STEEL })],
  });
}

function quoteBlock(text, attribution, lead) {
  const runs = [];
  if (lead) runs.push(new TextRun({ text: lead + " ", font: F_BODY, bold: true, size: 21, color: BLACK }));
  runs.push(new TextRun({ text: "“" + text + "”", font: F_BODY, italics: true, size: 21, color: STEEL }));
  if (attribution) {
    runs.push(new TextRun({ text: " – ", font: F_BODY, size: 21, color: STEEL }));
    runs.push(new TextRun({ text: attribution, font: F_BODY, bold: true, size: 21, color: BLACK }));
  }
  return new Paragraph({
    indent: { left: 200 },
    border: { left: { color: RED, space: 12, style: BorderStyle.SINGLE, size: 16 } },
    spacing: { before: 140, after: 140, line: 280 },
    children: runs,
  });
}

function metaBox(rows) {
  return rows.map((r, i) => new Paragraph({
    border: {
      top: i === 0 ? { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } : undefined,
      bottom: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 },
      left: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 },
      right: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 },
    },
    spacing: { before: 60, after: 60 },
    tabStops: [{ type: "left", position: 2300 }],
    children: [
      new TextRun({ text: r.label.toUpperCase() + "\t", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 4 }),
      new TextRun({ text: r.value, font: F_BODY, size: 19, color: CHARCOAL }),
    ],
  }));
}

function overviewBand(title, items) {
  const banner = new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { after: 0 },
    children: [new TextRun({ text: title.toUpperCase(), font: F_HEAD, bold: true, size: 22, color: WHITE })],
  });
  const rows = items.map((t, i) => new Paragraph({
    indent: { left: 200 },
    border: i === items.length - 1
      ? { bottom: { color: LINE_GRAY, space: 6, style: BorderStyle.SINGLE, size: 4 }, left: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 }, right: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } }
      : { left: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 }, right: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text: t, font: F_BODY, size: 21, color: CHARCOAL })],
  }));
  return [banner, ...rows, new Paragraph({ spacing: { after: 160 }, children: [] })];
}

function conclusionBand(title, text) {
  const banner = new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { after: 100 },
    children: [new TextRun({ text: title.toUpperCase(), font: F_HEAD, bold: true, size: 22, color: WHITE })],
  });
  return [banner, bodyPara(text)];
}

function statList(items) {
  return items.map((t) => new Paragraph({
    numbering: { reference: "brand-bullets", level: 0 },
    spacing: { after: 70, line: 250 },
    children: [new TextRun({ text: t, font: F_BODY, size: 21, color: CHARCOAL })],
  }));
}

function arItem(children) {
  return new Paragraph({
    numbering: { reference: "brand-bullets", level: 0 },
    spacing: { after: 60, line: 250 },
    children,
  });
}
function linkRun(url) {
  return new ExternalHyperlink({
    link: url,
    children: [new TextRun({ text: url, font: F_BODY, size: 21, color: "1155CC", underline: {} })],
  });
}
function pageBreak() { return new Paragraph({ children: [new PageBreak()] }); }

// ---- header/footer ----
const logoBuf = img("valletta-mark-black.png");
function makeHeader() {
  return new Header({
    children: [new Paragraph({
      tabStops: [{ type: "right", position: CONTENT_W }],
      border: { bottom: { color: RED, space: 8, style: BorderStyle.SINGLE, size: 16 } },
      children: [
        new ImageRun({ type: "png", data: logoBuf, transformation: { width: 150, height: 30 } }),
        new TextRun({ text: "\t" }),
        new TextRun({ text: "LEADERSHIP INSTRUCTOR OUTLINE", font: F_LABEL, bold: true, size: 15, color: STEEL, characterSpacing: 10 }),
      ],
    })],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Valletta Industries  |  Leadership Instructor Outline  –  Page ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.CURRENT], font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ text: " of ", font: F_BODY, size: 15, color: STEEL }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_BODY, size: 15, color: STEEL }),
      ],
    })],
  });
}
const emptyHeader = new Header({ children: [new Paragraph({ children: [] })] });
const emptyFooter = new Footer({ children: [new Paragraph({ children: [] })] });

// ================= CONTENT =================
const content = [];

// ---- cover ----
content.push(
  new Paragraph({ spacing: { before: 2600 }, alignment: AlignmentType.CENTER,
    children: [new ImageRun({ type: "png", data: img("valletta-mark-white.png"), transformation: { width: 300, height: 60 } })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400 },
    children: [new TextRun({ text: "INSTRUCTOR OUTLINE", font: F_LABEL, bold: true, size: 19, color: RED, characterSpacing: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 220 },
    children: [new TextRun({ text: "LEADERSHIP TRAINING", font: F_HEAD, bold: true, size: 52, color: WHITE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
    children: [new TextRun({ text: "OUTLINE", font: F_HEAD, bold: true, size: 52, color: WHITE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500 },
    children: [new TextRun({ text: "TIME: 4 HOURS", font: F_LABEL, bold: true, size: 17, color: "B9BBBE", characterSpacing: 6 })] }),
  pageBreak(),
);

// ---- course metadata ----
content.push(...metaBox([
  { label: "Time", value: "4 hours" },
  { label: "Method of Instruction", value: "Classroom lecture, PowerPoint presentation, classroom discussion, and observation/review during practical exercises." },
  { label: "Description", value: "In this period of instruction, we will discuss the importance of leadership principles and the components it takes to be an effective leader." },
  { label: "Special Requirements", value: "Classroom, laptop computer, presentation pointer, projector, and PowerPoint presentation (can be conducted by lecture only from the outline)." },
  { label: "Instructional Aides", value: "PowerPoint presentation, student outlines, handouts" },
]));

content.push(new Paragraph({ spacing: { after: 60 }, children: [] }));

// ---- Presentation / Introduction / Objective ----
content.push(
  sectionTitle("Presentation"),
  subHeading("Introduction"),
  ...note("SCRIPT", ["Good morning/afternoon/evening, my name is ____. Your next period of instruction will be on becoming an effective leader. (Instructor Experience)"]),
  subHeading("Objective"),
  bodyPara("The objective of this course is to learn the fundamentals of being a leader. As a supervisor, manager, or task leader you will be around people from different backgrounds and with different past experiences, and each may require a different style of leadership. It is your responsibility to effectively lead and complete assigned tasks while dealing with different personalities. Your people (subordinates) will determine if you are an effective or ineffective leader, and this can be measured by performance of assigned tasks. Effective leadership begins with having the proper mindset and attitude."),
  ...note("VIDEO 1 — SGT. TRAVIS MILLS", ["https://www.youtube.com/watch?v=eSytAgtLqVw"]),
  bio("(Retired United States Army Staff Sergeant Travis Mills of the 82nd Airborne is a recalibrated warrior, motivational speaker, actor, author and an advocate for veterans and amputees. Travis’s New York Times bestselling memoir, Tough as They Come, is currently available on sale in bookstores everywhere. Despite losing portions of both arms and legs from an IED while on active duty in Afghanistan, Travis continues to overcome life’s challenges, breaking physical barriers and defying odds. Travis lives by his motto: “Never give up. Never quit.”)"),
  quoteBlock("The only thing more contagious than a good attitude is a bad one.", "David Goggins", "Positive Attitude:"),
  bio("(David Goggins is the Author of Can’t Hurt Me: Master Your Mind and Defy the Odds chronicles David Goggins’ incredible life from perpetual victim to active duty Navy SEAL to world class ultra-athlete and world record holder. Graduate of SEAL training, Ranger school, and Air Force Tactical Air Control)"),
);

content.push(pageBreak());

// ---- Statistics ----
content.push(
  sectionTitle("Statistics"),
  bodyPara("For 30 years, MDA has helped many large corporations improve their financial and operating performance."),
  bio("According to MDA Training “5 Workplace Leadership Statistics, You Shouldn’t Ignore.” MDA Training, 12 Feb. 2020, mdatraining.com/blog/workplace-leadership-statistics/."),
  ...statList([
    "Employees supervised by highly engaged LEADERSHIP teams are 39% more likely to be engaged themselves.",
    "32% of employees lack the confidence to put new ideas to employers",
    "58% of Managers report that they never received any management training",
    "82% of employees don’t trust their boss, to tell the truth,",
    "79% of employees cite the “lack of appreciation” as a reason for quitting their job.",
  ]),
  bodyPara("It is paramount that leaders in the workplace are consistently rewarding hard work and success. Without this, employees who excel within their roles will feel undervalued and ultimately unhappy at the business, despite their strong performance."),
  bodyPara("So with these statistics in mind, what is a common denominator that can affect these results? What can we do as leaders to improve these numbers?"),
  quoteBlock("The single biggest way to impact an organization is to focus on leadership development. There is almost no limit to the potential of an organization that recruits good people, raises them as leaders, and continually develops them.", "John Maxwell."),
  bio("(John Maxwell has written more than 100 books that have been translated into fifty languages. He has authored several New York Times bestselling books about leadership and was named #1 leadership expert in the world by Inc. Magazine in 2014)"),
  new Paragraph({ spacing: { after: 60 }, children: [] }),
  ...overviewBand("Overview", [
    "Defining Leadership",
    "Examples of Effective Leadership",
    "Describe Components of Being an Effective Leader",
    "Ethical Characteristics for Leadership",
    "Describe Motivational Leadership",
    "Understand the Basics of Supervision and Evaluating Work Performance",
  ]),
);

content.push(pageBreak());

// ---- Defining Leadership ----
content.push(
  sectionTitle("Defining Leadership"),
  ...note("VIDEO 2", ["https://www.youtube.com/watch?v=abFAhCtUyMM", "We were soldiers, play the first 16 seconds about a leader going first"]),
  bodyPara("Definition—The ability to influence others to accomplish a task by providing a purpose, a direction, and appropriate motivation. Explaining the mission to subordinates helps them focus on the importance of the objective and allows them to perform in a more efficient and disciplined manner."),
  bodyPara("Although having a supervisory position provides the opportunity to be a leader; a position does not make you a leader. Being a leader is a choice that has nothing to do with your status on the organizational chart; once you decide to lead others, it will become easier to see where you can impact the mission the most."),
  bodyPara("We have all heard the phrase “Leaders Lead,” but not all leaders are influential. Leaders must set an example for all to follow. Good leaders set the standard and can meet it/surpass it. Leading by example instills confidence and respect from subordinates and makes the leader more effective."),
  bodyPara("Strive to be the best at your assignments and learn the positions above and below you. Understanding the tasks assigned to personnel on your team will build confidence in your leadership."),
  bodyPara("A leader looks for ways to better those around them and the mission. A leader looks for more responsibility and accepts the outcome no matter the success of your actions."),
  bodyPara("Make sound and timely decisions. A good leader makes a decision based on the immediately available information. As a leader being indecisive can result in problems getting worse rather than better. An immediate decision is still moving the team closer to completing the mission. If a decision does not get the desired result, discuss with subordinates and other leaders to learn from it."),

  sectionTitle("Examples of Effective Leadership"),
  bodyPara("Charismatic Leader—Charismatic leadership combines charm, interpersonal connection, and persuasive communication to motivate others. Some examples are Sir Winston Churchill, and Nelson Mandela."),
  bodyPara("Transformational Leader—Transformational leadership is when a leader’s behaviors influence followers and inspire them to perform beyond their perceived capabilities. Transformational leadership inspires people to achieve unexpected or remarkable results. Examples are Dr. Martin Luther King, Henry Ford, and Steve Jobs"),
  bodyPara("Servant Leader—Servant leadership occurs when the leader’s main goal and responsibility is to provide service to their people. Examples are Mahatma Gandhi and Mother Teresa."),
  bodyPara("Quiet Leaders—Quiet leaders recognize they cannot ask someone to do a task they wouldn’t or haven’t done. They set the example for others to follow. Silent leaders hold themselves to the same (or higher) standard than they hold for others. Trust. Silent leaders do not micromanage or nag others. Examples are Albert Einstein, Sir Isaac Newton, Rosa Parks, Bill Gates, and Warren Buffett."),
  ...note("VIDEO 3", ["https://www.youtube.com/watch?v=0fpK9591u6M", "We Were Soldier’s Leadership clip, different types of leaders"]),
  ...note("DISCUSSION", ["Discuss types of leadership in video and perceived traits.", "How does this impact a team, what does it make you feel?"]),
);

content.push(pageBreak());

// ---- Components of Effective Leadership ----
content.push(
  sectionTitle("Describe the Components of Effective Leadership"),
  subHeading("Leadership Traits"),
  bodyPara("A good leader encourages their staff to participate in all assigned tasks with clear instructions and supervision."),
  bodyPara("A good leader educates themselves to understand assigned tasks and mentor those below them. Learning the functions of their supervisors provide context for the direction of the mission and makes the leader a more valuable member of the team."),
  bodyPara("A good leader knows their capabilities and has an honest opinion of their strengths and weaknesses. This information is discovered through honest evaluation by supervisors and subordinates during regular performance discussions."),
  bodyPara("A good leader treats all team members with dignity and respect. Respect in its basic form shows that you are aware of someone’s rights, values, wishes, and other personal beliefs. To be aware of this information, a leader must regularly communicate to understand each team member’s individual needs. A leader always must respect subordinates to earn their respect."),
  bodyPara("A leader must possess professional character traits such as ambition, creativity, compassion, courage, flexibility, honesty (integrity), humility, loyalty, patience, discipline, and curiosity."),
  bodyPara("A leader understands how to manage stress and is capable of sharing those skills. Exercise, meditation, breathing exercises, and reading are all examples of stress-relieving activities. Also, honest discussions about specific topics can help relieve stress by providing clarity about the stressful issue"),

  subHeading("Communication"),
  bodyPara("Influential leaders must adapt their communication style to effectively communicate to their team."),
  bodyPara("Each employee will have different motivations, so understanding how to communicate with each team member is essential."),
  bodyPara("Effective leaders must be able to talk but also listen. It is essential to listen to your team and genuinely accept their input even if their suggestions are not part of the leader’s final instructions."),
  bodyPara("An effective leader must be transparent about the team’s direction to continue building trust with subordinates. Honestly assessing performance and acknowledging if the leader has made a mistake will encourage employees that they are safe to share information with the leader."),
  bodyPara("Effective leaders use communication tools to understand subordinate’s suggestions better. By asking open-ended questions like “tell me more” or “explain what you mean,” a leader can get more details and ensure they understand the information thoroughly."),
  bodyPara("Communication is not only verbal but how you carry yourself. Practicing simple body language cues will help establish interest and rapport. Making eye contact is a simple way to start changing body language cues."),
  bodyPara("A good leader will ask for feedback on their performance to subordinates, and understanding what subordinates need from the leader. The most important part of this is to implement change based on their input. The effort to implement change will continue to strengthen the trust of subordinates."),
);

content.push(pageBreak());

// ---- Observing Effective Follower Traits ----
content.push(
  sectionTitle("Observing Effective Follower Traits (Knowing Your People)"),
  quoteBlock("Why would you want to be someone called a follower? A simple answer is people follow because they derive benefits. The psychological payback of following exceeds the psychological cost of following. Throughout our human history, most humans were in small, nomadic clusters. These tribes offered protection, food, and survival. The groups with the best leader and followers had a higher probability of survival than those poorly led that consisted of poor followers. The physical benefits for followers outweighed the psychological costs and so most likely they stayed connected to the tribe. If some followers were dissatisfied with the leader’s goals and agenda, they had a choice of either fighting for the top position, or leaving to join other groups.", "(Project Management Institute 2021)", "The Psychology of Followers:"),
  bodyPara("Followers are an essential part of leadership, and being a follower is a straightforward concept. Following is the ability to take direction well, believe in a program, be part of a team, and deliver on your expectations. A follower can provide strength to the leader by contributing to the organization in areas that complement the leader’s position."),
  bodyPara("A follower has good judgment and will take direction but not follow blindly. Good judgment is required and can be learned from good leadership."),
  bodyPara("Good followers are good workers, and they need good direction to understand what is expected of them."),
  bodyPara("Followers can be categorized into multiple groups, such as followers with positive attitudes who will be motivated on their own. Others will have minimal levels of independent thinking and need constant direction. Also, negative followers will be more capable of thinking independently but do not contribute positively to the team. We can break these groups down further, but for this course, it is only essential to understand that each follower will be different in the leadership style that will inspire them the most."),
  bodyPara("To be effective, followers must be willing to share their ideas and opinions with leaders."),

  sectionTitle("Understanding the Mission or Task"),
  bodyPara("As a leader, you must have a purpose, and your drive will come from your mission."),
  bodyPara("The mission will help the team share priorities, set performance goals, plan performance rewards, and give a shared vision for the team."),
  bodyPara("The mission or task also gives an effective leader “vision.” Vision is the opportunity to see a path to success or failure and the future development of your team."),
  bodyPara("An effective leader can create small tasks to create growth on their team. A leader can plan short team-building exercises or task-specific training to focus the team on an assigned task. Often an effective will be managing multiple tasks for each member on their team based on the team member’s ability."),
  ...note("VIDEO 4", ["The first 3:27 of – https://www.youtube.com/watch?v=jYK-drFNI6o", "Jocko Willink/Mulligan Brothers interview that describes timing and response"]),
  ...note("DISCUSSION", ["Focusing on the appropriate time to execute decisions.", "Picking the right time to action change, (leadership capital)."]),
);

content.push(pageBreak());

content.push(
  bio("(Jocko Willink is a retired U.S. Navy SEAL officer, co-author of the #1 New York Times bestseller Extreme Ownership: How U.S. Navy SEALs Lead and Win, Dichotomy of Leadership, host of the top-rated Jocko Podcast, and co-founder of Echelon Front, where he serves as Chief Executive Officer, leadership instructor, speaker and strategic advisor. Jocko spent 20 years in the SEAL Teams, starting as an enlisted SEAL and rising through the ranks to become a SEAL officer. As commander of SEAL Team Three’s Task Unit Bruiser during the battle of Ramadi, he orchestrated SEAL operations that helped the “Ready First” Brigade of the U.S. Army’s First Armored Division bring stability to the violent, war-torn city. Task Unit Bruiser became the most highly decorated Special Operations Unit of the Iraq War."),
  bio("Jocko returned from Iraq to serve as Officer-in-Charge of training for all West Coast SEAL Teams. There, he spearheaded the development of leadership training and personally instructed and mentored the next generation of SEAL leaders who have continued to perform with great success on the battlefield. Jocko is the recipient of the Silver Star, the Bronze Star, and numerous other personal and unit awards."),
  bio("Upon retiring from the Navy, Jocko co-founded Echelon Front, a premier leadership consulting company, where he teaches the leadership principles he learned on the battlefield to help others lead and win. Jocko also authored the Discipline Equals Freedom Field Manual, a New York Times Bestseller, and the bestselling Way of the Warrior Kid children’s book series.)"),
  bodyPara("According to Simon Sinek, Leaders have always been told to learn to listen, He states that Good Leaders need to learn to listen and then speak last. He further states, “The skill that it takes to hold your opinion and comments until everyone has spoken, allows you to do two things, 1 It gives everyone the opportunity and feeling that they have been heard and that everyone has contributed, 2 it gives you the opportunity to hear everyone else’s input and feelings before you render your opinion.”"),

  sectionTitle("Ethical Characteristics for Leadership"),
  bodyPara("<strong>Fair</strong>—An ethical leader is fair, and they treat everyone on their team equally with no bias. Team members will not perform to their best ability if they feel like decisions are unfair and made with any bias."),
  bodyPara("<strong>Honest</strong>—Ethical leaders are honest and must always be transparent and fair. A good leader should give the unpopular truth to their team rather than a lie. Consistent honesty builds trust with your team and promotes the open sharing of information."),
  bodyPara("<strong>Respect</strong>—Leaders who actively listen to subordinates and do not dismiss their concerns will have a team focused on achieving the same objective. Although you may be higher in a chain of command, your team should feel as though they are equally important to the mission."),
  bodyPara("<strong>Value-Oriented</strong>—While each person has individual values, a good leader will make decisions based on the organization’s values. An ethical leader will share the organization’s values with the team and implement changes that adhere to those values."),
  bodyPara("<strong>Leads by Example</strong>—Employees will mimic the action of their leader. A leader cannot expect his team to make ethical decisions if they are unwilling to make ethical choices. An ethical leader takes ownership of their actions without placing blame on anyone else."),
  bodyPara("<strong>Prioritizes the Team</strong>—Ethical leaders will promote team building and foster a sense of community. Ethical leaders will help each team member to achieve personal and professional goals through regular communication."),
  quoteBlock("When setting expectations, no matter what has been said or written, if substandard performance is accepted and no one is held accountable if there are no consequences, then poor or substandard performance becomes the new standard. Therefore, leaders must enforce standards.", "Jocko Willink.", "Expectations:"),
);

content.push(pageBreak());

// ---- Motivational Leadership ----
content.push(
  sectionTitle("Describe Motivational Leadership"),
  quoteBlock("A leader must lead, but also be ready to follow. They must be aggressive, but not overbearing. A leader must be calm, but not robotic. They must be confident, but never cocky. A leader must be brave, but not foolhardy. They must have a competitive spirit, but be a gracious loser.", "Jocko Willink"),
  bodyPara("A motivational leader can make decisions and set clear goals for their teams. Motivational leaders see the best in their team and inspire them to accomplish a goal. Sometimes these goals are shared by the team or individual goals to better a team member."),
  bodyPara("What is the difference between Motivation and Inspiration?"),
  bodyPara("Inspiration is an external influence or pulling force that compels you to achieve something."),
  bodyPara("Motivation is an internal influence or a driving force that you feel on the inside to achieve something."),
  bodyPara("A good leader should try to inspire those around them. If the leader has a positive attitude and tries to help others succeed, it will encourage their team members to share those behaviors. An effective leader aims to inspire their team with knowledge, experience, and clear direction. Sometimes trying to “motivate” subordinates can feel fake. They may feel the leader isn’t experiencing the same doubts as them. When the leader focuses on inspiration as the goal, the subordinate will likely feel more connected to the leader. This thought process will continue to strengthen trust between the team."),
  bodyPara("An effective leader will make logical decisions based on the immediate information available. If the decision was wrong, explain the rationale behind it or what led you to the conclusion and learn from it."),
  ...note("OODA LOOP", ["Observe, Orient, Decide, and Act — a simple process to handle any situation."]),
  bodyPara("Know the strengths and weaknesses of subordinates and look out for their wellbeing."),
  quoteBlock("If your actions inspire others to dream more, learn more, do more and become more, then you are a leader.", "John Quincy Adams"),
);

content.push(pageBreak());

// ---- Supervision / Conclusion / Additional Reading ----
content.push(
  sectionTitle("Understand the Basics of Supervision and Evaluating Work Performance"),
  bodyPara("An effective leader does not Micro-Manage. Micromanagers stifle initiative, breed resentment, and lower morale for everyone. When a leader micromanages subordinates its takes away their ambition and desire to succeed, so there is no natural desire to perform because someone else will tell them when and how to do everything."),
  bodyPara("An effective leader is proactive and should avoid having a “hands-off” mentality. A “hands-off” leadership approach can lead to subordinates not having clear direction causing a lack of confidence in the chain of command. A lack of engagement can also cause team members to perceive that the leader doesn’t care about the team or the mission."),
  bodyPara("A leader will delegate supervision, responsibility, and authority to capable subordinates. Delegating responsibility to subordinates will help them to understand the challenges faced by supervisors. Sharing the supervisor’s role also gives experience to other team members and provides the leader an opportunity to communicate performance."),
  bodyPara("As a supervisor, you should ensure that all tasks are understood, supervised, and accomplished. This supervision must include clear instructions so your team can execute their jobs efficiently."),
  bodyPara("A good supervisor can perform the tasks of his subordinates and is capable of improving their team’s performance through technical proficiency and guidance."),
  bodyPara("A good leader will hold their team accountable with honest feedback on performance from each assigned task. Giving verbal performance evaluations should be done during the execution of assigned tasks and also with after-action discussions. Using regular written performance statements will reinforce the verbal directions during the performance of their assignments. Using a multiple approach system to performance evaluations will ensure all team members are aware of their performance in each area of their assigned task."),

  ...conclusionBand("Conclusion", "Today, we have reviewed ways to be an effective leader and the different factors that affect a team. We have discussed traits and tactics that you can adopt to build trust and understanding of your subordinates."),

  new Paragraph({ spacing: { after: 60 }, children: [] }),
  sectionTitle("Additional Reading"),
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "Several good books are recommended for follow-on information:", font: F_BODY, size: 21, color: CHARCOAL })] }),
  arItem([new TextRun({ text: "12 Rules for Life – Jordan B. Peterson", font: F_BODY, size: 21, color: CHARCOAL })]),
  arItem([new TextRun({ text: "Leadership and Training for the Fight – Paul Howe", font: F_BODY, size: 21, color: CHARCOAL })]),
  arItem([new TextRun({ text: "Extreme Ownership – Jocko Willink", font: F_BODY, size: 21, color: CHARCOAL })]),
  arItem([new TextRun({ text: "Can’t Hurt Me: Master Your Mind and Defy the Odds – David Goggins", font: F_BODY, size: 21, color: CHARCOAL })]),
  arItem([linkRun("https://www.johnmaxwell.com/my-purpose/")]),
  arItem([linkRun("https://echelonfront.com/jocko-willink/")]),
  arItem([linkRun("https://www.travismills.org/")]),
);

// ================= DOCUMENT =================
const doc = new Document({
  numbering: {
    config: [{
      reference: "brand-bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "■",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 220 } }, run: { color: RED, font: F_BODY, size: 16 } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } },
      titlePage: true,
    },
    headers: { default: makeHeader(), first: emptyHeader },
    footers: { default: makeFooter(), first: emptyFooter },
    children: content,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(HERE, "valletta_instructor_outline.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
