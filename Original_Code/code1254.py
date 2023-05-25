g = {}
n = int(input())
for i in range(n):
    s = input().split("";"")
    for j in range(0, 3, 2):
        k = s[j]
        if k in g:
            g[k][0] += 1
        else:
            g[k] = [1, 0, 0, 0, 0]
    if s[1] == s[3]:
        g[s[0]][2] += 1
        g[s[2]][2] += 1
    elif s[1] < s [3]:
        g[s[0]][3] += 1
        g[s[2]][1] += 1
    else:
        g[s[0]][1] += 1
        g[s[2]][3] += 1
for a, b in g.items():
    b[4] = 3 * b[1] + b[2]
    print(a + ':', *b)




 