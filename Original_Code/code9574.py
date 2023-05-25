# put your python code here
n = int(input())
s = [[0 for j in range(n)] for i in range(n)]
x = 1
for i in range(n):
    for a in range(i, n - i):# up-to-right
        s[i][a] = x
        x += 1
    for b in range(i + 1, n - i):# right-down
        s[b][n - 1 - i] = x
        x += 1
    for c in range(n - 1 - i, i, -1):# down-to-left
        s[n - 1 - i][c - 1] = x
        x += 1
    for d in range(n - 1 - i, i + 1, -1):# left-up
        s[d - 1][i] = x
        x += 1
for i in range(len(s)):
    for j in range(len(s[0])):
        print(s[i][j], end=' ')
    print() 