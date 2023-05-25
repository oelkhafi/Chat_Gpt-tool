glob = [{'global': '', 'vars': [], 'parent': None}]
def create(namespace, parent):
    glob.append({namespace: '', 'vars': [], 'parent': parent})
def add(namespace, var):
    for i in glob[::-1]:
        if namespace in i:
            i['vars'].append(var)
            break
def get(namespace, var):
    for i in glob[::-1]:
        if namespace in i:
            if var in i['vars']:
                return namespace
            else:
                return get(i['parent'], var)
        elif i['parent'] == None:
            return None
for i in range(int(input())):
    c = input().split()
    if 'get' in c:
        print(globals().get(c[0])(c[1], c[2]))
    else:
        globals().get(c[0])(c[1], c[2])
 