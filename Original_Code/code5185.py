size = int(input())

table = [[0 for j in range(size)] for i in range(size)]

lower_bond = 0
upper_bond = size - 1
squares_num = size - 2

count = 0
while count != size ** 2:
    turn = 0
    if lower_bond == upper_bond:
        count += 1
        table[lower_bond][upper_bond] = count
        break
    for k in range(4):
        turn += 1
        for i in range(lower_bond, upper_bond):
            count += 1
            if turn == 1:
                table[lower_bond][i] = count
            if turn == 2:
                table[i][upper_bond] = count
            if turn == 3:
                table[upper_bond][-i-1] = count
            if turn == 4:
                table[-i-1][lower_bond] = count
    lower_bond += 1
    upper_bond -= 1


for i in range(size):
    print(' '.join(map(str,table[i])))
 