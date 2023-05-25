def numerics(n):
    #your code
    return [n % 10, n // 10 % 10, n // 100 % 10, n // 1000 % 10]

def kaprekar_step(L):
    #your code
    L.sort()
    return ((1000*L[3] + 100*L[2] + 10*L[1] + L[0]) - (1000*L[0] + 100*L[1] + 10*L[2] + L[3]))

def kaprekar_loop(n):
    #your code
    if n <= 1000:
        print(""Ошибка! На вход подано число 1000"")
        return
    if numerics(n)[0] == numerics(n)[1] and numerics(n)[2] == numerics(n)[3] and numerics(n)[0] == numerics(n)[3]:
        print(f""Ошибка! На вход подано число {n} - все цифры одинаковые"")
        return
    while n != 6174:
        print(n)
        n = kaprekar_step(numerics(n))
    print(n) 