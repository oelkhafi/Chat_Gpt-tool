from collections import Counter

def duplicate():  # есть карты с одинаковым достоинством
    k = c.most_common()[0][1] - len(c)
    return ('Pair', 'Two Pairs', 'Three of a Kind', 'Full House', 'Four of a Kind')[k+2]

def unduplicate():  # карты с разным достоинством
    k, straight, flash = 0, False, False
    if max(value) - min(value) == 4:  # straight
        straight = True
        k = 1
    if len(suit) == 1:  # flush
        flash = True
        k = 2
    if straight and flash:
        if min(value) == 8:
            k = 4  # Royal
        else:
            k = 3  # straight + flush
    return ('High Card', 'Straight', 'Flush', 'Straight Flush', 'Royal Flush')[k]

cards = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
s = input().split()
value = tuple(map(cards.index, (i[:-1] for i in s)))  # кортеж из индексов введенных карт
suit = {i[-1] for i in s}
c = Counter(value)
print(f'{duplicate() if len(c) < 5 else unduplicate()}')
 