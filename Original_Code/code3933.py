def read_input():
    a = []
    for i in range(int(input().strip().split()[0])):
        a.append(list(map(int, input().strip().split())))
    i, j = map(int, input().strip().split())
    return a, i, j


def swap_cols(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]
    return a


def print_result(a):
    for row in a:
        print(*row)


print_result(swap_cols(*read_input()))
 