a = input()
if a == 'прямоугольник':
    b = float(input())
    c = float(input())
    print(b * c)
if a == 'треугольник':
    b = float(input())
    c = float(input())
    d = float(input())
    p = (b + c + d) / 2
    S = (p * (p - b) * (p - c) * (p - d)) ** .5
    print(S)
if a == 'круг':
    b = float(input())
    p = 3.14
    print(p * (b ** 2))
    



 