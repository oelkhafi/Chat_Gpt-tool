rows, columns = map(int, input().split())
lst = [input() for i in range(rows)]

for i in range(rows):
    if i == rows - 1:
        i = - 1
    for j in range(columns):
        if j == columns - 1:
            j = - 1
        if columns > 1:
            s = lst[i][j] + lst[i][j-1] + lst[i][j+1] + lst[i-1][j] + lst[i-1][j-1] + lst[i-1][j+1] +\
                lst[i+1][j] + lst[i+1][j-1] + lst[i+1][j+1] if len(lst) > 1\
                else lst[i][j] * 3 + lst[i][j-1] * 3 + lst[i][j+1] * 3
            count = s.count('X')
            if lst[i][j] == '.':
                print('X' if count == 3 else '.', end='')
            elif lst[i][j] == 'X':
                print('X' if 2 <= count - 1 <= 3 else '.', end='')
        else:
            s = lst[i] * 3 + lst[i+1] * 3 + lst[i-1] * 3
            count = s.count('X')
            if lst[i][j] == '.':
                print('X' if count == 3 else '.', end='')
            elif lst[i][j] == 'X':
                print('X' if 2 <= count-1 <= 3 else '.', end='')
    print()
 