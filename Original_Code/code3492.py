def FndSortLst (x,b):
  fst, lst = 0 , len(b)-1
  while fst != lst:
    if b[((fst + lst) // 2)] < x :
      fst = ((fst + lst) // 2) +1
    else :
      lst = ((fst + lst) // 2)
  if b[fst] == x:
    return fst
  else:
    return -1

def srt (a):
  
  while True:
    p = True
    for i in range (0,len(a)-1):
      if a[i] > a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
        p =False
    if p == True :
      break
  return a

x = int(input())
a = list(map(int,input().split()))
b = srt(a)


print(FndSortLst(x,a)) 