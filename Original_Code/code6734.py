all_parents = []
def checker(x, y):
    global all_parents

    all_parents += dict_mro[y]
    for i in dict_mro[y]:
        checker(x, i)

dict_mro = dict()
for i in range(int(input())):
    a = input().split(' ')
    if ':' in a:
        a.remove(':')
    for i in a:
        if i not in dict_mro:
            dict_mro[i] = []
    dict_mro[a[0]] = a[1:]
for i in range(int(input())):
    x, y = input().split()
    checker(x, y)
    if x in all_parents or x == y:
        print('Yes')
    else:
        print('No')
    all_parents = []

 