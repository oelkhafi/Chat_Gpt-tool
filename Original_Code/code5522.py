def kaprekar_check(n):
    m = len(str(n))
    k = len(set(list(map(int, str(n)))))

    if n == 100 or n == 1000 or n == 100000: return False
    if ((k > 1 and k < 7) and (m == 3 or m == 4 or m == 6)): return True
    return False


def numerics(n):
    if kaprekar_check(n):
        return list(map(int, str(n)))
    else:
        return 0


def kaprekar_step(L):
    n1 = int(''.join(map(str, sorted(L))))
    n2 = int(''.join(map(str, sorted(L)))[::-1])

    return n2 - n1 if n2 > n1 else n1 - n2


def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(""Ошибка! На вход подано число "" + str(n) + "", не удовлетворяющее условиям процесса Капрекара"")
        return 0
    tmp = 0
    s = set()

    print(n)
    while n not in[495, 6174, 549945, 631764]:

        if not kaprekar_check(n):
            print(""Ошибка! На вход подано число "" + str(n) + "", не удовлетворяющее условиям процесса Капрекара"")
            return 0

        n = kaprekar_step(numerics(n))
        if n == tmp: return n
        tmp = n

        if n in s:
            print(""Следующее число - ""+str(n)+"", кажется процесс зациклился..."")
            return 0
        s.add(n)
        print(n)

 