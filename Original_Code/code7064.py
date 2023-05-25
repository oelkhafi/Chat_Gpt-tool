def numerics(n):
    return list(map(int, str(n)))

def is_kaprekar_number_correct(n):
    is_length_correct = len(str(n)) in [3, 4, 6]
    is_digits_different = len(set(str(n))) != 1
    is_value_correct = n not in [100, 1000, 100000]
    return is_length_correct and is_digits_different and is_value_correct

def is_kaprekar_looped_in(n):
    try:
        if n in is_kaprekar_looped_in.sequence:
            return True
    except AttributeError:
        is_kaprekar_looped_in.sequence = []
    is_kaprekar_looped_in.sequence.append(n)
    return False
    
def kaprekar_step(L):
    number = ''.join(map(str, sorted(L)))
    return abs(int(number) - int(number[::-1]))

def kaprekar_loop(n):
    if not is_kaprekar_number_correct(n):
        print(""Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара"".format(n))
        return
    if is_kaprekar_looped_in(n):
        print(""Следующее число - {}, кажется процесс зациклился..."".format(n))
        return
    print(n)
    if n in [495, 6174, 549945, 631764]:
        return n
    number = numerics(n)
    result = kaprekar_step(number)
    result = kaprekar_loop(result)
 