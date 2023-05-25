#1 Ввод элементов матрицы
M, row, e = [0], -1, ['end']      # row = -1 для счёта индексов строк с нуля
while True:
    s = input().split()
    row += 1
    if (row == 0) and (s != e):
        M = s
    elif (row == 1) and (s != e):
        M = [M]
        [M.append(s)]
        if (len(M[-2]) != len(M[-1])):
            break
    elif (row > 1) and (s != e):
        [M.append(s)]
        if (len(M[-2]) != len(M[-1])):
            break
    elif (s == e):
        break

#2 Преобразование элементов матрицы из строк в целые числа,
#  создание N - маски матрицы M, заполненной нулями
if row == 1:                         # матрица с 1-й строкой
    for i in range(len(M)):
        M[i] = int(M[i])
    N = [0 * row for i in range(len(M))]
elif row > 1 and len(M[0]) == 1:     # матрица с 1-м столбцом
    for i in range(len(M)):
        M[i][0] = int(M[i][0])
    N = [[0] for i in range(len(M))]
elif row > 1 and len(M[0]) > 1:      # матрица размером n >= 2 
    if row < len(M[0]):              # строк меньше столбцов
        for j in range(len(M[0])):
            for i in range(row):
                M[i][j] = int(M[i][j])
        N = [[0] * len(M[0]) for i in range(row)]
    elif row > len(M[0]):            # строк больше столбцов
        for j in range(len(M[0])):
            for i in range(row):
                M[i][j] = int(M[i][j])
        N = [[0] * len(M[0]) for i in range(row)]
    elif row == len(M[0]):           # строк и столбцов поровну
        for j in range(len(M[0])):
            for i in range(row):
                M[i][j] = int(M[i][j])
        N = [[0] * row for i in range(len(M[i]))]

#3 Расчёт значений элементов выходной матрицы
for j in range(len(M)):
    for i in range(len(M)):
        if row == 1 and len(M) == 1:       # матрица из 1-го элемента 
            N[0] = M[0] * 4
        elif row == 1 and len(M) > 1:      # матрица с 1-й строкой
            if i == 0:                     # крайний слева
                N[0] = M[1] + M[-1] + M[0] * 2    
            elif i < (len(M) - 1):         # между
                N[i] = M[i-1] + M[i+1] + M[i] * 2
            elif i == (len(M) - 1):        # крайний справа
                N[-1] = M[0] + M[i-1] + M[-1] * 2
        elif row > 1 and len(M[0]) == 1:   # матрица с 1-м столбцом
            if i == 0:
                N[0][0] = M[0][0] * 2 + M[i-1][0] + M[i+1][0]
            elif i < (len(M) - 1):
                N[i][0] = M[i][0] * 2 + M[i-1][0] + M[i+1][0]
            elif i == (len(M) - 1):
                N[-1][0] = M[i][0] *2 + M[i-1][0] + M[0][0]
        elif row > 1 and len(M[0]) > 1:
            for j in range(len(M[0])):
                for i in range(row):       # для матриц размером (n x m) >= 2
                    N[i][j] = M[(i-1)%row][j] + M[(i+1)%row][j] + \
                              M[i][(j-1)%(len(M[0]))] + M[i][(j+1)%(len(M[0]))]
#4 Вывод
for i in range(row):
    if row == 1:
        print(*N)
    elif row > 1:
        print(*N[i]) 