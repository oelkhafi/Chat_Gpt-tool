def numerics(n):
    #your code
    s = str(n)
    return [int(x) for x in s]

def kaprekar_step(L):
    #your code
    s1 = sorted(L)
    s2 = sorted(L, reverse = True)
    s1 = ''.join([str(x) for x in s1])
    s2 = ''.join([str(x) for x in s2])
    return int(s2) - int(s1)
    

def kaprekar_loop(n):
    s = numerics(n)
    c = s[0]
    sm = 0
    for d in s:
        if d == c:
            sm += 1
    if n <= 1000:
        print(""Ошибка! На вход подано число 1000"")
        return
    if sm == 4:
        print (""Ошибка! На вход подано число "" + str(n) + "" - все цифры одинаковые"")
        return
    while True:
        print(n)
        if n == 6174:
            break
        l = numerics(n)
        k = kaprekar_step(l)
        n = k
         