def numerics(n):

    return list(map(int,str(n)))

def kaprekar_step(L):
    n1 = int(''.join(map(str, sorted(L))))
    n2 = int(''.join(map(str, sorted(L)))[::-1])

    return n2 - n1 if n2 > n1 else n1 - n2



def kaprekar_loop(n):

    if n == 1000:
        print(""Ошибка! На вход подано число 1000"")
        return 0
    if len(set(list(map(int,str(n))))) == 1:
        print(""Ошибка! На вход подано число ""+ str(n) + "" - все цифры одинаковые"")
        return 0
    
    print(n)
    while n!=6174:
        n = kaprekar_step(numerics(n))
        print(n)
       
 