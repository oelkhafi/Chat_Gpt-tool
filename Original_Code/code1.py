i=0
e=''
b=[[]]
while e!='end':
  e=input().split()
  if 'end' in e:
    break
  else:
    a=[int(j) for j in e]
    b+=[a]
    i+=1
b.remove([])
c=[]
i,j=0,0
for i in range(len(b)):
  for j in range(len(b[i])):
    if i==len(b)-1 and j!=len(b[i])-1:
      c.append(b[i-1][j]+b[0][j]+b[i][j-1]+b[i][j+1])
    elif j==len(b[i])-1 and i!=len(b)-1:
      c.append(b[i-1][j]+b[i+1][j]+b[i][j-1]+b[i][0])
    elif i==len(b)-1 and j==len(b[i])-1:
      c.append(b[i-1][j]+b[0][j]+b[i][j-1]+b[i][0])
    else:
      c.append(b[i-1][j]+b[i+1][j]+b[i][j-1]+b[i][j+1])
k=0
for i in range(len(b)):
  for j in range(len(b[i])):
    print(c[k], end=' ')
    k+=1
  print('')


 