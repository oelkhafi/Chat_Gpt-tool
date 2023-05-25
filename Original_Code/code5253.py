n = int(input())
lst = [[0 for j in range(n)] for i in range(n)]
i,j,k = 0,0,1
l,p,v,niz = 0,0,0,0
while True:
    lst[i][j]=k
    k+=1
    suuum = 0
    for ii in range(n):
        for jj in range(n):
            if lst[ii][jj]==0:
                suuum+=1
    if suuum == 0:
        break
    if p!=0:#вправо
        if n>j+1:
            if lst[i][j+1]==0:
                j+=1
                continue
            else:
                p=0
        else:
            p=0
    elif niz!=0:#вниз
        if n>i+1:
            if lst[i+1][j]==0:
                i+=1
                continue
            else:
                niz=0
        else:
             niz=0
    elif l!=0:#влево
        if 0<j:
            if lst[i][j-1]==0:        
                j-=1
                continue
            else:
                l=0
        else:
            l=0
    elif v!=0:#вверх
        if lst[i-1][j]==0:
            if lst[i-1][j]==0:
                i-=1
                continue
            else:
                v=0
        else:
            v=0
    else:
        l,p,v,niz = 0,0,0,0
    if n>j+1:        #вправо
        if lst[i][j+1]==0:
            j+=1
            p=1
            continue
    if n>i+1:#вниз
        if lst[i+1][j]==0:
            i+=1
            niz=1
            continue
    if 0<j:#влево
        if lst[i][j-1]==0:
            j-=1
            l=1
            continue
    if 0<i:#вверх
        if lst[i-1][j]==0:
            i-=1
            v=1
            continue
    break
for i in range(n):
    for j in range(n):
        print(lst[i][j],end="" "")
    print() 