import copy
a, b, c, z = [input().strip()], [], [], 0
while 'end' not in a:
    a += input().strip().split('\n')
for i in range(len(a)-1):
    b.append(a[i].split( ))
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])
c = copy.deepcopy(b)
for i in range(len(b)):
    for j in range(len(b[i])):
        for di in range(-1, 2, 2):
#            if di == -1 and len(b) == 2:
#                di = 0
            bi = (i + di)%len(b)
            z += b[bi][j]
        for dj in range(-1, 2, 2):
#            if dj == -1 and len(b[i]) == 2:
#                dj = 0
            bj = (j + dj)%len(b[i])
            z += b[i][bj]
        c[i][j] = z
        z = 0
for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j], end=' ')
    print()
 