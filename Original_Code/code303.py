import sys

from random import randint


def partition(seq):
    _ = randint(0, len(seq) - 1)
    seq[0], seq[_] = seq[_], seq[0]
    j, k = 0, 0
    for i in range(1, len(seq)):
        if seq[i] <= seq[0]:
            k += 1
            seq[i], seq[k] = seq[k], seq[i]
            if seq[k] < seq[0]:
                j += 1
                seq[k], seq[j] = seq[j], seq[k]
    seq[0], seq[j] = seq[j], seq[0]
    return j, k


def quick_sort(seq):
    if len(seq) <= 1:
        return seq

    m, n = partition(seq)
    return quick_sort(seq[:m]) + seq[m:n + 1] + quick_sort(seq[n + 1:])


def middle(p, q, lt, rt):
    if lt == rt:
        if q[lt] <= p and lt == len(q) - 1:
            lt += 1
        return lt
    delta = (rt - lt) // 2
    m = lt + delta
    if q[m] > p:
        rt = m
    elif q[m] == p:
        if p != q[m + 1]:
            lt = m + 1
        else:
            if delta:
                lt = m
            else:
                lt = rt
    else:
        if delta:
            lt = m
        else:
            lt = rt
    return middle(p, q, lt, rt)


def point_in_segments():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data.pop(0), data.pop(0)
    left = data[:2 * n:2]
    right = data[1:2 * n:2]
    points = data[2 * n:]
    lt = quick_sort(left)
    rt = quick_sort(right)
    result = []
    for point in points:
        if point < lt[0] or point > rt[-1]:
            result.append(0)
        else:
            result.append(
                middle(point, lt, 0, n - 1) - middle(point - 1, rt, 0, n - 1)
            )
    return result


if __name__ == '__main__':
    print(' '.join(map(str, point_in_segments())))
 