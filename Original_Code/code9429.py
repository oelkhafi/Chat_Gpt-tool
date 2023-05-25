a=[str(i) for i in input().split()]
b=[]
c=['end']
n=0
while a!=c:
    b+=[a]
    a=[str(i) for i in input().split()]
if len(b)>1 and len(b[0])>1:    
    for i in range(len(b)): 
        for j in range(len(b[0])):
            if j==len(b[0])-1:
                print(int(b[i-1][j])+int(b[i-len(b)+1][j])+int(b[i][j-1])+int(b[i][j-len(b[0])+1]),end=' ') 
                print()
            else:
                print(int(b[i-1][j])+int(b[i-len(b)+1][j])+int(b[i][j-1])+int(b[i][j-len(b[0])+1]),end=' ')
elif len(b)==1 and len(b[0])>1:
    for j in range(len(b[0])):
        print(int(b[0][j-1])+int(b[0][j-len(b[0])+1])+int(b[0][j])+int(b[0][j]),end=' ') 
elif len(b)>1 and len(b[0])==1:
    for i in range(len(b)):
        print(int(b[i-1][0])+int(b[i-len(b)+1][0])+int(b[i][0])+int(b[i][0]),end=' ') 
        print()
else:
    print(int(b[0][0])*4)




 