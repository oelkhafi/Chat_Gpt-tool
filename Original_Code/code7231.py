import sys


def diff(ai, bj):
    if ai == bj:
        return 0
    return 1 


def editdistbu(a, b):
    n, m = len(a) + 1, len(b) + 1
    d = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        d[i][0] = i
    for j in range(m):
        d[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            c = diff(a[i - 1], b[j - 1])
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c)
    return d[n - 1][m - 1]
    


def main():
    reader = (tuple(line.strip()) for line in sys.stdin)
    a = next(reader)
    b = next(reader)
    print(editdistbu(a, b))


if __name__ == '__main__':
    main()
 