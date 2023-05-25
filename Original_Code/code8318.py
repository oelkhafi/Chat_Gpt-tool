line = input()

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

print('x' + '-' * (len(line) * 4 + len(line)-1 if len(line) > 1 else 4) + 'x')

for i in range(7):
    s = [d[j][i] for j in line]
    ss = ' '.join(s)
    print('|' + ss + '|')

print('x' + '-' * (len(line) * 4 + len(line)-1 if len(line) > 1 else 4) + 'x')



 