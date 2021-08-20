"""Module is responsible for generating memes."""
from PIL import Image, ImageDraw, ImageFont
import os
import random
from random import randint


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        """os.makedirs() method in Python is \
        used to create a directory recursively. \
         That means while making leaf\
        directory if any intermediate-level directory\
        is missing, os.makedirs() \
        method will create them all."""

    def make_meme(self, img_path, quote, author, width=500) -> str:
        """This function functionality is to generate memes using width,ratio,\
        height and ImageDraw as well as ImageFont."""
        image = Image.open(img_path)
        w, h = image.size
        width = max(500, width)
        ratio = width / w
        height = int(ratio * h)
        image = image.resize((width, height), Image.NEAREST)
        ImageDraw.Draw(image).text((randint(0, len(quote) + len(author)), randint(0, len(quote) + len(author))), f'{quote}{author}', font=ImageFont.truetype('LilitaOne-Regular.ttf', size=20), fill='white')

        final_memeoutput_dir = r'{}/{}.png' .format(self.output_dir, random.randint(0, 10000))
        image.save(final_memeoutput_dir)
        return final_memeoutput_dir
