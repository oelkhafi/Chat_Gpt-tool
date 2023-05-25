from itertools import product
from skimage.io import imread, imshow
import numpy as np


def get_size_border(file_name):
    """"""
    The function takes the name of the image file. 
    Returns a tuple with the frame dimensions (left, top, right, bottom).
    """"""
    img = imread(file_name)
    x_size, y_size, _ = img.shape
    left, top, right, bottom = y_size, x_size, -1, -1
    for x, y in product(range(x_size), range(y_size)):
        if not np.array_equal(img[x, y], img[0, 0]):
            left, top = min(left, y), min(top, x)
            right, bottom = max(right, y), max(bottom, x)
    return left, top, y_size - right - 1, x_size - bottom - 1


if __name__ == ""__main__"":
    print(*get_size_border('img.png'))
 