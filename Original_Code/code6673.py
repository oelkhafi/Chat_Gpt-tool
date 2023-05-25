line1=[]
[line1.append(int(x)) for x in input().split()]

L=[] 
E=[]
i=1
while i<=line1[0]:
  [L.append(int(x)) for x in input().split()]
  if i%2!=0:
        [E.append(x) for x in range(1+line1[1]*(i-1),1+line1[1]*(i))]     
  else:
        [E.append(x) for x in range(line1[1]*(i),line1[1]*(i-1),-1)]
  #print E      
  i+=1
if line1[0]%2 !=0: E.remove(E[-1]) 
else: E.remove(E[-line1[1]]) 
#print E


def chetnost(L):
  c=1
  for element in L:
      i=L.index(element)
      while i<len(L):
        if element>L[i]: c*=-1
        i+=1
  return c  
if chetnost(L)==chetnost(E): print(""Бинго!"")
else: print(""Не повезло..."")
  



 