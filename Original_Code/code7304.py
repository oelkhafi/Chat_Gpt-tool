s=input()
d=1
j=1
m=''
for i in range(len(s)-1):
    d=1
    if s[i]==s[i+1]:
        j+=1
    elif s[i]!=s[i+1]:
        m=m+s[i]+str(j)
        j=1
if s[len(s)-1]==s[len(s)-2]:
    m=m+s[len(s)-1]+str(j)
elif s[len(s)-1]!=s[len(s)-2]:
    m=m+s[len(s)-1]+str(j)
else:
    m=m+s[len(s)-1]+str(j)

print(m)


 