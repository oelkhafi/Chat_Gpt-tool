n, m = (int(i) for i in input().split())  # определяем размеры сетки

# создание поля
field = []
for i in range(n):  # минируем поле
    field.append(list(input()))

# ""решение"" поля
for i in range(n):  # перебираем строки
    for j in range(m):  # перебираем столбцы
        if field[i][j] != '*':  # ячейка без мины
            field[i][j] = 0  # присваиваем 0 для инкремента
            for di in range(-1, 2):  # перебираем соседние строки (просто цифры -1 0 1)
                for dj in range(-1, 2):  # перебираем соседние столбцы (просто цифры -1 0 1)
                    x = i + di  # координата по строке
                    y = j + dj  # координата по столбцу
                    if 0 <= x < n and 0 <= y < m and field[x][y] == '*':  # проверка, что координаты в пределах поля и что поле является миной
                        field[i][j] += 1

# вывод ""решения""
for i in range(n):
    print(''.join(map(str, field[i])))
 