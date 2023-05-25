n=int(input())
a=[[0 for j in range(n)] for i in range(n)]
x1=0
x2=n
y1=0
y2=n
b=1
c=n**2
while b<=c:
  for i in range(y1,y2):
    a[x1][i]=b
    b+=1
  y2-=1
  if b>c:
    break
  for i in range(x1+1,x2):
    a[i][y2]=b
    b+=1
  x2-=1
  if b>c:
    break 
  for i in range(y2-1,y1-1,-1):
    a[x2][i]=b
    b+=1
  if b>c:
    break
  for i in range(x2-1,x1,-1):
    a[i][y1]=b
    b+=1
  y1+=1
  x1+=1
for i in range(0, n):
  for j in range(0, n):
    print(a[i][j], end=' ')
  print()
 