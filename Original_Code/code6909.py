n = int(input())
spir = [[0]*n for i in range(n)]
num = 1
i = 0
koef = 0
while koef < n//2:
    for j in range(koef,n-koef):
        spir[i][j] = num
        num += 1
    for i in range(koef+1,n-koef):
        spir[i][j] = num
        num += 1
    for j in range(n-(2+koef),koef-1,-1):
        spir[i][j] = num
        num += 1
    for i in range(n-(2+koef),koef,-1):
        spir[i][j] = num
        num += 1
    koef += 1
if n%2> 0: spir[n//2][n//2] = n*n
for i in spir:
    print(*i) 