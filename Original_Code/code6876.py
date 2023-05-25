cmds = ['create','add','get']
spacenames = {'global':None}
spacevars = {'global':[]}
n = int(input())
for i in range(n):
    cmd, namespace, varpar = input().split()
    if cmds.index(cmd) == 0: #create
        if varpar in spacenames:
            spacenames[namespace] = varpar
            spacevars[namespace] = []
    if cmds.index(cmd) == 1: #add
        if namespace in spacevars:
            spacevars[namespace]+=[varpar]
    if cmds.index(cmd) == 2: #get
        if spacevars.get(namespace) == None:
            print('None')
        else:
            while True:
                if varpar in spacevars[namespace]:
                    print(namespace)
                    break
                else:
                    if namespace != 'global':
                        namespace = spacenames[namespace]
                    else:
                        print('None')
                        break 