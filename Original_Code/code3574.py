# put your python code here
L = list(map(int, input().split()))

n , k = len(L), sum(L)

if n < 2:
    print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
elif (n == 2):
    if L[0]==L[1]:
        print('Кучки можно уравнять')
    else:
        print('Кучки нельзя уравнять') 
else:
    if (n%2==0) and (k%2==0):
        print('Кучки можно уравнять')
    elif (n%2!=0) and (k%2!=0):
        print('Кучки можно уравнять')
    elif (n%2==0) and (k%2!=0):
        print('Кучки нельзя уравнять')
    elif (n%2!=0) and (k%2==0):
        print('Кучки можно уравнять')  