x, y = map(int, input().split())
m = []
for i in range(x):
    m.append(list(input().strip()))
def neib(r, c, z):  #number of neighbours
    rl = r-1
    cl = c-1
    rr = (r+1) % len(z)
    cr = (c+1) % len(z[0])
    res = 0
    for i in [rl, r, rr]:
        for j in [cl, c, cr]:
            if z[i][j] == 'X':
                res += 1
    if z[r][c] == 'X':
        res -= 1
    return res

def life(tt, neibs): #next gen based on current and number of neibs
    if tt == ""X"":
        if neibs in [2, 3]:
            return ""X""
        else:
            return '.'
    else:
        if neibs == 3:
            return 'X'
    return '.'

for i in range(x):
    row = []
    for j in range(y):
        n = neib(i, j, m)
        print(life(m[i][j], n), end='')
    print() 