# -*- coding: utf-8 -*-

# символы исходного алфавита,
a1 = input()
# символы конечного алфавита
a2 = input()
# Делаем словарь для шифроыки
normal = dict(zip(a1, a2))
# Делаем словарь для дешивроыки
zhopa = dict(zip(a2, a1))
# Считываем для шифрования
a1 = input()
# Считываем для дешифрования
a2 = input()
# Шифруем
for i in a1:
    print(normal[i], end="""")
print()
# Дешифруем
for i in a2:
    print(zhopa[i], end="""")
 