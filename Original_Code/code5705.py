d = {}
for _ in range(int(input())):
  a = input().replace(':', ' ').split()
  d[a[0]] = a[1:]
  
for k, v in d.items():
  for k2, v2 in d.items():
    if k in v2:
      d[k2] += v
for _ in range(int(input())):
  c1, c2 = input().split()
  if c1 == c2:
    print('Yes')
  elif c1 in d[c2]:
    print('Yes')
  else:
    print('No')
               




 