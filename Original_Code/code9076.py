db = {'': [], 'global': ['', set()]}


def name_from(variable, namespace):
    if namespace == '':
        return None
    if variable in db[namespace][1]:
        return namespace
    return name_from(variable, db[namespace][0])


for i in range(int(input())):
    cmd, namespace, arg = input().split()

    if cmd == 'create':
        parent = arg
        db[namespace] = [parent, set()]

    if cmd == 'add':
        variable = arg
        db[namespace][1].add(variable)

    if cmd == 'get':
        variable = arg
        s = name_from(variable, namespace)
        print(s)
 