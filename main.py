from PIL import Image, ImageDraw, ImageFont
import os

pictures = [file for file in os.listdir() if file.endswith(('jpeg', 'png', 'jpg'))]
for image in pictures:
    picture = Image.open(image)
    picture = picture.resize((1080, 1080))
    picture = picture.convert("1")
    w, h = picture.size

    draw = ImageDraw.Draw(picture)
    text = "Monkey D.Luffy"

    font = ImageFont.truetype('arial.ttf', 50)
    textw, texth = draw.textsize(text, font)

    margin = 5
    x = w - textw - margin
    y = h - texth - margin

    draw.text((x, y), text, font=font, fill="Orange")

    picture.save(image)
