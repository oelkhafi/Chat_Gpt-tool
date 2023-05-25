def number(n, size):
    num = [' ' for x in range(2 * size + 5)]
    for i in range(len(num)):
        if i == 0 or i == len(num)-1:
            num[i] = '-'*(size + 2)
        else:
            if (i in(1, 2+size, 3+size*2) and n in (2,3,5,6,8,9)) or (n==4 and i==2+size) or (n==7 and i==1) or (n==0 and i in (1, 3+size*2)):
                num[i] = ' '+'-'*size+' '
            elif (n in (0, 4, 8, 9) and 1<i<=(1+size)) or (n in (0,6,8) and (size+2)<i<=(size*2+2)):
                num[i] = '|' + ' ' * size + '|'
            elif (n in (1, 2, 3, 7) and 1<i<=(1+size)) or (n in (1, 3, 4, 5, 7, 9) and (size+2)<i<=(size*2+2)):
                num[i] = ' ' * (size+1) + '|'
            elif (n in (5,6) and 1<i<=(1+size)) or (n == 2 and (size+2)<i<=(size*2+2)):
                num[i] = '|' + ' ' * (size+1)
            else:
                num[i] = ' '*(size+2)
    return num

s, size = input(), 2

for i in range(2 * size + 5):
    row = [number(int(x), size)[i] for x in s]
    if i==0 or 2 * size + 5 - i == 1:
        print('x'+'-'.join(row)+'x')
    else:
        print('|'+' '.join(row)+'|') 