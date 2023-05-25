def fndmin (a):
  mn = 0
  z = a[0]
  for i in range (1,len(a)):
    if a[mn] > a [i]:
      z = a[i]
      mn = i
  return z

def fndmx (a):
  mx=0
  g=a[0]
  for i in range (1,len(a)):
    if a[mx] < a[i]:
      g = a[i]
      mx = i 
  return g

a=[3, 5, 65, 67, 4, 2, 3, 6, 9, -10, -27, 6, 0, 8]
print(fndmin(a),fndmx(a), sep = ('\n'))





 