from PIL import ImageTk, Image
from tkinter import filedialog
import numpy
import matplotlib.pyplot as plt
from copy import deepcopy

sizeShow = [2, 5]

percent = -50
percent = percent/100


def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray


def setGrayColor(color):
    color = int(color)
    return [color, color, color]


file = filedialog.askopenfilename(title='Choose a file')

img = Image.open(file)
img = numpy.asarray(img)

rev = deepcopy(img)

r = deepcopy(img)
g = deepcopy(img)
b = deepcopy(img)

bright = deepcopy(img)



for i in range(len(img)):
    for j in range(len(img[i])):
        R = int(img[i][j][0])
        G = int(img[i][j][1])
        B = int(img[i][j][2])

        r[i][j] = setGrayColor(R)
        g[i][j] = setGrayColor(G)
        b[i][j] = setGrayColor(B)

        rev[i][j] = [255-R, 255-G, 255-B]
        
        if percent > 0 :
            R = R * percent + (1 - percent) + R
            G = G * percent + (1 - percent) + G
            B = B * percent + (1 - percent) + B
        else : 
            R = R * percent + R
            G = G * percent + G
            B = B * percent + B

        R = R > 255 and 255 or R
        G = G > 255 and 255 or G
        B = B > 255 and 255 or B
        bright[i][j] = [R,G,B]


plt.subplot(sizeShow[0], sizeShow[1], 1)
plt.imshow(img)

plt.subplot(sizeShow[0], sizeShow[1], 2)
plt.imshow(r)

plt.subplot(sizeShow[0], sizeShow[1], 3)
plt.imshow(g)

plt.subplot(sizeShow[0], sizeShow[1], 4)
plt.imshow(b)

plt.subplot(sizeShow[0], sizeShow[1], 5)
plt.imshow(rev)

plt.subplot(sizeShow[0], sizeShow[1], 6)
plt.hist(img.ravel(), 256, [0, 255])

plt.subplot(sizeShow[0], sizeShow[1], 7)
plt.hist(r.ravel(), 256, [0, 255])

plt.subplot(sizeShow[0], sizeShow[1], 8)
plt.hist(g.ravel(), 256, [0, 255])

plt.subplot(sizeShow[0], sizeShow[1], 9)
plt.hist(b.ravel(), 256, [0, 255])

plt.subplot(sizeShow[0], sizeShow[1], 10)
plt.imshow(bright)

plt.show()
