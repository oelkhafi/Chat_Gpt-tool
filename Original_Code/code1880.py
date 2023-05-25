s_X = [1, 1, 0, -1, -1, -1, 0, 1]
s_Y = [0, 1, 1, 1, 0, -1, -1, -1]
n, m = map(int, input().split())
field, new_field = [], []

for i in range(n):
    line = input()
    field.append([])
    for j in range(m):
        field[i].append(line[j])

for i in range(n):
    new_field.append([])
    for j in range(m):
        new_field[i].append([])

for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            count = 0
            for k in range(8):
                if field[(i + s_Y[k]) % n][(j + s_X[k]) % m] == 'X':
                    count += 1
            new_field[i][j] = 'X' if count == 3 else '.'

        if field[i][j] == 'X':
            count = 0
            for k in range(8):
                if field[(i + s_Y[k]) % n][(j + s_X[k]) % m] == 'X':
                    count += 1
            new_field[i][j] = 'X' if count == 2 or count == 3 else '.'

for p in range(n):
    print(''.join(new_field[p]))
 