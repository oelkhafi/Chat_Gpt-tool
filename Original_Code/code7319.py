def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

from collections import defaultdict

graph = defaultdict(list)

for i in range(int(input())):
    a = input().split(':')
    if len(a) == 1:
        continue
    for k in a[1].split():
        graph[a[0].strip()].append(k) 
for x in range(int(input())):
    b = input().split()
    if b[0] in (dfs(graph,b[1])):
        print('Yes')
    else:
        print('No') 