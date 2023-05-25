# put your python code here
from collections import Counter


def get_combination(hands):
    values = {v: k for k, v in enumerate(('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'))}

    hand_values, hand_suits = zip(*((values[c[:-1]], c[-1]) for c in hands.split()))

    subsequents_values = (sorted((i + j) % len(values) for j in range(len(hand_values))) for i in range(len(values)))
    hand_values = sorted(hand_values)

    if len(set(hand_suits)) == 1:
        if hand_values in subsequents_values:
            return 'Royal Flush' if hand_values[0] == len(values) - len(hand_values) else 'Straight Flush'
        else:
            return 'Flush'
    else:
        values_counters = Counter(hand_values).values()

        if 4 in values_counters:
            return 'Four of a Kind'
        elif 2 in values_counters and 3 in values_counters:
            return 'Full House'
        elif hand_values in subsequents_values:
            return 'Straight'
        elif 3 in values_counters:
            return 'Three of a Kind'
        elif len(values_counters) == 3 and 2 in values_counters:
            return 'Two Pairs'
        elif 2 in values_counters:
            return 'Pair'
        else:
            return 'High Card'


print(get_combination(input())) 