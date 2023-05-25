dim = int(input())
table = [[0 for i in range(dim)] for j in range(dim)]
i, j, cnt = 0, 0, 0
while 0 <= j < dim and 0 <= i < dim and table[i][j] == 0:
    while j < dim and table[i][j] == 0:
        cnt += 1
        table[i][j] = cnt
        j += 1
    i += 1
    j -= 1
    while i < dim and table[i][j] == 0:
        cnt += 1
        table[i][j] = cnt
        i += 1
    j -= 1
    i -= 1
    while j >= 0 and table[i][j] == 0:
        cnt += 1
        table[i][j] = cnt
        j -= 1
    j += 1
    i -= 1
    while i >= 0 and table[i][j] == 0:
        cnt += 1
        table[i][j] = cnt
        i -= 1
    i += 1
    j += 1
for i in table:
    for j in i:
        print(j, end='\t')
    print() 