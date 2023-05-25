import random
from bisect import bisect_left, bisect_right

def qsort(a):
    if len(a) < 2:
        return a
    pv = random.choice(a)
    left = [i for i in a if i < pv]
    centr = [pv] * a.count(pv)
    right = [j for j in a if j > pv]
    return qsort(left) + centr + qsort(right)


n, m = map(int, input().split())
a, b = [], []
for k in range(n):
    i, j = map(int, input().split())
    a.append(i)
    b.append(j)
vert = list(map(int, input().split()))
a1, b1 = qsort(a), qsort(b)

for v in vert:
    t1 = bisect_right(a1, v)
    t2 = bisect_left(b1, v)
    print(t1-t2, end=' ') 