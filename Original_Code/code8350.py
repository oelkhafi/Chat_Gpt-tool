def foo(namespace, var):
    '''
    рекурсивная функция, возвращает
    либо 'None' если в итоге namespace не найдено в словарях
    либо namespace если var найдено в dct_ns = {namespace:[..., var, ...], ...:[..., ...]}
    либо вызывает саму себя
        или с аргументами foo(<parent namespace>, var) для поиска в родительском пространстве имён
        или foo(None, var) если <parent namespace> не найдено в словаре dct_ns
    '''
    if namespace is None:
        return 'None'
    if var in dct_vr.get(namespace, []):
        return namespace
    else:
        return foo(dct_ns.get(namespace, None), var)

lst = [input() for i in range(int(input()))]

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
        otv.append(foo(cmd[1], cmd[2]))  # добавляем ответ в список ответов

[print(el) for el in otv]  # вывод ответов по-строчно
 