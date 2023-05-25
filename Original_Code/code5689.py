a = [int(i) for i in input().split()]
b = []
d = 0
c = 0
e = a[d]
f = a[c]
for ind in a:
    try:
        a[1]
    except IndexError:
        b.append(a[0])
    else:
        try:
            e = a[d-1]
            f = a[c+1]
            b.append(e + f)
        except IndexError:
            b.append(e + a[0])
    d += 1
    c += 1
print(*b)




 