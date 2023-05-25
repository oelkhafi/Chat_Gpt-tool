n, m = [int(i) for i in input().split()]
field = [[0 for i in range(m+2)] for j in range(n+2)]
for i in range(n):
  a = input()
  for j in range(m):
    if a[j] == '*':
      field[i+1][j+1] = '*'
      
for i in range(1, n+1):
  for j in range(1, m+1):
    if field[i][j] != '*':
      if field[i][j+1] == '*': field[i][j] += 1
      if field[i][j-1] == '*': field[i][j] += 1
      if field[i+1][j] == '*': field[i][j] += 1
      if field[i-1][j] == '*': field[i][j] += 1
      if field[i+1][j+1] == '*': field[i][j] += 1
      if field[i+1][j-1] == '*': field[i][j] += 1
      if field[i-1][j+1] == '*': field[i][j] += 1
      if field[i-1][j-1] == '*': field[i][j] += 1

for i in field[1:-1]:
  print(*i[1:-1], sep='')




 