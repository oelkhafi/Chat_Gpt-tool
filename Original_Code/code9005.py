matrix_len = int(input())
matrix = [[0 for i in range(matrix_len)] for i in range(matrix_len)]

# Счетчики для заполнения матрицы
i, j = 0, 0
# Счетчики краев заполнения матрицы
forward_go, reverse_go = matrix_len, -1
# Текущее число и максимальное число для заполнения
counter, counter_len = 1, matrix_len ** 2

# Цикл работает пока счетчики краев не сравняются и пока число для заполнения не достигнет максимального значения
while (forward_go > reverse_go) and (counter <= counter_len):

    # Заполнение на восток
    for j in range(j, forward_go, 1):
        matrix[i][j] = counter
        counter += 1
    # Шаг на юг, т.к. первый элемент столбца уже заполнили шагом ранее
    i += 1

    # Заполнение на юг
    for i in range(i, forward_go, 1):
        matrix[i][j] = counter
        counter += 1
    # Шаг на запад, т.к. последний элемент строки уже заполнили шагом ранее
    j -= 1
    forward_go -= 1

    # Заполнение на запад
    for j in range(j, reverse_go, -1):
        matrix[i][j] = counter
        counter += 1
    # Шаг на север, т.к. последний элемент столбца уже заполнили шагом ранее
    i -= 1
    reverse_go += 1

    # Заполнение на север
    for i in range(i, reverse_go, -1):
        matrix[i][j] = counter
        counter += 1
    # Шаг на восток, т.к. первый элемент строки уже заполнили шагом ранее
    j += 1


for item in matrix:
    print(*item, sep="" "")
 