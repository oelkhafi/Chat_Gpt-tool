a=[]
b=[]
while b!=['end']:
    b=[i for i in input().split()]
    if b!=['end']:
        a.append(b)
    else:
        break

import copy
b=copy.deepcopy(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        if (j+1!=len(a[i])) and (i+1!=len(a)):
            c=[int(a[i-1][j]), int(a[i+1][j]), int(a[i][j-1]), int(a[i][j+1])]
            c=sum(c)
            b[i][j]=c

        else:
            c=[int(a[i-1][j]), int(a[i+1-len(a)][j]), int(a[i][j-1]), int(a[i][j+1-len(a[i])])]
            c=sum(c)
            b[i][j]=c

for row in b:
   print(' '.join(map(str, row))) 