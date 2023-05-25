import sys
from math import inf

def dijkstra(V, start, W):
    d = [inf] * (len(V) + 1)
    d[start] = 0
    Q = set(V)

    while len(Q) > 0:
        u = min(Q, key=lambda v: d[v])
        Q.discard(u)
        for v in Q:
            if (u, v) in W:
                d_u_v = d[u] + W[(u, v)]
                if d[v] > d_u_v:
                    d[v] = d_u_v
    return d


def main():
    v, w = map(int, input().split())
    W = {}
    V = set(range(1, v + 1))
    for k in range(w):
        i, j, weight = map(int, input().split())
        W[(i, j)] = weight
    start, end = map(int, input().split())

    dists = dijkstra(V, start, W)
    print(-1 if dists[end] == inf else dists[end])


if __name__ == ""__main__"":
    main()
 