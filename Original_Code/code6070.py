import copy
field = [['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
 ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
#new = field.copy()
new=copy.deepcopy(field)
k = int(input())
for z in range(k):
    for m in range(0,10):
        for n in range(0,10):
            l = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if i == 0 and j == 0: continue
                    try:
                        l.append(field[m+j][n+i])
                    except:
                        continue
            if field[m][n] == '.':
                if l.count('#') == 3:
                    new[m][n] = '#'
            if field[m][n] == '#':
                if l.count('#')<2 or l.count('#')>3:
                    new[m][n] = '.'
    field = copy.deepcopy(new)
for i in new:
    print(i) 