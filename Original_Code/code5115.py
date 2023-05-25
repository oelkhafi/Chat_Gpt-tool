import numpy as np
from itertools import product


def align(in_file, check_point, indent=0.05, shift=15):
    # определяем шаг нарезки и размер рамки
    step, border = img.shape[0] // 3, round(img.shape[1] * indent)

    # разрезаем и убираем рамку
    b_channel, g_channel, r_channel = [img[step * i + border:step * (i + 1) - border, border:-border] for i in range(3)]

    # создаем переменные для хранения максимальных значений корелляций и соответсвующих им сдвигов
    r_maxcol, b_maxcol, r_shift, b_shift = 0, 0, (None, None), (None, None)

    # перебираем все возможные сдвиги
    for cur_shift in product(range(-shift, shift + 1), range(-shift, shift + 1)):
        # сдвигаем зеленый канал
        cur_img = np.roll(g_channel, cur_shift[0], axis=0)
        cur_img = np.roll(cur_img, cur_shift[1], axis=1)
        # находим корреляцию и обновляем значения переменных для красного, если необходимо
        r_cor = (cur_img * r_channel).sum()
        if r_maxcol < r_cor:
            r_maxcol, r_shift = r_cor, cur_shift
        # находим корреляцию и обновляем значения переменных для синего, если необходимо
        b_cor = (cur_img * b_channel).sum()
        if b_maxcol < b_cor:
            b_maxcol, b_shift = b_cor, cur_shift

    return (check_point[0] + b_shift[0] - step, check_point[1] + b_shift[1]), (
        check_point[0] + r_shift[0] + step, check_point[1] + r_shift[1])
 