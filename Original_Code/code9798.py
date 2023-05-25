table = {}
n = int(input())

for _ in range(n):
    c1, n1, c2, n2 = [int(x) if x.isdigit() else x for x in input().split(';')]
    if c1 not in table.keys():
        table.update({c1:[0, 0, 0, 0, 0]})
    if c2 not in table.keys():
        table.update({c2:[0, 0, 0, 0, 0]})
    table[c1][0] += 1
    table[c2][0] += 1
    if n1 > n2:
        table[c1][1] += 1
        table[c1][4] += 3
        table[c2][3] += 1
    elif n1 == n2:
        table[c1][2] += 1
        table[c1][4] += 1
        table[c2][2] += 1
        table[c2][4] += 1
    if n1 < n2:
        table[c1][3] += 1
        table[c2][1] += 1
        table[c2][4] += 3

for key, value in table.items():
    print('{}: {}'.format(key, ' '.join(map(str, value))))
 