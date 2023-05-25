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


def check(dct, parent, child):

    if is_parent(dct, parent, child):
        return 'Yes'
    else:
        return 'No'


dct = {}

# Ввод данных
n = int(input())
for _ in range(n):
    lst = input().split()
    dct[lst[0]] = lst[2:]

# Ввод запросов и вывод ответа
q = int(input())
for _ in range(q):
    parent, child = input().split()
    print(check(dct, parent, child))
 