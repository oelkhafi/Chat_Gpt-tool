import sys


def prev(n):
    dev3 = n // 3 if n % 3 == 0 else 0
    dev2 = n // 2 if n % 2 == 0 else 0
    return (dev3, dev2, n - 1)


def calc_step(n):
    d = [1e6] + [0] * n
    for i in range(2, n + 1):
        d[i] = min(d[prev(i)[0]], d[prev(i)[1]], d[prev(i)[2]]) + 1
    return d


def restore_chain(a, n, k):
    b = [n]
    for i in range(k, 0, -1):
        n = [j for j in prev(n) if a[j] == i - 1][0]
        b.insert(0, n)
    return b


def main():
    n = next(int(line) for line in sys.stdin)
    lst = calc_step(n)
    print(lst[n])
    print(*restore_chain(lst, n, lst[n]))


if __name__ == '__main__':
    main()
 