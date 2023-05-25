b=[]
r=0
a= input().split(', ')
for i in range(len(a)):
    b.append(int(a[i]))
b1=sorted(b)
if b1[0]!=b1[1]:
    print(b.index(b1[0]))
elif b1[0]==b1[1] and b1[1]!=b1[2]:
    z=b.index(b1[0])
    b[z]=''
    z1=b.index(b1[1])
    print(z+z1)
else:
    for i in range(len(b1)):
        if b1[i]==b1[i+1]:
            z=b.index(b1[i+1])
            b[z]=''
            r+=z
        else:
            r+=b.index(b1[0])
            break
    print(r)

 