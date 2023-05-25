import numpy as np
L = list(map(int, input().split()))

n , k = len(L), sum(L)
# n - количество кучек
# k - сумма бумажек в кучках
if L:
    max = np.max(L)
    x = max

def funk(x, k, n):
    if (n*x - k)%2 == 0:
        print(int((n*x - k)/2), x)
        return 0
    else:
        return  x+1

if n < 2:
    print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
elif (n == 2):
    if L[0]==L[1]:
        print(0,L[0])
    else:
        print('Кучки нельзя уравнять') 
else:
    
    while (x!=0):
        if (n%2==0) and (k%2==0):
             x = funk(x, k, n) 
        elif (n%2!=0) and (k%2!=0):
             x = funk(x, k, n)
        elif (n%2==0) and (k%2!=0):
            print('Кучки нельзя уравнять')
            x = 0
        elif (n%2!=0) and (k%2==0):
             x = funk(x, k, n)  