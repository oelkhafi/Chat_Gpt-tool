#Создание матрицы n x n и заполнение ее нулями:
n = int(input())
a = [[0 for j in range(n)] for i in range(n)] 

#Заполнение матрицы числами по спирали:
i, j, count = [0, -1, 0]
while count < n * n:
  while j < n - 1 and a[i][j+1] == 0: #движение вправо
    j += 1
    count += 1
    a[i][j] = count
  while i < n - 1 and a[i+1][j] == 0: #движение вниз
    i += 1
    count += 1
    a[i][j] = count
  while j > 0 and a[i][j-1] == 0: #движение влево
    j -= 1
    count += 1
    a[i][j] = count
  while i > 0 and a[i-1][j] == 0: #движение вверх
    i -= 1
    count += 1
    a[i][j] = count

#Распечатка матрицы:
for i in range (n):
  print()
  for j in range (n):
    print (a[i][j],'', end='') 