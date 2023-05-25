import numpy as np


n, m = (int(i) for i in input().split())
t = np.array([[float(i) for i in input().split()] for _ in range(n)])
a, b = np.hsplit(t, (m, ))
if np.linalg.matrix_rank(a) != np.linalg.matrix_rank(t):
    print('NO')
elif np.linalg.matrix_rank(a) < m:
    print('INF')
else:
    if n == m:
        print('YES', ' '.join(str(round(*i, 5)) for i in np.linalg.solve(a, b)), sep='\n')
    else:
        x = [0] * m
        c = 0
        while c < m:
            cr = None
            for r in range(c, n):
                if cr is None or abs(t[r][c]) > abs(t[cr][c]):
                    cr = r
            if cr and cr != c:
                t[c], t[cr] = t[cr], t[c]
            t[c] = [i / t[c][c] for i in t[c]]
            for r in range(c+1, n):
                t[r] = [t[r][i] - t[c][i] * t[r][c] for i in range(m+1)]
            c += 1
        for i in range(m-1, -1, -1):
            x[i] = round(t[i][-1] - sum(x * t for x, t in zip(x[i+1:], t[i][i+1:-1])), 5)
        print('YES', ' '.join(str(i) for i in x), sep='\n')
 