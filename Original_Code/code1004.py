a=[int(i) for i in input().split()]
a.sort()
s=[]
z=""""
if len(a)>1:
    for j in range(len(a)):
        b=a.count(a[j])  
        if b>1:
            s.append(a[j])
    for k in range(len(s)-1):
        if s[k]==s[k+1] and k+1<len(s):
            continue
        else:
            z+=str(s[k])+"" ""
if len(s)>0:
    z+=str(s[k])
print (z)




 