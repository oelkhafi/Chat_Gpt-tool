matrix=[]
x='Start'
beginning=True
while x!='end':
    x=input()
    if x=='end':
       break
    x= [int(i) for i in x.split()]
    if beginning:
        cow=len(x)
        beginning=False
    if cow == len(x):
        matrix.append(x)
    else:
        print(""Ошибка!"")
matrix2 =[[0 for j in range(cow)] for i in range(len(matrix))]
for j in range (len(matrix)):
    for i in range(cow):
        if 0 < i < cow-1:
            matrix2[j][i] += matrix[j][i-1]+ matrix[j][i+1]
        if i==0 and i == cow-1:
            matrix2[j][i]+=matrix[j][i]*2
        if i==0 and i < cow-1:
            matrix2[j][i] += matrix[j][cow-1]+ matrix[j][i+1]
        if i==cow-1 and i>0:
            matrix2[j][i] += matrix[j][i-1]+ matrix[j][0]

        if 0 < j < len(matrix)-1:
            matrix2[j][i] += matrix[j-1][i]+matrix[j+1][i]
        if j==0 and j==len(matrix)-1:
            matrix2[j][i] += matrix[j][i] * 2
        if j == 0 and j < len(matrix)-1:
            matrix2[j][i]+=matrix[len(matrix)-1][i]+ matrix[j+1][i]
        if j == len(matrix) - 1 and j > 0:
            matrix2[j][i] +=  matrix[j-1][i]+ matrix[0][i]
for j in range(len(matrix2)):
   for i in range (cow):
       print(matrix2[j][i],end=' ')
   print() 