from skimage.io import imread, imsave, imshow
import numpy as np
from itertools import product, accumulate


# читаем файл с изображением
img = imread('img.png')
#  создаем гистограмму изображения
values, bin_edges = np.histogram(img, bins=range(257))
# считаем функцию sdf
sdf = list(accumulate(values))
# находим sdf_min
sdf_min = min(i for i in sdf if i)
# определяем границы для прохождения по массиву
x, y = img.shape
# проходим по всем пикселям и меняем на новое значение
for row,col in product(range(x),range(y)):    
    bright = img[row, col]
    img[row, col] = round(255 * (sdf[bright] - sdf_min) / (img.size - 1))
# записываем изображение в файл    
imsave('out_img.png', img)
 