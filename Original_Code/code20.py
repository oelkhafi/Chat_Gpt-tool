s = {
    '2': 0, '3': 1, '4': 2, '5': 3,
    '6': 4, '7': 5, '8': 6, '9': 7,
    '10': 8, 'J': 9, 'Q': 10, 'K': 11,
    'A': 12
    }
a = input().split()
b = []
for i in a:
    b.append(s[i[:-1]])
    b = sorted(b)
if a[0][-1]==a[1][-1]==a[2][-1]==a[3][-1]==a[4][-1]:
    if (b==[8, 9, 10, 11, 12]):
        print('Royal Flush')
    elif b[0]==b[1]-1==b[2]-2==b[3]-3==b[4]-4 or b[0]==b[1]-1==b[2]-2==b[3]-3==b[4]-12:
        print('Straight Flush')
    else:
        print('Flush')
else:
    if b[0]==b[3] or b[1]==b[4]:
        print('Four of a Kind')
    elif (b[0]==b[1] and b[2]==b[4]) or (b[0]==b[2] and b[3]==b[4]):
        print('Full House')
    elif (b[0]==b[1]-1==b[2]-2==b[3]-3==b[4]-4) or (b[0]==b[1]-1==b[2]-2==b[3]-3==b[4]-12):
        print('Straight')
    elif b[0]==b[2] or b[1]==b[3] or b[2]==b[4]:
        print('Three of a Kind')
    elif ((b[0]==b[1] or b[1]==b[2]) and b[3]==b[4]) or (b[0]==b[1] and (b[2]==b[3] or b[3]==b[4])):
        print('Two Pairs')
    elif b[0]==b[1] or b[1]==b[2] or b[2]==b[3] or b[3]==b[4]:
        print('Pair')
    else:
        print('High Card')
 