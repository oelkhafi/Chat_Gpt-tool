import sys


def merge(lf, rt):
    count_inv = lf.pop() + rt.pop()
    temp = []
    while lf and rt:
        if lf[0] > rt[0]:
            count_inv += len(lf)
            temp.append(rt.pop(0))
        else:
            temp.append(lf.pop(0))
    temp.extend(lf) if lf else temp.extend(rt)
    temp.append(count_inv)
    return temp


def qty(qu):
    count = 0
    if len(qu) == 1:
        qu.append(count)
        return qu
    else:
        left = qu[:len(qu) // 2]
        right = qu[len(qu) // 2:]
        return merge(qty(left), qty(right))


def qty_of_inversions():
    n = int(sys.stdin.readline())
    q = list(map(int, sys.stdin.readline().split()))
    assert len(q) == n
    print(qty(q)[-1])


if __name__ == '__main__':
    qty_of_inversions()
 