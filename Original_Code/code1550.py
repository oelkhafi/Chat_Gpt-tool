from numpy import histogram
from skimage.io import imread


def find(k, first, second, step):
    for i in range(first, second, step):
        if values[i] - k > 0:
            return i
        else:
            k -= values[i]


img = imread('img.png')
k = round(img.size * 0.05)
values, bin_edges = histogram(img, range(257))
newmin = find(k, img.min(), img.max(), 1)
newmax = find(k, img.max(), img.min(), -1)
print(newmin, newmax)




 