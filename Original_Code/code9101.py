def kaprekar_n(n, counted_n):
    if n in [495, 6174, 549945, 631764]:
        return
    nlist = list(str(n))
    n1 = ''.join(sorted(nlist))
    n2 = ''.join(sorted(nlist, reverse=True))
    new_n = abs(int(n1) - int(n2))
    if new_n in counted_n:
        print('Следующее число - {0}, кажется процесс зациклился...'.format(new_n))
        return
    counted_n.add(new_n)
    print(new_n)
    kaprekar_n(new_n, counted_n)


def kaprekar_loop(n):
    if n in [100, 1000, 100000] or len(str(n)) not in [3, 4, 6] or len(
            set(str(n))) == 1:
        print(
            'Ошибка! На вход подано число {0}, не удовлетворяющее условиям '
            'процесса Капрекара'.format(n))
        return False
    print(n)
    kaprekar_n(n, {n}) 