#!/usr/bin/python3

deck = (""2"", ""3"", ""4"", ""5"", ""6"", ""7"", ""8"", ""9"", ""10"", ""J"", ""Q"", ""K"", ""A"")


def count_cards(cards, deck):
    cards = [card[:-1] for card in cards]
    return [cards.count(card) for card in deck]


def check_flush(cards):
    suits = [card[-1] for card in cards]
    if len(set(suits)) == 1:
        return True
    return False


def check_straight(cards):
    for index in range(len(deck)):
        num_of_cards = count_cards(cards, (deck[index:]+deck[:index]))
        if ("""".join([str(num) for num in num_of_cards[:5]])) == ""11111"":
            return True
    return False


def check_royal(cards):
    cards = [card[:-1] for card in cards]
    for value in (""10"", ""J"", ""Q"", ""K"", ""A""):
        if value not in cards:
            return False
    return True


def best_hand(cards):
    if check_royal(cards) and check_flush(cards):
        return ""Royal Flush""
    elif check_straight(cards) and check_flush(cards):
        return ""Straight Flush""
    elif (4 in count_cards(cards, deck)):
        return ""Four of a Kind""
    elif ((3 in count_cards(cards, deck)) and (2 in count_cards(cards, deck))):
        return ""Full House""
    elif check_flush(cards):
        return ""Flush""
    elif check_straight(cards):
        return ""Straight""
    elif (3 in count_cards(cards, deck)):
        return ""Three of a Kind""
    elif (count_cards(cards, deck).count(2) == 2):
        return ""Two Pairs""
    elif (2 in count_cards(cards, deck)):
        return ""Pair""
    else:
        return ""High Card""


if __name__ == '__main__':
    data = input().split()
    print(best_hand(data))

    # Test
    # data_dict = {""9C JC QC KC AC"": ""Flush"",
                 # ""9C JC QC KC 9D"": ""Pair"",
                 # ""AC JC QC KC AD"": ""Pair"",
                 # ""2C 2S QC KC 9D"": ""Pair"",
                 # ""10H JD QD KS AC"": ""Straight"",
                 # ""2C 3C 4C 5C AC"": ""Straight Flush"",
                 # ""6S 7S 8S 9S 10S"": ""Straight Flush"",
                 # ""10C 7D 8S 9H 6C"": ""Straight"",
                 # ""2C 3D 4S 5H AC"": ""Straight"",
                 # ""AC 3D 9C 5C 6C"": ""High card"",
                 # ""AC 2H 3D 4C 5C"": ""Straight"",
                 # ""AC QC QC 10C AC"": ""Flush"",
                 # ""10H JH QH KH AH"": ""Royal Flush"",
                 # ""JS QS AS KS 10S"": ""Royal Flush"",
                 # ""10S 10D 10C KD AD"": ""Three"",
                 # ""AC 10D 10C AS AD"": ""Full House"",
                 # ""AC 2D 2C AS AD"": ""Full House"",
                 # ""2C 10D 10C 2S 2D"": ""Full House"",
                 # ""10C JS AC 10D AH"": ""Two pair"",
                 # ""10C 10S 10D 10D AH"": ""Four"",
                 # ""AC AS 10D AD AH"": ""Four"",
                 # ""9C JC QH KC AC"": ""High card"",
                 # ""10C AS 10H AD AC"": ""Full House"",
#                  ""10H AC QD KS JH"": ""Straight""}

    # for card in data_dict:
        # print(card, ""-->"", data_dict[card], "">>>"", best_hand(card.split()))
 