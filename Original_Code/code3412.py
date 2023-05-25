# put your python code here
n = int(input())
matrix = [[0]*n for i in range(n)]
x, i, j = 1, 0, 0
while x <= n**2:
    matrix[i][j] = x
    if (i + j < n-1) and i <= j+1:
        j += 1
    elif (j + i >= n-1) and i < j:
        i += 1
    elif (i + j > n-1) and i >= j:
        j -= 1
    else:
        i -= 1
    x += 1
for el in matrix:
    print(*el)



 