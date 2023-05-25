n = int(input())
b = [[0 for j in range(n)] for i in range(n)]
k=0
top,bottom,left = False,False,False
right=True
yr=0 
xr1=0 
xr2=n-1
yb1=1 
yb2=n-1 
xb=n-1
yl=n-1 
xl1=2
xl2=n
yt1=2
yt2=n-1
xt=0
while True:
    if k==n**2:break
    if right:
        for j in range(xr1,xr2+1):
            k+=1
            b[yr][j] = k
        xr1+=1
        xr2-=1
        yr+=1
        right = False
        bottom = True
        continue
    if bottom:
        for i in range(yb1, yb2+1):
            k+=1
            b[i][xb] = k
        yb1+=1
        yb2-=1
        xb-=1
        bottom = False
        left = True
        continue
    if left:
        for j in range(xl1,xl2+1):
            k+=1
            b[yl][-j]=k
        xl1+=1
        xl2-=1
        yl-=1
        left = False
        top = True
        continue
    if top:
        for i in range(yt1,yt2+1):
            k+=1
            b[-i][xt] = k
        yt1+=1
        yt2-=1
        xt+=1
        top = False
        right = True
        continue
for i in b:
    print(*i) 