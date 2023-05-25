#ввод
m = n =int(input())
#начало записи с проверкой на ввод единицы
if n>1:
  x=[[0 for i in range(n)] for j in range(n)] #список для записи
  z=[int(i) for i in range(n)]                #список индексов
  #переменные
  b,k=0,0
  a,st=1,1
  #запись списка
  while a<n**2:
      for y in range(2):
          #цикл по горизонтали
          for j in z[b:m-1:st]:
              x[k][j]=a
              a+=1
          k=j+st
          #цикл по вертикали
          for i in z[b:m-1:st]:
              x[i][k]=a
              a+=1
          k=i+st
          #реверс диапазона
          st*=-1
          b=k
          m=n-k
      #уменьшение диапазона - переход на следущий круг
      b+=1
      k+=1
      m-=1
  #проверка последнего числа для нечетного n
  if n%2!=0: x[i][j]=a    
  #вывод    
  for i in range(n):
      for j in range(n):
          print(x[i][j], end='\t')
      print()
else: print(n) #вывод единицы 