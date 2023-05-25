from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import clip, dstack


def search_bright_min_max(image):

    pixels = sorted(image.flatten().tolist())
    pixels_length = len(pixels)
    k = round(pixels_length * 0.05)
    sliced_pixels = pixels[k + 1:pixels_length - k]

    return sliced_pixels[0], sliced_pixels[-1]


def stable_auto_contrast(image):

    max_bright = 1
    image_min = search_bright_min_max(image)[0]
    image_max = search_bright_min_max(image)[1]

    return (image - image_min) * (max_bright / (image_max - image_min))


img = img_as_float(imread('img.png'))

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

y = 0.2126 * r + 0.7152 * g + 0.0722 * b
u = -0.0999 * r - 0.3360 * g + 0.4360 * b
v = 0.6150 * r - 0.5586 * g - 0.0563 * b

y = clip(stable_auto_contrast(y), 0, 1)

r = y + 1.2803 * v
g = y - 0.2148 * u - 0.3805 * v
b = y + 2.1279 * u

out_img = clip(dstack((r, g, b)), 0, 1)
imsave('out_img.png', img_as_ubyte(out_img))
 