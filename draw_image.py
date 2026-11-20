#!/usr/bin/env python3
"""Render one 1024x1024 front page: THE WORLD TODAY, 19 November 2026.

Layout (my own): cream paper, serif masthead with a double rule, a
full-width lead story, then a two-column grid of the remaining five
stories. Every story is a dict; a tiny block-flow engine lays the
blocks out column by column.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

PAGE = 1024
MARGIN = 48
CONTENT_W = PAGE - 2 * MARGIN

PAPER = (248, 244, 234)
INK = (26, 26, 24)
ACCENT = (155, 34, 38)
MUTED = (90, 90, 82)
RULE = (26, 26, 24)
FAINT = (180, 175, 162)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def spaced(text, gap):
    """Letterspace a caps line by hand (Pillow has no tracking)."""
    return (" " * gap).join(list(text))


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


STORIES = [
    {
        "kicker": "World Court",
        "head": "ICJ: Myanmar committed genocide against the Rohingya",
        "sub": "9-6 ruling, first against a state; reparations ordered",
        "lead": True,
    },
    {
        "kicker": "Summit",
        "head": "Trump, Xi & Putin meet in Shenzhen",
        "sub": "First three-way summit; joint peace declaration",
    },
    {
        "kicker": "Markets",
        "head": "Anthropic debuts on Nasdaq after the largest IPO in history",
        "sub": "$81bn raised; shares priced $83",
    },
    {
        "kicker": "Middle East",
        "head": "Houthi attacks damage Riyadh's tallest tower",
        "sub": "Strikes hit the capital's tallest tower",
    },
    {
        "kicker": "Economy",
        "head": "IMF: world debt soon to hit 100% of GDP",
        "sub": "Highest since WWII, fund warns",
    },
    {
        "kicker": "South Asia",
        "head": "Bangladesh hit by violence amid protests",
        "sub": "Unrest as exiled ex-leader's party protests",
    },
]


def draw_masthead(draw):
    title = font(SERIF_BOLD, 62)
    draw.text((PAGE // 2, 44), "THE WORLD TODAY", font=title,
              fill=INK, anchor="ma")
    draw.line([(MARGIN, 128), (PAGE - MARGIN, 128)], fill=RULE, width=3)
    draw.line([(MARGIN, 134), (PAGE - MARGIN, 134)], fill=RULE, width=1)
    date_font = font(SANS_BOLD, 19)
    draw.text((PAGE // 2, 146), spaced("THURSDAY · 19 NOVEMBER 2026", 1),
              font=date_font, fill=ACCENT, anchor="ma")


def draw_story(draw, story, x, y, width, head_size, sub_size, lead=False):
    """Draw one story block at (x, y); return the y just below it."""
    kicker_f = font(SANS_BOLD, 15 if not lead else 17)
    draw.text((x, y), story["kicker"].upper(), font=kicker_f, fill=ACCENT)
    y += 24 if not lead else 28

    head_f = font(SERIF_BOLD, head_size)
    line_h = int(head_size * 1.28)
    for line in wrap(draw, story["head"], head_f, width):
        draw.text((x, y), line, font=head_f, fill=INK)
        y += line_h
    y += 6

    sub_f = font(SANS, sub_size)
    sub_h = int(sub_size * 1.35)
    for line in wrap(draw, story["sub"], sub_f, width):
        draw.text((x, y), line, font=sub_f, fill=MUTED)
        y += sub_h
    return y


def draw_footer(draw):
    draw.line([(MARGIN, 968), (PAGE - MARGIN, 968)], fill=FAINT, width=1)
    foot = font(SANS, 15)
    draw.text((PAGE // 2, 978), "SIX STORIES · COMPILED 19 NOVEMBER 2026",
              font=foot, fill=MUTED, anchor="ma")


def build():
    img = Image.new("RGB", (PAGE, PAGE), PAPER)
    draw = ImageDraw.Draw(img)

    draw_masthead(draw)

    lead = STORIES[0]
    y = draw_story(draw, lead, MARGIN, 178, CONTENT_W, 40, 20, lead=True)
    draw.line([(MARGIN, y + 16), (PAGE - MARGIN, y + 16)], fill=RULE, width=2)

    grid_top = y + 34
    col_w = (CONTENT_W - 32) // 2
    left_x = MARGIN
    right_x = MARGIN + col_w + 32
    # vertical divider between the two columns
    draw.line([(PAGE // 2, grid_top), (PAGE // 2, 950)], fill=FAINT, width=1)

    rest = STORIES[1:]
    left_col = rest[:3]
    right_col = rest[3:]

    cursor = grid_top
    for i, story in enumerate(left_col):
        cursor = draw_story(draw, story, left_x, cursor, col_w, 28, 18)
        if i < len(left_col) - 1:
            draw.line([(left_x, cursor + 14), (left_x + col_w, cursor + 14)],
                      fill=FAINT, width=1)
            cursor += 40

    cursor = grid_top
    for i, story in enumerate(right_col):
        cursor = draw_story(draw, story, right_x, cursor, col_w, 28, 18)
        if i < len(right_col) - 1:
            draw.line([(right_x, cursor + 14), (right_x + col_w, cursor + 14)],
                      fill=FAINT, width=1)
            cursor += 40

    draw_footer(draw)
    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG")
    print("saved", out, img.size)


if __name__ == "__main__":
    build()
