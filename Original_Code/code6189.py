import json

kids = set()

def find_child(parent, kids, clr_set=False):
    if clr_set:
        kids = set()
        kids.add(parent)
    for c in child[parent]:
        kids.add(c)
        kids = find_child(c, kids)
    return kids

json_str = json.loads(input())
child = {}
for js in json_str:
    if js['name'] not in child: child[js['name']] = []
    for jp in js['parents']:
        if jp not in child: child[jp] = []
        child[jp].append(js['name'])
for key in sorted(child.keys()):
    kids = find_child(key, kids, clr_set=True)
    print(key, ':', len(kids)) 