def numerics(n):
    return [int(k) for k in str(n)]

def kaprekar_step(L):
    L = sorted(L)
    L_obr = list(reversed(L))
    chislo1 = int(''.join((str(i) for i in L)))
    chislo2 = int(''.join((str(i) for i in L_obr)))
    if chislo1 > chislo2:
        return chislo1 - chislo2
    else:
        return chislo2 - chislo1

def kaprekar_loop(n):
    while True:
        if n == 1000:
            print('Ошибка! На вход подано число 1000')
            break
        if len(set(numerics(n))) < 2:
            print('Ошибка! На вход подано число {} - все цифры одинаковые'.format(n))
            break
        if n != 6174:
            print(n)
            n = kaprekar_step(numerics(n))
        elif n == 6174:
            print(n)
            break 