n = int(input())
start_n = n
matrix = [[0 for j in range(n)] for i in range(n)]
result = n ** 2
a = 0  # накопитель значений для ячеек
while a < result:
    for j in range(n):  # движемся слева направо
        i = -n
        if matrix[i][j] == 0:
            a += 1 
            matrix[i][j] += a
            if matrix[i][j] == result:
                break
    for i in range(n):  # движемся сверху вниз
        if matrix[i][j] == 0:
            a += 1 
            matrix[i][j] += a
            if matrix[i][j] == result:
                break
    if i == n - 1:  # движемся справа налево
        while j >= 0:
            if matrix[i][j] == 0:
                a += 1  
                matrix[i][j] += a
                j -= 1
            elif matrix[i][j] == result:
                break
            else: 
                j -= 1
    if j < 0:  # движемся снизу вверх
        j = -n
        while i >= 0:
            if matrix[i][j] == 0:
                a += 1  
                matrix[i][j] += a
                i -= 1
            elif matrix[i][j] == result:
                break
            else: 
                i -= 1
    n -= 1    
for i in range(start_n):  # переходим к печати
    for j in range(start_n):
        print(matrix[i][j], end=' ')
    print()
 