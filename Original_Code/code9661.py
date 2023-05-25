class_num = int(input())
class_text_lines = [input().rstrip() for x in range(class_num)]
req_num = int(input())
req_text_lines = [input() for x in range(req_num)]

inherit_dict = {y[0].rstrip(): y[1:] for y in [a.split(sep=':') for a in class_text_lines]}
for key in inherit_dict:
    if len(inherit_dict[key]) > 0:
        var: str = inherit_dict[key][0]
        lst = var.split()
        inherit_dict[key] = lst
req_lst = [x.split() for x in req_text_lines]


def is_parent(cls_parent):
    return True


def is_parent(cls_parent: str, cls_child: str) -> bool:
    if cls_parent == cls_child:
        return True
    parents = inherit_dict[cls_child]
    if not parents:
        return False
    for parent in parents:
        condition = is_parent(cls_parent, parent)
        if condition:
            return True
        else:
            continue
    return False


for request in req_lst:
    b = False
    if len(request) == 1:
        b = is_parent(request[0])
    else:
        b = is_parent(*request)
        if b:
            print('Yes')
        else:
            print('No') 