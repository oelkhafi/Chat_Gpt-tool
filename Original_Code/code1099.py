from functools import reduce, partial
from itertools import combinations as cmb


def getValueOrder(value):
    order = {'6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 11,
             'Q': 12,
             'K': 13,
             'A': 14}
    if value in order:
        return order[value]
    return None


def getCardOrder(card, trump):
    (value, suit) = card
    order = getValueOrder(value)
    if order is None:
        return None
    if suit == trump:
        order *= 10
    return order


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


""""""
res - (processCode, prevOrder);
    processCode - code of previous comparsion:
       -  None - there was not comparsion;
       -  0 - not in order (Error);
       -  1 - increased order;
       - -1 - decreasd order;
    prevOrder;
order - order value of the current card
""""""
def processOrder(res, order):
    (processCode, prevOrder) = res
    if prevOrder == -1:
        # fist entrance
        return (processCode, order)
    if processCode == 0:
        return res
    
    cmpSign = sign(order-prevOrder)
    
    if processCode == None:
        # fist compare
        return (cmpSign, order)
    if processCode != cmpSign:
        return (0,0)
    
    return (cmpSign, order)
    

""""""
Take list of cards. Eache card contains two chars.
First is value. Second is suit.
Trump is a code of trump suit.
""""""
def cmpCards(cards, trump):
    notComparable = any(map(
        lambda p: p[0][1]!=p[1][1] and p[0][1]!=trump and p[1][1]!=trump,
        cmb(cards, 2)))
    if notComparable:
        return ""Error""
    
    orders = map(partial(getCardOrder, trump=trump), cards)
    (processCode,_) = reduce(processOrder, orders, (None,-1))
    
    if processCode < 0:
        return ""First""
    if processCode > 0:
        return ""Second""
    
    return ""Error""

    
cards = list(map(lambda x: [x[:-1], x[-1]], input().strip().split()))
trump = input().strip()

print(cmpCards(cards, trump))
 