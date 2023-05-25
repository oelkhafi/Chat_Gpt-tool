d = {}
li = []
s = []
for _ in range(int(input())):
  b = input().replace(':', ' ').split()
  d[b[0]] = b[1:]
for _ in range(int(input())):
  li.append(input())

for k, v in d.items():
  for k2, v2 in d.items():
    if k in v2:
      d[k2] += v

for i in li:
  for j in d[i]:
    if i not in s:
      if j in li and li.index(j) < li.index(i):
        s.append(i)
for i in s:
  print(i)



 