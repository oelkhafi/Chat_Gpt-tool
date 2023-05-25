#1 Ввод размера матрицы
n = int(input())

#2 Построение квадратной матрицы [n x n], заполненной нулями
M = [[0 for j in range(n)]for i in range(n)] 

#3 Длина пути: S[i] = n*n
vector = [[i, i] for i in range(1, n + 1)]  # длины i-тых векторов
S = sum(vector, [])[:-1]                    # длина пути         

#4 Координаты центра матрицы для нечётных и чётных n
N = n // 2
if n % 2 == 1:      # нечётные n
    x, y = N, N                             # координаты центра 
    dx, dy = [0,1,0,-1],[-1,0,1,0]          # векторы изменения координат:
elif n % 2 == 0:    # чётные n                (влево-вниз-вправо-вверх)
    x, y = N, N - 1                         # координаты центра
    dx, dy = [0,-1,0,1],[1,0,-1,0]          # векторы изменения координат:
M[x][y] = n*n       # центр матрицы           (вправо-вверх-влево-вниз)

#5 Заполнение матрицы
step = 1
for i in range(len(S)):
    for j in range(S[i]):
        x += dx[i % 4]
        y += dy[i % 4]
        M[x % n][y % n] = n * n - step
        if n * n - step == 1:
            break
        step += 1
M[0][0] = 1         # начало матрицы

#6 Выходная матрица
[print(*M[i]) for i in range(n)] 