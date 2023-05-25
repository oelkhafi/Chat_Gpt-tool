a = int(input())
b = {}
for i in range(a):
    c = input().split(';')
    for j in c[::2]:
        if j not in b.keys():
            b[j] = [0, 0, 0, 0, 0]
        b[j][0] += 1
    if c[1] > c[3]:
        b[c[0]][1] += 1
        b[c[2]][3] += 1
        b[c[0]][4] += 3
    elif c[3] > c[1]:
        b[c[2]][1] += 1
        b[c[0]][3] += 1
        b[c[2]][4] += 3
    else:
        b[c[0]][2] += 1
        b[c[2]][2] += 1
        b[c[0]][4] += 1
        b[c[2]][4] += 1
for key in b:
    print(key+':', end="" "")
    for i in range(len(b[key])):
        print(b[key][i], end="" "")
    print()




 