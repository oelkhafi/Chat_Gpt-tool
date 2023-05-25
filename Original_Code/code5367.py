#!/usr/bin/env python3
# coding=utf-8


import sys


# as input numbers are abs(n) <= 100
INF = 101


def row_max_sum(row):
    cur_sum = max_sum = -INF

    for element in row:
        cur_sum = max(element, cur_sum + element)
        max_sum = max(max_sum, cur_sum)

    return max_sum


def get_max_sum(matrix):
    row_length = len(matrix[0])
    matrix_length = len(matrix)
    max_sum = -INF

    for i in range(matrix_length):
        cur_row = [0 for i in range(row_length)]
        for j in range(i, matrix_length):
            cur_row = [x + y for x, y in zip(cur_row, matrix[j])]
            cur_sum = row_max_sum(cur_row)

            if cur_sum > max_sum:
                max_sum = cur_sum

    return max_sum


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    M, N = next(reader)
    matrix = [next(reader) for _ in range(M)]
    print(get_max_sum(matrix))


if __name__ == ""__main__"":
    main()
 