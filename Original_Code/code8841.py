def add(space, var):
    global data
    data[space].append(var)
    return


def create(new_space, parent):
    global data
    data[new_space] = [parent]
    return


def get(space, var):
    while True:
        if var in data[space]:
            print(space)
            return
        if space == 'global':
            print('None')
            return
        space = data[space][0]


n = int(input())
data = {'global': []}
for x in range(n):
    a, b, c = map(str, input().split())
    eval(a)(b, c)
exit() 