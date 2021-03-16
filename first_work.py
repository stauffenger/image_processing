from matplotlib import pyplot

from models.image import Image

def main():
    rgb_image = Image(path="./images/flores.jpg", title="Original Image")
    
    mask_image = Image(path="./images/flores.jpg", title="Lucas Pascoal")

    dark_green = [16, 39, 13]
    light_green = [190, 208, 25]
    mask_image.add_mask(dark_green, light_green)
    mask_image.apply_mask()
    mask_image.update_window()

    pyplot.show()

if __name__ == '__main__':
    main()