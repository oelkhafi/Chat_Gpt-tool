def par_in_list(par, son):
    """"""Собирает всех родителей в один список""""""
    global mas
    try:
        mas += classes[son]
        for i in classes[son]:
            par_in_list(par, i)
    except:
        pass
mas, res = [], []
classes = {}
n = int(input())
for _ in range(n):
    string = input()
    if ':' in string:
        clas, parents = string.split(':')
        classes[clas.strip()] = set(parents.split())
    else:
        clas = string.strip()
        classes[clas] = {}
q = int(input())
for _ in range(q):
    par, son = input().split()
    if par == son:
        res.append('Yes')
        continue
    par_in_list(par, son)
    if par in set(mas):
        res.append('Yes')
        mas.clear()
    else:
        res.append('No')
        mas.clear()
for i in res:
    print(i)
 