from PIL import Image, ImageOps, ImageDraw, ImageFont
from pathlib import Path
import random

# Save current dir
currentFilePath = Path(__file__).parents[0]
outputDir = Path(__file__).parents[1] / 'data'

# Save text
text1 = 'what is the name of this item?'
text2 = 'Ignore the random lines lol'

img_name = 'epic_guard.png'

class_names = [
    "apple",
    "banana",
    "chip",
    "coin",
    "dragon scale",
    "epic coin",
    "epic fish",
    "fish",
    "golden fish",
    "life potion",
    "mermaid hair",
    "ruby",
    "unicorn horn",
    "wolf skin",
    "zombie eye"
]

font = 'arial.ttf'

background = Image.open(currentFilePath / 'assets' / 'background.png')
foreground = Image.open(currentFilePath / 'assets' / 'dragon scale.png')


def save(i, type):
    numstr = str(i).zfill(4)

    item = type

    # Create new image and paste background
    background = Image.new('RGBA', (700, 200), '#81b29a')
    img = Image.open(currentFilePath / 'assets' /
                     'background.png').convert("RGBA")
    background.paste(img, (0, 0), img)
    img = background

    # Open asset image
    img = Image.open(currentFilePath / 'assets' /
                     f'{item}.png')

    # Randomly resize asset
    width, height = img.size
    random_multipler = random.random() * 1.5 + random.randrange(1, 3)
    img = img.resize((round(width * random_multipler),
                     round(height * random_multipler)))
    width, height = img.size

    # Random greyscale
    if random.random() <= 0.5:
        img = img.convert("LA").convert("RGBA")
    else:
        img = img.convert("RGBA")

    # Random coords of image
    img_paste_coords = (random.randrange(50, 85), random.randrange(45, 80))
    background.paste(
        img,
        img_paste_coords,
        img)
    img = background

    # New Overlay
    new_img = Image.new('RGBA', (700, 200), (255, 255, 255))
    new_img.paste(img, (0, 0, 700, 200), img)
    img = new_img

    # Load font
    font_size = random.randrange(30, 38)
    font = ImageFont.truetype("arial.ttf", size=font_size)

    # Set up
    draw = ImageDraw.Draw(img)

    # Set random text coordinates
    text_coords = (
        img_paste_coords[0] + width + random.randrange(20, 50),
        img_paste_coords[1] + random.randrange(5, 20)
    )

    # Random lines
    if random.random() <= 0.5:
        for i in range(random.randrange(1, 4)):
            draw.line(
                generate_lines(
                    img_paste_coords[0], width, img_paste_coords[1], height),
                fill=(random.randrange(0, 256),
                      random.randrange(0, 256),
                      random.randrange(0, 256)),
                width=random.randrange(4, 7))
        # Draw text if lines were drawn
        draw.text(
            (text_coords[0], text_coords[1] + font_size),
            text2,
            font=font,
            align="left",
            fill=(256, 256, 256)
        )

    draw.text(
        text_coords,
        text1,
        font=font,
        align="left",
        fill=(256, 256, 256)
    )

    img.save(outputDir / f'{item}' / f'{numstr}.png')


def generate_lines(img_x, img_width, img_y, img_height):
    x1 = img_x
    y1 = random.randrange(img_y, img_y + img_height)
    x2 = random.randrange(img_x + round(img_width / 2), img_x + img_width)
    y2 = random.randrange(img_y, img_y + img_height)
    return [(x1, y1), (x2, y2)]


if __name__ == '__main__':
    Path(currentFilePath / 'outs').mkdir(parents=True, exist_ok=True)
    for name in class_names:
        Path(outputDir / f'{name}').mkdir(parents=True, exist_ok=True)
        for i in range(750):
            print(i)
            save(i, name)
