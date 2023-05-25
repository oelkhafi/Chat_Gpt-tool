def add_namespace(child_name: str, parent_name: str):
    namespaces[child_name] = parent_name


def add_var_to_namespace(var_name: str, namesp_name: str):
    namespaces_vars[var_name] = namesp_name


def get_namespace_for_var(var_name: str, namesp_name: str)-> str:
    if namespaces_vars.get(var_name):
        if namespaces_vars[var_name] == namesp_name:
            return namesp_name
        else:
            parent = namespaces[namesp_name]
            if parent == 'None':
                return None
            else:
                return get_namespace_for_var(var_name, parent)
    else:
        return None


commands_cnt = int(input())
namespaces = {'global': 'None'} # child : parent
namespaces_vars = {}
prints = []
for i in range(0, commands_cnt):
    cmd, namesp, arg = input().strip().split()
    if cmd == 'create':
        add_namespace(namesp, arg)
    if cmd == 'add':
        add_var_to_namespace(arg, namesp)
    if cmd == 'get':
       prints.append(get_namespace_for_var(arg, namesp))
print(*prints, sep='\n') 