kol = int(input())
i = v = n = p = ochki = sch = 0
vivod = vivod1 = vivod2 = []
sttr = ''
while kol > 0:
    kom = input().split(';')
    if kom[1] > kom[3]:
        v += 1
        i += 1
        ochki += 3
        vivod += [kom[0], i,  v, n, p, ochki]
        v = ochki = 0
        p += 1
        vivod += [kom[2], i,  v, n, p, ochki]
        p = i = 0
    if kom[1] == kom[3]:
        n += 1
        ochki += 1
        i += 1
        vivod += [kom[0], i,  v, n, p, ochki]
        vivod += [kom[2], i, v, n, p, ochki]
        n = ochki = i = 0
    if kom[1] < kom[3]:
        p += 1
        i += 1
        vivod += [kom[0], i, v, n, p, ochki]
        p = 0
        v += 1
        ochki += 3
        vivod += [kom[2], i, v, n, p, ochki]
        v = ochki = i = 0
    kol -= 1
z = v = n = p = ochki = sch = 0
g = []
for i in vivod:
    if type(i) == str and i not in g:
        g += [i]
for i in range(len(g)):
    for j in range(len(vivod)):
        if g[i] == vivod[j]:
            z += vivod[j + 1]
            v += vivod[j + 2]
            n += vivod[j + 3]
            p += vivod[j + 4]
            ochki += vivod[j + 5]
    print(g[i] + ':' + str(z), v, n, p, ochki)
    z = v = n = p = ochki = sch = 0             