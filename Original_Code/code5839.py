import numpy as np


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


sigma = float(input())
gauss_core = create_gauss_core(sigma)

for row in range(gauss_core.shape[0]):
    for val in gauss_core[row]:
        print('%.5f' % val, end=' ')
    print()
 