n = int(input())
m = [[0]*n for i in range(n)]
i,j,nc = 0,0,0
while nc+1 <= n*n:
    while nc < n*n and m[i][j%len(m)] == 0:
            nc+=1
            m[i][j] = nc
            j+=1
    j-=1
    i+=1
    while nc < n*n and m[i%len(m)][j] == 0:
            nc+=1
            m[i][j] = nc
            i+=1
    j-=1
    i-=1
    while nc < n*n and m[i][j%len(m)] == 0:
            nc+=1
            m[i][j] = nc
            j-=1
    i-=1
    j+=1
    while nc < n*n and m[i%len(m)][j] == 0:
            nc+=1
            m[i][j] = nc
            i-=1
    i+=1
    j+=1
[print(*i) for i in m] 