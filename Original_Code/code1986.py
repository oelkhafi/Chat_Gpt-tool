val = input().split()
x = [list(input().replace('.', '0').replace('*', '1')) for i in range(int(val[0]))]

def getCell(i, j):
    if (i > -1 and i < len(x) and j > -1 and j < len(x[0])):
        return int(x[i][j])
    else:
        return 0


for i in range(len(x)):
    if (i != 0):
        print()
    for j in range(len(x[i])):
        if (x[i][j] != '1'):
            sum = 0
            sum += getCell(i - 1, j)
            sum += getCell(i + 1, j)
            sum += getCell(i, j - 1)
            sum += getCell(i, j + 1)
            sum += getCell(i - 1, j - 1)
            sum += getCell(i + 1, j - 1)
            sum += getCell(i + 1, j + 1)
            sum += getCell(i - 1, j + 1)
            print(sum, end='')
        else:
            print('*', end='')
print()
 