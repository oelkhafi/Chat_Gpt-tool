n, m = [int(i) for i in input().split()]
mx = [[0]*m for _ in range(n)]
c = 1
for _ in range(min(n, m)-1):
    i = 0
    for j in range(_, -1, -1):
        mx[i][j] = c
        mx[n-1-i][m-1-j] = n*m - c + 1
        i = i+1
        c += 1
if m<n:
    for _ in range(n-m+1):
        i = _
        for j in range(m-1, -1, -1):
            mx[i][j] = c
            i = i+1
            c += 1
else:
    pass
    for _ in range(n-1, m):
        j = _
        for i in range(n):
            mx[i][j] = c
            j = j-1
            c += 1
                 
print('\n'.join(''.join(' '*(4 - len(str(el)))+str(el) for el in row) for row in mx)) 