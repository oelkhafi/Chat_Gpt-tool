n = int(input())
i = 1
start, stop = 0, n
m = [[0 for i in range(n)] for j in range(n)]
while i <= n*n:
    for x in range(start, stop):
        m[start][x] = i
        i += 1
    start += 1
    for x in range(start, stop):
        m[x][stop - 1] = i
        i += 1
    stop -= 1
    start -= 1
    for x in range(stop, start, -1):
        m[stop][x - 1] = i
        i += 1
    start +=1
    for x in range(stop, start, -1):
        m[x - 1][start - 1] = i
        i += 1
for i in range(n):
    for j in range(n):
        print(m[i][j], end = ' ')
    print()
 