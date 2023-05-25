from sys import stdin
from collections import defaultdict

def cut_points(edges):
    adj = defaultdict(set)
    nv = 0
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
        nv = max(nv, a+1, b+1)
    cuts = set()
    visited = [False] * nv

    for root in adj.keys():
        if visited[root]:
            continue
        cur_val = 0
        k_val = [None] * nv
        l_val = [None] * nv

        root_degree = 0
        visited[root] = True
        k_val[root] = l_val[root] = cur_val
        cur_val += 1
        stack = [(None, root, iter(adj[root]))]

        while stack:
            grand, parent, children = stack[-1]
            for child in children:
                if visited[child]:
                    if k_val[child] < k_val[parent]:  # back edge
                        l_val[parent] = min(l_val[parent], k_val[child])
                    continue
                visited[child] = True
                if parent == root:
                    root_degree += 1
                k_val[child] = l_val[child] = cur_val
                cur_val += 1
                stack.append((parent, child, iter(adj[child])))
                break
            else:
                stack.pop()
                if grand is not None and grand != root:
                    l_val[grand] = min(l_val[grand], l_val[parent])
                    if l_val[parent] >= k_val[grand] and grand != root:
                        cuts.add(grand)
        if root_degree > 1:
            cuts.add(root)
    return sorted(cuts)

print(*cut_points(map(int, s.split()) for s in stdin)) 