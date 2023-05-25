# put your python code here
n = int(input())
a = {'север':[0,0], 'запад':[0,0], 'юг':[0,0], 'восток':[0,0]}
for i in range(n):
    i = input().split()
    if i[0] == 'север':
        a['север'][1] += int(i[1])
    elif i[0] == 'запад':
        a['запад'][0] += int(i[1])
    elif i[0] == 'юг':
        a['юг'][1] += int(i[1])
    elif i[0] == 'восток':
        a['восток'][0] += int(i[1])
    #else:
        #print('Ошибка ввода данных')
print(int(a['восток'][0]) - int(a['запад'][0]), end=' ')
print(int(a['север'][1]) - int(a['юг'][1]))





 