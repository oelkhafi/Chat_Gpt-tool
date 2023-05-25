import json


def graph(parent, result):
    result.add(parent)
    for child in objects[parent] - result:
        graph(child, result)
    return result


data = json.loads(input())
T_NAME = 'name'
T_PARENTS = 'parents'
objects = {}

for row in (data):
    child = row[T_NAME]
    if child not in objects:
        objects[child] = set()
    for parent in row[T_PARENTS]:
        if parent not in objects:
            objects[parent] = set()
        objects[parent].add(child)
        
for parent in sorted(objects.keys()):
    print(parent, ':', len(graph(parent, set())))




 