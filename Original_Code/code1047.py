import copy
s, s1=[], []
while True:
    a=input().split()
    n=len(a)-1
    a.insert(0, a[n])
    a.append(a[1])
    s.append(a)
    b=len(s)
    b1=len(s[0])
    if a==['end', 'end', 'end']:
        s.insert((b-1),s[0])
        s.insert(0,s[b-2])  
        s1=copy.deepcopy(s)
        s1=s1[:b+1]
        for i in range(1,b):
            for j in range(1,b1-1):
                s1[i][j]=int(s[i][j-1])+int(s[i][j+1])+int(s[i+1][j])+int(s[i-1][j])
        for i in range(1,b):
            for j in range(1,b1-1):
                print (s1[i][j], end=' ')
            print()
        break

 