a = []

while True:
  b = input().split()
  if b == ['end']:
    break
  else:
    a.append(b)

c = [[0 for j in range(len(a[i]))]for i in range(len(a))]

for i in range(len(a)):
  for j in range(len(a[i])):
    c[i][j] = int(a[i][j])

if len(c) == 1 and len(c[i]) == 1:
  print((c[0][0]) + c[0][0] + c[0][0] + c[0][0])
  
elif len(c) == 1 and len(c[i]) >= 2:
  d = [[0 for j in range(len(c[i]))]for i in range(len(c))]
  for i in range(len(c)):
    for j in range(len(c[i])):
      if i == 0 and j == 0:
        d[i][j] = c[i][j] + c[i][j] + c[i][len(c[i])-1] + c[i][j+1]
      if i == 0 and j == (len(c[i])-1):
        d[i][j]= c[i][j] + c[i][j] + c[i][0] + c[i][len(c[i])-2]
      if i == 0 and 0 < j < (len(c[i])-1):
        d[i][j] = c[i][j] + c[i][j] + c[i][j-1] + c[i][j+1]
  for i in range(len(d)):
    for j in range(len(d[i])):
      print(d[i][j], end=' ')
      
elif len(c) > 1 and len(c[i]) == 1:
  f = [[0 for j in range(len(c[i]))]for i in range(len(c))]
  for i in range(len(c)):
    for j in range(len(c[i])):
      if i == 0 and j ==0:
        f[i][j] = c[len(c)-1][j] + c[i+1][j] + c[i][j] + c[i][j]
      if 0 < i < (len(c)-1) and j == 0:
        f[i][j] = c[i-1][j]+ c[i+1][j] + c[i][j] + c[i][j]
      if i == (len(c)-1) and j == 0:
        f[i][j] = c[len(c)-2][j] + c[0][j] + c[i][j] + c[i][j]
  for i in range(len(f)):
    for j in range(len(f[i])):
      print(f[i][j], end=' ')
    print()
      
elif len(c) == 2 and len(c[i]) == 2:
  e = [[0 for j in range(len(c[i]))]for i in range(len(c))]
  for i in range(len(c)):
    for j in range(len(c[i])):
      if i == 0 and j == 0:
        e[i][j] = c[1][j] + c[1][j] + c[i][1] + c[i][1]
      if i == 0 and j == 1:
        e[i][j] = c[1][j] + c[1][j] + c[i][0] + c[i][0]
      if i == 1 and j == 0:
        e[i][j] = c[0][j] + c[0][j] + c[i][1] + c[i][1]
      if i ==1 and j == 1:
        e[i][j] = c[0][j] + c[0][j] + c[i][0] + c[i][0]
  for i in range(len(e)):
    for j in range(len(e[i])):
      print(e[i][j], end=' ')
    print()
      

else:
  ex = [[0 for j in range(len(c[i]))]for i in range(len(c))]

  for i in range(len(c)):
    for j in range(len(c[i])):
      if i == 0 and j == 0:
        ex[i][j] = c[len(c)-1][j] + c[i+1][j] + c[i][len(c[i])-1] + c[i][j+1]
      if i == 0 and 0 < j < (len(c[i])-1):
        ex[i][j] = c[len(c)-1][j] + c[i+1][j] + c[i][j-1] + c[i][j+1]
      if i == 0 and j == (len(c[i])-1):
        ex[i][j] = c[len(c)-1][j] + c[i+1][j] + c[i][len(c[i])-2] + c[i][0]
      if 0 < i < (len(c)-1) and 0 < j < (len(c[i])-1):
        ex[i][j] = c[i-1][j] + c[i+1][j] + c[i][j-1] + c[i][j+1]
      if 0 < i < (len(c)-1) and j == 0:
        ex[i][j] = c[i-1][j] + c[i+1][j] + c[i][len(c[i])-1] + c[i][j+1]
      if 0 < i < (len(c)-1) and j == (len(c[i])-1):
        ex[i][j] = c[i-1][j] + c[i+1][j] + c[i][len(c[i])-2] + c[i][0]
      if i == (len(c)-1) and j == 0:
        ex[i][j] = c[len(c)-2][j] + c[0][j] + c[i][len(c[i])-1] + c[i][j+1]
      if i == (len(c)-1) and 0 < j < (len(c[i])-1):
        ex[i][j] = c[len(c)-2][j] + c[0][j] + c[i][j-1] + c[i][j+1]
      if i == (len(c)-1) and j == (len(c[i])-1):
        ex[i][j] = c[len(c)-2][j] + c[0][j] + c[i][len(c[i])-2] + c[i][0]
      
  for i in range(len(ex)):
    for j in range(len(ex[i])):
      print(ex[i][j], end=' ')
    print()  
    





 