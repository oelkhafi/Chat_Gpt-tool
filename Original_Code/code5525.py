def super_L(n):
    if n in [0]:
        return 2
    if n in [1]:
        return 1
    elif n in [2]:
        return 3
    elif n % 6 in [0]:
        n /= 6
        n=int(n)
        return super_L(n) ** 6 - 6 * (-1) ** n * super_L(n) ** 4 + 9 * super_L(n) ** 2 - 2*(-1) ** n
    elif n % 5 in [0]:
        n /= 5
        n = int(n)
        return super_L(n) ** 5 - 5 * (-1) ** n * super_L(n) ** 3 + 5 * super_L(n)
    elif n % 4 in [0]:
        n /= 4
        n = int(n)
        return super_L(n) ** 4 - 4 * (-1) ** n * super_L(n) ** 2 + 2
    elif n % 3 in [0]:
        n /= 3
        n = int(n)
        return super_L(n) ** 3 - 3 * (-1) ** n * super_L(n)
    elif n % 2 in [0]:
        n /= 2
        n = int(n)
        return super_L(n)**2 - 2*(-1)**n
    else: return super_L(n - 2) + super_L(n - 1) 