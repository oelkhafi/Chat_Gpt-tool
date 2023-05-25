pi = 3.14
forma = input()
if forma == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c) / 2
    s = (p*(p-a)*(p-b)*(p-c)) ** 0.5
    print(s)
elif forma == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print(s)
elif forma == 'круг':
    r = int(input())
    s = pi * (r ** 2)
    print(s)




 