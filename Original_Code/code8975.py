def numerics(n): return list(map(int,str(n)))

def kaprekar_step(L):
    L1 = list(map(str,sorted(L)))
    L2 = L1[::-1]
    a = int("""".join(L1))
    b = int("""".join(L2))
    return b - a

def kaprekar_loop(n):
    if n == 1000:
        print(""Ошибка! На вход подано число 1000"")
        return
    L1 = list(map(str,sorted(numerics(n))))
    if L1[0] == L1[3]:
        print(f""Ошибка! На вход подано число {n} - все цифры одинаковые"")
        return
    a, b = n, 0
    while a != b:
        print(a)
        a, b = kaprekar_step(numerics(a)), a 