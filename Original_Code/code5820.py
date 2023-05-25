import json

json_data = input()
data = json.loads(json_data)

child_parents = dict()
parent_children = dict()
parents_list = list()

# заполняем словарь {""потомок"": [предки]}
for class_ in data:
    child_parents[class_['name']] = class_['parents']

# заполняем словарь {""предок"": [потомки]}
for child, parents in child_parents.items():
    parent_children[child] = []
    for parent in parents:
        parent_children[parent] = []
for child, parents in child_parents.items():
    for parent in parents:
        parent_children[parent].append(child)

# добавляем к потомкам их потомков
for parent in parent_children.keys():
    for child in parent_children[parent]:
        parent_children[parent] += parent_children[child]

for parent in parent_children.keys():
    parents_list.append(parent)
    parent_children[parent] = set(parent_children[parent])
    
parents_list.sort()

# +1 в результате потому что: ""гарантируется, что никакой класс не наследуется от себя явно или косвенно..."" (c) :D
for parent in parents_list:
    print(parent, ':', len(parent_children[parent]) + 1) 