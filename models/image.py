import sys
import numpy
from matplotlib import pyplot

import cv2

index = 0

def window_index():
    global index
    index += 1
    return index

def key_press_event(event):
    sys.stdout.flush()
    if event.key == 'q':
        print("Closing all windows...")
        pyplot.close(fig='all')
        print("Exiting...")
        sys.exit(0)
    elif event.key == 'x':
        figure = pyplot.gcf()
        title = figure.canvas.get_window_title()
        print(f"Closing '{title}' window...")
        pyplot.close()

def show(block=True):
    pyplot.show(block=block)

def pause(seconds=0):
    pyplot.pause(seconds)

def close(fig=None):
    pyplot.close(fig=fig)

def set_lower_and_upper_color(rgb_one, rgb_two):
    formatted_one = numpy.uint8([[rgb_one]])
    formatted_two = numpy.uint8([[rgb_two]])
    hsv_one = cv2.cvtColor(formatted_one, cv2.COLOR_RGB2HSV)
    hsv_two = cv2.cvtColor(formatted_two, cv2.COLOR_RGB2HSV)
    lower_color = []
    upper_color = []
    for index in range(0, len(hsv_one[0][0])):
        current_one = hsv_one[0][0][index]
        current_two = hsv_two[0][0][index]
        if current_one <= current_two:
            lower_color.append(current_one)
            upper_color.append(current_two)
        else:
            lower_color.append(current_two)
            upper_color.append(current_one)
    return numpy.float32(lower_color), numpy.float32(upper_color)

class Image():
    def __init__(self, path=None, title="Image", cmap="rgb"):
        self._cmap = self.set_cmap(cmap)
        self._path = path
        self.title = title
        self._mask = None
        self._connection_id = None
        self.set_image(path, cmap)

    def set_cmap(self, cmap):
        if cmap in ("rgb", "rgba", "gray"):
            return cmap
        else:
            error_name = "InvalidColormap"
            error_description = f"The Colormap {cmap} isn't valid. "
            error_description += "Please choose between the following options: 'rgb', 'rgba' or 'gray'."
            raise NameError(error_name, error_description)
            

    def set_image(self, path, cmap, reset_mode=False):
        if path:
            self._image = cv2.imread(path)
            self.convert_image_colormap(cmap, bgr=True)
        else:
            self._image = None
        if not reset_mode:
            self.set_window()

    def set_frame(self, frame, cmap="rgb", reset_mode=False):
        self._original_frame = frame
        self._image = frame
        self.convert_image_colormap(cmap, bgr=True)
        if not reset_mode:
            self.set_window()

    def convert_image_colormap(self, cmap, bgr=False):
        if bgr:
            if cmap == "rgb":
                self._image = cv2.cvtColor(self._image, cv2.COLOR_BGR2RGB)
            elif cmap == "rgba":
                self._image = cv2.cvtColor(self._image, cv2.COLOR_BGR2RGBA)
            elif cmap == "gray":
                self._image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
            else:
                error_name = "InvalidColormap"
                error_description = f"The Colormap {cmap} isn't valid. "
                error_description += "Please choose between the following options: 'rgb', 'rgba' or 'gray'."
                raise NameError(error_name, error_description)
        else:
            if self._cmap == "rgb":
                if cmap == "rgba":
                    self._image = cv2.cvtColor(self._image, cv2.COLOR_RGB2RGBA)
                elif cmap == "gray":
                    self._image = cv2.cvtColor(self._image, cv2.COLOR_RGB2GRAY)
                elif cmap == "rgb":
                    print("This image it's already on rgb colormap.")
                else:
                    error_name = "InvalidColormap"
                    error_description = f"The Colormap {cmap} isn't valid for this image. "
                    error_description += "Please choose between the following options: 'rgba' or 'gray'."
                    raise NameError(error_name, error_description)
            elif self._cmap == "rgba":
                if cmap == "rgb":
                    self._image = cv2.cvtColor(self._image, cv2.COLOR_RGBA2RGB)
                elif cmap == "gray":
                    self._image = cv2.cvtColor(self._image, cv2.COLOR_RGBA2GRAY)
                elif cmap == "rgba":
                    print("This image it's already on rgba colormap.")
                else:
                    error_name = "InvalidColormap"
                    error_description = f"The Colormap {cmap} isn't valid for this image. "
                    error_description += "Please choose between the following options: 'rgb' or 'gray'."
                    raise NameError(error_name, error_description)
            elif self._cmap == "gray":
                if self._path is not None:
                    self.set_image(self._path, cmap)
                else:
                    self.set_frame(self._original_frame, cmap)
            self._cmap = self.set_cmap(cmap)
    
    def add_mask(self, dark_rgb_color, light_rgb_color):
        if self._cmap == 'rgb':
            hsv_image = cv2.cvtColor(self._image, cv2.COLOR_RGB2HSV)
            lower_color, upper_color = set_lower_and_upper_color(dark_rgb_color, light_rgb_color)
            mask = cv2.inRange(hsv_image, lower_color, upper_color)

            if self._mask is None:
                self._mask = mask
            else:
                self._mask = cv2.bitwise_or(self._mask, mask)
        else:
            error_name = "InvalidColormap"
            error_description = f"The Colormap {cmap} isn't valid for add mask. "
            error_description += "Please use a rgb image."
            raise NameError(error_name, error_description)

    def reset_mask(self):
        self._mask = None
        if self._path is not None:
            self.set_image(self._path, self._cmap, reset_mode=True)
        else:
            self.set_frame(self._original_frame, self._cmap, reset_mode=True)

    
    def apply_mask(self):
        mask_image = cv2.bitwise_and(self._image, self._image, mask=self._mask)
        self._image = mask_image

    def window(self, on_key_press, new=True):
        if new:
            self._window_id = window_index()
        figure = pyplot.figure(self._window_id)
        figure.canvas.set_window_title(self.title)        
        if self._connection_id is not None:
            figure.canvas.mpl_disconnect(self._connection_id)
        self._connection_id = figure.canvas.mpl_connect("key_press_event", on_key_press)

    def set_window(self, on_key_press=key_press_event):
        self.update_window(on_key_press=on_key_press, new=True)
    
    def update_window(self, on_key_press=key_press_event, new=False):
        self.window(on_key_press, new=new)
        if self._image is not None:
            cmap = None
            if self._cmap not in ("rgb", "rgba"):
                cmap = self._cmap
            pyplot.imshow(self._image, cmap=cmap)