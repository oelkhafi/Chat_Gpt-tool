a = []
b = ''
i = 0
sum = 0
while b != 'end':     # Ввод значений матрицы и запись в список a , до подачи строки 'end'
    try:
        a += [list(map(int, input().split()))]
        b = a[i]
        i+=1
    except:
        break   
row, col = len(a), len(max(a))   # записываем размерность матрицы row - строка, col - столбец             
B = [[0 for i in range(col)] for i in range(row)]    # Заполнение матрицы нулями
for i in range(row):
    for j in range(col):
        for di in range(-1,2):
            for dj in range(-1,2):
                ai = i + di
                aj = j + dj
                if -1<= ai < row and -1<= aj < col:
                    if (ai == i-1 and aj == j) or (ai == i and aj == j+1) or (ai == i+1 and aj == j) or (ai == i and aj == j-1):
                        sum += a[ai][aj]
                elif ai == row:
                    if (ai == i+1 and aj == j): 
                        sum += a[-row][aj]
                elif aj == col:
                    if(ai == i and aj == j+1): 
                        sum += a[ai][-col]
        print(sum, end= ' ')
        sum = 0
    print() 