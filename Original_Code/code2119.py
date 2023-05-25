n = int(input())
namesp = {
    'global': {
                'parent': None,
                'vars': set(),
                }
            }


def create(namespace, parent):
    namesp[namespace] = {
                'parent': parent,
                'vars': set(),
                }


def add(namespace, variable):
    namesp[namespace]['vars'].add(variable)


def get_ns(namespace, variable):
    while namespace is not None:
        if variable in namesp[namespace]['vars']:
            return namespace
        else:
            namespace = namesp[namespace]['parent']
    return None


for i in range(n):
    cmd, arg1, arg2 = input().split()
    if cmd == 'add':
        add(arg1, arg2)
    elif cmd == 'create':
        create(arg1, arg2)
    elif cmd == 'get':
        print(get_ns(arg1, arg2))
 