n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]
y = x = 0
lst = [x for x in range(1, n*n+1)]
w = 0

while lst:
    for i in range(x, n):
        x = i
        matrix[y][x] = lst.pop(0)
    if y < n:
        y += 1
    for i in  range(y, n):
        matrix[y][x] = lst.pop(0)
        if y < n-1:
            y += 1
    n -= 1
    x -= 1
    for i in range(n-1, w-1, -1):
        matrix[y][x]=lst.pop(0)
        if x > w:
            x -= 1
    w += 1
    y -= 1
    for i in range(n-1, w-1, -1):
        matrix[y][x]=lst.pop(0)
        if y > w: 
            y -= 1
    x += 1
for el in matrix:
    for z in el:
        print(z, end=' ')
    print()
 