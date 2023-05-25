s = input()
st=''
digest=''
y=0
z=0
for j in (s):
  while y <= (len(s)-1) and s[z] == s[y]:
    st+=s[y]
    y+=1
  if len(st)>0:
    digest+=st[0]+str(len(st))
    st=''
  while y <= (len(s)-1) and s[z] != s[y]:
    z=y
    st+=s[y]
    y+=1
    if y < len(s) and s[z] != s[y]:
       digest+=st[0]+str(len(st))
       st=''
print(digest)




 