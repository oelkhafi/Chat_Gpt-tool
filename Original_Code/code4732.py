a = sorted([int(i) for i in input().split()])   # сортируем введённый список
i = 1                                           # присваиваем счётчику 1, так как будем идти с конца списка
n = len(a)                                      # вводим изначальную длину списка, чтобы программа каждый раз её не считала
if n == 1:                                      # если список состоит из одного элемента, то
    del a[0]                                    # удаляем его
while i < n:                                    # перебираем список от последнего до второго элемента 
    if a[n-i] != a[n-i-1]:                      # если элемент неравен предыдущему, то
        del a[n-i]                              # удаляем его
        i += 1                                  # переходим к предыдущему элементу
        if i == n:                              # если элемент первый, то
            del a[0]                            # удаляем и его
            break                               # заканчиваем цикл
    elif a[n-i] == a[n-i-1]:                    # если же элемент равен предыдущему, то
        while a[n-i] == a[n-i-1]:               # перебираем равные элементы
            del a[n-i]                          # удаляя каждый, если предыдущий равен ему
            i += 1                              # переходим к предыдущему элементу
            if i == n:                          # если он оказался первым, то
                break                           # заканчиваем цикл
            if i == n - 1:                      # если элемент второй, то
                del a[0]                        # удаляем первый
                i = n                           # переходим на него
                break                           # и заканчиваем цикл
        i += 1                                  # переходим к следующему элементу, чтобы сохранить один из повторяющихся элементов
if len(a) != 0:                                 # если список не пуст, то
    for i in a:                                 # все элементы получившегося списка
        print(i, end=' ')                       # выводим на печать
else:                                           # инече
    print()                                     # выводим пустую строку
 