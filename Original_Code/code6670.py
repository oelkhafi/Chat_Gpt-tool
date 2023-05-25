L=list(map(int,input().split()))
i=0
Chet=-1
Nechet=0

if (L[0]+L[1])%2: Nechet-=1
else: Chet-=1

while i<L[0]:
  j=0
  while j<L[1]:
    if (i+j)%2: Nechet+=1
    else: Chet+=1
    #print (j)
    j+=1
  i+=1
if Chet==Nechet: print(""Замостить можно"")
else: print(""Замостить нельзя"")





 