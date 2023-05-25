# put your python code here
dic={}
for i in range(int(input())):
    s=input()
    if "":"" in s:
        s1=s[:s.index("":"")-1]
        s2=s[s.index("":"")+1:].split()
        dic[s1]=s2
        for elem in s2:
            if elem in dic.keys():
                dic[s1].extend(dic[elem])
        for key in dic.keys():
            if s1 in dic[key]:
                dic[key].extend(dic[s1])
                
    else:
        dic[s]=[]
for m in dic.keys():
    dic[m]=list(set(dic[m]))
#print(dic)
inp=[]
res=[]
for i in range(int(input())):
    s=input()
    inp.append(s)
    if len(dic[s]) >0: 
        for elem in dic[s]:
            if elem in inp:
                res.append(s)
                break
for k in res:
    print(k)



 