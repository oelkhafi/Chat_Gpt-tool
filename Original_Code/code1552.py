from skimage.io import *
from numpy import *
from skimage import img_as_float, img_as_ubyte

img = img_as_float(imread('img.png'))
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

y = 0.2126 * r + 0.7152 * g + 0.0722 * b
u = -0.0999 * r - 0.3360 * g + 0.4360 * b
v = 0.6150 * r - 0.5586 * g - 0.0563 * b

img_mi, k = sort(y.flatten()), round(y.size * 0.05)
y = clip((y - img_mi[k]) / (img_mi[-k] - img_mi[k]), 0, 1)

r = clip(y + 1.2803 * v, 0, 1)
g = clip(y - 0.2148 * u - 0.3805 * v, 0, 1)
b = clip(y + 2.1279 * u, 0, 1)

image = img_as_ubyte(dstack((r, g, b)))
imsave('out_img.png', image)
 