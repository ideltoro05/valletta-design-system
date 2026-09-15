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

function romanBand(numeral, text) {
  return new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { before: 260, after: 160 },
    children: [
      new TextRun({ text: numeral + "  ", font: F_HEAD, bold: true, size: 24, color: RED }),
      new TextRun({ text: text.toUpperCase(), font: F_HEAD, bold: true, size: 24, color: WHITE }),
    ],
  });
}

function epoHeading(label, text) {
  return new Paragraph({
    spacing: { before: 220, after: 120 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 10 } },
    children: [
      new TextRun({ text: label + "  ", font: F_HEAD, bold: true, size: 22, color: RED }),
      new TextRun({ text: text.toUpperCase(), font: F_HEAD, bold: true, size: 22, color: BLACK }),
    ],
  });
}

function subHeading(text) {
  return new Paragraph({
    spacing: { before: 160, after: 80 },
    children: [new TextRun({ text: text.toUpperCase(), font: F_LABEL, bold: true, size: 18, color: BLACK, characterSpacing: 4 })],
  });
}

function bodyPara(text) {
  return new Paragraph({ spacing: { after: 120, line: 260 }, children: [new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL })] });
}

function leadIn(label, text) {
  return new Paragraph({
    spacing: { after: 120, line: 260 },
    children: [
      new TextRun({ text: label + " ", font: F_BODY, bold: true, size: 20, color: BLACK }),
      new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL }),
    ],
  });
}

function note(tag, lines) {
  const paras = [];
  paras.push(new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: "EFEFEC" },
    border: { left: { color: RED, space: 10, style: BorderStyle.SINGLE, size: 16 } },
    spacing: { before: 90, after: 20 },
    children: [new TextRun({ text: tag, font: F_LABEL, bold: true, size: 14, color: RED, characterSpacing: 6 })],
  }));
  lines.forEach((l, i) => {
    paras.push(new Paragraph({
      shading: { type: ShadingType.CLEAR, color: "auto", fill: "EFEFEC" },
      border: { left: { color: RED, space: 10, style: BorderStyle.SINGLE, size: 16 } },
      spacing: { after: i === lines.length - 1 ? 90 : 20 },
      children: [new TextRun({ text: l, font: F_BODY, size: 18, color: CHARCOAL })],
    }));
  });
  return paras;
}

function quoteBlock(text, attribution) {
  const runs = [new TextRun({ text: "“" + text + "”", font: F_BODY, italics: true, size: 20, color: STEEL })];
  if (attribution) {
    runs.push(new TextRun({ text: " – ", font: F_BODY, size: 20, color: STEEL }));
    runs.push(new TextRun({ text: attribution, font: F_BODY, bold: true, size: 20, color: BLACK }));
  }
  return new Paragraph({
    indent: { left: 200 },
    border: { left: { color: RED, space: 12, style: BorderStyle.SINGLE, size: 16 } },
    spacing: { before: 130, after: 130, line: 270 },
    children: runs,
  });
}

const IND = [0, 300];
function outlineItem(label, text, level = 0) {
  return new Paragraph({
    indent: { left: IND[level] },
    spacing: { after: 90, line: 255 },
    children: [
      new TextRun({ text: label + " ", font: F_BODY, bold: true, size: 20, color: RED }),
      new TextRun({ text, font: F_BODY, size: 20, color: CHARCOAL }),
    ],
  });
}

function statList(items) {
  return items.map((t) => new Paragraph({
    numbering: { reference: "brand-bullets", level: 0 },
    spacing: { after: 70, line: 250 },
    children: [new TextRun({ text: t, font: F_BODY, size: 20, color: CHARCOAL })],
  }));
}

function refBlock(items) {
  const paras = [new Paragraph({
    border: { top: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 }, left: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 }, right: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 60, after: 30 },
    children: [new TextRun({ text: "REFERENCES", font: F_LABEL, bold: true, size: 15, color: RED, characterSpacing: 8 })],
  })];
  items.forEach((t, i) => {
    paras.push(new Paragraph({
      border: {
        bottom: i === items.length - 1 ? { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } : undefined,
        left: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 },
        right: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 },
      },
      spacing: { after: i === items.length - 1 ? 60 : 30 },
      children: [new TextRun({ text: t, font: F_BODY, size: 16, color: STEEL })],
    }));
  });
  return paras;
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
        new TextRun({ text: "EFFECTIVE MOTIVATIONAL LEADERSHIP – SUPPORTING INFORMATION", font: F_LABEL, bold: true, size: 13, color: STEEL, characterSpacing: 6 }),
      ],
    })],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Valletta Industries  |  Effective Motivational Leadership – Supporting Information  –  Page ", font: F_BODY, size: 15, color: STEEL }),
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
    children: [new TextRun({ text: "SUPPORTING INFORMATION", font: F_LABEL, bold: true, size: 19, color: RED, characterSpacing: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 220 },
    children: [new TextRun({ text: "EFFECTIVE MOTIVATIONAL", font: F_HEAD, bold: true, size: 46, color: WHITE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
    children: [new TextRun({ text: "LEADERSHIP", font: F_HEAD, bold: true, size: 46, color: WHITE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500 },
    children: [new TextRun({ text: "LEADERSHIP TRAINING", font: F_LABEL, bold: true, size: 17, color: "B9BBBE", characterSpacing: 6 })] }),
  pageBreak(),
);

// ---- References ----
content.push(...refBlock([
  "https://www.projectmanagement.com/contentPages/article.cfm?ID=570414&thisPageURL=/articles/570414/Leading-in-High-Stress-Environments#_=_",
  "https://www.360training.com/blog/8-characteristics-ethical-leader",
  "https://www.pmi.org/learning/library/importance-of-effective-followers-5887",
]));
content.push(new Paragraph({ spacing: { after: 60 }, children: [] }));

// ---- II. Presentation ----
content.push(
  romanBand("II.", "Presentation"),
  ...note("NOTE", ["Show Slide “Effective Motivational Leadership” — Introduce yourself to the class."]),
  leadIn("INTRODUCTION:", "Good morning/afternoon/evening, my name is __________. Your next period of instruction will be on Effective Motivational Leadership."),
  ...note("NOTE", ["Show Slide “Why are you here?” — Solicit feedback from students and get them talking about why they are sitting in the course."]),
  leadIn("GAIN ATTENTION:", "Being a manager/leader on any SOC contract you will be around people all from different backgrounds and with different past experiences and it is your responsibility to effectively lead and complete assigned tasks all while dealing with different personalities. Your people (subordinates) will determine if you are an effective or in-effective leader. Effective leadership begins with having the proper mindset and attitude."),
  ...note("VIDEO 1 — SGT. TRAVIS MILLS", ["06:14 — https://www.youtube.com/watch?v=eSytAgtLqVw", "Talk about the video as it pertains to a positive attitude"]),
  quoteBlock("The only thing more contagious than a good attitude is a bad one.", "David Goggins"),
);

content.push(pageBreak());

// ---- Statistics ----
content.push(
  ...note("NOTE", ["Show Slide “Statistics” — Discuss each and solicit feedback. Continue with “Statistics Continued” slide."]),
  subHeading("Statistics"),
  bodyPara("According to MDA Training “5 Workplace Leadership Statistics You Shouldn't Ignore.” MDA Training, 12 Feb. 2020, mdatraining.com/blog/workplace-leadership-statistics/."),
  ...statList([
    "Employees who are supervised by highly engaged LEADERSHIP teams are 39% more likely to be engaged themselves.",
    "32% of employees lack the confidence to put new ideas to employers",
    "58% of Managers report that they never received any management training",
    "82% of employees don’t trust their boss to tell the truth",
    "79% of employees cite the “lack of appreciation” as a reason for quitting their job.",
  ]),
  bodyPara("So with these numbers in mind, what is the one common denominator that I/You/We can do to change these numbers? We can be better examples of the leader we want above us."),
  ...note("NOTE", ["Show Slide — John Maxwell Quote"]),
  quoteBlock("The single biggest way to impact an organization is to focus on leadership development. There is almost no limit to the potential of an organization that recruits good people, raises them up as leaders and continually develops them.", "John Maxwell"),
);

content.push(pageBreak());

// ---- Performance Objectives ----
content.push(
  ...note("NOTE", ["Show Slide “Terminal Performance Objective”"]),
  subHeading("Introduction of Performance Objectives"),
  new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "Terminal Performance Objective (TPO)(s):", font: F_BODY, bold: true, size: 20, color: BLACK })] }),
  outlineItem("TPO 1:", "Students will be able to properly define and identify leadership styles and be able to motivate subordinates and effectively lead."),
  ...note("NOTE", ["Show Slide “Enabling Performance Objectives”"]),
  new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "Enabling Performance Objective (EPO)(s):", font: F_BODY, bold: true, size: 20, color: BLACK })] }),
  outlineItem("EPO 1:", "Define Leadership"),
  outlineItem("EPO 2:", "Identify and discuss examples of effective and in-effective leadership."),
  outlineItem("EPO 3:", "List and describe in detail the four (4) components of effective leadership."),
  outlineItem("EPO 4:", "List four (4) Ethics qualities found in a professional work environment."),
  outlineItem("EPO 5:", "Describe what motivational leadership is."),
  outlineItem("EPO 6:", "Understand the basics of supervision and evaluating work performance."),
  ...note("VIDEO 2 — “WE WERE SOLDIERS”", ["00:16 — https://www.youtube.com/watch?v=abFAhCtUyMM", "Solicit feedback"]),
);

content.push(pageBreak());

// ---- EPO 1: Define Leadership ----
content.push(
  epoHeading("EPO 1:", "Define leadership."),
  ...note("NOTE", ["Show Slide “Leadership” and “Leadership Continued”"]),
  subHeading("Leadership"),
  outlineItem("a.", "Definition — The ability to influence others to accomplish a task by proviing a purpose, a direction and appropriate motivation. Explaining the mission to subordinates helps them keep the importance of the objective up front and allows them to perform in a more efficient and disciplined manner."),
  outlineItem("b.", "Leadership is not a rank, leadership is not a position, leadership is a choice. It has nothing to do with your position on the organizational chart, once you make a conscious decision to look after the person on your left and your right you have become a leader."),
  outlineItem("c.", "We have all heard the phrase “Leaders Lead” well do they? Leaders must set the example for all to follow. Good leaders set the standard and can meet it/surpass it. Leading by example instills confidence and respect in their leaders and in turn makes them more effective."),
  outlineItem("d.", "Be technically proficient, give off a good/positive vibe not a negative one"),
  outlineItem("e.", "Seek responsibility and always take responsibility for your actions, good or bad"),
  outlineItem("f.", "Make sound and timely decisions. A good leader makes a decision, right wrong or indifferent make a decision, indecision or no decision is wrong every time and can result in an adverse action. If the decision was the wrong one, explain the rationale behind it or what led you to the decision and learn from it."),

  epoHeading("EPO 2:", "Identify and discuss examples of effective and in-effective leadership."),
  ...note("NOTE", ["Show Slide “Charismatic Leader” — There will be examples and photos of each, discuss and solicit feedback."]),
  outlineItem("a.", "Sir Winston Churchill — Charismatic Leader, led with passion, used charm to gain followers and put other people before himself. Other examples, Fidel Castro, Malcolm X and Nelson Mandela."),
);

content.push(pageBreak());

content.push(
  ...note("NOTE", ["Show Slide “Transformational Leader” — There will be examples and photos of each, discuss and solicit feedback."]),
  outlineItem("b.", "Dr. Martin Luther King — Transformational Leader, showed other people their visions, very passionate about his own visions and people followed him because he was honest. Some other examples Henry Ford, Steve Jobs and Adolf Hitler."),
  ...note("NOTE", ["Show Slide “Servant Leader” — There will be examples and photos of each, discuss and solicit feedback."]),
  outlineItem("c.", "Mahatma Ghandi — Servant Leader — took care of everyone before he gave followers what they want. Another example is Mother Teresa."),
  ...note("NOTE", ["Show Slide “Quiet Leaders” — There will be examples and photos of each, discuss and solicit feedback."]),
  outlineItem("d.", "Rosa Parks — Quiet Leaders are actually Introverts — Don’t try to be a leader, just comes natural and when they think of something that needs to be done, they do it and don’t rely on someone else. Other examples President Barrack Obama, Bill Gates and Warren Buffett."),
  ...note("NOTE", ["Show Slide “Effective vs. In-Effective” — Examples of 3 controversial leaders are presented. Discuss each and how their methods made them a good or bad leader."]),
  outlineItem("e.", "Examples of In-Effective Leadership — [Solicit feedback from the class and discuss names that come up] David Koresh, Osama Bin Laden, Saddam Hussein, etc. Were they ineffective leaders or were they good leaders with bad intentions?"),
  ...note("VIDEO 3 — “WE WERE SOLDIERS”", ["01:06 — https://www.youtube.com/watch?v=0fpK9591u6M", "Solicit feedback"]),
  ...note("NOTE", ["Show Slide “What type of leaders were depicted in the two clips” “What type of leader, are you?”"]),
);

content.push(pageBreak());

// ---- EPO 3: Four components ----
content.push(
  epoHeading("EPO 3:", "List and describe in detail the four (4) components of effective leadership."),
  ...note("NOTE", ["Show Slide “4 Components of Effective Leadership”"]),
  subHeading("1. Leader"),
  outlineItem("a.", "A good leader encourages his/her staff to participate in all assigned tasks"),
  outlineItem("b.", "A good leader educates his/herself to understand and mentor those below them and also support those above"),
  outlineItem("c.", "A good leader knows his/her capabilities to include strengths/weaknesses and limitations"),
  outlineItem("d.", "A good leader knows his/her staffs strengths, weaknesses and looks out for their well being"),
  outlineItem("e.", "A good leader is disciplined and leads effectively and treats all members with dignity and respect"),
  outlineItem("f.", "A good leader must possess professional character traits"),
  outlineItem("g.", "A good leader must manage stress and avoid burnout"),
  quoteBlock("A leader must lead, but also be ready to follow. They must be aggressive, but not overbearing. A leader must be calm, but not robotic. They must be confident, but never cocky. A leader must be brave, but not foolhardy. They must have a competitive spirit, but be a gracious loser.", "Jocko Willink"),

  ...note("NOTE", ["Show Slide “Follower”"]),
  subHeading("2. Follower"),
  outlineItem("a.", "Followers need encouragement"),
  outlineItem("b.", "Deserves praise when earned"),
  outlineItem("c.", "Constantly evaluated and may need to be reprimanded and/or punished"),
  outlineItem("d.", "A follower will develop their mutual trust, respect and confidence from a good leader leading by example, being respectful and keeping them informed"),
  outlineItem("e.", "Followers volunteer to help"),
);

content.push(pageBreak());

content.push(
  ...note("NOTE", ["Show Slide “Situation”"]),
  subHeading("3. Situation"),
  outlineItem("a.", "Understanding the situation is very important. One leadership style may not work in all situations. Leadership styles need to be fluid"),
  outlineItem("b.", "Consider all available resources and factors during any given situation"),
  outlineItem("c.", "Consider the followers competence, motivation and commitment to job performance"),
  outlineItem("d.", "Timing of actions and/or reactions may also be important."),
  ...note("VIDEO 4 — JOCKO WILLINK / MULLIGAN BROTHERS INTERVIEW", ["3:27 — https://www.youtube.com/watch?v=jYK-drFNI6o&pbjreload=10", "The interview discusses proper timing and response"]),
  ...note("NOTE", ["Show Slide “Communications”"]),
  subHeading("4. Communications"),
  outlineItem("a.", "Exchange information, ideas and insure you are precisely understood and you understand your staff"),
  outlineItem("b.", "The proper method of communication may vary and is situational dependent"),
  outlineItem("c.", "Effective communication is demonstrated in the completion of assigned tasks in a timely manner"),
  outlineItem("d.", "Understanding that there is more than one way to get to a desired result"),
  outlineItem("e.", "Communication must travel upward and downward"),
  ...note("NOTE", ["Show Slide “According to Simon Sinek”"]),
  bodyPara("According to Simon Sinek, Leaders have always been told to learn to listen, He states that Good Leaders need to learn to listen and then speak last. He further states “The skill that it takes to hold your opinion and comments until everyone has spoken, allows you to do two things, 1 It gives everyone the opportunity and feeling that they have been heard and that everyone has contributed, 2 it gives you the opportunity to hear everyone else’s input and feelings before you render your opinion”"),
);

content.push(pageBreak());

// ---- EPO 4: Ethics ----
content.push(
  epoHeading("EPO 4:", "List four (4) Ethics qualities found in a professional work environment."),
  ...note("NOTE", ["Show Slide “Ethics”"]),
  outlineItem("1.", "Loyalty — Support and defend the group/organization"),
  outlineItem("2.", "Duty — Accomplish all assigned tasks to the best of your ability"),
  outlineItem("a.", "Self-Reflection — This is the process of understanding your own strengths, and weaknesses, and grow the understanding of who you are. Being realistic about your values, and what makes you act the way you do. It is a constant evaluation of who you are, and what you want to become.", 1),
  outlineItem("3.", "Selfless Service — Put self-interest, personal advantage and self-gain aside and do what is best for the group/organization"),
  outlineItem("4.", "Integrity — Be honest, upright, avoid deception and live with respectful values"),
  outlineItem("a.", "Ownership — Taking ownership includes solving problems, being decisive, not placing blame, and taking responsibility for actions. Morale of subordinates can be damaged if a leader is not accountable for their own actions. Also holding subordinates accountable is very important, because it teaches them to have ownership over their performance.", 1),
  ...note("NOTE", ["Show Slide “Expectations” — Jocko Willink Quote"]),
  outlineItem("b.", "Expectations — “When setting expectations, no matter what has been said or written, if substandard performance is accepted and no one is held accountable, if there are no consequences, then poor or substandard performance becomes the new standard. Therefore, leaders must enforce standards.” – Jocko Willink.", 1),
  ...note("NOTE", ["Show Slide “Questions”"]),
  bodyPara("How does a leader maintain these qualities and how does this relate to what we do in training and our job performance every day?"),
);

content.push(pageBreak());

// ---- EPO 5: Motivational Leadership ----
content.push(
  epoHeading("EPO 5:", "Describe what motivational leadership is."),
  ...note("NOTE", ["Show Slide “What is Motivational Leadership?” — Solicit feedback"]),
  ...note("NOTE", ["Show Slide “Motivational Leadership”"]),
  outlineItem("a.", "Motivation good or bad should be displayed; disciplined when they fail to meet a required task but also be prepared to compliment when they meet or exceed a task."),
  outlineItem("b.", "What is the difference between Motivation and Inspiration?"),
  outlineItem("–", "Motivation is an external influence or driving force", 1),
  outlineItem("–", "Inspiration is an internal influence or pulling force.", 1),
  outlineItem("c.", "As a leader we need to try and inspire those around us. If we stay motivated and positive, we should hope those around us will also choose to be motivated and in turn be motivated in a positive direction. It’s a little thing, but if we try to inspire people it will feel more natural and if you try to “motivate” people it can seem fake."),
  ...note("VIDEO 5 — UNDERSTANDING MOTIVATION AND INSPIRATION", ["3:16 — https://www.youtube.com/watch?v=kr725Lm7bfM"]),
  ...note("NOTE", ["Show Slide “Motivation Leadership Continued”"]),
  outlineItem("f.", "Make sound and timely decisions. A good leader makes a decision, right wrong or indifferent make a decision, indecision or no decision is wrong every time and can result in an adverse action. If the decision was the wrong one, explain the rationale behind it or what led you to the decision and learn from it. OODA LOOP — Explain the process to Observe, Orient, Decide, and Act. A simple process to handle any situation."),
  outlineItem("g.", "Know the strengths and weaknesses of subordinates, and look out for their wellbeing."),
  quoteBlock("If your actions inspire others to dream more, learn more, do more and become more then you are a leader.", "John Quincy Adams"),
);

content.push(pageBreak());

// ---- EPO 6: Supervision ----
content.push(
  epoHeading("EPO 6:", "Understand the basics of supervision and evaluating work performance."),
  new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: "Considerations", font: F_BODY, bold: true, size: 20, color: BLACK })] }),
  ...note("NOTE", ["Show Slide “Basics of Supervision and Evaluation”"]),
  outlineItem("a.", "Don’t over supervise — These are referred to as Micro Managers. Micro Managers stifle initiative, breed resentment and lower morale for everyone. It’s like the common cold, and highly contagious."),
  outlineItem("b.", "Issue tasks, and let your subordinate work the task. Let the task mature, and offer feedback on current progress. Don’t get stuck telling your subordinate exactly how to accomplish a task."),
  outlineItem("c.", "Don’t under supervise — This can lead to miscommunications, lack of confidence in the chain of command, and the perception that you as the leader do not care about the team and/or the mission"),
  outlineItem("d.", "Don’t be afraid to delegate leadership, responsibility, and authority. This will make sure subordinates understand what goes into making decisions and have a better understanding of the end task. This also helps start building a better leader by challenging them to be successful."),
  outlineItem("e.", "Ensure that all tasks are understood, supervised, and accomplished. This can be done through clear and concise instructions. These instructions should be supervised, and then feedback provided to the subordinate about performance"),
  outlineItem("f.", "Practice what you preach. Subordinates should want to learn from a good leader, the same is true that a bad leader can instill bad habits in good people. Perform as if everyone knows each choice you make, and will be critical of all of your decisions."),
  ...note("VIDEO 6 — “5 SIGNS YOU ARE A MICRO MANAGER”", ["5:30 — https://www.youtube.com/watch?v=mehkUPN8u6E — Hans Fenzel"]),
);

content.push(pageBreak());

// ---- III. Review ----
content.push(
  romanBand("III.", "Review"),
  subHeading("Conclusion"),
  ...note("NOTE", ["Show Slide “Conclusion”"]),
  bodyPara("Today, we have discussed both effective and in-effective leadership styles. We have discussed traits that you can adopt to make you a better leader in the work place."),
  ...["Define Leadership", "List examples of Effective Leadership", "4 Components of Effective Leadership",
      "4 Ethics Qualities", "What is Motivational Leadership", "Basics of Supervising and Evaluating Work Performance"]
    .map((t) => new Paragraph({ numbering: { reference: "brand-bullets", level: 0 }, spacing: { after: 70, line: 250 }, children: [new TextRun({ text: t, font: F_BODY, size: 20, color: CHARCOAL })] })),
  ...note("NOTE", ["Show Slide “Questions”"]),
  bodyPara("At this time, are there any questions on what we have discussed today?"),

  romanBand("IV.", "Follow On Assignment"),
  ...note("NOTE", ["Show Slide “Follow on Reading Suggestions”"]),
  bodyPara("There are several good books that are recommended for follow on information:"),
  ...["Leadership and Training for the Fight – Paul Howe", "Extreme Ownership – Jocko Willink", "Can’t Hurt Me: Master Your Mind and Defy the Odds – David Goggins"]
    .map((t) => new Paragraph({ numbering: { reference: "brand-bullets", level: 0 }, spacing: { after: 70, line: 250 }, children: [new TextRun({ text: t, font: F_BODY, size: 20, color: CHARCOAL })] })),
  ...note("NOTE", ["Show Slide “Credits”"]),
  ...note("NOTE", ["Show Slide “Eric DeLaune Contact Information”"]),

  romanBand("V.", "Student Sign-In Sheet"),
  bodyPara("All students must complete the student sign-in sheet for EVERY period of instruction."),
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
  fs.writeFileSync(path.join(HERE, "valletta_supporting_information.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
