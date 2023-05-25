l = [input().split(';') for i in range(int(input()))]
table = {}
for i in l:
    if i[0] not in table.keys():
        table[i[0]] = [0, 0, 0, 0, 0]
    if i[2] not in table.keys():
        table[i[2]] = [0, 0, 0, 0, 0]
    table[i[0]][0] += 1
    table[i[2]][0] += 1
    if i[1] > i[3]:
        table[i[0]][1] += 1
        table[i[2]][3] += 1
        table[i[0]][4] += 3
    elif i[1] < i[3]:
        table[i[2]][1] += 1
        table[i[0]][3] += 1
        table[i[2]][4] += 3
    else:
        table[i[0]][2] += 1
        table[i[2]][2] += 1
        table[i[0]][4] += 1
        table[i[2]][4] += 1
for k, v in table.items():
    print(k, end = ':')
    print(*v) 