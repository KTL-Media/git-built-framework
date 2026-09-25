#!/usr/bin/env python3
"""GIT BUILT carousel v2: illustrated frame background + crisp text overlay."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1350
WHITE = (245, 245, 247)
GRAY = (185, 185, 192)
GOLD = (255, 194, 26)
DIM = (120, 120, 128)

BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

D = os.path.expanduser("~/workspace/your_files/git-built-carousel")
BG = Image.open(os.path.join(D, "media-generation-gitbuilt-carousel-bg-0-09578af2-2f57-404e-86a9-5c50b1cb9fb6.png")).convert("RGB")
# cover-fit to 1080x1350
scale = max(W / BG.width, H / BG.height)
bg = BG.resize((int(BG.width * scale) + 1, int(BG.height * scale) + 1), Image.LANCZOS)
x0 = (bg.width - W) // 2
y0 = (bg.height - H) // 2
bg = bg.crop((x0, y0, x0 + W, y0 + H))

def font(path, size):
    return ImageFont.truetype(path, size)

def tracked(d, xy, text, fnt, fill, tracking=6):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += d.textlength(ch, font=fnt) + tracking

SLIDES = [
    ("GIT BUILT", ["STOP BUILDING", "AI AGENTS."], "The most controversial thing I'll say\nabout AI all year."),
    ("THE PAIN", ["15 half-built", "agents."], "Working half the time.\nBreaking the other half."),
    ("THE PROBLEM", ["Wire them all", "together?"], "They told you to build a separate agent\nfor everything \u2014 then connect them all.\nNo wonder AI feels stupid."),
    ("THE TURN", ["The smartest", "people do the", "exact opposite."], None),
    ("THE SOLUTION", ["Build ONE", "agent."], "Give it a playbook for every job:\nemail, content, leads, reports, support."),
    ("THE AI DELEGATION LOOP", ["3 files.", "That's the system."], "PROCESS \u00b7 TOOLBOX \u00b7 PROOF"),
    ("01 \u2014 PROCESS", ["Document how", "YOU do it."], "Have ChatGPT or Claude interview you\nabout the job \u2014 then save every step."),
    ("02 \u2014 TOOLBOX", ["Your approved", "weapons."], "Scripts, templates, prompts \u2014\nlinked straight to the playbook."),
    ("03 \u2014 PROOF", ["Nothing ships", "unchecked."], "Write a checklist your agent must pass\nBEFORE it delivers anything."),
    ("THE RULE", ["Fix the playbook.", "Not the chat."], "Comment PLAYBOOK and I'll send you\nthe free starter kit."),
]

CX = W // 2
for i, (kicker, head, body) in enumerate(SLIDES, 1):
    img = bg.copy()
    d = ImageDraw.Draw(img)

    # slide number, top-right of dark zone
    fn = font(BOLD, 32)
    num = f"{i:02d} / 10"
    d.text((W - 70 - d.textlength(num, font=fn), 560), num, font=fn, fill=GOLD)

    y = 640
    fk = font(BOLD, 38)
    kw = sum(d.textlength(c, font=fk) + 5 for c in kicker) - 5
    tracked(d, (CX - kw / 2, y), kicker, fk, GOLD, tracking=5)
    y += 72
    d.rectangle([CX - 60, y, CX + 60, y + 7], fill=GOLD)
    y += 56

    for line in head:
        f, size = font(BLACK, 116), 116
        while d.textlength(line, font=f) > W - 170 and size > 56:
            size -= 6
            f = font(BLACK, size)
        lw = d.textlength(line, font=f)
        d.text((CX - lw / 2, y), line, font=f, fill=WHITE,
               stroke_width=2, stroke_fill=(0, 0, 0))
        y += int(size * 1.18)
    y += 44

    if body:
        fbd = font(REG, 42)
        for line in body.split("\n"):
            lw = d.textlength(line, font=fbd)
            d.text((CX - lw / 2, y), line, font=fbd, fill=GRAY,
                   stroke_width=1, stroke_fill=(0, 0, 0))
            y += 62

    # footer brand
    ff = font(BOLD, 26)
    f1 = "GIT BUILT \u00b7 A SUBSIDIARY OF IMAGINARIUM"
    w1 = d.textlength(f1, font=ff)
    d.text((CX - w1 / 2, H - 150), f1, font=ff, fill=WHITE,
           stroke_width=1, stroke_fill=(0, 0, 0))
    ff2 = font(REG, 22)
    f2 = "BUILD IDEAS. BREAK LIMITS. MAKE IMPACT."
    w2 = sum(d.textlength(c, font=ff2) + 3 for c in f2)
    tracked(d, (CX - w2 / 2, H - 110), f2, ff2, GOLD, tracking=3)

    img.save(os.path.join(D, f"gb-slide-{i:02d}.png"))
    print("saved", i)
print("done")
