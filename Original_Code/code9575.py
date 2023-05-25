# put your python code here
n = int(input())
table = [[0 for x in range(n)] for y in range(n)]
w = n
offs = 0
d = 0
while w >= 1:
    h = w - 2
    for c in range(0, w):
        idx = n - c - offs - 1
        table[offs][offs + c] = c + d + 1
        table[n - offs - 1][idx] = c + d + 2 * h + 3
        if c in range(1, w - 1):
            table[offs + c][n - offs - 1] = w + c + d
            table[idx][offs] = w + c + d + 2 * h + 2
    d += 2 * w + 2 * h
    w -= 2
    offs += 1
for i in range(len(table)):
    for j in range(len(table[0])):
        print (table[i][j], end=' ')
    print() 