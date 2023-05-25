# put your python code here
n = int(input())
a = [[i for i in range(1, n+1)] for j in range (n)]
c, row, col = 0, 0, 0
if n % 2 != 0:
    x = int((n - 1) / 2)
    y = int((n - 1) / 2)
else:
    x = int(n / 2)
    y = int(n / 2 - 1)
while a[x][y] < n**2:
    for i in range(row+1, n-row):
        c += 1
        a[i][n - 1 - row] = a[0+row][n - 1 - row] + c
    c = 0
    for i in range(0+col, n - 1 - col):
        c += 1
        a[n - 1 - col][i] = a[n - 1 - col][n - 1 - col] + n - c - 2*col
    c = 0
    for i in range(1+row, n - 1-row):
        c += 1
        a[i][0+row] = a[n-1-row][0+row] + n - 1 - 2*row - c
    row += 1
    c = 0
    for i in range(1+col, n - 1-col):
        c += 1
        a[1+col][i] = a[1+col][0+col] + c
    col += 1
    c = 0
for i in a:
    for el in i:
        print(el, end=' ')
    print()



 