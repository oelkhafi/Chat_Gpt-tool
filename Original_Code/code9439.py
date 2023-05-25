n=int(input())
z=[]
for i in range(n):
    s=input().split(' ')
    z+=[s]
x=0
y=0
for j in range(len(z)):
    if z[j][0]=='север':
        y+=int(z[j][1])
    elif z[j][0]=='юг':
        y-=int(z[j][1])
    elif z[j][0]=='восток':
        x+=int(z[j][1])
    elif z[j][0]=='запад':
        x-=int(z[j][1])
print(x,y)



 