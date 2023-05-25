new=[]
field = input()
if field[0]=='#':
    if field[1]=='.':
        new.append('.')
    else:
        new.append('#')
elif field[0]=='.':
    if field[1]=='#':
        new.append('#')
    else:
        new.append('.')
for i in range(1,len(field)-1):
    if field[i]== '#':
        if (field[i - 1] == '#' and field[i + 1] == '#') or (field[i - 1] == '.' and field[i + 1] == '.'):
            new.append('.')
        else:
            new.append('#')
    elif field[i]== '.':
        if field[i - 1]== '#' or field[i + 1]== '#':
            new.append('#')
        else:
            new.append('.')
if field[-1]=='#':
    if field[-2]=='.':
        new.append('.')
    else:
        new.append('#')
elif field[-1]=='.':
    if field[-2]=='#':
        new.append('#')
    else:
        new.append('.')
print(new) 