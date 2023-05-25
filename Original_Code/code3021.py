mx, ln = [], []
n = input()
while n!=""end"":
    for i in n.split():
        ln.append(int(i))
    mx.append(ln)
    ln = []
    n = input()

big = [[0 for j in range(len(mx[0])+2)] for i in range(len(mx)+2)]
bgcol, bgrow = len(big[0]), len(big)

for i in range(1, bgrow -1):
    for j in range(1, bgcol -1):
        big[i][j] = mx[i-1][j-1]
        
for i in 0, -1:
    for j in range(1, bgcol-1):
        if i == 0:
            big[i][j] = big[i-2][j]
        else: big[i][j] = big[1][j]
        
for i in range(1, bgrow-1):
    for j in 0, -1:
        if j== 0:
            big[i][j] = big[i][j-2]
        else: big[i][j] = big[i][1]

for i in range(1, bgrow -1):
    for j in range(1, bgcol -1):
        mx[i-1][j-1] = big[i-1][j]+ big[i+1][j]+ big[i][j-1]+big[i][j+1]
for i in mx:
    for j in i:
        print(j, end="" "")
    print()

 