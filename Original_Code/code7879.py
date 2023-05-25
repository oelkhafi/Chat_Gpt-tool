
b, c = float (input ()), float (input ())

ugol = float (input ())

from math import sin, cos, sqrt, pi

ugol = ugol / 180 * pi

a = sqrt (b ** 2 + c ** 2 - 2 * b * c * cos (ugol))

p = (a + b + c) / 2

s1 = sqrt (p * (p - a) * (p - b) * (p - c))

print ('{:5.2f}'.format (s1))

s2 = b * c * sin (ugol) / 2

print ('{:5.2f}'.format (s2))




 