from functools import total_ordering, reduce
from operator import sub, eq
from itertools import starmap
from collections import Counter


@total_ordering
class Card:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['C', 'D', 'H', 'S']
    value_index = {v: i for i, v in enumerate(values)}
    suit_index = {s: i for i, s in enumerate(suits)}
    def __init__(self, name):
        self.suit = name[-1]
        self.value = name[:-1]
        self.suit_idx = Card.suit_index[self.suit]
        self.value_idx = Card.value_index[self.value]
        self.rank = self.value_idx + 2

    def same_suit(self, other):
        return self.suit_idx == other.suit_idx
        
    def __eq__(self, other):
        return self.suit_idx == other.suit_idx \
               and self.value_idx == other.value_idx

    def __lt__(self, other):
        if self.value_idx == other.value_idx:
            return self.suit_idx < other.suit_idx
        return self.value_idx < other.value_idx

    def __sub__(self, subtrahend):
        return self.value_idx - subtrahend.value_idx
        
    def __str__(self):
        return self.value + self.suit

    
class PokerHand():
    rank_detectors = [
        (""Royal Flush"", lambda ph: ph.is_royal_flush()),
        (""Straight Flush"", lambda ph: ph.is_straight_flush()),
        (""Four of a Kind"", lambda ph: ph.is_count_values(4)),
        (""Full House"", lambda ph: ph.is_full_house()),
        (""Flush"", lambda ph: ph.is_flush()),
        (""Straight"", lambda ph: ph.is_straight()),
        (""Three of a Kind"", lambda ph: ph.is_count_values(3)),
        (""Two Pairs"", lambda ph: ph.is_two_pairs()),
        (""Pair"", lambda ph: ph.is_count_values(2)) ]
    
    def __init__(self, cards):
        self.cards = sorted(cards)
        
    def rank_name(self):
        for name, detector in PokerHand.rank_detectors:
            if detector(self):
                return name
        return 'High Card'
    
    def same_suit(self):
        first = self.cards[0]
        return all(map(lambda c: c.same_suit(first), self.cards[1:]))

    def count_values(self):
        res = Counter(map(lambda card: card.value, self.cards))
        return res.most_common(5)

    def count_suits(self):
        res = Counter(map(lambda card: card.suit, self.cards))
        return res.most_common(5)

    def is_count_values(self, count):
        cnt = self.count_values()
        return cnt[0][1] == count
    
    def is_royal_flush(self):
        if not self.same_suit():
            return False
        for card, value in zip(self.cards, Card.values[8:]):
            if card.value != value:
                return False
        return True
    
    def is_straight_flush(self):
        return self.same_suit() and self.is_straight()

    def is_full_house(self):
        cnt = self.count_values()
        return cnt[0][1] == 3 and cnt[1][1] == 2

    def is_flush(self):
        cnt = self.count_suits()
        return cnt[0][1] == 5

    def is_straight(self):
        difs = starmap(sub, zip(self.cards[1:], self.cards[:-1]))        
        return all(map(lambda x: x == 1, difs))

    def is_two_pairs(self):
        cnt = self.count_values()
        return cnt[0][1] >= 2 and cnt[1][1] == 2
    
    def __str__(self):
        return "" "".join(map(str, self.cards))


if __name__ == ""__main__"":
    cards = map(Card, input().split())
    ph = PokerHand(cards)
    print(ph.rank_name())
 