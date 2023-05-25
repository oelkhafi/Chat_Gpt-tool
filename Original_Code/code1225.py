d1 = '    '
d2 = ' -- '
d3 = '   |'
d4 = '|   '
d5 = '|  |'
image = {0 : (d2, d5, d5, d1, d5, d5, d2),
         1 : (d1, d3, d3, d1, d3, d3, d1),
         2 : (d2, d3, d3, d2, d4, d4, d2),
         3 : (d2, d3, d3, d2, d3, d3, d2),
         4 : (d1, d5, d5, d2, d3, d3, d1),
         5 : (d2, d4, d4, d2, d3, d3, d2),
         6 : (d2, d4, d4, d2, d5, d5, d2),
         7 : (d2, d3, d3, d1, d3, d3, d1),
         8 : (d2, d5, d5, d2, d5, d5, d2),
         9 : (d2, d5, d5, d2, d3, d3, d2),
        }

line = list(map(int, ''.join(input().split())))
frame = 'x' + '-' * 5 * len(line) + 'x'
print(frame)
for i in range(7):
    print ('|', end='')
    for n in line:
        print(image[n][i], end=' ')
    print('|')
print(frame)




 