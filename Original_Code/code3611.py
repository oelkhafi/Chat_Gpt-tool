# create foo global
def funk_cmd(name, arg):
    if arg == 'global':
        dict_namesp[None] = [arg]
        if arg in dict_namesp:
            if name not in dict_namesp[arg]:
                dict_namesp[arg] += [name]
        else:
            dict_namesp[arg] = [name]
    else:
        if arg in dict_namesp:
            if name not in dict_namesp[arg]:
                dict_namesp[arg] += [name]
        else:
            dict_namesp[arg] = [name]
    return dict_namesp

def funk_arg(name, arg):
    if name in dict_arg:
        if arg not in dict_arg[name]:
            dict_arg[name] += [arg]
    else:
        dict_arg[name] = [arg]
    return dict_arg
    
def funk_get(name, arg):
    if name in dict_arg and arg in dict_arg[name]:
        return name
    else:
        for key, value in dict_namesp.items():
            if name in value:
                if name is not None:
                    return funk_get(key, arg)
                else:
                    return None
        
n, k = int(input()), 0
dict_namesp = {}
dict_arg = {}
while k!= n:
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        funk_cmd(namesp,arg)
    elif cmd == 'add':
        funk_arg(namesp,arg)
    elif cmd == 'get':
        print(funk_get(namesp,arg))
    
    k+=1
 