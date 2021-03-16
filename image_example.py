import numpy
from matplotlib import pyplot
from random import seed, randint

import cv2

from models.image import Image

def show_image(image_number="1"):
    if image_number == "1":
        rgb_image = Image(path="./images/example.jpg", title="Image Processing Class")
    elif image_number == "2":
        grayscale_image = Image(path="./images/example.jpg", title="Grayscale", cmap="gray")
    elif image_number == "3":
        dark_color = numpy.array([120, 68, 32])
        light_color = numpy.array([230, 164, 129])
        mask_image = Image(path="./images/example.jpg", title="Mask Image")
        mask_image.add_mask(dark_color, light_color)
        mask_image.apply_mask()
        mask_image.update_window()
        pyplot.show(block=False)
        pyplot.pause(2)
        mask_image.reset_mask()
        dark_color = numpy.array([25, 20, 14])
        light_color = numpy.array([135, 122, 96])
        mask_image.add_mask(dark_color, light_color)
        mask_image.apply_mask()
        mask_image.update_window()
        pyplot.pause(0) #a It's needed because of the block argument in pyplot.show(block=False)
    else:
        error_name = "ImageNumberNotFound"
        error_description = f"The image number {image_number} was not found. "
        error_description += "Please, choose a number between the following options: '1', '2' and '3'."
        raise NameError(error_name, error_description)

    pyplot.show()

if __name__ == '__main__':
    seed()
    number = randint(1, 3)
    show_image(image_number=str(number))

