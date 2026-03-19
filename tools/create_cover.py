#!/usr/bin/env python3
"""
Generate a KDP ebook cover for 'Partner, Don't Police'.

Output: cover.png (1600 x 2560 px, KDP ebook standard portrait)
"""

import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Dimensions — KDP ebook cover: 1600 x 2560 (portrait, 1:1.6 ratio)
WIDTH = 1600
HEIGHT = 2560

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMIC_PATH = PROJECT_ROOT / "images" / "cover-comic.png"
OUTPUT_PATH = PROJECT_ROOT / "cover.png"

# Colours
BG_COLOUR = (255, 255, 255)
TITLE_COLOUR = (20, 20, 20)
SUBTITLE_COLOUR = (80, 80, 80)
AUTHOR_COLOUR = (100, 100, 100)


def get_font(size, bold=False):
    """Try to load a clean system font, fall back to default."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    bold_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    paths = bold_paths if bold else font_paths
    for path in paths:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size, index=1 if bold and path.endswith(".ttc") else 0)
            except (OSError, IndexError):
                try:
                    return ImageFont.truetype(path, size)
                except OSError:
                    continue
    return ImageFont.load_default()


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def main():
    # Create canvas
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOUR)
    draw = ImageDraw.Draw(img)

    # Fonts
    title_font = get_font(100, bold=True)
    subtitle_font = get_font(48)
    author_font = get_font(48)

    # Title — split across two lines
    line1 = "Partner,"
    line2 = "Don't Police"
    l1x = (WIDTH - text_width(draw, line1, title_font)) // 2
    l2x = (WIDTH - text_width(draw, line2, title_font)) // 2
    draw.text((l1x, 280), line1, fill=TITLE_COLOUR, font=title_font)
    draw.text((l2x, 410), line2, fill=TITLE_COLOUR, font=title_font)

    # Subtitle
    subtitle = "AI in the Business Classroom"
    sx = (WIDTH - text_width(draw, subtitle, subtitle_font)) // 2
    draw.text((sx, 570), subtitle, fill=SUBTITLE_COLOUR, font=subtitle_font)

    # Comic strip
    comic = Image.open(COMIC_PATH)
    if comic.mode == "RGBA":
        bg = Image.new("RGB", comic.size, BG_COLOUR)
        bg.paste(comic, mask=comic.split()[3])
        comic = bg

    # Scale comic to fit width with padding
    top_margin = 650
    bottom_margin = 250
    max_comic_width = WIDTH - 200
    max_comic_height = HEIGHT - top_margin - bottom_margin
    ratio = min(max_comic_width / comic.width, max_comic_height / comic.height)
    new_size = (int(comic.width * ratio), int(comic.height * ratio))
    comic = comic.resize(new_size, Image.LANCZOS)

    # Centre comic, shifted up
    comic_x = (WIDTH - comic.width) // 2
    comic_y = top_margin + (max_comic_height - comic.height) // 3  # bias upward
    img.paste(comic, (comic_x, comic_y))

    # Draw rough pencil-style border around the comic panel
    border_pad = 20
    bx1 = comic_x - border_pad
    by1 = comic_y - border_pad
    bx2 = comic_x + comic.width + border_pad
    by2 = comic_y + comic.height + border_pad

    random.seed(42)  # reproducible wobble
    border_colour = (35, 35, 35)

    # Overshoot: some lines extend past the corner
    # (start_overshoot, end_overshoot) in pixels — 0 means clean corner
    overshoots = {
        "top": (-12, 18),     # extends past top-left, overshoots top-right
        "bottom": (8, -6),    # overshoots bottom-left, short on bottom-right
        "left": (15, 0),      # overshoots past top-left corner
        "right": (0, 10),     # clean top, overshoots past bottom-right
    }

    for side in ["top", "bottom", "left", "right"]:
        points = []
        steps = 60
        os_start, os_end = overshoots[side]
        for i in range(steps + 1):
            t = i / steps
            wobble = random.uniform(-4, 4)
            # Add slight drift so lines aren't perfectly parallel
            drift = (t - 0.5) * random.uniform(-3, 3)
            if side == "top":
                x = (bx1 - os_start) + t * ((bx2 + os_end) - (bx1 - os_start))
                points.append((x + wobble, by1 + wobble + drift))
            elif side == "bottom":
                x = (bx1 - os_start) + t * ((bx2 + os_end) - (bx1 - os_start))
                points.append((x + wobble, by2 + wobble + drift))
            elif side == "left":
                y = (by1 - os_start) + t * ((by2 + os_end) - (by1 - os_start))
                points.append((bx1 + wobble + drift, y + wobble))
            elif side == "right":
                y = (by1 - os_start) + t * ((by2 + os_end) - (by1 - os_start))
                points.append((bx2 + wobble + drift, y + wobble))
        draw.line(points, fill=border_colour, width=5)

    # Author
    author = "Michael Borck"
    ax = (WIDTH - text_width(draw, author, author_font)) // 2
    draw.text((ax, HEIGHT - 120), author, fill=AUTHOR_COLOUR, font=author_font)

    # Save
    img.save(OUTPUT_PATH, "PNG", dpi=(300, 300))
    print(f"Cover saved to: {OUTPUT_PATH}")
    print(f"Dimensions: {WIDTH} x {HEIGHT} px")


if __name__ == "__main__":
    main()
