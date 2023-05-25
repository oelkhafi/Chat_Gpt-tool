from numpy import histogram
import numpy
from skimage.io import imread, imsave


def find(k, first, second, step):
    for i in range(first, second, step):
        if values[i] - k > 0:
            return i
        else:
            k -= values[i]


img = imread('img.png')
k = round(img.size * 0.05)
mn = img.min()
mx = img.max()
values, bin_edges = histogram(img, range(257))
newmin = find(k, mn, mx, 1)
newmax = find(k, mx, mn, -1)
image = numpy.asarray(imread('img.png'), dtype='int')
image = (image - newmin) * 255 / (newmax - newmin)
image = numpy.clip(image, 0, 255)
imsave('out_img.png', numpy.asarray(image, dtype='int'))


 