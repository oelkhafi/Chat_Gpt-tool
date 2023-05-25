a = int(input())
cv = a
b = [[0] * a for i in range(a)]
c = []
p, z, r, d, x, y = 0, 0, 0, 0, 0, 0
for i in range((a * a)+1):
    if i != 0:
        c.append(i)
while r != cv * cv:
    for i in range(a):
        b[p][z] = c[r]
        r += 1
        z += 1
    p += 1
    a -= 1
    z -= 2
    for j in range(a):
        b[p][z+1] = c[r]
        r += 1
        p += 1
    p -= 1
    for k in range(a):
        b[p][z] = c[r]
        r += 1
        z -= 1
    p -= 1
    a -= 1
    for l in range(a):
        b[p][d] = c[r]
        r += 1
        p -= 1
    d += 1
    z = d
    p += 1
for n in range(cv):
    print(*b[n])




 