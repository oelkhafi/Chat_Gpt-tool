from collections import defaultdict
v,e = map(int,input().split())
E = defaultdict(lambda: [])
for _ in range(e):
    v1,v2 = map(int,input().split())
    E[v1].append(v2)
    E[v2].append(v1)
if not all(map(lambda x:len(x) and len(x)%2==0, E.values())):
    print('NONE')
else:
    visited, c = [0]*(v+1), 1
    def dfs(u):
        visited[u] = c
        for v in E[u]:
            if not visited[v]:
                dfs(v)
    for u in range(1,v+1):
        if not visited[u]:
            dfs(u)
            c += 1
    if c-1 > 1:
        print('NONE')
    else:
        cycle = []
        def euler(v):
            for w in E[v]:
                E[v].remove(w)
                E[w].remove(v)
                euler(w)
            cycle.append(v)
        euler(1)
        print(*cycle[:-1]) 