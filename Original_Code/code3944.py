def get_edit_distance(a, b):
    len_a = len(a) + 1
    len_b = len(b) + 1
    matrix = [[0 for _ in range(len_b)] for _ in range(len_a)]
    for x in range(len_a):
        matrix[x][0] = x
    for y in range(len_b):
        matrix[0][y] = y

    for x in range(1, len_a):
        for y in range(1, len_b):
            if a[x - 1] == b[y - 1]:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1],
                    matrix[x][y - 1] + 1
                )
            else:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1] + 1,
                    matrix[x][y - 1] + 1
                )
    return matrix[len_a - 1][len_b - 1]


print(get_edit_distance(input(), input()))
 