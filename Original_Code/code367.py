n, k, z = int(input()), 0, 0
matrix = [[0 for _ in range(n)] for _ in range(n)]
while n - 2 * k > 1:
    for j in range(k, n - k - 1):
        z += 1
        matrix[k][j] = z
    for i in range(k, n - k - 1):
        z += 1
        matrix[i][n - k - 1] = z
    for j in range(n - 1 - k, k, -1):
        z += 1
        matrix[n - 1 - k][j] = z
    for i in range(n - 1 - k, k, -1):
        z += 1
        matrix[i][k] = z
    k += 1
if n % 2:
    z += 1
    matrix[k][k] = z
for item in matrix:
    print(*item)




 