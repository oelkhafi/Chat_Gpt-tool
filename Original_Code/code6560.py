import re

def duplication(values):
    hand = """".join(sorted(values))
    pattern = r'((\w)(\2+))'
    res = re.findall(pattern, hand)
    if len(res) == 1:
        if len(res[0][0]) == 2:
            return 100
        elif len(res[0][0]) == 3:
            return 300
        else:
            return 800
    elif len(res) == 2:  
        if len(res[0][0]) == 2 and len(res[1][0]) == 2:
            return 200
        else:
            return 700
    return 0

def flush(suits):
    hand = """".join(sorted(suits))
    pattern = r'((\w)(\2+))'    
    res = re.findall(pattern, hand)
    if len(res[0][0]) == 5:
        return 500
    else:
        return 0
    
def straight(values):
    cards = ""23456789TJQKA""
    values.sort(key = lambda x: cards.find(x))
    hand = """".join(values)
    if hand in cards:
        if hand.endswith(""A""):
            return 499
        else:
            return 400
    else:
        return 0
    
def hand_score(hand):    
    hand = hand.replace(""10"", ""T"").split()
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    d = duplication(values)
    f = flush(suits)
    s = straight(values)

    score = {
          0 : ""High Card"",
        100 : ""Pair"",
        200 : ""Two Pairs"",
        300 : ""Three of a Kind"",
        400 : ""Straight"",
        499 : ""Straight"",
        500 : ""Flush"",
        700 : ""Full House"",
        800 : ""Four of a Kind"",
        900 : ""Straight Flush"",
        999 : ""Royal Flush""
    }
    
    return score[d + f + s]

print(hand_score(input()))

 