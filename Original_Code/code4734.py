n = int(input())
a = [[0 for i in range(n)] for i in range(n)]
k = 1
m = n
i = 0
j = 0
while k <= n**2:
    for s in range(m):
        a[i][j] = k
        k += 1
        j += 1
    i += 1
    j -= 1
    m -= 1
    for s in range(m):
        a[i][j] = k
        k += 1
        i += 1
    i -= 1
    j -= 1
    for s in range(m):
        a[i][j] = k
        k += 1
        j -= 1
    i -= 1
    j += 1
    m -= 1
    for s in range(m):
        a[i][j] = k
        k += 1
        i -= 1
    i += 1
    j += 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
 