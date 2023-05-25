a=[]
lenX=0
lenY=0
while True:
    v=input()
    if v=='end':
        break
    else:
        a.append([int(i) for i in v.split()])
if a!=[]:
    lenY=len(a[0])
    lenX=len(a)
s=[[0 for j in range(lenY)] for i in range(lenX)]
for i in range(lenX):
    for j in range(lenY):
        s[i][j]=a[i-1][j]+a[i-lenX+1][j]+a[i][j-1]+a[i][j-lenY+1]
for i in range(lenX):
    for j in range(lenY):
        print(s[i][j], end=' ')
    print()

 