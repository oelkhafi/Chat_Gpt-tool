n = int(input())
sl_v = {'None':['global']} # Родитель : NameSpace
sl = {'global':[]} # NameSpace : переменные


def get(ns, x):
    if x in sl[ns]:
        print(ns)

    elif x not in sl[ns] and ns == 'global':
        print('None')

    else:
        for key in sl_v.keys():
            if ns in sl_v[key]:
                
                if x in sl[key]:
                    print(key)
                else:
                    get(key,x)


for req in range(n):
    req = input().split()

    if req[0] == 'create': # NameSpace Родитель

        if req[2] in sl_v and req[1] not in sl_v[req[2]]:
            sl_v[req[2]].append(req[1])
            sl[req[1]] = []
        else:
            sl_v[req[2]] = [req[1]]
            sl[req[1]] = []

    elif req[0] == 'add': # NameSpace Переменная

        if req[1] in sl and req[2] not in sl[req[1]]:
            sl[req[1]].append(req[2])

    elif req[0] == 'get': # NameSpace Переменная

        get(req[1], req[2])
 