n = int(input())
m = [[0] * n for i in range(n)]
i, j, = 0, 0
x, y = 1, 1
xMove = True

for r in range(1, n ** 2 + 1):
    if xMove:
        if 0 <= j <= n - 1 and m[i][j] == 0:
            m[i][j] = r
            j += x
        else:
            xMove = not xMove
            x *= -1  # двигаться по x обратно
            j += x  # вернуть обратно координату по x
            i += y  # сместить по y
            m[i][j] = r  # записать
            i += y  # сместить по y
    else:
        if 0 <= i <= n - 1 and m[i][j] == 0:
            m[i][j] = r
            i += y
        else:
            xMove = not xMove
            y *= -1  # двигаться по y обратно
            j += x  # сместить по x
            i += y  # вернуть обратно координату по y
            m[i][j] = r  # записать
            j += x  # сместить по x
for row in m:
    for item in row:
        print(item, end=' ')
    print()

 