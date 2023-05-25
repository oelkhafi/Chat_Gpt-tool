def super_L(n):
    if n <= 1: return 2 - n
    if n % 6 == 0: return L6n(n)
    if n % 5 == 0: return L5n(n)
    if n % 4 == 0: return L4n(n)
    if n % 3 == 0: return L3n(n)
    if n % 2 == 0: return L2n(n)
    L0, L1 = 2, 1
    for _ in range(1, n):
        L0, L1 = L1, L0 + L1
    return L1


def L6n(nn):
    n = nn // 6
    return super_L(n) ** 6 - (-1) ** n * 6 * super_L(n) ** 4 + 9 * super_L(n) ** 2 - (-1) ** n * 2


def L5n(nn):
    n = nn // 5
    return super_L(n) ** 5 - (-1) ** n * 5 * super_L(n) ** 3 + 5 * super_L(n)


def L4n(nn):
    n = nn // 4
    return super_L(n) ** 4 - (-1) ** n * 4 * super_L(n) ** 2 + 2


def L3n(nn):
    n = nn // 3
    return super_L(n) ** 3 - (-1) ** n * 3 * super_L(n)


def L2n(nn):
    n = nn // 2
    return super_L(n) ** 2 - (-1) ** n * 2
 