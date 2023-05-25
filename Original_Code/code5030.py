import numpy as np
import numpy.linalg as la

m = int(input())

X = np.empty((m, m))
y = np.empty(m)

for i in range(m):
    xi, yi = map(float, input().split())
    for j in range(m):
        X[i, j] = xi ** j
    y[i] = yi

c = la.solve(X, y)
print(*c)




 