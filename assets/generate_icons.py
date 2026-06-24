#!/usr/bin/env python3
"""One-off helper: render the "YM" brand mark to PNG/ICO icons.

Matches the inline SVG favicon: rounded-rect #2E5AE6 with white bold "YM".
Run from the repo root: python3 assets/generate_icons.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

BLUE = (46, 90, 230, 255)
WHITE = (255, 255, 255, 255)

FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/SFNS.ttf",
    "/Library/Fonts/Arial Bold.ttf",
]


def load_font(size):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def render(size):
    # Supersample 4x for crisp anti-aliasing, then downscale.
    scale = 4
    s = size * scale
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    radius = int(s * (10 / 38))  # same corner ratio as the SVG (rx=10 on 38)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=radius, fill=BLUE)

    font = load_font(int(s * 0.42))
    text = "YM"
    box = d.textbbox((0, 0), text, font=font)
    tw, th = box[2] - box[0], box[3] - box[1]
    pos = ((s - tw) / 2 - box[0], (s - th) / 2 - box[1])
    d.text(pos, text, font=font, fill=WHITE)

    return img.resize((size, size), Image.LANCZOS)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)

    render(180).save(os.path.join(here, "apple-touch-icon.png"))
    render(192).save(os.path.join(here, "icon-192.png"))
    render(512).save(os.path.join(here, "icon-512.png"))

    # Multi-size favicon.ico at repo root
    render(256).save(
        os.path.join(root, "favicon.ico"),
        sizes=[(16, 16), (32, 32), (48, 48)],
    )
    print("Icons generated.")


if __name__ == "__main__":
    main()
