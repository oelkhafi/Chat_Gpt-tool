import sys
from collections import defaultdict
sys.setrecursionlimit(8000)
E,v = defaultdict(lambda: []),0
for line in sys.stdin:
    v1, v2 = map(int, line.split())
    E[v1].append(v2)
    E[v2].append(v1)
    v = max(v - 1, max(v1,v2)) + 1
visited, up, tin, time, cutpoint = [0]*v, [0]*v, [0]*v, 0, set()
def dfs(w, p):
    global time
    time += 1
    up[w] = tin[w] = time
    visited[w],count = 1,0
    for u in E[w]:
        if visited[u]:
            up[w] = min(up[w], tin[u])
        else:
            dfs(u, w)
            count += 1
            up[w] = min(up[w], up[u])
            if p != -1 and up[u] >= tin[w]:
                cutpoint.add(w)
        if p == -1 and count >= 2:
            cutpoint.add(w)
for i in range(v):
    if not visited[i]:
        dfs(i, -1)
print(*cutpoint) 