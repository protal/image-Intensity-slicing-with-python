from PIL import ImageTk, Image
from tkinter import filedialog
import numpy
import matplotlib.pyplot as plt
from copy import deepcopy

sizeShow = [2, 2]

def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray


def setGrayColor(color):
    color = int(color)
    return [color, color, color]

file = filedialog.askopenfilename(title='Choose a file')

img = Image.open(file)
img = numpy.asarray(img)

output = deepcopy(img)

colorRang = [
    [[255,0,0], 210],
    [[0,255,0], 170],
    [[0,0,255], 130],
    [[255,255,0], 90],
    [[255,0,255], 50],
    [[0,255,255], 0],
]

for i in range(len(img)):
    for j in range(len(img[i])):
        color = getGrayColor(img[i][j])
        for k in range(len(colorRang)):
            if(color >= colorRang[k][1]):
                output[i][j] = colorRang[k][0];
                break
        




plt.subplot(sizeShow[0], sizeShow[1], 1)
plt.imshow(img)

plt.subplot(sizeShow[0], sizeShow[1], 2)
plt.imshow(output)

plt.subplot(sizeShow[0], sizeShow[1], 3)
plt.hist(img.ravel(), 256, [0, 256])

plt.show()
