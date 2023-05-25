import json


def is_parent(classes_dict, parent, child):
    d = classes_dict
    if parent == child or parent in d[child]:
        return True
    else:
        for sub_child in d[child]:
            if sub_child in d and is_parent(d, parent, sub_child):
                return True

            
js = json.loads(input())

classes_dict = {}
for el in js:
    classes_dict[el['name']] = el['parents']

lst = []
for el1 in classes_dict.keys():
    count = 0
    for el2 in classes_dict.keys():
        if is_parent(classes_dict, el1, el2):
            count += 1
    lst.append(el1 + ' : ' + str(count))
lst.sort()
print('\n'.join(lst))
 