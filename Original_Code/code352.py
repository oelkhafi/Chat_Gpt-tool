def neighbors(x, y):
    k = -1 if world[x][y] == 'X' else 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if world[(x + dx) % n][(y + dy) % m] == 'X':
                k += 1
    return k


def life(n, m, world):
    new_world = [[world[i][j] for j in range(m)] for i in range(n)]
    for x in range(n):
        for y in range(m):
            k = neighbors(x, y)
            if k == 3:
                new_world[x][y] = 'X'
            elif k == 2:
                new_world[x][y] = world[x][y]
            else:
                new_world[x][y] = '.'
    return new_world


if __name__ == '__main__':
    n, m = map(int, input().split())
    world = [list(map(str, input())) for _ in range(n)]
    print(*(''.join(row) for row in life(n, m, world)), sep='\n')
 