def f_no_recurse(namespace, var):
    '''
    нерекурсивная функция, если переменная var не нашлась в текущем namespace
    ф-я заменяет namespace на родительский namespace из словаря dct_ns до тех пор,
    пока не найдёт var или не достигнет предела пространств имён (None)
    '''
    while var not in dct_vr.get(namespace, []):  # будем повышать namespace пока не встретим в нём переменную var
        namespace = dct_ns.get(namespace, None)
        if namespace is None:  # если повышать уже некуда, прервём цикл
            break
    return namespace

# # для отладки раскомментировать
# lst = [
#     'add global a',
#     'add global X',
#     'create foo global',
#     'add foo b',
#     'get foo a',  # global
#     'get foo c',  # None
#     'create bar foo',
#     'add bar a',
#     'get bar a',  # bar
#     'get bar b',  # foo
# ]

lst = [input() for i in range(int(input()))]

otv = []  # список ответов
dct_ns = {}  # {'bar': 'foo', 'foo': 'global'}
dct_vr = {}  # {'bar': ['a'], 'global': ['a', 'X'], 'foo': ['b']}
for el in lst:
    cmd = el.split()
    if cmd[0] == 'add':
        dct_vr[cmd[1]] = dct_vr.get(cmd[1], []) + [cmd[2]]

    if cmd[0] == 'create':
        dct_ns[cmd[1]] = cmd[2]  # ПИ: РОДИТЕЛЬ_ПИ

    if cmd[0] == 'get':
        otv.append(f_no_recurse(cmd[1], cmd[2]))  # добавляем ответ в список ответов

[print(el) for el in otv]  # вывод ответов по-строчно
 