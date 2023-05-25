t=int(input())
n,m,b,k,s,y,x=0,0,1,-2,-1,t,t
z=[[0 for j in range(0,y)] for i in range(0,y)]
while t>=1:
    for j in range(m,t):
        z[-x][j]=n+1
        n+=1
    for i in range(b,t):
        z[i][x-1]=n+1
        n+=1
    for j in range(k,-t,-1):
        z[x-1][j]=n+1
        n+=1
    for i in range(s,-t,-1):
        z[i][-x]=n+1
        n+=1
    t-=1
    x-=1
    m+=1
    k-=1
    b+=1
    s-=1
for i in range(y):
    for j in range(y):
        print(z[i][j],end=' ')
    print()




 