from skimage.io import imread, imsave
from skimage import img_as_float
from numpy import dstack, roll


def color_channels_align(aligned_channel, base_channel, pix_range_start=-15, pix_range_end=16):
    """""" Функция выравнивает цветовые каналы с фотографии Прокудина-Горского друг относительно друга.

    Принимает вырезанные массивы цветовых каналов с фотографии
    и диапазон перекрытия каналов.
    Возвращает значения сдвига каналов относительно друг друга.

    """"""

    aligned_channel_shift = []

    for col in range(pix_range_start, pix_range_end):
        shifted_aligned_channel_col = roll(aligned_channel, col, 1)
        for row in range(pix_range_start, pix_range_end):
            shifted_aligned_channel_row = roll(shifted_aligned_channel_col, row, 0)
            aligned_channel_shift.append(((base_channel * shifted_aligned_channel_row).sum(), row, col))

    aligned_channel_row, aligned_channel_col = max(aligned_channel_shift)[1], max(aligned_channel_shift)[2]

    return aligned_channel_row, aligned_channel_col


def align(img, coords_g):
    """""" Функция сопоставляет изображения с фотографий Прокудина-Горского.

     Принимает загруженное изображение и координаты точки на зеленом канале,
     возвращает координаты точек на синем и красном каналах.

    """"""

    row_g, col_g = coords_g
    img_f = img_as_float(img)

    color_channel_vert_size = img_f.shape[0] // 3
    b = img_f[:color_channel_vert_size]
    g = img_f[color_channel_vert_size:2 * color_channel_vert_size]
    r = img_f[2 * color_channel_vert_size:3 * color_channel_vert_size]

    trim_val = 7
    v_trim = color_channel_vert_size * trim_val // 100
    h_trim = img_f.shape[1] * trim_val // 100
    b = b[v_trim:b.shape[0] - v_trim, h_trim:b.shape[1] - h_trim]
    g = g[v_trim:g.shape[0] - v_trim, h_trim:g.shape[1] - h_trim]
    r = r[v_trim:r.shape[0] - v_trim, h_trim:r.shape[1] - h_trim]

    b_row, b_col = color_channels_align(b, g)
    r_row, r_col = color_channels_align(r, g)

    row_b = (row_g - color_channel_vert_size) - b_row
    col_b = col_g - b_col
    row_r = (img_f.shape[0] - (2 * color_channel_vert_size - row_g)) - r_row
    col_r = col_g - r_col

    return (row_b, col_b), (row_r, col_r)
 