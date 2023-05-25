prn_numbers = set()

def numerics(n):
    return list(map(int, str(n)))

def kaprekar_check(n):
    return len(str(n)) in (3, 4, 6) and n not in (100, 1000, 100000) and len(set(numerics(n))) > 1

def kaprekar_step(L):
    str_sort = ''.join(map(str, sorted(L)))
    return int(str_sort[::-1])-int(str_sort)

def kaprekar_loop(n):
    global prn_numbers
    if n not in prn_numbers: prn_numbers.add(n)
    if kaprekar_check(n):
        print(n)
        if n not in {495, 6174, 549945, 631764}:
            next_kaprekar = kaprekar_step(numerics(n))
            if next_kaprekar in prn_numbers:
                print(""Следующее число - {}, кажется процесс зациклился..."".format(next_kaprekar))
            else:
                kaprekar_loop(next_kaprekar)
    else:
        print(""Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара"".format(n)) 