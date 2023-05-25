S = n = int(input())  # S - сколько шагов нужно сделать, n - вспомогательная переменная
finish = n * n  # последнее число
step, line_x = 0, 0  # step - счетчик, line_x - вспомогательная переменная
matrix = [[0 for j in range(n)]for i in range(n)]
while step != finish:
    for i in range(S):  # вправо
        step += 1
        matrix[line_x][line_x + i] = step  # смещение и заполнение ячейки вправо
    S -= 1
    for i in range(S):  # вниз
        step += 1
        matrix[line_x + i + 1][n - 1] = step  # смещение и заполнение ячейки вниз
    for i in range(S):  # влево
        step += 1
        matrix[n - 1][n - 2 - i] = step  # смещение и заполнение ячейки влево
    S -= 1
    for i in range(S):  # вверх
        step += 1
        matrix[n - 2 - i][line_x] = step  # смещение и заполнение ячейки вверх
    line_x += 1  # убираем заполненый ряд
    n -= 1  # убираем заполненый столбик
for j in range(len(matrix)):  # вывод спиральной матрицы
    for i in range(len(matrix)):
        print(matrix[j][i], end=' ')
    print() 