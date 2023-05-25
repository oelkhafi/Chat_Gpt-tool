from collections import defaultdict
from queue import Queue
v, e = map(int,input().split())
E, dist, colors, q = defaultdict(lambda: []), [0]*v, [0]*v, Queue()
for _ in range(e):
    v1, v2 = map(int,input().split())
    E[v1].append(v2)
    E[v2].append(v1)
def bfs(u):
    q.put(u)
    colors[u] = 1
    while not q.empty():
        w = q.get()
        for z in E[w]:
            if not colors[z]:
                colors[z] = 1
                dist[z] = dist[w] + 1
                q.put(z)
        colors[w] = 1
bfs(0)
print("" "".join(map(str,dist))) 