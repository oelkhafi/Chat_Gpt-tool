a = input().split()
matrix = []
while True:
    if a != ['end']:
        a = [int(i) for i in a]
        matrix.append(a)
        a = input().split()
    if a == ['end']:
        break
rows = len(matrix)  # строки
cols = len(matrix[0]) # колонки
i = 0
j = 0
while i <= rows - 1: # самая нижняя строка
    while j <= cols - 1:  # самый правый столбец
        if j != cols - 1 and i != rows - 1:  # некрайние нигде, вроде работает
            above = matrix[i - 1][j]
            right = matrix[i][j + 1]
            left = matrix[i][j - 1]
            below = matrix[i + 1][j]
            summA = above + below + left + right
            print(summA, end = ' ')
            j += 1
            if j == cols - 1:
                continue 
        if j != cols - 1 and i == rows - 1:  # не-правый нижний 
            above = matrix[i - 1][j]
            left = matrix[i][j - 1]
            below = matrix[0][j]  # верхняя в противоположной
            right = matrix[i][j + 1]
            summA = above + below + left + right
            print(summA, end = ' ')
            j += 1
            if j == cols - 1:
                continue
        if j == cols - 1 and i != rows - 1:  # посл.столбец непоследней стр.
            above = matrix[i - 1][j]
            left = matrix[i][j - 1]
            right = matrix[i][0]
            below = matrix[i + 1][j]
            summA = above + right + left + below
            print(summA, end = ' ')
            j += 1
        if j == cols - 1 and i == rows - 1:
            above = matrix[i - 1][j]
            left = matrix[i][j - 1]
            summA = above + matrix[0][j] + left + matrix[i][0]
            print(summA, end = ' ')
            break
    j = 0
    i += 1
    print()
     