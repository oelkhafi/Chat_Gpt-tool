n, m = (int(i) for i in input().split())  # чтение размеров поля
a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
b = [[0 for j in range(m)] for i in range(n)]  # новое поле для второго цикла

for i in range(n):
    row = list(i for i in input())
    for j1, j in enumerate(row):
        a[i][j1] = j  # расставляем клетки
        continue


for i in range(n):
    for j in range(m):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ai = (i + di)%n
                aj = (j + dj)%m
                if a[ai][aj] == ""X"":
                    b[i][j] += 1
        if a[i][j] == ""X"":
            b[i][j] -= 1

# вывод результата
for i in range(n):
    for j in range(m):
        if a[i][j] == ""X"" and (b[i][j] == 2 or b[i][j] == 3):
            print('X', end='')
        elif a[i][j] == ""X"" and (b[i][j] < 2 or b[i][j] > 3):
            print('.', end='')
        elif a[i][j] == ""."" and b[i][j] == 3:
            print('X', end='')
        else:
            print('.', end='')
    print()
 