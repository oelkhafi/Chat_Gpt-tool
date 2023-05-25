s, n, c=[], [], [] 
c1 = 0 
a=int(input())
for i in range(a):
    i=int(input())
    s.append(i)
    if i%2==0:
        c.append(i)
    else:
        n.append(i)
    c.sort()
    n.sort()
if len(c)==0:
    c[0]=0
elif len(n)==0:
    n[0]=0
c1=c[0]+n[0]
for j in range(len(s)):
    if s[j]<c1:
        s[j]=s[j]+c1
print (*s)




 