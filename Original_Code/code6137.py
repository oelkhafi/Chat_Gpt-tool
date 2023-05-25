n = int(input())
a = []
chet = []
nechet = []
#### Находит четные и нечетные и строим из них 2 списка.
for i in range(n):
    a.append(int(input()))
for i in a:
    if i % 2 == 0:
        chet.append(i)
    else:
        nechet.append(i)
#### Добавляем в список 0,если список получился пустой.
if len(chet) == 0:
    chet.append(0)
if len(nechet) == 0:
    nechet.append(0)
#### Находим минимум обоих списков и складываем.
sum = min(chet) + min(nechet)
#### Прибавляем сумму к элементам списка.
for i in range(n):
    if a[i] < sum:
        a[i] = a[i] + sum
#### Выводим их по одному, через пробел.
for i in range(n):
    print(a[i], end="" "")
 