a1 = ' -- '
a2 = '|  |'
a3 = '    '
a4 = '   |'
a5 = '|   '
d = {'0': [a1, a2, a2, a3, a2, a2, a1],
     '1': [a3, a4, a4, a3, a4, a4, a3],
     '2': [a1, a4, a4, a1, a5, a5, a1],
     '3': [a1, a4, a4, a1, a4, a4, a1],
     '4': [a3, a2, a2, a1, a4, a4, a3],
     '5': [a1, a5, a5, a1, a4, a4, a1],
     '6': [a1, a5, a5, a1, a2, a2, a1],
     '7': [a1, a4, a4, a3, a4, a4, a3],
     '8': [a1, a2, a2, a1, a2, a2, a1],
     '9': [a1, a2, a2, a1, a4, a4, a1]}
s = input().strip()
print(f""""""x{'-'*(len(s)*4+len(s)-1)}x"""""")
for y in range(7):
    print('|', end='')
    for x, i in enumerate(s):
        print(d[i][y], end='|' if x == len(s)-1 else ' ')
    print()
print(f""""""x{'-'*(len(s)*4+len(s)-1)}x"""""", end='') 