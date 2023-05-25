# put your python code here
class_num = int(input())
class_text_lines = [input().rstrip() for x in range(class_num)]
req_num = int(input())
exceptions_ = [input() for x in range(req_num)]
inherit_dict = {}
for line in class_text_lines:
    exc = line.split(':')
    exc[0] = exc[0].strip()
    if len(exc) == 1:
        inherit_dict[exc[0]] = []
    else:
        stroka = exc[1].strip()
        parents = [x.strip() for x in stroka.split(' ')]
        inherit_dict[exc[0]] = parents


def is_child_of_earlier_exception(exceptions: list) -> bool:
    length = len(exceptions)
    for i in range(0, length):
        for j in range(0, i):
            if is_parent(exceptions[i], exceptions[j]):
                print(exceptions[i])
                break


def is_parent(child: str, parent: str) -> bool:
    if child == parent:
        return True
    parents = inherit_dict[child]
    if not parents:
        return False
    for cur_parent in parents:
        condition = is_parent(cur_parent, parent)
        if condition:
            return True
        else:
            continue
    return False

is_child_of_earlier_exception(exceptions_)

 