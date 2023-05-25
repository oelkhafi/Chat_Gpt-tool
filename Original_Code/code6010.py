set,table = [input().split(';') for i in range(int(input()))],{}

for i in set:
  for j in i:
    if not j.isdigit(): table[j] = [0,0,0,0,0]

for i in set:
  if int(i[1]) > int(i[3]): 
    table.get(i[0])[1] += 1
    table.get(i[0])[4] += 3
    table.get(i[2])[3] += 1

  if int(i[1]) < int(i[3]):
    table.get(i[2])[1] += 1
    table.get(i[2])[4] += 3
    table.get(i[0])[3] += 1

  if int(i[1]) == int(i[3]):
    table.get(i[0])[2] += 1
    table.get(i[0])[4] += 1
    table.get(i[2])[2] += 1
    table.get(i[2])[4] += 1

  table.get(i[0])[0] += 1
  table.get(i[2])[0] += 1

for k,v in table.items():
  print(k + ':',*v) 