import math

def f(x):
    return ((2*x**2)-3*x-5)/((3*x**2)+x+1)

x0=0
dx_list=[10000000000.0]
for dx in dx_list:
    lim=[]
    lim.append(round(f(x0+dx),3))
print(lim[-1])

dx_list=[-10000000000.0]
for dx in dx_list:
    lim=[]
    lim.append(round(f(x0+dx),3))
print(lim[-1])



 