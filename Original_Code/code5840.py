import numpy as np
from skimage.io import imread, imsave


def gaussian(sigma, x, y):
    return (1 / (2 * np.pi * sigma ** 2)) * np.e ** ((-x ** 2 - y ** 2) / (2 * sigma ** 2))


def create_gauss_core(sigma):
    k = round(3 * sigma) * 2 + 1
    gauss_core = np.ones((k, k))
    x = np.arange(-(k // 2), k // 2 + 1)
    y = np.arange(k // 2, -(k // 2 + 1), -1)

    for row in range(gauss_core.shape[0]):
        for col in range(gauss_core.shape[1]):
            gauss_core[row][col] = gaussian(sigma, x[row], y[col])

    return gauss_core / gauss_core.sum()


def gaussian_blur(image, core):

    blurred_image = np.zeros((image.shape[0] - core.shape[0] + 1, image.shape[1] - core.shape[1] + 1))

    for row in range(image.shape[0] + 1):
        for col in range(image.shape[1] + 1):
            if row + core.shape[0] <= image.shape[0] and col + core.shape[1] <= image.shape[1]:
                batch = image[row:row + core.shape[0], col:col + core.shape[1]]
                blurred_image[row][col] = (batch * core).sum()
            else:
                continue

    return blurred_image


img = imread('img.png')
sigma = 0.66
gauss_core = create_gauss_core(sigma)
imsave('out_img.png', gaussian_blur(img, gauss_core).astype('uint8'))
 