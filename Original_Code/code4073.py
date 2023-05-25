# C, D, H, S
value = { '6' : 1, '7' : 2, '8' : 3, '9': 4, '10' : 5, 'J' : 6, 'Q' : 7, 'K' : 8, 'A' : 9} 
card = input().split()
w = input()
#print(card[0][:-1],card[0][-1])
#print(card[1][:-1],card[1][-1])

if card[0][-1] == w and card[1][-1] == w:
    if value[card[0][:-1]] > value[card[1][:-1]]: print(""First"")
    if value[card[1][:-1]] > value[card[0][:-1]]: print(""Second"")
    if value[card[1][:-1]] == value[card[0][:-1]]: print(""Error"")
        
elif card[0][-1] == w: print(""First"")
elif card[1][-1] == w: print(""Second"")
    
elif card[0][-1] != card[1][-1] and card[1][-1] != w and card[0][-1] != w:
    print(""Error"")

elif value[card[0][:-1]] > value[card[1][:-1]] and card[0][-1] == card[1][-1] and card[1][-1] != w:
    print(""First"")
    
elif value[card[1][:-1]] > value[card[0][:-1]] and card[0][-1] == card[1][-1] and card[0][-1] != w:
    print(""Second"")
 