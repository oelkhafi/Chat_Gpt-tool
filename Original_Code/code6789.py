nspc = {'global':{'parent':None, 'vars':set()}}

def create(dct, nsp, vr):
    if vr in dct.keys():
        dct[vr][nsp]={'vars':set(), 'parent':vr}
    else:
        for key in dct.keys():
            if type(dct[key]) == dict:
                for val in dct[key]:
                    if val == vr:
                        dct[key][vr][nsp]={'vars':set(), 'parent':vr}
                create(dct[key], nsp, vr)

def add(dct, nsp, vr):
    if nsp in dct.keys():
        dct[nsp]['vars'].add(vr)
    else:
        for key in dct.keys():
            if type(dct[key]) == dict:
                for val in dct[key]:
                    if val == nsp:
                        dct[key][nsp]['vars'].add(vr)
                add(dct[key], nsp, vr)

def get(dct, nsp, vr):
    global res
    if nsp in dct.keys():
        if vr in dct[nsp]['vars']:
            res = nsp
        else: 
            get(nspc, dct[nsp]['parent'], vr)
    else:
        for key in dct.keys():
            if type(dct[key]) == dict:
                for val in dct[key]:
                    if val == nsp:
                        if vr in dct[key][val]['vars']:
                            res = nsp
                        else:
                            get(nspc, dct[key][val]['parent'], vr)
                get(dct[key], nsp, vr)
for i in range(int(input())):
    cmd, nsp, vr = input().split()
    if cmd == 'create':
        create(nspc, nsp, vr)
    elif cmd == 'add':
        add(nspc, nsp, vr)
    elif cmd == 'get':
        res = None
        get(nspc, nsp, vr)
        print(res)
 