# -*- coding: utf-8 -*-

n = int(input())
# Захреначили пустую матрицу
mas = [[0] * n for i in range(n)]
# Захреначили список поворотов
l_povorot = [n]
for i in range(n-1,0,-1):
    l_povorot.append(i)
    l_povorot.append(i)
# Стартовое положение заполнения матрицы по спирали
cx, cy = 0, -1
# Прирост в зависимости от направления
pr1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
pr2 = 0
z = 1
# Цикл с учетом общего количества поворотов спирали
for i in range(0, 2 * n -1):
    for j in range(l_povorot[i]):
        cx = cx + pr1[pr2][0]
        cy = cy + pr1[pr2][1]
        mas[cx][cy] = z
        z += 1
    pr2 += 1
    if pr2 == 4:
        pr2 = 0
for i in mas:
    print(*i)
 