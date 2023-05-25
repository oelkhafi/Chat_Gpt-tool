n=int(input())
a=[[j+1 for j in range(n)] for i in range(n)]
i=0;j=0;cnt=0;x=n;y=0
while n-cnt>=1:
    cnt+=1
    # вниз
    i+=1;j-=1
    for y in range(x+1,x+1+(n-cnt)):
        a[i][j]=y
        i+=1
    # влево
    i-=1;j-=1
    for x in range(y+1,y+1+(n-cnt)):
        a[i][j]=x
        j-=1
    cnt+=1
    # вверх
    i-=1;j+=1
    for y in range(x+1,x+1+(n-cnt)):
        a[i][j]=y
        i-=1
    # вправо
    i+=1;j+=1
    for x in range(y+1,y+1+(n-cnt)):
        a[i][j]=x
        j+=1
for row in a:
    print(*row) 