d = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

x = int(input())

i = 1000
levels = []
vals = []
while i >= 1:
    letter = d[i]
    l = (x - sum(levels)) // i
    levels.append(l * i)
    if i == 1000:
        if 1 <= l <= 3:
            val = letter * l
        else:
            val = ''
    else:
        if 1 <= l <= 3:
            val = letter * l
        elif l == 4:
            val = letter + d[i * 5]
        elif 5 <= l <= 8:
            val = d[i * 5] + letter * (l - 5)
        elif l == 9:
            val = letter + d[i * 10]
        else:
            val = ''
    vals.append(val)
    i = int(i / 10)
print(''.join(vals)) 