
n, m = list(map(int, input().split()))
pole = [input() for _ in range(n)]
pole_new = []

for i in range(n):
    new_line = []
    for j in range(m):
        count_near = 0
        for k in (i-1, i, i+1):
            for z in (j-1, j, j+1):
                count_near += (0, 1)[pole[k%n][z%m] == 'X']
        
        if pole[i][j] == '.' and count_near == 3:
            new_line.append('X')
        elif pole[i][j] == 'X' and 2 < count_near < 5:
            # для клетки Х она тоже посчитается: 2 < count < 5
            new_line.append('X')
        else:
            new_line.append('.')
    pole_new.append(''.join(new_line))

print(*pole_new, sep='\n')
 