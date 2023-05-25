import sys


def binary_search(a, d, x):
    l, r = 0, len(d) - 1
    while l <= r:
        m = l + (r - l) // 2
        if a[d[m]] < x:
            r = m - 1
        elif a[d[m]] >= x:    
            l = m + 1
    return l


def restoreindex(r, k, n):
    res = [k + 1]
    for i in range(n - 1):
        res.insert(0, r[k] + 1)
        k = r[k]
    return res


def lds_nlogn(a, n):
    d = [0]
    r = [-1] * n
    for i in range (1, n):
        if a[i] <= a[d[-1]]:
            r[i] = d[-1]
            d += [i]
        elif a[i] > a[d[0]]:
            d[0] = i
        else:
            j = binary_search(a, d, a[i])
            d[j] = i
            r[i] = d[j - 1]
    return restoreindex(r, d[-1], len(d))


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, = next(reader)
    lst = next(reader)
    seq = lds_nlogn(lst, n)
    print(len(seq))
    print(*seq)


if __name__ == '__main__':
    main()
 