def numerics(n):
    return [int(k) for k in str(n)]

def kaprekar_step(L):
    L = sorted(L)
    L_obr = list(reversed(L))
    chislo1 = int(''.join((str(i) for i in L)))
    chislo2 = int(''.join((str(i) for i in L_obr)))
    if chislo1 > chislo2:
        return chislo1 - chislo2
    else:
        return chislo2 - chislo1

true_len = [3,4,6]
false_num = [100, 1000, 100000]
kaprekar_nums = [495, 6174, 549945, 631764]


def kaprekar_check(n):
    if len(str(n)) in true_len:
        if n not in false_num:
            if len(set(numerics(n))) >= 2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def kaprekar_loop(n):
    loop_lst = []
    while True:
        if not kaprekar_check(n):
            print('Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара'.format(n))
            break
        if n not in kaprekar_nums:
            if n in loop_lst:
                print('Следующее число - {}, кажется процесс зациклился...'.format(n))
                break
            else:    
                print(n)
                loop_lst.append(n)
                n = kaprekar_step(numerics(n))
        elif n in kaprekar_nums:
            print(n)
            break



 