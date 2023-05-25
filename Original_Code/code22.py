s = input()
a1 = 'x'
a2 = '|'
a3 = '|'
a4 = '|'
a5 = '|'
a6 = '|'
a7 = '|'
a8 = '|'
a9 = 'x'
for i in range(len(s)):
    a1 += '-----'
    a9 += '-----'
    if s[i] == '1' or s[i] == '4':
        a2 += '     '
    else:
        a2 += ' --  '
    if s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '7':
        a3 += '   | '
        a4 += '   | '
    elif s[i] == '5' or s[i] == '6':
        a3 += '|    '
        a4 += '|    '
    else:
        a3 += '|  | '
        a4 += '|  | '
    if s[i] == '0' or s[i] == '1' or s[i] == '7':
        a5 += '     '
    else:
        a5 += ' --  '
    if s[i] == '0' or s[i] == '6' or s[i] == '8':
        a6 += '|  | '
        a7 += '|  | '
    elif s[i] == '2':
        a6 += '|    '
        a7 += '|    '
    else:
        a6 += '   | '
        a7 += '   | '
    if s[i] == '1' or s[i] == '4' or s[i] == '7':
        a8 += '     '
    else:
        a8 += ' --  '
print(a1[:-1]+'x')
print(a2[:-1]+'|')
print(a3[:-1]+'|')
print(a4[:-1]+'|')
print(a5[:-1]+'|')
print(a6[:-1]+'|')
print(a7[:-1]+'|')
print(a8[:-1]+'|')
print(a9[:-1]+'x')
 