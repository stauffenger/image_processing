import sys
from random import seed, randint

from models.image import Image, show, pause, close

def on_press(event):
    sys.stdout.flush()
    if event.key == 'q' or event.key == 'x':
        print("Closing window...")
        close(fig='all')
        print("Exiting...")
        sys.exit(0)

def show_image(image_number="1"):
    if image_number == "1":
        rgb_image = Image(path="./images/example.jpg", title="Image Processing Class")
    elif image_number == "2":
        grayscale_image = Image(path="./images/example.jpg", title="Grayscale", cmap="gray")
    elif image_number == "3":
        dark_color = [120, 68, 32]
        light_color = [230, 164, 129]
        mask_image = Image(path="./images/example.jpg", title="Mask Image")
        mask_image.add_mask(dark_color, light_color)
        mask_image.apply_mask()
        mask_image.update_window()
        show(block=False)
        pause(2)
        mask_image.reset_mask()
        dark_color = [25, 20, 14]
        light_color = [135, 122, 96]
        mask_image.add_mask(dark_color, light_color)
        mask_image.apply_mask()
        mask_image.update_window(on_key_press=on_press)
    else:
        error_name = "ImageNumberNotFound"
        error_description = f"The image number {image_number} was not found. "
        error_description += "Please, choose a number between the following options: '1', '2' and '3'."
        raise NameError(error_name, error_description)

    show()

if __name__ == '__main__':
    seed()
    number = randint(1, 3)
    show_image(image_number=str(number))

