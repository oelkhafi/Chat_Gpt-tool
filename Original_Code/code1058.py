b, s, s1={}, 0, 0
for i in range(int(input())):
    a=input().split()
    if a[0] not in b:
        b[a[0]]=a[1]
    else:
        b[a[0]]+=a[1]
for i in b:
    for j in b[i]:
        s+=int(j)
        s1+=1
    b[i]=round(s/s1,1)
    s, s1=0, 0
b= sorted(b.items())        
for i in b:
    print (*i)




 