def rotate(oldmatrix, matrixsize):
    newmatrix = [[0] * matrixsize for x in range(matrixsize)]
    for y in range(matrixsize):
        for x in range(matrixsize):
            newmatrix[y][x] = oldmatrix[x][matrixsize - y - 1]

    del oldmatrix
    return newmatrix


def fill(m, n):
    if n is 1:
        return [[1]]
    value = 1
    for circle in range(n - 1):
        for side in range(4):
            lastx = circle
            for x in range(circle, n - 1 - circle):
                m[circle][x] = value
                if value == n ** 2:
                    break
                value += 1
                lastx = x

            if m[circle][lastx] == 0:
                m[circle][lastx] = value
                break

            m = rotate(m, n)

    return m


size = int(input())
print('\n'.join(' '.join(map(str, c)) for c in fill([[0] * size for x in range(size)], len([[] * size] * size)))) 