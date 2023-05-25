def numerics(n):
    return list(map(int, str(n)))

def kaprekar_step(L):
    less = ''.join(map(str, sorted(L)))
    return int(less[::-1]) - int(less)

def kaprekar_check(n):
    return n not in [100, 1000, 100000] \
        and len(numerics(n)) in [3, 4, 6] \
        and len(set(str(n))) != 1

def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
        return

    numbers = set()
    print(n)
    while n not in [495, 6174, 549945, 631764]:
        numbers.add(n)
        n = kaprekar_step(numerics(n))
        if n in numbers:
            print(f'Следующее число - {n}, кажется процесс зациклился...')
            break
        print(n)
 