row, col = input().split()
row, col = int(row), int(col)
field = [
    [(0 if i == ""."" else 1)
        for i in input()]
        for i in range(row)
        ]

def ExtendedField(row, col):
    newfield = [[0 for i in range(col + 2)]for j in range(row + 2)]
    for i in range(row):
        newfield[i + 1][1:col + 1] = field[i][0:col]
    return newfield

newfield = ExtendedField(row, col)
for i in range(1, row+1):
    for j in range(1, col+1):
        x = newfield[i][j]
        if x == 1:
            print(""*"", end="""")
        else:
            xi = i - 1
            xj = j - 1
            res = (
                sum(newfield[xi+0][xj:(xj+3)])+
                sum(newfield[xi+1][xj:(xj+3)])+
                sum(newfield[xi+2][xj:(xj+3)])
                ) - x
            print(res, end="""")
    print() 