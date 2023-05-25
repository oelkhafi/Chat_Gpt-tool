def wisdom_multiplication(x, y, length_check=True):
    a = 100 - x
    b = 100 - y
    
    first_part = str(100 - a - b)
    second_part = str(a * b)

    if length_check:
        if len(second_part) < 2:
            second_part = f""0{second_part}""
    
    return int(first_part + second_part)


def multiplication_check(x, y, length_check=True):
    return wisdom_multiplication(x, y, length_check) == x * y


def multiplication_check_list(start=10, stop=99, length_check=True):
    n, m = 0, 0
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            if multiplication_check(x, y, length_check):
                n += 1
            else:
                m += 1

    print(""Правильных результатов:"", n)
    print(""Неправильных результатов:"", m) 