s = input()
if s == 'int':
    a, b = int(input()), int(input())
    if a == 0 and b == 0:
        print('Empty Ints')
    else:
        print(a+b)
elif s == 'str':
    st = input()
    if not st:
        print('Empty String')
    else:
        print(st)
elif s == 'list':
    st2 = input().split()
    if not st2:
        print('Empty List')
    else:
        print(st2[-1])
else:
    print('Unknown type') 