import copy
n = abs(int(input()))
a = []
k = 1
c = 0
r = -1
m = copy.deepcopy(n)
for i in range(n):
    a.append([])
    for l in range(0, n):
      a[i].append([])

while k <= m*m:
    if n-1 <= c:
        n += 1
    for col in range(c, n-1):
        a[c][col] = k
        k += 1
    if k < m*m:
        for row in range(c, n-1):
            a[row][r] = k
            k += 1
        for col in range(r, -n, -1):
            a[r][col] = k
            k += 1
        for row in range(r, -n, -1):
            a[row][c] = k
            k += 1
    n -= 1
    c += 1
    r -= 1

for row in range(0, len(a)):
    for col in range(0, len(a[0])):
        print(a[row][col], end=""\t"")
    print()




 