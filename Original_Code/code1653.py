def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_step(L):
    return int(''.join(str(i) for i in sorted(L, reverse=True))) - \
           int(''.join(str(i) for i in sorted(L)))

def kaprekar_loop(n):
        if n == 6174:
            print (n)
        elif n <= 1000:
            print(""Ошибка! На вход подано число 1000"")
        elif len({int(i) for i in str(n)}) == 1:
            print(""Ошибка! На вход подано число {} - все цифры одинаковые"".format(str(n)))
        else:
            while n != 6174:
                print(n)
                n = numerics(n)
                n = kaprekar_step(n)
            print(n)
 