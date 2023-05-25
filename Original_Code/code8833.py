n = int(input())
x = y = 0
s = 1
world_2d = ([[0 for x in range(n)] for y in range(n)])
world_2d[0][0] = 1
while s < (n**2):
    while (x + 1) != n and world_2d[y][x + 1] == 0:
        x += 1
        s += 1
        world_2d[y][x] = s
    while (y + 1) != n and world_2d[y + 1][x] == 0:
        y += 1
        s += 1
        world_2d[y][x] = s
    while x != 0 and world_2d[y][x - 1] == 0:
        x -= 1
        s += 1
        world_2d[y][x] = s
    while y != 0 and world_2d[y - 1][x] == 0:
        y -= 1
        s += 1
        world_2d[y][x] = s
for y in range(n):
    for x in range(n):
        print(world_2d[y][x], end=' ')
    print()
 