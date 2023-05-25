import json


def get_parent(name):
    for x in db:
        if x['name'] == name:
            return x
    return None


def find_children(parent):
    children = set()
    for child in parent['children']:
        children.add(child)
        children = children.union(find_children(get_parent(child)))
    return children


db = json.loads(input())

for child in db:
    child['children'] = set()

for child in db:
    for name in child['parents']:
        parent = list(filter(lambda x: x['name'] == name, db))[0]
        parent['children'].add(child['name'])

print(*sorted(map(lambda x: f""{x['name']} : {len(find_children(x)) + 1}"", db)), sep='\n')
 