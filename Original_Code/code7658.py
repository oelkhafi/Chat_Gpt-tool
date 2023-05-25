d = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def sort_s(s):
    for i in range(4):
        for j in range(4):
            if d.index(s[j][:-1]) > d.index(s[j+1][:-1]):
                s[j], s[j+1] = s[j+1], s[j]
    return s
                
def same(s):
    if s[0][-1] == s[1][-1] and s[0][-1] == s[2][-1] and s[0][-1] == s[3][-1] and s[0][-1] == s[4][-1]:
        return True
    return False

s = input().split()
s = sort_s(s)

if s[0][:-1] == '10' and s[1][:-1] == 'J' and s[2][:-1] == 'Q' and s[3][:-1] == 'K' and s[4][:-1] == 'A' and same(s):
    print('Royal Flush')
elif same(s) and (d.index(s[4][:-1]) - d.index(s[3][:-1]) == 1 and d.index(s[3][:-1]) - d.index(s[2][:-1]) == 1 and d.index(s[2][:-1]) - d.index(s[1][:-1]) == 1 and d.index(s[1][:-1]) - d.index(s[0][:-1]) == 1 or s[0][:-1] == '2' and s[1][:-1] == '3' and s[2][:-1] == '4' and s[3][:-1] == '5' and s[4][:-1] == 'A'):
    print('Straight Flush')
elif d.index(s[3][:-1]) == d.index(s[2][:-1]) and d.index(s[2][:-1]) == d.index(s[1][:-1]) and (d.index(s[4][:-1]) == d.index(s[3][:-1]) or d.index(s[1][:-1]) == d.index(s[0][:-1])):
    print('Four of a Kind')
elif ( d.index(s[4][:-1]) == d.index(s[3][:-1]) and d.index(s[3][:-1]) == d.index(s[2][:-1]) and d.index(s[1][:-1]) == d.index(s[0][:-1]) ) or ( d.index(s[4][:-1]) == d.index(s[3][:-1]) and d.index(s[2][:-1]) == d.index(s[1][:-1]) and d.index(s[1][:-1]) == d.index(s[0][:-1]) ):
    print('Full House')
elif same(s):
    print('Flush')
elif d.index(s[4][:-1]) - d.index(s[3][:-1]) == 1 and d.index(s[3][:-1]) - d.index(s[2][:-1]) == 1 and d.index(s[2][:-1]) - d.index(s[1][:-1]) == 1 and d.index(s[1][:-1]) - d.index(s[0][:-1]) == 1 or (s[0][:-1] == '2' and s[1][:-1] == '3' and s[2][:-1] == '4' and s[3][:-1] == '5' and s[4][:-1] == 'A'):
    print('Straight')
elif d.index(s[4][:-1]) == d.index(s[3][:-1]) and d.index(s[3][:-1]) == d.index(s[2][:-1]) or d.index(s[3][:-1]) == d.index(s[2][:-1]) and d.index(s[2][:-1]) == d.index(s[1][:-1]) or d.index(s[2][:-1]) == d.index(s[1][:-1]) and d.index(s[1][:-1]) == d.index(s[0][:-1]):
    print('Three of a Kind')
elif (d.index(s[4][:-1]) == d.index(s[3][:-1]) and d.index(s[2][:-1]) == d.index(s[1][:-1])) or (d.index(s[3][:-1]) == d.index(s[2][:-1]) and d.index(s[1][:-1]) == d.index(s[0][:-1])) or (d.index(s[4][:-1]) == d.index(s[3][:-1]) and d.index(s[1][:-1]) == d.index(s[0][:-1])):
    print('Two Pairs')
elif d.index(s[4][:-1]) == d.index(s[3][:-1]) or d.index(s[3][:-1]) == d.index(s[2][:-1]) or d.index(s[2][:-1]) == d.index(s[1][:-1]) or d.index(s[1][:-1]) == d.index(s[0][:-1]):
    print('Pair')
else:
    print('High Card') 