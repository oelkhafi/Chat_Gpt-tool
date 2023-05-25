from skimage.io import imread, imsave
from numpy import histogram


def cdf(x, h):
    return h[:x + 1].sum()


def find_min_cdf(cdfs):
    for key in sorted(cdfs.keys()):
        if cdfs[key] != 0:
            return cdfs[key]


img = imread('img.png')
img_shape = img.shape
h, bins = histogram(img, bins=range(257))

cdfs = {i: cdf(i, h) for i in range(256)}
cdf_min = find_min_cdf(cdfs)
d = h.sum() - 1
max_bright = 255
img_ = img.ravel()

for i in range(len(img_)):
    img_[i] = round(((cdfs[img_[i]] - cdf_min) / d) * max_bright)

imsave('out_img.png', img_.reshape(img_shape))
 