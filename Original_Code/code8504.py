values = {'6': 1, '7': 2, '8': 3,
          '9': 4, 'T': 5, 'J': 6,
          'Q': 7, 'K': 8, 'A': 9
          }
card_check = input().split()
for i in card_check:
    if '10' in i:
        card_check[card_check.index(i)] = 'T' + i[2]
first, second = card_check
trump = input()
if trump not in first and trump not in second:
        if first[1] == second[1] and first[0] != second[0]:
            print('First' if values[first[0]] > values[second[0]] else 'Second')
        else:
            print('Error')
else:
    if trump in first and trump in second:
        if first[0] != second[0]: 
            print('First' if values[first[0]] > values[second[0]] else 'Second')
        else:
            print('Error')
    elif trump in first:
        print('First')
    else:
        print('Second')
             