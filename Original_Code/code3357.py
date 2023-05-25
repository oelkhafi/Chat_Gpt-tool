def check_variable(v):
    s = list(v)
    t, k = 0, 0
    for i in s:
        if i >= '0' and i <= 'z' or i == '_':
            t += 0
        else:
            t += 1
    if v[0] < 'A' or ' ' in s:
        k = 1
    else:
        k = 0
    if k + t == 0:
        text = 'Можно использовать'
    else:
        text = 'Нельзя использовать'
    return text


v = input()
while v != 'Поработали, и хватит':
    print(check_variable(v))
    v = input()
 