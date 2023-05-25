yy = int(input())
S=yy
matrix=[[0 for j in range(yy)]for i in range(yy)]
result=0
finish=yy**2
xx=0
while (result!=finish):
    for i in range(S):
        result+=1
        matrix[xx][xx+i]=result
    S-=1
    for i in range(S):
        result+=1
        matrix[xx+i+1][yy-1]=result
    for i in range(S):
        result += 1
        matrix[yy-1][yy-2-i] = result
    S-=1
    for i in range(S):
        result += 1
        matrix[yy-2-i][xx] = result
    xx+=1
    yy-=1
for j in range(len(matrix)):
    for i in range(len(matrix)):
        print(matrix[j][i], end=' ')
    print()
 