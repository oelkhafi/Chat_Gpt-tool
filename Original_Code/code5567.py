def numerics(n):
    return list(map(int, str(n)))
    
def kaprekar_step(n):
    low = list(map(str, sorted(numerics(n))))
    up = low[::-1]
    return int(''.join(up))- int(''.join(low))
    
def kaprekar_loop(n):
    if kaprekar_check(n):
        print(n)
        check = []
        while n not in (495, 6174, 549945, 631764):
            n = kaprekar_step(n)
            if n in check:
                print(f'Следующее число - {n}, кажется процесс зациклился...')
                break
            check.append(n)
            print(n)

def kaprekar_check(n):
    if n == 1000 or len(set(numerics(n))) == 1 or n in (100, 1000, 100000):
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
        return False
    return True
 