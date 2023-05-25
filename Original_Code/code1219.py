n, m = map(int,input().split())
empty = '.'
life = 'X'
field=[]
for i in range (n):
    field += [list(input())]
for i in range(n):
    for j in range(m):
        a = (i + 1) % n
        b = (j + 1) % m
        c = i - 1
        d = j - 1
        count=0
        if field[i][b] == life: count+=1
        if field[i][d] == life: count+=1
        if field[a][j] == life: count+=1
        if field[a][b] == life: count+=1
        if field[a][d] == life: count+=1
        if field[c][j] == life: count+=1
        if field[c][b] == life: count+=1
        if field[c][d] == life: count+=1
        if ((count == 3 and field[i][j] == empty) or
            ((count == 2 or count == 3) and field[i][j] == life)):
            print(life, end='')
        else:
            print(empty, end='')
    print()




 