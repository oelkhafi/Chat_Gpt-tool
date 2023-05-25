# put your python code here
tree_origin, tree_parents, lst_parents = {}, {}, []
for i in range(int(input())):
    s = input().split()
    tree_origin[s[0]] = s[2:] if len(s) > 1 else []

def find_path(start, path):
    for node in tree_origin[start]:
        if node not in path:
            path.add(node)
            find_path(node, path)

for el in tree_origin:
    way = set()
    find_path(el, way)
    tree_parents[el] = list(way)

for ever in range(int(input())):
    s = input()
    if s not in lst_parents:
        lst_parents.append(s)
        for val in tree_parents[s]:
            if val in lst_parents:
                print(s)
                break

 