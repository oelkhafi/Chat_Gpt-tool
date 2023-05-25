num_table = []
while True:
    line = input()
    if line == 'end':
        break
    else:
        num_list = [int(i) for i in line.split()]
        num_table.append(num_list)

rows = len(num_table)
columns = len(num_table[0])
new_table = [[0 for j in range(columns)] for i in range(rows)]

for i in range(rows):
    for k in range(columns):
        new_table[i][k] = (num_table[i][k-columns+1] 
                        + num_table[i][k-1] 
                        + num_table[i-rows+1][k]
                        + num_table[i-1][k])

for i in range(rows):
    print(' '.join(map(str,new_table[i])))        
 