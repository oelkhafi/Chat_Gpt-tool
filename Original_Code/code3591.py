from numpy import sqrt
A = input()
pi = 3.14

def Geron():
    a,b,c = [ float(input()) for i in range(3) ]
    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))
                 
def Rect():
    a,b = [float(input()) for i in range(2)]
    return a*b

def Circle():
    r = float(input())
    return pi*r**2

if A == 'треугольник':
    print(Geron())
    
elif A == 'прямоугольник':
    print(Rect())
    
elif A == 'круг':
    print(Circle()) 