m = []
while True:
    inp = input()
    if inp == 'end':
        break
    m.append([int(i) for i in inp.split()])

r = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]

for i in range(len(m)):
    for j in range(len(m[i])):
        for d_i in (-1, 0, 1):
            for d_j in (-1, 0, 1):
                if d_i in (-1, 1) and d_j == 0 or d_i == 0 and d_j in (-1, 1):
                    r_i = i + d_i if i + d_i < len(m) else 0
                    r_j = j + d_j if j + d_j < len(m[i]) else 0
                    r[i][j] += m[r_i][r_j]

for row in r:
    print(*row, sep='\t')
 