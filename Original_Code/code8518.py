# put your python code here
a = [int(i) for i in input().split()]
a.sort()
repeated = []
x = 0
if len(a) == 1:
    print() #если только одно число, ничего не выводится
else:
    for e in a:
        x += 1 #счетчик, чтобы сравнивать числа только справа от переменной
        if x == len(a):
            break #если прошли все числа, больше сравнивать не нужно
        elif e in repeated:
            continue #если число уже в списке повторяющихся, больше его проверять не нужно
        else:
            j = a[x] #число с индексом на один больше индекса переменной, которую мы сравниваем
            if e == j:
                repeated.append(e) #если переменная и следующая равны (а у нас числа отсортированы по возрастанию), то добавляем переменную в список повторяющихся
    for e in repeated:
        print(e, end = ' ')



 