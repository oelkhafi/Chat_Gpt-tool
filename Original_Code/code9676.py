def super_L(n):
    if n % 6 == 0:
        n = int(n/6)
        return super_L(n)**6 - 6*(-1)**n*super_L(n)**4 + 9*super_L(n)**2 - 2*(-1)**n
    if n % 5 == 0:
        n = int(n/5)
        return super_L(n)**5 - 5*(-1)**n*super_L(n)**3 + 5*super_L(n)
    if n % 4 == 0:
        n = int(n/4)
        return super_L(n)**4 - 4*(-1)**n*super_L(n)**2 + 2
    if n % 3 == 0:
        n = int(n/3)
        return super_L(n)**3 - 3*(-1)**n*super_L(n)
    if n % 2 == 0:
        n = int(n/2)
        return super_L(n)**2 - 2*(-1)**n
    return luka(2,1,n)

def luka(L0, L1, n):
    if n == 0: return L0
    if n == 1: return L1
    Ln = L0 + L1
    Ln_1 = L1
    Ln_2 = L0
    if n == 2: return Ln
    for i in range(3, n + 1):
        Ln_2 = Ln_1
        Ln_1 = Ln
        Ln = Ln_1 + Ln_2
    return Ln 