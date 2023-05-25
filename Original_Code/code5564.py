def numerics(n):
    return list(map(int, str(n)))
    
def kaprekar_step(n):
    l = numerics(n)
    low = list(map(str, sorted(l)))
    up = low[::-1]
    return int(''.join(up))- int(''.join(low))
    
def kaprekar_loop(n):
    if check(n):
        print(n)
        while n != 6174:
            n = kaprekar_step(n)
            print(n)

def check(n):
    if n == 1000:
        print('Ошибка! На вход подано число 1000')
        return False
    if len(set(numerics(n))) == 1:
        print(f'Ошибка! На вход подано число {n} - все цифры одинаковые')
        return False
    return True
 