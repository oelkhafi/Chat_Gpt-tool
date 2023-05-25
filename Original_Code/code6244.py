d={}
for i in range(int(input())):
    s=input().split(';')

    if s[0] not in d: d.setdefault(s[0],[0,0,0,0,0])
    if s[2] not in d: d.setdefault(s[2],[0,0,0,0,0])

    d[s[0]][0]+=1
    d[s[2]][0]+=1

    if s[1]>s[3]:
        d[s[0]][1]+=1
        d[s[2]][3]+=1
        d[s[0]][4]+=3
    if s[1]==s[3]:
        d[s[0]][2]+=1
        d[s[2]][2]+=1
        d[s[0]][4]+=1
        d[s[2]][4]+=1
    if s[1]<s[3]:
        d[s[0]][3]+=1
        d[s[2]][1]+=1
        d[s[2]][4]+=3

for i in d:
    print(i+':',end='')
    print(*d[i]) 