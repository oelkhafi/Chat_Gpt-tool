n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
k = 1
for f in range(n // 2):
    h = n - (f + 1)
    for j in range(f, h): # строка
        a[f][j] = k
        k += 1
    for i in range(f, h): # колонка
        a[i][h] = k
        k += 1
    for j in range(h, f, -1): # строка
        a[h][j] = k
        k += 1
    for i in range(h, f, -1): # колонка
        a[i][f] = k
        k += 1
if n % 2 != 0:
    a[n // 2][n // 2] = k
for i in range(n):
    print(*a[i])
 