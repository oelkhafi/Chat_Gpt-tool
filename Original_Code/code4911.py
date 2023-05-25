from sys import stdin

movements = stdin.read().splitlines()[1:]
x, y = 0, 0

for movement in movements:
    t = movement.split()

    if t[0] == 'север':
        y += int(t[1])
    elif t[0] == 'юг':
        y -= int(t[1])
    elif t[0] == 'восток':
        x += int(t[1])
    elif t[0] == 'запад':
        x -= int(t[1])
    else:
        raise Exception('Hmm...something went wrong...')

print(x, y)
 