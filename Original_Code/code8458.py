def shorten_way(x):
    if x >= 27 or x <= -27:
        x = x % 27
    return(x)


steps = int(input())
line = input().strip()
abc = ' abcdefghijklmnopqrstuvwxyz'
answer = ''

steps = shorten_way(steps)

for letter in line:
    address = abc.find(letter) + steps
    address = shorten_way(address)
    letter = abc[address]
    answer += letter

print('Result: ""{}""'.format(answer))
 