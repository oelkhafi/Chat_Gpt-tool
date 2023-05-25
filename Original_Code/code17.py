import json
x=input()
d=json.loads(x)
s={}
for i in d:
    for j in i[""parents""]:
        if j!='':
            if j not in s:
                s[j]=[i[""name""]]
            else:
                s[j].append(i[""name""])
for i in d:
    if i[""name""] not in s:
        s[i[""name""]]=''
for i in s:
    for j in s[i]:
        if j in s:
            for k in s[j]:
                if k not in s[i]:
                    s[i].append(k)
rez={}
for j in s:
    if j in s:
        rez[j]=len(s[j])+1
    else:
        rez[j]=1
z=[]
for i in rez:
    z.append(i+' : '+str(rez[i]))
z=sorted(z)
for i in z:
    print(i) 