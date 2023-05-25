lst = [input() for _ in range(2)]
lst.sort()
a = ''.join(lst)
t = ('paper', 'rock', 'scissors')
game_map = {
    f'{t[0]}{t[1]}': 'Paper wins!',
    f'{t[0]}{t[2]}': 'Scissors win!',
    f'{t[1]}{t[2]}': 'Rock wins!',
    f'{t[0]}{t[0]}': ""It's a tie!"",
    f'{t[1]}{t[1]}': ""It's a tie!"",
    f'{t[2]}{t[2]}': ""It's a tie!"",
}
res = game_map.get(a)
if not res:
    print('Invalid input! You have not entered rock, paper or scissors, try again.')
else:
    print(res)



 