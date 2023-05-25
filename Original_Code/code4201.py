# put your python code here

n = int(input())
pos = 0
cur = 1
res = [[0] * n for i in range(n)]
while pos <= n//2:
    if pos == n-1-pos:
        res[pos][pos] = cur
    else:
        for i in range(cur,cur+n-1-2*pos):
            res[pos][pos+i-cur]=i
        cur = cur+n-1-2*pos
        for j in range(cur,cur+n-1-2*pos):
            res[pos+j-cur][n-1-pos]=j
        cur = cur+n-1-2*pos
        for i in range(cur,cur+n-1-2*pos):
            res[n-1-pos][n-1-pos+cur-i]=i
        cur = cur+n-1-2*pos
        for j in range(cur,cur+n-1-2*pos):
            res[n-1-pos+cur-j][pos]=j
        cur = cur+n-1-2*pos
    pos += 1
for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    print()


 