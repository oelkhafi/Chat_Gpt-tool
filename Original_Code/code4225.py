def numerics(n):
    return [int(i) for i in str(n)] 

def kaprekar_step(L):
    min_number_str = ''.join(map(str, sorted(L)))
    return int(min_number_str[::-1]) - int(min_number_str)

def kaprekar_check(n):
    if len(numerics(n)) not in [3,4,6]:
        return False
    if len(set(numerics(n))) == 1:        
        return False
    if n in [100, 1000, 100000]:
        return False
    return True

def kaprekar_loop(n):
    #your code
    if not kaprekar_check(n):
        print(""Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара"".format(n))
        return
    l = []
    while n not in l:
        l.append(n)
        n = kaprekar_step(numerics(n))
    print(*l,sep='\n')        
    if n != l[-1]:
        print('Следующее число - {}, кажется процесс зациклился...'.format(n))
    



 