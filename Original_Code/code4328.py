def is_kvadrat(i0, j0):
    i, j = i0, j0
    while True:
        if field[i0][j] == '1' and field[i][j0] == '1':
            i, j = i+1, j+1
        elif field[i0][j] == field[i][j0] == '0':
            return True
        else:
            return False
            
        
lines, rows = map(int, input().split())
field = [input().split() for _ in range(lines)]

# add empty borders
field = [['0']*(rows+2)] + [['0'] + field[i] + ['0'] for i in range(lines)] + [['0']*(rows+2)]

count = 0
for i in range(1, lines+1):
    for j in range(1, rows+1):
        if field[i][j] == '1' and field[i-1][j] == '0' and field[i][j-1] == '0':
            count += is_kvadrat(i, j)
print(count)
 