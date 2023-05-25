import json


def reverse(inp):  # вернём граф в виде словаря {родитель: [список наследников]}
    dct = {}
    for el in inp:
        dct[el['name']] = dct.get(el['name'], [])  # чтобы не забыть при выводе про класс без наследников, для каждого класса добавим пустой список наследников
        for p in el.get('parents', []):
            dct[p] = dct.get(p, []) + [el.get('name', '')]
    return dct


def get_all_childs(p, dct, lst):
    childs = dct.get(p, [])
    for c in childs:
        if c not in lst:
            get_all_childs(c, dct, lst)
            lst.append(c)
    return lst

level1 = reverse(json.loads(input()))
[print(""{} : {}"".format(k, len(get_all_childs(k, level1, [])) + 1)) for k, v in sorted(level1.items(), key=lambda x: x[0], reverse=False)]
 