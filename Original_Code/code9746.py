def Check(class_list, parent, child, path=[]):
    path = path + [child]
    if child == parent:
        return path
    if child not in class_list:
        return False
    for n in class_list[child]:
        if n not in path:
            newpath = Check(class_list, parent, n, path)
            if newpath:
                return newpath
    return False


classes = {'object': ['object']}

for i in list(input().replace(':', ' ').split() for i in range(int(input()))):
    if len(i) == 1:
        classes.update({i[0]: ['object']})
    else:
        classes.update({i[0]: i[1:]})

for i in list(input().split() for i in range(int(input()))):
    if Check(classes, i[0], i[1]):
        print('Yes')
    else:
        print('No')
 