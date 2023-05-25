values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

cards, trump = input().split(), input()

card1 = values.index(cards[0][:-1])
card1suit = cards[0][-1]
card1trump = card1suit is trump

card2 = values.index(cards[1][:-1])
card2suit = cards[1][-1]
card2trump = card2suit is trump

variousSuits = card1suit is not card2suit

if variousSuits:
    if card1trump:
        print('First')
    elif card2trump:
        print('Second')
    else:
        print('Error')
else:
    if card1 > card2:
        print('First')
    elif card1 < card2:
        print('Second')
    else:
        print('Error') 