# формируем список входных строк
v=[]
enter=0
while enter!='end':  
    enter=input()
    v.append(enter)

# модифицируем одномерный список в матрицу
m=[x.split() for x in v] 
# отбрасываем строку end
mx=m[:-1]

#основная часть
row=[]                         # заготовка i-ой строки результирующей матрицы
mtx=[]                         # заготовка результирующей матрицы
for i in range(len(mx)):
    for j in range(len(mx[i])):
        s=int(mx[i-1][j]) + int(mx[i-len(mx)+1][j]) + int(mx[i][j-1]) + int(mx[i][j-len(mx[i])+1])
                               # формируем список i-ой строки
        row.append(s)
                               # порционно добавляем копии стррок в заготовку матрицы
    mtx.append(row.copy())
    row.clear() 

# выводим результат
for i in mtx: print(*i)    


 