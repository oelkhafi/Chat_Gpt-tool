# put your python code here
import sys


def area_of_triangle(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_rectangle(a, b):
    return a * b


def area_of_circle(r):
    pi = 3.14
    return pi * r * r


AREAS = {'triangle': area_of_triangle,
         'rectangle': area_of_rectangle,
         'circle': area_of_circle}

shape, *sides = sys.stdin.read().splitlines()
sides = tuple(map(float, sides))
print(AREAS[shape](*sides))
 