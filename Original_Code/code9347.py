a=list(input())
d=[]
dic={}
i=0
f=sorted(a)
while i<len(f):
    b=a.count(f[i])
    d.append((f.count(f[i]), f[i]))
    dic[f[i]]=""""
    i+=b
d=sorted(d, reverse=True)
if len(d)==1:
    dic[d[0][1]]=""0""
while len(d)>1:
    l=len(d)
    for c in d[-1][1]:
        dic[c]=""0""+dic[c]
    for c in d[-2][1]:
        dic[c]=""1""+dic[c]
    d.append((d[l-2][0]+d[l-1][0],d[l-2][1]+d[l-1][1]))
    d.remove(d[l-1])
    d.remove(d[l-2])
    d=sorted(d, reverse=True)
   

res=""""
for c in a:
    res+=dic[c]

print(len(set(a)), len(res))
for k, v in dic.items():
    print(k + "": "" + v)
print(res) 