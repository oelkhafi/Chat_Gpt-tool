
a = float (input ())
b = float (input ())
c = float (input ())
d = float (input ())
#First triangle

s1 = a*b/2

from math import sqrt

t = sqrt(a**2 + b ** 2)
p = (c+d+t)/2
s2 = sqrt(p*(p-d)*(p-c)*(p-t))

s = s1+s2
print (int(s))





 