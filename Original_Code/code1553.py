from numpy import *
from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte

img = img_as_float(imread('img.png'))
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

rr=mean(r)
gg=mean(g)
bb=mean(b)

avg=(rr+gg+bb)/3

rw=rr/avg
gw=gg/avg
bw=bb/avg

r=clip(r/rw,0,1)
g=clip(g/gw,0,1)
b=clip(b/bw,0,1)

image = img_as_ubyte(dstack((r, g, b)))
imsave('out_img.png', image)
 