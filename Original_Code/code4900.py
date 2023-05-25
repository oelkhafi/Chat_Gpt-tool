n = int(input())
matrix = [[0] * n for x in range(n)]
value, m = 1, 0

matrix[n//2][n//2] = n**2

for i in range(n//2):
    for j in range(n-m):
        matrix[i][j+i] = value
        value += 1
    for j in range(i+1, n-i):
        matrix[j][-i-1] = value
        value += 1
    for j in range(i+1, n-i):
        matrix[-i-1][-j-1] = value
        value += 1
    for j in range(i+1, n-(i+1)):
        matrix[-j-1][i] = value
        value += 1
    m += 2

for row in matrix:
    print(*row)
 