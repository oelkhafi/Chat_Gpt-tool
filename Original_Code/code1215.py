cards = '67891JQKA'
reply = ('Second', 'Error', 'First')

a, b = map(str,input().split())
x = a [-1]
y = b [-1]
if x == y:
    r = cards.find (a [0]) - cards.find (b [0])
    if r > 1:
        r = 1
    elif r < -1:
        r = -1
else:
    w = input()
    if x == w:
        r = 1
    elif y == w:
        r = -1
    else:
        r = 0
print (reply [r + 1])




 