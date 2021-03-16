import numpy
from matplotlib import pyplot
from random import seed, randint

import cv2

from models.image import Image

def show_video():
    '''
    #video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #a This is used to capture the webcam video
    video = cv2.VideoCapture('./videos/example.avi')

    rgb_image = Image(title="Original Video")
    mask_image = Image(title="Mask Video")
    running = True
    while running:
        running, frame = video.read()
        rgb_image.set_frame(frame)

        light_color = numpy.array([120, 68, 32])
        dark_color = numpy.array([230, 164, 129])
        mask_image.set_frame(frame)
        mask_image.add_mask(light_color, dark_color)
        mask_image.apply_mask()
        mask_image.update_window()

        pyplot.pause(1)
        pyplot.show(block=False)
    '''
    pass

if __name__ == '__main__':
    show_video()