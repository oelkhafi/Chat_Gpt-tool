n = int(input())
d={}
for i in range(n):
    l=input().split("";"")
    if l[0] in d:
        d[l[0]][0]+=1
    else:
        d[l[0]]=[1,0,0,0]
    if l[2] in d:
        d[l[2]][0]+=1
    else:
        d[l[2]]=[1,0,0,0]
    if l[1]==l[3]: 
        d[l[0]][2]+=1
        d[l[2]][2]+=1
    elif int(l[1])>int(l[3]): 
        d[l[0]][1]+=1
        d[l[2]][3]+=1
    else          : 
        d[l[0]][3]+=1
        d[l[2]][1]+=1
for key in d.keys():
    print (key, end="":"")
    for i in d[key]:
      print (i, end="" "")
    print (d[key][1]*3+d[key][2])



 