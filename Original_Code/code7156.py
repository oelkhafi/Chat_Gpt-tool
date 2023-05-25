import copy


def count_neighbours(i, j):
    n = 0
    n_rows = [(rows+r)%rows for r in range(i-1, i+2, 1)]
    n_columns = [(columns+c)%columns for c in range(j-1, j+2, 1)]
    for p in n_rows:
        for q in n_columns:
            if ((p-i) != 0 or (q-j) != 0) and field0[p][q] == 'X':
                n += 1
    return n


rows, columns = map(int, input().split())
field0, field1 = [], []
for i in range(rows):
    row = list(input())
    field0.append(row)
field1 = copy.deepcopy(field0) 

for i in range(rows):
    for j in range(columns):
        n = count_neighbours(i, j)
        if (n < 2 or n > 3) and field0[i][j] == 'X':
            field1[i][j] = '.'
        elif n == 3 and field0[i][j] == '.':
            field1[i][j] = 'X'
        # in all other cases the cell remains unchanged

for i in range(rows):
    print(''.join(field1[i])) 