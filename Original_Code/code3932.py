def swap_elements(m):
    res = []
    for i in range(len(m)):
        new_row = []
        for j in range(len(m[i])):
            new_row.append(sum((m[i - 1][j], m[(i + 1) % len(m)][j],
                                m[i][j - 1], m[i][(j + 1) % len(m[i])])))
        res.append(new_row)
    return res


def read_input():
    m = []
    while True:
        line = input()
        if line == 'end':
            break
        m.append(list(map(int, line.strip().split())))
    return m


def print_result(m):
    for row in m:
        print(*row)


swapped = swap_elements(read_input())
print_result(swapped)
 