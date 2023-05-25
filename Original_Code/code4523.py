rows, columns = [int(x) for x in input().split(maxsplit = 2)]
matrix = []
buffer = 0
for counter in range(rows):
    matrix.append([])
    for counter2 in range(columns):
        if counter % 2 == 0:
            if counter2 % 2 == 0:
                buffer += 1
                matrix[counter].append(buffer)
            else:
                matrix[counter].append(0)
        else:
            if counter2 % 2 == 0:
                matrix[counter].append(0)
            else:
                buffer += 1
                matrix[counter].append(buffer)
        print('{0:4}'.format(matrix[counter][counter2]), end = '')
    print()
 