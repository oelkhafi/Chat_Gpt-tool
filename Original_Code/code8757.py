a = int(input())
b = []
for i in range(a):
    b.append([])
    for j in range(a):
        b[i].append(0)
c = 1
d = 0
while c <= a ** 2:
    for i in range(d, a - d):
        b[d][i] = c
        c += 1
    for i in range(d, a - 1 - d):
        b[i + 1][a - 1 - d] = c
        c += 1
    for i in range(a - 1 - d, d, -1):
        b[a - 1 - d][i - 1] = c
        c += 1
    for i in range(a - 1 - d, d + 1, -1):
        b[i - 1][d] = c
        c += 1
    d += 1
for i in range(len(b)):
    print(*b[i]) 