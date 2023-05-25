def cell(a):
    b = []
    if a[0] == '#' and a[1] == '.':
        b.append('.')
    elif a[0] == '.' and a[1] == '#':    
            b.append('#')
    else:
        b.append(a[0])
    
    for i in range(1, len(a)-1):
        if a[i] == '#' and (a[i-1] == a[i+1] == '#'):
            b.append('.')
        elif a[i] == '#' and (a[i-1] == a[i+1] == '.'):    
            b.append('.')
        elif a[i] == '.' and (a[i-1] == '#' or a[i+1] == '#'):
            b.append('#')
        else:
            b.append(a[i])
        
    if len(a) > 1:
        if a[-1] == '#' and a[-2] == '.':
            b.append('.')
        elif a[-1] == '.' and a[-2] == '#':
            b.append('#')
        else:
            b.append(a[-1])
    return b       

a = ['#', '.', '.', '.', '.', '#']

k = int(input())
for i in range(k):
    a = cell(a)
        
print(a)    



 