root = (""global"", True)
objects = {root: {}}


def enum_objects_paths():
    stack = [(objects, root, iter(objects[root]))]
    while stack:
        objs, start, children = stack[-1]
        try:
            end = next(children)
            stack.append((objs[start], end, iter(objs[start][end])))
        except StopIteration:
            yield [(o, s) for o, s, _ in stack]
            stack.pop()


def insert_object(parent, target):
    o = min(filter(lambda p: parent in [s[1] for s in p], enum_objects_paths()), key=len)[-1]
    o[0][o[1]].update({target: {}})


def get_object(ns, var):
    objs = min(filter(lambda p: ns in [s[1] for s in p], enum_objects_paths()), key=len)
    for o in reversed(objs):
        if var in o[0][o[1]]:
            return o[1][0]
    return None


for i in range(int(input())):
    c, ns, v = input().strip().split()
    {""create"": lambda y, x: insert_object((x, True), (y, True)),
     ""add"": lambda x, y: insert_object((x, True), (y, False)),
     ""get"": lambda x, y: print(get_object((x, True), (y, False)))}[c](ns, v) 