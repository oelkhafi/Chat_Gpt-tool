import math

FIGURE = input()
PI = 3.14

def rectangle(a, b):
    return a * b

def triangle(a,b,c):
    p = (a + b + c) // 2
    return math.sqrt((p*(p-a)*(p-b)*(p-c)))
    
def circle(r):
    return r**2 * PI

if FIGURE == 'прямоугольник':
    print(rectangle(int(input()), int(input())))
          
elif FIGURE == 'треугольник':
     print(triangle(int(input()), int(input()), int(input())))
        
elif FIGURE == 'круг':
    print(circle(int(input())))



 