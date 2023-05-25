#1 Исходные данные
parents = {'global': 'None'}
variables = {'global': []}
requests, get = [], []
#2 Ввод запросов
for i in range(int(input())):
    requests.append(input().lower().split())
#3 Заполнение parents, variables и get
for i in range(len(requests)):
    if requests[i][0] == 'create':
        parents[requests[i][1]] = requests[i][2]
    elif requests[i][0] == 'add' and requests[i][1] not in variables:
        variables[requests[i][1]] = [requests[i][2]]
    elif requests[i][0] == 'add' and requests[i][1] in variables:
        variables[requests[i][1]].append(requests[i][2])
    elif requests[i][0] == 'get':
        get.append(requests[i])
        del requests[i][0]
#4 Поиск пространств имён, ближайших для переменных
for i in range(len(get)):
    ns = get[i][0]
    var = get[i][1]
    while True:
        if ns in variables:
            if var in variables[ns]:
                print(ns)
                break
            elif var not in variables[ns]:
                ns = parents[ns]
        elif ns not in parents and var in variables['global']:
            print('global')
            break
        elif ns not in parents and var not in variables['global']:
            print('None')
            break
        elif ns not in variables:
            ns = parents[ns] 