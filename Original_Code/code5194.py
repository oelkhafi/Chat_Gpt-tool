''set relations of classes'''


n = int(input())  # number of classes

classes_dict = {}  # {child: parents}
for i in range(n):

    '''reading and parsing'''
    stdin = input().split(':')
    child = stdin[0].strip()
    parents = set()
    if len(stdin) == 2:
        parents.update(stdin[1].split())

    '''write to the dict'''
    if child in classes_dict:
        classes_dict[child].update(parents)
    else:
        classes_dict[child] = parents


'''checking relations of classes'''


def is_parent(classes_dict, parent, child):
    d = classes_dict
    if parent == child or parent in d[child]:
        return True
    else:
        for sub_child in d[child]:
            if sub_child in d and is_parent(d, parent, sub_child):
                return True


q = int(input())  # number of requests
for i in range(q):
    class_1, class_2 = input().split()
    print('Yes' if is_parent(classes_dict, class_1, class_2) else 'No')
 