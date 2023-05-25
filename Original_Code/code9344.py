n,s,tchk=int(input()),[],[]
for i in range(n):
    a,b=map(int,input().split())
    s.append([a,b])
s.sort()
for i in range(1,len(s)):
    if s[i-1][1]>=s[i][0]:
        s[i][1]=min(s[i-1][1],s[i][1])
        if i==len(s)-1:
            tchk.append(s[i])
    elif s[i-1][1]<s[i][0]:
        tchk.append(s[i-1])
        if i==len(s)-1:
            tchk.append(s[i])
    
print(len(tchk))
for t in tchk:
    print(t[0],end="" "")




 