flag = True
x = []
while(flag):
  a = [ i for i in input().split()]
  if (a != ['end']):
    x.append(a)
  else:
    flag = False

l, h = len(x), len(x[0])

for i in range(l):
  if(i != 0):
    print()
  for j in range(h):
    sum = 0
    sum += int(x[i-1][j])
    sum += int(x[i+1-l][j])
    sum += int(x[i][j-1])
    sum += int(x[i][j+1-h])
    print(sum, end= ' ') 