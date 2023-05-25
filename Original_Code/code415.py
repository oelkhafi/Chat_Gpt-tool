import sys
lines = [map(int, line.split()) for line in sys.stdin]
n, e, d = lines[0]
parent, res = [*range(n + 1)], 1

def root(i):
    while i != parent[i]: i = parent[i]
    return i

def convolution(i, p):
    while i != p: parent[i], i = p, parent[i]

for i, j in lines[1:e+1]:
    pj = root(j)
    convolution(i, pj)
    convolution(j, pj)

for i, j in lines[e+1:]:
    res *= root(i) != root(j)

print(res) 