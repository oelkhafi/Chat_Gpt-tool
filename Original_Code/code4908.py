from sys import stdin

games = [x.split(';') for x in stdin.read().splitlines()[1:]]

data = {}
for game in games:
    if game[0] not in data:
        data.update({game[0]: [0, 0, 0, 0, 0]})
    if game[2] not in data:
        data.update({game[2]: [0, 0, 0, 0, 0]})

for game in games:
    if game[1] > game[3]:
        data[game[0]][1] += 1
        data[game[0]][4] += 3
        data[game[2]][3] += 1
    elif game[1] < game[3]:
        data[game[0]][3] += 1
        data[game[2]][1] += 1
        data[game[2]][4] += 3
    else:
        data[game[0]][2] += 1
        data[game[0]][4] += 1
        data[game[2]][2] += 1
        data[game[2]][4] += 1

    data[game[0]][0] += 1
    data[game[2]][0] += 1

for team, stat in data.items():
    print(f'{team}:', end='')
    print(*stat)
 