a = int(input())
b = int(input())
c = int(input())
if a > b:
  max = a
  if b > c:
    min = c
    ost = b
  else:
    min = b
    if a > c:
      ost = c
    else:
      max = c
      ost = a
elif b > c:
  max = b
  if a > c:
    min = c
    ost = a
  else:
    min = a
    ost = c
else:
  max = c
  min = a
  ost = b
print(max)
print(min)
print(ost) 