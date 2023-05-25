card1, card2 = input().split()
trump = input()

values = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
c1_val, c1_suit = card1[:-1], card1[-1:]
c2_val, c2_suit = card2[:-1], card2[-1:]

if c1_suit == c2_suit:
    if values.index(c1_val) > values.index(c2_val):
        ans = 0
    else:
        ans = 1
elif trump in (c1_suit, c2_suit):
    if c1_suit == trump:
        ans = 0
    else:
        ans = 1
else:
    ans = 2
print(['First', 'Second', 'Error'][ans])





 