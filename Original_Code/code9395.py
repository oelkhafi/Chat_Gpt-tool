def is_parent(dct, parent, child):
    # Предварительные проверки
    parents = dct.get(child, None)
    if parents is None:
        return False
    elif parent == child:
        return True
    # Основные проверки
    if parent in parents:
        return True
    else:
        for new_child in parents:
            if is_parent(dct, parent, new_child):
                return True
        return False

def check(dct, ex_list, child):
    for parent in ex_list:
        if is_parent(dct, parent, child):
            return True
    return False


dct = {}
ex_list = list()

# Ввод данных
n = int(input())
for _ in range(n):
    lst = input().split()
    dct[lst[0]] = lst[2:]

# Ввод запросов и вывод ответа
q = int(input())
for _ in range(q):
    ex = input()
    if ex in ex_list:
        continue
    elif check(dct, ex_list, ex):
        ex_list.append(ex)
        print(ex)
    else:
        ex_list.append(ex) 