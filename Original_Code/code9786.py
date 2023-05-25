ns = {'global': {'parent':'', 'vars': []}}

def func(*args):
    def create(namespace, parent):
        if not namespace in ns.keys():
            ns.update({namespace: {'parent': parent}})

    def add(namespace, var):
        if namespace in ns.keys():
            if not 'vars' in ns[namespace].keys():
                ns[namespace].update({'vars':[var]})
            else:
                ns[namespace]['vars'].append(var)

    def get(namespace, var):
        if namespace == '':
            return None
        elif 'vars' in ns[namespace].keys() and var in ns[namespace]['vars']:
            return namespace
        else:
            return get(ns[namespace]['parent'], var)

    ff = {'create': create, 'add': add, 'get': get}
    ff[args[0]](args[1], args[2]) if args[0] != 'get' else print(ff[args[0]](args[1], args[2]))


n = int(input())
for i in range(n):
    func(*input().split()) 