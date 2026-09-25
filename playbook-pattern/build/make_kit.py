#!/usr/bin/env python3
"""Build the AI Delegation Loop Starter Kit PDF (GIT BUILT lead magnet)."""
from fpdf import FPDF
import os

D = os.path.expanduser("~/workspace/your_files/git-built-carousel")
OUT = os.path.join(D, "AI-Delegation-Loop-Starter-Kit.pdf")

BG = (11, 11, 14)
WHITE = (245, 245, 247)
GRAY = (170, 170, 178)
GOLD = (255, 194, 26)
CARD = (20, 20, 26)

class Kit(FPDF):
    def page_bg(self):
        self.set_fill_color(*BG)
        self.rect(0, 0, 210, 297, "F")

    def brand_footer(self):
        self.set_y(-22)
        self.set_font("noto", "B", 8)
        self.set_text_color(*GOLD)
        self.cell(0, 5, "GIT BUILT  \u00b7  A SUBSIDIARY OF IMAGINARIUM", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("noto", "", 7)
        self.set_text_color(*GRAY)
        self.cell(0, 5, "BUILD IDEAS. BREAK LIMITS. MAKE IMPACT.", align="C")

    def kicker(self, text):
        self.set_font("noto", "B", 11)
        self.set_text_color(*GOLD)
        self.cell(0, 8, text.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*GOLD)
        self.set_line_width(1.2)
        self.line(10, self.get_y(), 34, self.get_y())
        self.ln(8)

    def headline(self, text, size=26):
        self.set_font("noto", "B", size)
        self.set_text_color(*WHITE)
        self.multi_cell(0, size * 0.5, text)
        self.ln(4)

    def body(self, text, size=11):
        self.set_font("noto", "", size)
        self.set_text_color(*GRAY)
        self.multi_cell(0, 6.5, text)
        self.ln(3)

    def prompt_box(self, title, text):
        self.set_font("noto", "B", 10)
        self.set_text_color(*GOLD)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(*CARD)
        self.set_draw_color(*GOLD)
        self.set_line_width(0.4)
        x, y = self.get_x(), self.get_y()
        self.set_font("notomono", "", 9)
        self.set_text_color(*WHITE)
        self.set_x(14)
        self.multi_cell(182, 5.5, text, border=1, fill=True)
        self.ln(5)

    def checklist(self, items):
        self.set_font("noto", "", 11)
        self.set_text_color(*GRAY)
        for it in items:
            self.cell(0, 8, f"  [ ]  {it}", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

pdf = Kit("P", "mm", "A4")
pdf.set_auto_page_break(True, margin=28)
pdf.set_margins(10, 14, 10)
pdf.add_font("noto", "", "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf", uni=True)
pdf.add_font("noto", "B", "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf", uni=True)
pdf.add_font("notoblack", "B", "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf", uni=True)
pdf.add_font("notomono", "", "/usr/share/fonts/truetype/noto/NotoSansMono-Regular.ttf", uni=True)

# COVER
pdf.add_page()
pdf.page_bg()
pdf.ln(38)
pdf.set_font("noto", "B", 13)
pdf.set_text_color(*GOLD)
pdf.cell(0, 8, "GIT BUILT  \u00b7  A SUBSIDIARY OF IMAGINARIUM", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(10)
pdf.set_font("noto", "B", 40)
pdf.set_text_color(*WHITE)
pdf.multi_cell(0, 17, "THE AI\nDELEGATION\nLOOP", align="C")
pdf.ln(8)
pdf.set_draw_color(*GOLD)
pdf.set_line_width(1.5)
pdf.line(85, pdf.get_y(), 125, pdf.get_y())
pdf.ln(8)
pdf.set_font("noto", "", 14)
pdf.set_text_color(*GRAY)
pdf.cell(0, 8, "Free Starter Kit", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(6)
pdf.set_font("noto", "", 11)
pdf.multi_cell(0, 6.5, "Stop building 15 half-broken agents.\nBuild ONE agent with a playbook \u2014 and get real work out of AI.", align="C")
pdf.brand_footer()

# THE IDEA
pdf.add_page()
pdf.page_bg()
pdf.kicker("The idea")
pdf.headline("One agent.\nOne playbook.\nReal output.")
pdf.body("Most people build a separate AI agent for every job \u2014 email, content, leads, reports, support \u2014 then try to wire them all together. The result: 15 half-built agents that work half the time and eat your week in maintenance.")
pdf.body("The people getting real leverage from AI do the opposite. They run ONE capable agent and hand it a playbook for every job. The playbook is just three files:")
pdf.set_font("noto", "B", 12)
pdf.set_text_color(*WHITE)
for n, t in [("01", "PROCESS \u2014 how YOU do the job"),
             ("02", "TOOLBOX \u2014 your approved prompts & templates"),
             ("03", "PROOF \u2014 the checklist it must pass before shipping")]:
    pdf.set_text_color(*GOLD)
    pdf.write(7, f"{n}  ")
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 8, t, new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)
pdf.body("This kit gives you all three \u2014 with copy-paste prompts to build each one today.")
pdf.brand_footer()

# FILE 01 - PROCESS
pdf.add_page()
pdf.page_bg()
pdf.kicker("File 01 \u2014 Process")
pdf.headline("Document how\nYOU do it.")
pdf.body("Don't write the SOP yourself. Make the AI interview YOU \u2014 it asks better questions than you'll think to answer. Paste this into ChatGPT or Claude:")
pdf.prompt_box("COPY-PASTE: THE INTERVIEW PROMPT",
"""Act as a world-class operations consultant. I want to document my process for [JOB] so an AI agent can execute it exactly the way I do.

Interview me ONE question at a time. Ask about:
- What triggers this job to start
- Every step, in order, with nothing skipped
- The tools and logins involved
- Decisions I make along the way, and how I make them
- What "done right" looks like
- The mistakes a beginner always makes

Keep asking until you can write the full process back to me as a numbered SOP. Ask your first question now.""")
pdf.body("Save the result as PROCESS-[job].md. That's file one. Do it for every job you want the agent to run.")
pdf.brand_footer()

# FILE 02 - TOOLBOX
pdf.add_page()
pdf.page_bg()
pdf.kicker("File 02 \u2014 Toolbox")
pdf.headline("Your approved\nweapons.")
pdf.body("Your agent is only as good as the raw material you feed it. The toolbox is a folder of everything already proven to work \u2014 linked from the playbook so the agent reaches for it every time.")
pdf.prompt_box("YOUR TOOLBOX FOLDER STRUCTURE",
"""TOOLBOX/
  voice-examples.md      <- 5-10 samples of YOUR writing
  hooks-that-worked.md   <- your best openers, with notes
  offer-one-pagers.md    <- what you sell, in plain words
  banned-list.md         <- words/phrases you never use
  templates/             <- your reusable formats""")
pdf.body("Rule: if the agent ever produces something off-brand, don't argue with the chat \u2014 add the correction to the toolbox. The toolbox compounds. The chat doesn't.")
pdf.brand_footer()

# FILE 03 - PROOF
pdf.add_page()
pdf.page_bg()
pdf.kicker("File 03 \u2014 Proof")
pdf.headline("Nothing ships\nunchecked.")
pdf.body("This is the file that separates toys from systems. Before your agent delivers anything, it must pass every item on the PROOF checklist. Example for content:")
pdf.checklist(["Hook lands in the first line",
               "One idea per post \u2014 no rambling",
               "Written in my voice (see voice-examples.md)",
               "CTA included and specific",
               "Zero words from banned-list.md",
               "Formatted for the platform it's posting to"])
pdf.prompt_box("COPY-PASTE: THE PROOF INSTRUCTION",
"""Before you show me any output, run it against PROOF.md line by line. For every item you fail, fix it and re-check. Only show me output that passes 100%. List which checklist version you passed.""")
pdf.brand_footer()

# THE RULE + CTA
pdf.add_page()
pdf.page_bg()
pdf.kicker("The rule")
pdf.headline("Fix the playbook.\nNot the chat.")
pdf.body("Every time your agent gets it wrong, resist the urge to re-prompt in the chat. Open the playbook instead: was the PROCESS unclear? Is the TOOLBOX missing an example? Is the PROOF checklist too weak? Fix the file, and every future run gets better forever.")
pdf.ln(4)
pdf.set_draw_color(*GOLD)
pdf.set_line_width(0.6)
y0 = pdf.get_y()
pdf.set_fill_color(*CARD)
pdf.rect(10, y0, 190, 52, "DF")
pdf.set_xy(16, y0 + 6)
pdf.set_font("noto", "B", 13)
pdf.set_text_color(*WHITE)
pdf.cell(0, 8, "Want this built for your business?", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(16)
pdf.set_font("noto", "", 11)
pdf.set_text_color(*GRAY)
pdf.multi_cell(178, 6.5, "GIT BUILT designs AI systems for operators.\nFollow @imaginarium2026 \u2014 new playbooks drop weekly.")
pdf.brand_footer()

pdf.output(OUT)
print("saved", OUT, os.path.getsize(OUT), "bytes")
