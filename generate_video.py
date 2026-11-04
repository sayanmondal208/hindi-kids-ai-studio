
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

OUTPUT = "output"
os.makedirs(OUTPUT, exist_ok=True)

WIDTH, HEIGHT = 1280, 720
SCENES = [
    ("एक प्यारा खरगोश", "एक हरे-भरे जंगल में एक छोटा खरगोश रहता था।"),
    ("खरगोश की दोस्ती", "एक दिन उसे एक छोटा कछुआ मिला।"),
    ("मदद का वादा", "खरगोश ने अपने नए दोस्त की मदद करने का वादा किया।"),
    ("सच्ची दोस्ती", "दोनों ने मिलकर जंगल में खुशी से जीवन बिताया।"),
]

def make_scene(title, story, number):
    img = Image.new("RGB", (WIDTH, HEIGHT), (120, 190, 230))
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 430, WIDTH, HEIGHT), fill=(80, 165, 85))
    draw.ellipse((90, 80, 300, 290), fill=(40, 125, 65))
    draw.ellipse((900, 60, 1150, 300), fill=(40, 125, 65))

    # Cartoon rabbit
    draw.ellipse((510, 300, 750, 550), fill=(245, 235, 220))
    draw.ellipse((535, 180, 610, 360), fill=(245, 235, 220))
    draw.ellipse((650, 180, 725, 360), fill=(245, 235, 220))
    draw.ellipse((560, 380, 585, 405), fill=(20, 20, 20))
    draw.ellipse((675, 380, 700, 405), fill=(20, 20, 20))
    draw.ellipse((610, 420, 650, 450), fill=(240, 120, 140))

    draw.rectangle((0, 590, WIDTH, 720), fill=(255, 255, 255))
    draw.text((40, 610), title, fill=(20, 40, 80))
    draw.text((40, 660), story, fill=(30, 30, 30))

    img.save(f"{OUTPUT}/scene_{number}.png")

for i, (title, story) in enumerate(SCENES):
    make_scene(title, story, i)

with open(f"{OUTPUT}/story.txt", "w", encoding="utf-8") as f:
    for title, story in SCENES:
        f.write(title + "\n" + story + "\n\n")

print("Cartoon scenes created successfully!")
print("Next step: create an MP4 video using FFmpeg.")
