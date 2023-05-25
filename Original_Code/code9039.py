a = int(input())
n = a//2 + a%2
cn, lastnum = 0, 0
out = [[0 for _ in range(a)] for __ in range(a)]
while cn < n:
    for j in range(cn, a - cn):
        lastnum += 1
        out[cn][j] = lastnum
    if lastnum == a*a: break
    for j in range(cn + 1, a - cn):
        lastnum += 1
        out[j][a - cn - 1] = lastnum
    if lastnum == a*a: break
    for j in range(a - cn - 2, cn - 1, -1):
        lastnum += 1
        out[a - cn - 1][j] = lastnum
    if lastnum == a*a: break
    for j in range(a - cn - 2, cn, -1):
        lastnum += 1
        out[j][cn] = lastnum
    if lastnum == a*a: break
    cn += 1;
[print(*out[i], sep = "" "") for i in range(a)]
 