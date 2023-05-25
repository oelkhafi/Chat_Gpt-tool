def create(namespace, parent):
    namespaces.append({'namespace': namespace, 'parent': parent, 'var': []})

def add(namespace, var):
    for ns in namespaces:
        if ns['namespace'] == namespace and var not in ns['var']:
            ns['var'].append(var)

def get(namespace, var):
    for ns in namespaces:
        if ns['namespace'] == namespace: 
            if var in ns['var']:
                return ns['namespace']
            elif ns['parent'] == None:
                return None
            else:
                return get(ns['parent'], var)

namespaces = []
create('global', None)

for i in range(int(input())):
    cmd, par1, par2  = input().split(' ')
    if cmd == 'add':
        add(par1, par2) 
    elif cmd == 'get':
        print(str(get(par1, par2)))
    elif cmd == 'create':
        create(par1, par2)
 