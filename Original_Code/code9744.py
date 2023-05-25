c = [input().split() for i in range(int(input()))]# put your python code here
spaces = {'global': {'parent': None, 'vars': []}}


def add(namespace, v):
    spaces[namespace]['vars'].append(v)


def create(namespace, v):
    spaces.update({namespace: {'parent': v, 'vars': []}})


def get_from(namespace, v):
    if v in spaces[namespace]['vars']:
        return namespace
    elif v not in spaces[namespace]['vars'] and namespace == 'global':
        return None
    else:
        return get_from(spaces[namespace]['parent'], v)


for i in c:
    if i[0] == 'add':
        add(i[1], i[2])
    elif i[0] == 'create':
        create(i[1], i[2])
for i in c:
    if i[0] == 'get':
        print(get_from(i[1], i[2]))
 