exception_mro = dict()
exception_list = []
def f(x):
    for i in exception_mro[x]:
        if i in exception_list:
            return True
    for i in exception_mro[x]:
        return f(i)

for i in range(int(input())):
    a = input().split()
    if len(a) == 1:
        exception_mro[a[0]] = []
    else:
        exception_mro[a[0]] = a[2:]
for i in range(int(input())):
    x = input()
    if f(x) == True:
        print(x)
    exception_list += [x]





 