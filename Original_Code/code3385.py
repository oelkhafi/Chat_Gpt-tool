# put your python code here
a = input().split()
b = []
while a != ['end']:
    for i in range(len(a)):
        a[i] = int(a[i])
    b.append(a)
    a = input().split()
c = []
n = len(b)
m = len(b[0])
for i in range(n):
    for j in range(m):
        c.append(int(b[i][j-m+1]) + int(b[i][j-1]) + int(b[i-n+1][j]) + int(b[i-1][j]))
    for i in c:    
        print(i, end=' ')
    print()
    c = []



 