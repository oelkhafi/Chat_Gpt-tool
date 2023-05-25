import numpy as np
from skimage.io import imread, imsave


def convolution(image, kernel):

    convolved_image = np.zeros((image.shape[0] - kernel.shape[0] + 1, image.shape[1] - kernel.shape[1] + 1))
    k = kernel / kernel.sum()

    for row in range(image.shape[0] + 1):
        for col in range(image.shape[1] + 1):
            if row + kernel.shape[0] <= image.shape[0] and col + kernel.shape[1] <= image.shape[1]:
                batch = image[row:row + kernel.shape[0], col:col + kernel.shape[1]]
                convolved_image[row][col] = (batch * k).sum()
            else:
                continue

    return convolved_image


img = imread('img.png')
kernel = np.array([[-1, -2, -1], [-2, 22, -2], [-1, -2, -1]])

imsave('out_img.png', np.clip(convolution(img, kernel), 0, 255).astype('uint8'))
 