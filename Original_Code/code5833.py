from skimage.io import imread, imsave
from numpy import clip


def search_bright_min_max(image):

    pixels = sorted(image.flatten().tolist())
    pixels_length = len(pixels)
    k = round(pixels_length * 0.05)
    sliced_pixels = pixels[k + 1:pixels_length - k]

    return sliced_pixels[0], sliced_pixels[-1]


def stable_auto_contrast(image):
    
    max_bright = 255
    image_min = search_bright_min_max(image)[0]
    image_max = search_bright_min_max(image)[1]
    
    return (image - image_min) * (max_bright / (image_max - image_min))


img = imread('img.png')
comp_img = stable_auto_contrast(img.astype('float'))
out_img = clip(comp_img, 0, 255)
imsave('out_img.png', out_img.astype('uint8'))
 