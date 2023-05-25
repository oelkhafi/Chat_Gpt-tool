import numpy
from skimage.io import imread
img = imread('img.png')
border = img[0, 0]
v,s,_ = img.shape

def findY(h, l, yy, x=s//2):
    while True:
        y = (h + l) // 2
        if numpy.array_equal(img[y, x], border) and numpy.array_equal(img[y+yy, x], border) == False:
            if yy > 0: return y+1
            else: return v-y
        if numpy.array_equal(img[y, x], border):
            if yy>0: l = y
            else: h=y
        else:
            if yy>0: h = y
            else: l=y

def findX(h, l, xx, y=v//2):
    while True:
        x = (h + l) // 2
        if numpy.array_equal(img[y, x], border) and numpy.array_equal(img[y, x+xx], border) == False:
            if xx > 0: return x+1
            else: return s-x
        if numpy.array_equal(img[y, x], border):
            if xx>0: l = x
            else: h=x
        else:
            if xx>0: h = x
            else: l=x

print(findX(s, 0, 1),findY(v, 0, 1), findX(s, 0, -1),findY(v, 0, -1))
 