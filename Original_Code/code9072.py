# Квадрат из чисел, закрученных по спирали

# Создаём таблицу n * n из нулей
n = int(input())
table = [[0 for i in range(n)] for j in range(n)]
table[0] = [i for i in range(1, n + 1)]   # Заполнили первую строку

x, y = n - 1, 0     # Текущие координаты ячейки спирали
current = n         # Текущее значение ячейки спирали
dx, dy = 0, 1       # Направление вектора спирали

# Забиваем таблицу убывающей последовательностью
for k in range(n - 1, 0, -1):
    for j in range(2):
        for i in range(k):
            current += 1
            x += dx
            y += dy
            table[y][x] = current
        # Поворотики (лучше бы сделал через тригонометрию)
        if dy == 1: dx, dy = -1, 0
        elif dx == 1: dx, dy = 0, 1
        elif dy == -1: dx, dy = 1, 0
        elif dx == -1: dx, dy = 0, -1

# Печать таблицы
for x in range(n):
    for y in range(n):
        print(table[x][y], end=' ')
    print()
 