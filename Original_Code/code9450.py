def triangle():
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)


def rect():
    print(int(input())*int(input()))


def circle():
    print(3.14*int(input())**2)


def shapes(shape):
    return {
        'треугольник': triangle,
        'прямоугольник': rect,
        'круг': circle
    }.get(shape, 'error')


shapes(input())()




 