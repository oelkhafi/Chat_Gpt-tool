''set relations of exeption classes'''


n = int(input())  # number of classes

exeptions_dict = {}  # {child: parents}
for i in range(n):

    '''reading and parsing'''
    stdin = input().split(':')
    child = stdin[0].strip()
    parents = set()
    if len(stdin) == 2:
        parents.update(stdin[1].split())

    '''write to the dict'''
    if child in exeptions_dict:
        exeptions_dict[child].update(parents)
    else:
        exeptions_dict[child] = parents


'''checking relations of exeption classes'''


def is_parent(classes_dict, parent, child):
    d = classes_dict
    if parent == child or parent in d[child]:
        return True
    else:
        for sub_child in d[child]:
            if sub_child in d and is_parent(d, parent, sub_child):
                return True


m = int(input())  # number of exceptions processed
stack = []
for i in range(m):
    exeption = input()
    for i in stack:
        if is_parent(exeptions_dict, i, exeption):
            print(exeption)
            break
    stack.append(exeption)
 