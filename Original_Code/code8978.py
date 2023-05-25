def kaprekar_check(n):
    str1 = str(n)
    if len(str1) not in [3, 4, 6]: return False
    if len(set(x for x in str1)) == 1: return False
    if n in[100, 1000, 100000]: return False
    return True

def numerics(n): return list(map(int,str(n)))

def kaprekar_step(L):
    L1 = list(map(str,sorted(L)))
    L2 = L1[::-1]
    a = int("""".join(L1))
    b = int("""".join(L2))
    return b - a

def kaprekar_loop(n):
    if not kaprekar_check(n):
        print( f""Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара"")
        return
    L = []
    a = n
    while a not in L:
        print(a)
        L.append(a)
        a = kaprekar_step(numerics(a))
    if L[-1] != a: print(f""Следующее число - {a}, кажется процесс зациклился..."")



 