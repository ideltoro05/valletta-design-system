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

const IND = [0, 260, 620, 980]; // twips per outline level 0..3

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

function outlineItem(label, text, level = 1, bold = false) {
  const runs = [];
  if (label) runs.push(new TextRun({ text: label + " ", font: F_BODY, bold: true, size: 21, color: RED }));
  if (bold) {
    runs.push(new TextRun({ text, font: F_BODY, size: 21, bold: true, color: BLACK }));
  } else {
    runs.push(...parseInline(text));
  }
  return new Paragraph({
    indent: { left: IND[level] },
    spacing: { after: 90, line: 260 },
    children: runs,
  });
}

function plainBullet(text) {
  return new Paragraph({
    numbering: { reference: "brand-bullets", level: 0 },
    spacing: { after: 90, line: 260 },
    children: [new TextRun({ text, font: F_BODY, size: 21, color: CHARCOAL })],
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

function secTitle(letter, title) {
  return new Paragraph({
    spacing: { before: 300, after: 140 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 10 } },
    children: [new TextRun({ text: `${letter}.  ${title.toUpperCase()}`, font: F_HEAD, bold: true, size: 27, color: BLACK })],
  });
}

function plainTitle(title) {
  return new Paragraph({
    spacing: { before: 300, after: 140 },
    border: { bottom: { color: RED, space: 4, style: BorderStyle.SINGLE, size: 10 } },
    children: [new TextRun({ text: title.toUpperCase(), font: F_HEAD, bold: true, size: 27, color: BLACK })],
  });
}

function overviewBlock(items) {
  const banner = new Paragraph({
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BLACK },
    spacing: { after: 0 },
    children: [new TextRun({ text: "OVERVIEW", font: F_HEAD, bold: true, size: 24, color: WHITE })],
  });
  const rows = items.map(([letter, t], i) => new Paragraph({
    indent: { left: 200 },
    border: i === items.length - 1
      ? { bottom: { color: LINE_GRAY, space: 6, style: BorderStyle.SINGLE, size: 4 }, left: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 }, right: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } }
      : { left: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 }, right: { color: LINE_GRAY, space: 8, style: BorderStyle.SINGLE, size: 4 } },
    spacing: { before: 90, after: 90 },
    children: [
      new TextRun({ text: `${letter}. `, font: F_BODY, bold: true, size: 21, color: RED }),
      new TextRun({ text: t, font: F_BODY, size: 21, color: CHARCOAL }),
    ],
  }));
  return [banner, ...rows, new Paragraph({ spacing: { after: 160 }, children: [] })];
}

function bulletPara(children) {
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
        new TextRun({ text: "LEADERSHIP TRAINING STUDENT HANDOUT", font: F_LABEL, bold: true, size: 15, color: STEEL, characterSpacing: 10 }),
      ],
    })],
  });
}
function makeFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Valletta Industries  |  Leadership Training Student Handout  –  Page ", font: F_BODY, size: 15, color: STEEL }),
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

content.push(
  new Paragraph({ spacing: { before: 2600 }, alignment: AlignmentType.CENTER,
    children: [new ImageRun({ type: "png", data: img("valletta-mark-white.png"), transformation: { width: 300, height: 60 } })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500 },
    children: [new TextRun({ text: "LEADERSHIP TRAINING", font: F_HEAD, bold: true, size: 52, color: WHITE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
    children: [new TextRun({ text: "STUDENT HANDOUT", font: F_HEAD, bold: true, size: 52, color: WHITE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500 },
    children: [new TextRun({ text: "“If your actions inspire others to dream more, learn more, do more and become more, then you are a leader.”", font: F_BODY, italics: true, size: 22, color: "D8D9DB" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 },
    children: [new TextRun({ text: "– John Quincy Adams.", font: F_BODY, bold: true, size: 20, color: RED })] }),
  pageBreak(),
);

content.push(...overviewBlock([
  ["A", "Define Leadership"],
  ["B", "Examples of Effective Leadership"],
  ["C", "Describe components of being an effective leader."],
  ["D", "Ethical Characteristics for Leadership"],
  ["E", "Describe what motivational leadership is"],
  ["F", "Understand the basics of supervision and evaluating work performance."],
]));

content.push(
  secTitle("A", "Defining Leadership"),
  outlineItem("a.", "Definition – The ability to influence others to accomplish a task by providing a purpose, a direction, and appropriate motivation.", 1),
  outlineItem("b.", "Being a supervisor doesn’t make you a leader", 1),
  outlineItem("c.", "Lead by Example", 1),
  outlineItem("d.", "Strive to be the best", 1),
  outlineItem("e.", "Make those around you better", 1),
  outlineItem("f.", "Make sound and timely decisions.", 1),

  secTitle("B", "Examples of Effective Leadership"),
  plainBullet("Charismatic Leader"),
  plainBullet("Transformational Leader"),
  plainBullet("Servant Leader"),
  plainBullet("Quiet Leaders"),

  secTitle("C", "Describe the Components of Effective Leadership"),
  outlineItem("", "Leadership Traits", 1, true),
  outlineItem("1.", "A good leader encourages their people", 2),
  outlineItem("2.", "A good leader knows the position above and below them", 2),
  outlineItem("3.", "A good leader is honest about their capabilities", 2),
  outlineItem("4.", "A good leader treats all team members with dignity and respect", 2),
  outlineItem("5.", "A good leader must possess professional character traits such as", 2),
  outlineItem("a.", "ambition", 3), outlineItem("b.", "creativity", 3), outlineItem("c.", "compassion", 3),
  outlineItem("d.", "courage", 3), outlineItem("e.", "flexibility", 3), outlineItem("f.", "honesty (integrity)", 3),
  outlineItem("g.", "humility", 3), outlineItem("h.", "loyalty", 3), outlineItem("i.", "patience", 3),
  outlineItem("j.", "discipline", 3), outlineItem("k.", "curiosity", 3),
  outlineItem("6.", "A good leader understands how to manage stress", 2),
  outlineItem("a.", "Exercise", 3), outlineItem("b.", "Meditation", 3),
  outlineItem("c.", "Discussing with peers, friends, or professional therapy", 3),
  outlineItem("d.", "Eat healthy", 3), outlineItem("e.", "Regular Breaks", 3), outlineItem("f.", "Breathing Drills", 3),
);

content.push(pageBreak());

content.push(
  outlineItem("", "Communication", 1, true),
  outlineItem("1.", "Understand your people and what they need", 2),
  outlineItem("2.", "You must be able to listen", 2),
  outlineItem("3.", "Be honest about your performance and your team’s performance", 2),
  outlineItem("4.", "Ask questions like “tell me more” or “explain what you mean”", 2),
  outlineItem("5.", "Communication with body language", 2),
  outlineItem("6.", "Seek feedback from your team", 2),

  outlineItem("", "Observing Effective Follower Traits (Knowing your People)", 1, true),
  quoteBlock(
    "Why would you want to be someone called a follower? A simple answer is people follow because they derive " +
    "benefits. The psychological payback of following exceeds the psychological cost of following. Throughout our " +
    "human history, most humans were in small, nomadic clusters. These tribes offered protection, food, and " +
    "survival. The groups with the best leader and followers had a higher probability of survival than those " +
    "poorly led that consisted of poor followers. The physical benefits for followers outweighed the psychological " +
    "costs and so most likely they stayed connected to the tribe. If some followers were dissatisfied with the " +
    "leader’s goals and agenda, they had a choice of either fighting for the top position, or leaving to join " +
    "other groups.",
    "(Project Management Institute 2021)", "The Psychology of Followers"
  ),
  outlineItem("1.", "Followers are an essential", 2),
  outlineItem("2.", "Types of followers", 2),
  outlineItem("a.", "Passive/sheep", 3), outlineItem("b.", "Conformist/Yes People", 3),
  outlineItem("c.", "Alienated", 3), outlineItem("d.", "Effective", 3),
  outlineItem("3.", "A follower has good judgment", 2),
  outlineItem("4.", "Good followers are good workers", 2),
  outlineItem("5.", "To be effective, followers must be willing to share their ideas and opinions with leaders.", 2),

  outlineItem("", "Understanding the Mission or Task", 1, true),
  outlineItem("1.", "Identify the mission", 2),
  outlineItem("2.", "Have a shared vision to accomplish a task", 2),
  outlineItem("3.", "Regularly create team tasks", 2),

  secTitle("D", "Ethical Characteristics for Leadership"),
  outlineItem("", "<strong>Fair</strong> – An ethical leader is fair, and they treat everyone on their team equally with no bias.", 1),
  outlineItem("", "<strong>Honest</strong> – Ethical leaders are honest and must always be transparent and fair.", 1),
  outlineItem("", "<strong>Respect</strong> – Listening to subordinate and valuing opinions of the team.", 1),
  outlineItem("", "<strong>Value-Oriented</strong> – A good leader will make decisions based on the organization's values, and the values of the mission.", 1),
  outlineItem("", "<strong>Leads by Example</strong> – Employees will mimic the action of their leader.", 1),
  outlineItem("", "<strong>Makes the team a priority</strong> – Ethical leaders will promote team building and foster a sense of community.", 1),
  quoteBlock(
    "When setting expectations, no matter what has been said or written, if substandard performance is accepted " +
    "and no one is held accountable if there are no consequences, then poor or substandard performance becomes " +
    "the new standard. Therefore, leaders must enforce standards.",
    "Jocko Willink.", "Expectations"
  ),
);

content.push(pageBreak());

content.push(
  secTitle("E", "Describe What Motivational Leadership Is"),
  quoteBlock("The only thing more contagious than a good attitude is a bad one.", "David Goggins."),
  outlineItem("", "A motivational leader can make decisions and set clear goals for their teams.", 1),
  outlineItem("", "What is the difference between Motivation and Inspiration?", 1),
  outlineItem("", "Inspiration is an external influence or pulling force that compels you to achieve something.", 2),
  outlineItem("", "Motivation is an internal influence or a driving force that you feel on the inside to achieve something.", 2),
  outlineItem("", "A good leader should try to inspire those around them.", 1),
  outlineItem("", "An effective leader will make logical decisions based on the immediate information available. If the decision was wrong, explain the rationale behind it or what led you to the conclusion and learn from it.", 1),
  outlineItem("–", "<strong>OODA loop:</strong> Observe, Orient, Decide, and Act.", 2),
  outlineItem("", "Know the strengths and weaknesses of subordinates and look out for their wellbeing.", 1),
  quoteBlock(
    "A leader must lead, but also be ready to follow. They must be aggressive, but not overbearing. A leader " +
    "must be calm, but not robotic. They must be confident, but never cocky. A leader must be brave, but not " +
    "foolhardy. They must have a competitive spirit, but be a gracious loser.",
    "Jocko Willink"
  ),

  secTitle("F", "Understand the Basics of Supervision and Evaluating Work Performance"),
  outlineItem("", "An effective leader does not Micro-Manage.", 1),
  outlineItem("", "An effective leader is proactive and should avoid having a “hands-off” mentality.", 1),
  outlineItem("", "A leader will delegate supervision, responsibility, and authority to capable subordinates.", 1),
  outlineItem("", "A leader should ensure that all tasks are understood, supervised, and accomplished.", 1),
  outlineItem("", "A good supervisor can perform the tasks of his subordinates", 1),
  outlineItem("", "A good leader will hold their team accountable with honest feedback on performance from each assigned task.", 1),

  plainTitle("Additional Reading"),
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "Several good books are recommended for follow on information:", font: F_BODY, size: 21, color: CHARCOAL })] }),
  bulletPara([new TextRun({ text: "12 Rules for Life – Jordan B. Peterson", font: F_BODY, size: 21, color: CHARCOAL })]),
  bulletPara([new TextRun({ text: "Leaders eat last – Simon Sinek", font: F_BODY, size: 21, color: CHARCOAL })]),
  bulletPara([new TextRun({ text: "Leadership and Training for the Fight - Paul Howe", font: F_BODY, size: 21, color: CHARCOAL })]),
  bulletPara([new TextRun({ text: "Extreme Ownership – Jocko Willink", font: F_BODY, size: 21, color: CHARCOAL })]),
  bulletPara([new TextRun({ text: "Can’t Hurt Me: Master Your Mind and Defy the Odds – David Goggins", font: F_BODY, size: 21, color: CHARCOAL })]),
  bulletPara([linkRun("https://www.johnmaxwell.com/my-purpose/")]),
  bulletPara([linkRun("https://echelonfront.com/jocko-willink/")]),
  bulletPara([linkRun("https://www.travismills.org/")]),
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
  fs.writeFileSync(path.join(HERE, "valletta_student_handout_v3.docx"), buf);
  console.log("docx written", buf.length, "bytes");
});
