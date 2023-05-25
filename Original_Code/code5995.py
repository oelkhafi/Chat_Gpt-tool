s=input()
k=len(s)
i,j=0,1
y=str()

while i<k:
  while j<=k:
    if s[i]==s[j-k]:
      x=s[i:j+1]
    else:
      x=s[i:j]
      break
    j+=1
  y=s[i]+str(len(x))
  print(y,end='')
  i=j
  j+=1




 