# Цикл с заполнением матрицы, пока не будет введена строка ""end"":
matrix = []
while True: 
  temp = input().split()
  if temp[0] != 'end':
    stroka = []
    for i in temp: #переносим из temp цифры в stroka, преобразуя их в вещественные числа
      stroka.append(int(i))
    matrix.append(stroka)
  else: break #выход из цикла заполнения матрицы

#Создание новой матрицы и заполнение ее нулями
mnew = [[0 for j in range (len(matrix[i]))] for i in range (len(matrix)) ]

# Выполнение расчётов и заполнение новой матрицы:
for i in range (len(matrix)): #цикл по всем строкам старой матрицы
  for j in range (len(matrix[i])): #цикл по всем столбцам старой матрицы

    # если строка последняя, то в формуле для вычисления вместо [i+1] --> [0]
    if i == (len(matrix) - 1) and j != (len(matrix[i]) - 1):
      temp = matrix[i-1][j] + matrix [0][j] + matrix[i][j-1] + matrix[i][j+1]
    
    # если столбец последний, то в формуле для вычисления вместо [j+1] --> [0]  
    elif i != (len(matrix) - 1) and j == (len(matrix[i]) - 1):
      temp = matrix[i-1][j] + matrix [i+1][j] + matrix[i][j-1] + matrix[i][0]

    # если и строка и столбец последние, то в формуле вместо [i+1] --> [0] и [j+1] --> [0]  
    elif i == (len(matrix) - 1) and j == (len(matrix[i]) - 1):
      temp = matrix[i-1][j] + matrix [0][j] + matrix[i][j-1] + matrix[i][0]

    # в остальных случаях формула обычная:  
    else:
      temp = matrix[i-1][j] + matrix [i+1][j] + matrix[i][j-1] + matrix[i][j+1]
    mnew[i][j] = temp

# Распечатка новой матрицы:
for i in range (len(mnew)):
  print()
  for j in range (len(mnew[i])):
    print (mnew[i][j],'', end='') 