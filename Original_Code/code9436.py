n=int(input())
b=[n]
for i in range(n):
    b+=[input().split(';')]
z={}
for i in range(1,len(b)):
    z[b[i][0]]=[0,0,0,0,0]
    z[b[i][2]]=[0,0,0,0,0]
for i in range(1,len(b)):
    if int(b[i][1])>int(b[i][3]):
        z[b[i][0]][4]+=3
        z[b[i][0]][1]+=1
        z[b[i][0]][0]+=1
        z[b[i][2]][0]+=1
        z[b[i][2]][3]+=1
    elif int(b[i][1])==int(b[i][3]):
        z[b[i][0]][4]+=1
        z[b[i][0]][2]+=1
        z[b[i][0]][0]+=1
        z[b[i][2]][4]+=1
        z[b[i][2]][2]+=1
        z[b[i][2]][0]+=1
    elif int(b[i][1])<int(b[i][3]):
        z[b[i][2]][4]+=3
        z[b[i][2]][0]+=1
        z[b[i][2]][1]+=1
        z[b[i][0]][3]+=1
        z[b[i][0]][0]+=1
for key in z:
    x=z[key]
    print(str(key)+str(':'),end='')
    print(*x)




 