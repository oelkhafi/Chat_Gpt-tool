n = int(input())
parents = list(map(int, input().split()))
distance = [0 for _ in range(n)]
nodes = dict()

# развернули все указатели
for i, parent in enumerate(parents):
    if parent not in nodes:
        nodes[parent] = {i}
    else:
        nodes[parent].add(i)

# выполнили обход в ширину
max_distance = 0
queue = [nodes[-1].pop()]
while queue:
    el = queue.pop(0)
    if el not in nodes:
        continue
    for child in nodes[el]:
        queue.append(child)
        distance[child] = distance[el] + 1

print(max(distance) + 1) 