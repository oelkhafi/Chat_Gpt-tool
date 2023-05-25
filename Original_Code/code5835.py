from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import clip, dstack


def get_grey_world_coefficients(image):

    red_average = image[:, :, 0].mean()
    green_average = image[:, :, 1].mean()
    blue_average = image[:, :, 2].mean()

    average = (red_average + green_average + blue_average) / 3

    red_coefficient = red_average / average
    green_coefficient = green_average / average
    blue_coefficient = blue_average / average

    return red_coefficient, green_coefficient, blue_coefficient


img = img_as_float(imread('img.png'))

r_w, g_w, b_w = get_grey_world_coefficients(img)
new_r, new_g, new_b = img[:, :, 0] / r_w, img[:, :, 1] / g_w, img[:, :, 2] / b_w
out_img = clip(dstack((new_r, new_g, new_b)), 0, 1)

imsave('out_img.png', img_as_ubyte(out_img))
 