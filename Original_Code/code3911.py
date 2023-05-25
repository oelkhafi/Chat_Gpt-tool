from math import sqrt


def rectangle_area():
    a, b = int(input()), int(input())
    return a * b


def triangle_area():
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def circle_area():
    r = int(input())
    return 3.14 * (r ** 2)


shape_fun = {'rectangle': rectangle_area,
             'circle': circle_area,
             'triangle': triangle_area}


print(shape_fun[input()]())

 