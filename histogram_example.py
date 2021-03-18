from models.image import Image, show, close, pause

def main():
    image = Image(path="./images/example.jpg", title="Aula 17/03", cmap='gray')
    show(block=False)
    image.show_histogram()
    pause(3)

    image.convert_image_colormap(cmap="rgb")
    image.update_window()
    image.update_histogram()
    show()

if __name__ == '__main__':
    main()