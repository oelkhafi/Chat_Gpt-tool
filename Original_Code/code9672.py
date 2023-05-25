# put your python code here
import json

raw_str = input().strip()
inh_dict = {}
data = json.loads(raw_str)
for obj in data:
    cls_name = obj[""name""]
    cls_parents = obj[""parents""]
    inh_dict[cls_name] = cls_parents

def inheritance_counter():
    count_dict = {}
    for key_cls in inh_dict:
        count_dict[key_cls] = count_of_childs(key_cls)
    return count_dict

def count_of_childs(parent_name):
    counter = 1
    for key_cls in inh_dict:
        if key_cls == parent_name:
            continue
        parents = inh_dict[key_cls]
        for parent in parents:
            if parent == parent_name:
                counter += 1
                break
            if is_parent(parent, parent_name):
                counter += 1
                break
    return counter

def is_parent(child_name, parent_name):
    parents = inh_dict[child_name]
    for parent in parents:
        if parent_name == parent:
            return True
        if is_parent(parent, parent_name):
            return True
    return False

res = inheritance_counter()
for key in sorted(res):
    print(""{0} : {1}"".format(key, res[key])) 