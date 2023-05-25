# Принимаем строку
str = input()

# Вычисляем статистику символов
stats = {}
for s in str:
    if s not in stats:
        stats[s] = 1
    else:
        stats[s] += 1
tree = list(stats.items())

# Строим дерево
while len(tree) > 1:
    tree.sort(key=lambda i: i[1], reverse=True)
    ltree = tree.pop()
    rtree = tree.pop()
    node = [[ltree[0], rtree[0]], ltree[1] + rtree[1]]
    tree.append(node)
tree = tree[0][0]   # Убрали теперь уже ненужные веса


def bcode(tree, symbol):
    # Функция обхода дерева, возвращает код символа
    if type(tree) is not list:
        return ''
    lchild = tree[0]
    rchild = tree[1]
    if lchild == symbol:
        return '0'
    elif rchild == symbol:
        return '1'
    else:
        l = bcode(lchild, symbol)
        r = bcode(rchild, symbol)
        if l != '':
            return '0' + l
        if r != '':
            return '1' + r
        return ''


# Создаём таблицу кодов
codes = dict()
for s in stats.keys():
    code = bcode(tree, s)
    codes[s] = code
if tree == s:   # На случай, если строка состоит всего из 1 символа
    codes[s] = '1'

# Кодируем строку
result = ''
for s in str:
    result += codes[s]

# Выводим всё на печать
print(len(codes), len(result))
for s in codes:
    print(s + ':', codes[s])
print(result)
 