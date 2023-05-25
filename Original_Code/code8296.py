ok_status = ''


def search(vocab, list1, namespace, var):
    global ok_status
    for i in list1:
        step = i.split(':')
        if step[1] == namespace:
            if var in vocab[step[0]]:
                ok_status = step[0]
                return
            else:
                search(vocab, list1, namespace=step[0], var=var)


count = int(input())
scopes = {'name': {}, 'vars': set()}
lst = []
while count != 0:
    row = input().split()
    if 'global' in row:
        if row[0] == 'create':
            scopes['name'][row[1]] = set()
        elif row[0] == 'add':
            scopes['vars'].add(row[2])
        else:
            print('global' if row[2] in scopes['vars'] else 'None')
    else:
        if 'get' not in row:
            if row[1] in scopes['name']:
                scopes['name'][row[1]].add(row[2])
            else:
                scopes['name'][row[1]] = set()
                lst.append(row[2] + ':' + row[1])
        else:
            if row[2] in scopes['name'][row[1]]:
                print(row[1])
            else:
                search(scopes['name'], lst, row[1], row[2])
                if ok_status == '' and row[2] not in scopes['vars']:
                    print('None')
                elif ok_status == '' and row[2] in scopes['vars']:
                    print('global')
                else:
                    print(ok_status)
                ok_status = ''
    count -= 1


 