'''
Creates random images based on range value.
'''

import random
import uuid

from PIL import Image, ImageDraw


def generate_random_image(width=128, height=128):
    rand_pixels = [random.randint(0, 255) for _ in range(width * height * 3)]
    rand_pixels_as_bytes = bytes(rand_pixels)
    text_and_filename = str(uuid.uuid4())

    random_image = Image.frombytes('RGB', (width, height), rand_pixels_as_bytes)

    draw_image = ImageDraw.Draw(random_image)
    draw_image.text(xy=(0, 0), text=text_and_filename, fill=(255, 255, 255))
    random_image.save(r"".format(file_name=text_and_filename)) #enter in directory in which you wnat to save randomly generated images. Put into .jpg or .jpeg format

# Generate 42 random images:
for _ in range(42):
    generate_random_image()
