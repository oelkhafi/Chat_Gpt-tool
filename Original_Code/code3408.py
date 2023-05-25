# put your python code here
namespaces = {'global': {'parent': None, 'var': []}}
for i in range(int(input())):
    cmd, nm, var = input().split()
    if cmd == 'create':
        namespaces[nm] = {'parent': var, 'var': []}
    elif cmd == 'add':
        namespaces[nm]['var'] += [var]
    else:
        for key in namespaces.keys():
            if var in namespaces[nm]['var']:
                print(nm)
                break
            elif var not in namespaces[nm]['var'] and namespaces[nm]['parent'] != None:
                nm = namespaces[nm]['parent']
                if var in namespaces[nm]['var']:
                    print(nm)
                    break
            else:
                print(None)
                break



 