def poker(lst):
    from collections import defaultdict

    def seq(r):
        a = sorted([i - r[0] for i in r]) == [0, 1, 2, 3, 4]
        return a or r == [0, 1, 2, 3, 12]

    ind = dict(zip(['2', '3', '4', '5', '6', '7', '8', '9', '10',\
                      'J', 'Q', 'K', 'A'], range(13)))
    lst1 = sorted([ind[card[:-1]] for card in lst])
    lst2 = set([i[-1] for i in lst])
    dct = defaultdict(list)
    for i in set(lst1):
        dct[lst1.count(i)].append(i)
    if len(lst2) == 1 and lst1 == [8, 9, 10, 11, 12]:
        return 'Royal Flush'
    elif len(lst2) == 1 and seq(lst1):
        return 'Straight Flush'
    elif len(dct[4]) == 1:
        return 'Four of a Kind'
    elif len(dct[3]) == 1 and len(dct[2]) == 1:
        return 'Full House'
    elif len(lst2) == 1:
        return 'Flush'
    elif seq(lst1):
        return 'Straight'
    elif len(dct[3]) == 1:
        return 'Three of a Kind'
    elif len(dct[2]) == 2:
        return 'Two Pairs'
    elif len(dct[2]) == 1:
        return 'Pair'
    else:
        return 'High Card'

lst = input().split()
print(poker(lst))
 