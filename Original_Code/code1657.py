def numerics(n):
    return [int(i) for i in str(n)]


def kaprekar_step(L):
    return int(''.join(str(i) for i in sorted(L, reverse=True))) - \
           int(''.join(str(i) for i in sorted(L)))


def kaprekar_loop(n):
    x = set()
    if n in {495, 6174, 549945, 631764}:
        print(n)
    elif len(str(n)) not in {3, 4, 6} or n in {100, 1000, 100000} or len({int(i) for i in str(n)}) == 1:
        print(""Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара"".format(str(n)))
    else:
        while True:
            if n not in x:
                print(n)
                x.add(n)
                n = numerics(n)
                n = kaprekar_step(n)
            elif n in {495, 6174, 549945, 631764}:
                break
            elif n in x:
                print('Следующее число - {}, кажется процесс зациклился...'.format(str(n)))
                break 