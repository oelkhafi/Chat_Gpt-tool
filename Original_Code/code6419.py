n = int(input())
a = [[0]*n for i in range(n)] #пустая матрица n*n
s = 0 #счётчик заполнитель матрицы
m = 0 #поправка
b = n*n 
while s != b:
    for i in range(n):#право начиная с первой ячейки a[0][0]
        a[0+m][i+m] = s+1
        s +=1
    for i in range(1,n):#вниз
        a[i+m][n-1+m] = s+1
        s +=1
    for i in range(1,n):#влево
        a[n-1+m][n-1-i+m] = s+1
        s +=1
    for i in range(1,n-1):#вверх
        a[n-1-i+m][-n-m] = s+1
        s +=1
    n=n-2
    m=m+1

for i in range(int(b**0.5)):
    print(*a[i]) 