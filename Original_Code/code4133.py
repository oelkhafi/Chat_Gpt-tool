n, z = int(input()), 1
dy = dx = x = 0
dn = n
a = [[0 for j in range(n)] for i in range(n)]
while z <= n**2:
        for y in range(dy,dn):
            a[x][y] = z
            y += 1
            z += 1
        for x in range(dx,(dn-1)):
            x += 1
            y = dn-1
            a[x][y] = z
            z += 1
        for y in range((dn-1),dy,-1):
            y -= 1
            a[x][y] = z
            z += 1
        for x in range((dn-1),(dn-(n-1)+dy+dx),-1):
            x -= 1
            a[x][y] = z
            z += 1
        dy += 1
        dn -= 1
        dx += 1
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
 