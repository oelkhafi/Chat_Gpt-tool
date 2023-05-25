# put your python code here
a = []
j = input()
while j != 'end':
    j = [int(i) for i in j.split()]
    a.append(j)
    j = input() #приходится вызывать ввод новых значений в цикле, чтобы проверять, нет ли end
qty_line = len(a) #длина строки
qty_col = len(a[0])#длина столбца. Есть другой способ?
b = [[0 for j in range(qty_col)] for i in range(qty_line)]#новая матрица для результатов, того же размера, что и а
for i in range(qty_line):
    for j in range(qty_col):
        b[i][j] = a[i-1][j] + a[i - qty_line + 1][j] + a[i][j-1] + a[i][j - qty_col +1]
#чтобы не получалось ошибок с правыми и нижними клетками, их индексы считаем как индекс вычисляемой клетки-длина строки+1
for i in range(qty_line):
    for j in range(qty_col):
        print(b[i][j], end=' ')
    print()



 