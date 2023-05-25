n=int(input())
a=[[0 for j in range(n)] for i in range(n)]
i=0 #строки
j=0 #столбцы
k=1 #значения ячеек
d=0 #ограничение на движение по направлению
while k<=n**2: #цикл движения вправо
    while j<(n-d) and k<=n**2:
        a[i][j]=k
        k+=1
        if j==(n-d-1):
            break
        else:
            j+=1
    i+=1
    while i<(n-d-1) and k<=n**2: #цикл движения вниз
        a[i][j]=k
        k+=1
        if i==(n-d-1):
            break
        else:
            i+=1
    while j>=(0+d) and k<=n**2: #цикл движения влево
        a[i][j]=k
        k+=1
        if j==(0+d):
            break
        else:
            j-=1
    i-=1
    while i>=(0+d) and k<=n**2: #цикл движения вверх
        a[i][j]=k
        k+=1
        if i==(0+d+1):
            break
        else:
            i-=1
    j+=1
    d+=1
for f in range(n):
    for g in range(n):
        print(a[f][g], end=' ')
    print()
 