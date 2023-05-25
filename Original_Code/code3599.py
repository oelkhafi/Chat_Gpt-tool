n = int(input())
k,h,L = 1, 0, [[0 for j in range(n)] for i in range(1,n+1)]
while h < n:   
    for i in range(h,n-1-h):
        for j in range(h,n-1-h):
            if i == h:
                L[i][j] = k
                k+=1            
        L[i][n-1-h] = k
        k+=1          
    for i in range(h+1,n-h):
        for j in range(h+1,n-h):
            if i == h+1:
                L[-1-h][-j] = k
                k+=1
        L[-i][0+h] =k
        k+=1   
    h+=1
if n%2 == 1:
    L[int(n/2)][int(n/2)] = k
for i in L:
    print(*i, end = ' ')
    print() 