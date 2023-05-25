import numpy as np
from skimage.io import imread, imsave


def median_filter(image, filter_size):

    filtered_image = np.zeros((image.shape[0] - filter_size[0] + 1, image.shape[1] - filter_size[1] + 1))

    for row in range(image.shape[0] + 1):
        for col in range(image.shape[1] + 1):
            if row + filter_size[0] <= image.shape[0] and col + filter_size[1] <= image.shape[1]:
                batch = image[row:row + filter_size[0], col:col + filter_size[1]]
                filtered_image[row][col] = np.median(batch)
            else:
                continue

    return filtered_image


imsave('out_img.png', median_filter(imread('img.png'), (7, 7)).astype('uint8'))
 