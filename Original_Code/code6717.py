a, b = int(input()), 1
c = [[0 for j in range(a)] for i in range(a)]
x, y, z = 0, 0, 0
while b <= a**2:
    for i in range(a):
        for j in range(a-z):
            c[x][y] = b
            b += 1
            y += 1
        y -= 1
        x += 1
        z += 1
        for j in range(a-z):
            c[x][y] = b
            b += 1
            x += 1
        y -= 1
        x -= 1
        for j in range(a-z):
            c[x][y] = b
            b += 1
            y -= 1
        y += 1
        x -= 1
        z += 1
        for j in range(a-z):
            c[x][y] = b
            b += 1
            x -= 1
        x += 1
        y += 1

for i in c:
    print(*i)



 