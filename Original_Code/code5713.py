import json
d = {}
li = json.loads(input())
for i in range(len(li)):
    for parent in li[i][""parents""]:
        if parent in d.keys():
            d[parent].add(li[i][""name""])
        else:
            d[parent] = {li[i][""name""]}


def count_parents(start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex in d.keys():
                queue.extend(d[vertex] - visited)
            else:
                pass
    return len(visited)

l = set()
for k, v in d.items():
    l.add(k)
    l = l | v

for i in sorted(l):
    print(i + "" : "" + str(count_parents(i))) 