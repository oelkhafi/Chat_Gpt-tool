size = int(input())
number = size
matrix = []
for counter in range(number):
    matrix.append([])
    for counter2 in range(number):
        matrix[counter].append(0)
directions = []
for counter in range(1, number):
    directions.append('right')
for counter in range(1, number):
    directions.append('down')
for counter in range(1, number):
    directions.append('left')
number -= 1
while number > 1:
    if directions[-1] == 'left':
        for counter in range(1, number):
            directions.append('up')
        for counter in range(1, number):
            directions.append('right')
    elif directions[-1] == 'up':
        for counter in range(1, number):
            directions.append('right')
        for counter in range(1, number):
            directions.append('down')
    elif directions[-1] == 'right':
        for counter in range(1, number):
            directions.append('down')
        for counter in range(1, number):
            directions.append('left')
    elif directions[-1] == 'down':
        for counter in range(1, number):
            directions.append('left')
        for counter in range(1, number):
            directions.append('up')
    number -= 1
rows = 0
columns = 0
matrix[0][0] = 1
value = 1
for counter in range(len(directions)):
    value += 1
    if directions[counter] == 'right':
        columns += 1
    elif directions[counter] == 'down':
        rows += 1
    elif directions[counter] == 'left':
        columns -= 1
    elif directions[counter] == 'up':
        rows -= 1
    matrix[rows][columns] = value
for counter in range(size):
    for counter2 in range(size):
        print(matrix[counter][counter2], end = ' ')
    print()
 