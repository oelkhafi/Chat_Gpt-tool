lst = [list(input().split(';')) for i in range(int(input()))]
table = {}
for i in lst:
    for k in range(0, 3, 2):
        if k not in table:
            table[i[k]] = [0, 0, 0, 0, 0]
for i in lst:
    for j in range(0, 3, 2):
        if int(i[j + 1]) > int(i[j - 1]):
            table[i[j]][0] += 1
            table[i[j]][1] += 1
            table[i[j]][4] += 3
        elif int(i[j + 1]) == int(i[j - 1]):
            table[i[j]][0] += 1
            table[i[j]][2] += 1
            table[i[j]][4] += 1
        else:
            table[i[j]][0] += 1
            table[i[j]][3] += 1
for g in table:
    print(g, end='')
    print(':', end='')
    print(*table[g])
 