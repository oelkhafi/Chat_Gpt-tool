n = int(input())
a = [[0] * n for i in range(n)]

xmin = 0
xmax = n-1
ymin = 0
ymax = n-1
b = 0
bmax = n ** 2

while b != bmax:
    # Идем вправо по горизонтали
    for i in range(xmin, xmax+1):
        b += 1
        a[ymin][i] = b
    ymin += 1 # Убираем из диапазона обхода матрицы строку сверху
    
    # Идем вниз по вертикали
    for i in range(ymin, ymax+1):
        b += 1
        a[i][xmax] = b
    xmax -= 1 # Убираем из диапазона обхода матрицы колонку справа
    
    # Идем влево по горизонтали
    for i in reversed(range(xmin, xmax+1)):
        b += 1
        a[ymax][i] = b
    ymax -= 1 # Убираем из диапазона обхода матрицы строку снизу
    
    # Идем вверх по вертикали
    for i in reversed(range(ymin, ymax+1)):
        b += 1
        a[i][xmin] = b
    xmin += 1 # Убираем из диапазона обхода матрицы колонку слева
        
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print() 