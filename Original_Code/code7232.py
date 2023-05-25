import sys


def knapsackbu(c, w, n):
    d = [[0] * c for _ in range(n)]
    for i in range(1, n):
        for j in range(1, c):
            d[i][j] = d[i - 1][j]
            if w[i - 1] <= j:
                d[i][j] = max(d[i][j], d[i - 1][j - w[i - 1]] + w[i - 1])
    return d[-1][-1]


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    capacity, n = next(reader)
    weight_list = tuple(next(reader))
    print(knapsackbu(capacity + 1, weight_list, n + 1))


if __name__ == '__main__':
    main()
 