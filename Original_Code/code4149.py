def create(ns, namesp, arg):
    ns[namesp] = {'parent': arg, 'vars': []}


def add(namesp, arg):
    ns[namesp]['vars'].append(arg)


def get(namesp, arg):
    if namesp in ns.keys():
        if arg in ns[namesp]['vars']:
            return print(namesp)
        elif ns[namesp]['parent'] != None:
            get(ns[namesp]['parent'], arg)
        else:
            return print(ns[namesp]['parent'])
    else:
        return print(ns['global']['parent'])


ns = {'global': {'parent': None, 'vars': []}}
n = int(input())
if 1<=n<=100:
    for i in range(n):
        cmd, namesp, arg = input().split()
        if cmd == 'get':
            get(namesp, arg)
        elif cmd == 'add':
            add(namesp, arg)
        elif cmd == 'create':
            create(ns, namesp, arg)
 