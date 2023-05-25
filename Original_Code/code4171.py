n, m = (int(i) for i in input().split())  # чтение размеров поля и числа мин
a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
for i in range(n):
    row = list(i for i in input())
    for j1, j in enumerate(row):
        if j == ""*"":
            a[i][j1] = -1  # расставляем мины
            continue


for i in range(n):
    for j in range(m):
        if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
# вывод результата
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('0', end='')
        else:
            print(a[i][j], end='')
    print()
 