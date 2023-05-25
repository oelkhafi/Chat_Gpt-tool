def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_step(L):
    L = sorted(map(str,L))
    return int(''.join(L[::-1]))-int(''.join(L))

def kaprekar_check(n):
    L=numerics(n)
    if len(L) in (3,4,6) and len(set(L)) != 1 and n not in (100,1000,100000):
        return True
    else:
        return False

def kaprekar_loop(n):
    setk={0}
    if not kaprekar_check(n):
        print(""Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара"".format(n))
        return
    while True:
        if n in (495, 6174, 549945, 631764) and n not in setk:
            print(n)
            break
        if n in setk:
            print(""Следующее число - {}, кажется процесс зациклился..."".format(n))
            break
        else:
            if len(numerics(n)) == 6:
                setk.add(n)
        print(n)
        L = numerics(n)
        n = kaprekar_step(L)
 