lst = []
number_chet = None
number_ne_chet = None
n = int(input())
for i in range(n):
    x = int(input())
    lst.append(x)
    if x % 2 == 0:
        if number_chet is None:
            number_chet = x
        else:
            if x < number_chet:
                number_chet = x
    else:
        if number_ne_chet is None:
            number_ne_chet = x
        else:
            if x < number_ne_chet:
                number_ne_chet = x
res_sym = number_chet + number_ne_chet
for j in range(0, len(lst)):
    if (number_ne_chet is None) or (number_chet is None):
        break
    elif lst[j] < res_sym:
        lst[j] += res_sym
print(*lst)
 