str_in = input()
frame = f'x{""-"" * (len(str_in) * 5 - 1)}x'
numbers = [
    [1, 2, 2, 0, 2, 2, 1],
    [0, 4, 4, 0, 4, 4, 0],
    [1, 4, 4, 1, 3, 3, 1],
    [1, 4, 4, 1, 4, 4, 1],
    [0, 2, 2, 1, 4, 4, 0],
    [1, 3, 3, 1, 4, 4, 1],
    [1, 3, 3, 1, 2, 2, 1],
    [1, 4, 4, 0, 4, 4, 0],
    [1, 2, 2, 1, 2, 2, 1],
    [1, 2, 2, 1, 4, 4, 1]
]

patterns = [
    '    ',
    ' -- ',
    '|  |',
    '|   ',
    '   |'
]


print(frame)
for i in range(7):
    s_out = ''
    for k in str_in:
        s_out += patterns[numbers[int(k)][i]] + ' '
    print(f'|{s_out[:-1]}|')
print(frame)
 