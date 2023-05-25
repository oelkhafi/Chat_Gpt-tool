import json

data = json.loads(input())
t_name = 'name'
t_parents = 'parents'
objects = {}

def graph(parent, result):
    result.add(parent)
    for child in objects[parent] - result:
        graph(child, result)
    return result

for row in (data):
    child = row[t_name]
    if child not in objects:
        objects[child] = set()
    for parent in row[t_parents]:
        if parent not in objects:
            objects[parent] = set()
        objects[parent].add(child)

for parent in sorted(objects.keys()):
    print(parent, ':', len(graph(parent, set())))






 