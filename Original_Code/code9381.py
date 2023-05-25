a = []

while True:
    s = input()
    if s == 'end':
        break
    else:
        a.append([int(i) for i in s.split()])
        
for i in range(len(a)):
    for j in range(len(a[i])):
        s = 0
        s += a[i-1][j] # добавим значение ячейки слева
        s += a[i][j-1] # добавим значение ячейки сверху
        if i+1 == len(a):
            s += a[0][j] # выход за границу, добавим значение первой ячейки в строке
        else:
            s += a[i+1][j]  # добавим значение ячейки справа
        if j+1 == len( a[i]):
            s += a[i][0] # выход за границу, добавим значение первой ячейки в колонке
        else:
            s += a[i][j+1] # добавим значение ячейки снизу
        
        print(s, end=' ')
    print() 