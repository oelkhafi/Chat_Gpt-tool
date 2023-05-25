a = int(input())
seq = 0
matrix = [list([0]*a) for i in range (a)]
for i in range (a):
    for x in range(a):
        if matrix[i][a-(a-x)]==0:
          seq += 1
          matrix[i][a-(a-x)]=str(seq)
    for x in range(a):
        if matrix[x][(a-1)-i] ==0:
          seq += 1
          matrix[x][(a-1)-i]=str(seq)
    for x in range(a):
        if matrix[a-i-1][(a-(x+1)) - a]==0:
          seq += 1
          matrix[a-i-1][(a-(x+1)) - a]=str(seq)
    for x in range(a):
        if matrix[a-i-1][(a-(x+1)) - a]==0:
          seq += 1
          matrix[a-i-1][(a-(x+1)) - a]=str(seq)
    for x in range(a):
        if matrix[a+(-1-x)][i]==0:
          seq += 1
          matrix[a+(-1-x)][i]=str(seq)
for i in range(a):
    print(' '.join(matrix[i]))
 