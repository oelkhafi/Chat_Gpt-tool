n = int(input())
k=sorted([int(input()) for i in range (n)])
for j in range(1,k[0]+1):
    if k[0]%j==k[n-1]%j==0:
            m=j
print (m)
pr=True
for j in range(2,m+1):
    if m%j==0 and j!=m:
        print ('NO')
        pr=False
        break
if m==1:
    print('NO')
    pr=False
if pr:
    print('YES')





 