mem = {'global': [None,]}
n = int(input())
for i in range(n):
    cmd, scope, parm = map(str, input().split())
    if cmd == 'create':
         mem.update ({scope : [parm]})
    elif cmd == 'add':
        mem [scope].append(parm)
    else:
        find = None;
        while scope != None and find == None:
            var = mem [scope]
            for i in range (1, len (var)):
                if var [i] == parm:
                    find = scope
                    break
            scope = mem [scope] [0]
        print (find)




 