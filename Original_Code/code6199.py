def luka(n):
    L0, L1 = 2, 1
    for i in range(n):
        L0, L1 = L1, L0 + L1
    return L0

def L6n(n):
    n //= 6
    Ln = super_L(n)
    return Ln ** 6 - 6 * (-1) ** n * Ln ** 4 + 9 * Ln ** 2 - 2 * (-1) ** n

def L5n(n):
    n //= 5
    Ln = super_L(n)
    return Ln ** 5 - 5 * (-1) ** n * Ln ** 3 + 5 * Ln

def L4n(n):
    n //= 4
    Ln = super_L(n)
    return Ln ** 4 - 4 * (-1) ** n * Ln ** 2 + 2

def L3n(n):
    n //= 3
    Ln = super_L(n)
    return Ln ** 3 - 3 * (-1) ** n * Ln

def L2n(n):
    n //= 2
    Ln = super_L(n)
    return Ln ** 2 - 2 * (-1) ** n

def super_L(n):
    if n < 2:
        return luka(n)
    elif not n % 6:
        return L6n(n)
    elif not n % 5:
        return L5n(n)
    elif not n % 4:
        return L4n(n)
    elif not n % 3:
        return L3n(n)
    elif not n % 2:
        return L2n(n)
    else:
        return luka(n) 