from skimage.io import imread
from skimage.color import rgb2gray

img = imread('img.png')
g_img = rgb2gray(img)
frame = g_img[0, 0]
h_mid_line = g_img.shape[0] // 2
v_mid_line = g_img.shape[1] // 2

right_border = 0
top_border = 0
left_border = 0
bottom_border = 0

for pix in list(g_img[h_mid_line]):
    if pix == frame:
        right_border += 1
    else:
        break

for pix in (g_img[:, v_mid_line]):
    if pix == frame:
        top_border += 1
    else:
        break

for pix in reversed(list(g_img[h_mid_line])):
        if pix == frame:
            left_border += 1
        else:
            break

for pix in reversed(list(g_img[:, v_mid_line])):
        if pix == frame:
            bottom_border += 1
        else:
            break

print(right_border, top_border, left_border, bottom_border)
 