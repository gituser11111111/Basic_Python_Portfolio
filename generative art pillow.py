import random
import uuid
from PIL import Image, ImageDraw
import os

def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name


run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

for i in range(10):
    directory_name = '' # enter in directory
    image = Image.new('RGB', (2000, 2000))
    width, height = image.size

    rectangle_width = 100
    rectangle_height = 100

    number_of_squares = random.randint(10, 550)

    draw_image = ImageDraw.Draw(image)
    for i in range(number_of_squares):
        rectangle_x = random.randint(0, width)
        rectangle_y = random.randint(0, height)

        rectangle_shape = [
            (rectangle_x, rectangle_y),
            (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
        draw_image.rectangle(
            rectangle_shape,
            fill=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        )
    image.save('') #enter in directory where you want this to be saved.
