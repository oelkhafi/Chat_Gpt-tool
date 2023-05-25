c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c += [a]
st = len(c)
col = len(c[0])
b = []
for i in range(st):
    for j in range(col):
        b += [int(c[i-1][j]) + int(c[i-st+1][j]) + int(c[i][j-1]) + int(c[i][j-col+1])]
z = 0
w = [[0] * col for i in range(st)]
for i in range(st):
    for j in range(col):
        if w[i][j] == 0:
            w[i][j] = b[z]
            z += 1

for j in range(st):
    for i in range(col):
        print(w[j][i], end=' ')
    print()




 