# put your python code here
n=int(input())
a=[[0 for i in range(n)]for j in range(n)]
s=1
for k in range((n//2)+1):
    for j in range(k,n-1-k):
        a[k][j]=s
        s+=1
    for i in range(k,n-1-k):
        a[i][n-1-k]=s
        s+=1
    for j in range(k+1,n-k):
        a[n-1-k][-j]=s
        s+=1
    for i in range(k+1,n-k):
        a[-i][k]=s
        s+=1
if n%2==0:
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
elif n%2==1:
    a[n//2][n//2]=n**2
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print() 