# What is this?

That's my study about image processing based on my class in college. Here I'm gonna make code examples about how to use "pyplot" and "opencv" libraries to process images and upload all the class works.
Well, all the libraries are chosen by my teacher, but I made a change in how to use them. I switched the 'opencv-python' for the "opencv-contrib-python-headless" and because of that, I'm using "pyplot" to generate the GUI instead of "opencv" as my teacher did.

## Why use opencv contrib python headless?

As said by the documentation of "opencv" on PyPi, this library has a heavy dependency chain to create GUI, and some of these dependencies are no longer supported by the "Qt" framework, and since I use Fedora, an operating system made to be up to date, I preferred to use only libraries/frameworks that still have some support. So, I chose the "opencv-contrib-python-headless" package of the library "opencv" because this package makes me able to use all the assets of the "opencv" except the ones used for generating the GUI, then I'm using the "pyplot" to generating all the necessaries GUI.

> "These packages are smaller than the two other packages above because they do not contain any GUI functionality (not compiled with Qt / other GUI components). This means that the packages avoid a heavy dependency chain to X11 libraries and you will have for example smaller Docker images as a result. You should always use these packages if you do not use cv2.imshow et al. or you are using some other package (such as PyQt) than OpenCV to create your GUI." [opencv-python 4.5.1.48 documentation on PyPi](https://pypi.org/project/opencv-python/) - Access in 03/15/2021.

# Getting started

## How to install the dependencies on Linux

`$ python -m pip install -r requirements.txt`

| dependency | Version |
|:-----------|:-------:|
| numpy | 1.19.4 |
| matplotlib | 3.3.4 |
| opencv-contrib-python-headless | 4.5.1.48 |

## How to start the program on Linux

The project is divided based on the class works, which means that each work will be in a different file, and will be initialized separated.

### First work

>"Alterar o programa abaixo, para que seja apresentado somente a cor VERDE conforme o exemplo em anexo(flores.jpg). No Caption da Janela deverá constar o seu nome(Trocar Resultado pelo seu nome)."

Honestly even in Portuguese these phrases alone no make much sense, so I'll translate the idea that the teacher wanted to give instead of the lesson statement: Change the code below to load the image in attachment instead of the video and use a mask to only show the green parts of the image. The window title needs to be your name.

```
import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

while True:
_,frame = cap.read()
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

baixo_azul = np.array([100, 100, 100])
alto_azul = np.array([130, 255, 255])

mask = cv2.inRange(hsv, baixo_azul, alto_azul)

res = cv2.bitwise_and(frame, frame, mask = mask)

cv2.imshow('Frame', frame)
cv2.imshow('Mascara', mask)
cv2.imshow('Res', res)

k = cv2.waitKey(5) & 0xFF

if k == 27:
break

cap.release()
cv2.destroyAllWindows()
```
#### How to run

`$ python first_work.py`

## How to use the Image class made by me

To make easier the manipulation of images during all the works I made a class to handle the basic issues, for example, load an image, convert the colormap, set windows configurations, handle key pressed events, update the window content, add, reset and apply masks on the image. And to make it even easier, I made two code examples that use almost all the functions in the class in case someone wants to reuse the class or even improve it.

The first example it's how to manipulate images with the class (`image_example.py`) and the second one it's how to manipulate video frames with the class (`video_example.py`).

### How to run the examples

`$ python image_example.py` and `$ python video_example.py`


# References

- [opencv](https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html)
- [matplotlib](https://matplotlib.org/3.3.4/api/)
- [pyplot](https://matplotlib.org/3.3.4/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)
- [numpy](https://numpy.org/doc/stable/)
- [matplotlib events](https://matplotlib.org/3.3.4/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect)