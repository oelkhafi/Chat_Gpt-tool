import sys

n, m = map(int, next(sys.stdin).split())
data = []
for line in sys.stdin:
    bool_line = []
    for symbol in line.strip():
        bool_line.append(int(symbol == '*'))
    data.append(bool_line)

mines = [(row, column) for column in range(m) for row in range(n) if data[row][column]]

for row in range(n):
    for column in range(m):
        if (row, column) in mines:
            print('*', sep='', end='')
        else:
            s = sum([1 for i in (-1, 0, 1) for j in (-1, 0, 1) if (row+i, column+j) in mines])
            print(s, sep='', end='')
    print()
 