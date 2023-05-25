# put your python code here
n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
k = 1
oborot = 0

#количество оборотов
if n%2 == 0:
    chet = n//2
else:
    chet = n//2+1
    
for i in range(chet):
    #Верх
    for j in range(oborot,n-oborot):
        a[i][j] = k
        k += 1  
    #Право    
    for j in range(i+1,n-i):
        a[j][-i-1] = k
        k += 1
    #Низ
    for j in range(i+1,n-i):
        a[-i-1][-j-1] = k
        k += 1
    #Лево
    for j in range(i+1,n-(i+1)):
        a[-j-1][i] = k
        k += 1
    oborot += 1
    
for i in a:
    print(*i) 