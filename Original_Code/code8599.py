def par_in_list(par, son):
    """"""Собирает всех родителей в один список""""""
    global mas
    try:
        mas += child_dict[son]
        for i in child_dict[son]:
            par_in_list(par, i)
    except:
        pass

import json
pars_string = json.loads(input())
class_dict = {}
child_dict = {}
mas = []
for i in pars_string:
    class_dict[i['name']] = i[""parents""]
# формируем словарь с детьми, сначала создаём пустые списки
for key in class_dict.keys():
    child_dict[key] = []
# в списки заносем дочерние классы, словарь родители: [дети]
for k in child_dict.keys():
    for key, val in class_dict.items():
        if k in val:
            child_dict[k].append(key)
res = {}
for i in child_dict.keys():
    mas.clear()
    for j in child_dict.keys():
        par_in_list(j, i)
        res[i] = list(set(mas))
keyses = list(child_dict.keys())
keyses.sort()
for i in keyses:
    print(i, ':', str(len(res[i]) + 1)) 