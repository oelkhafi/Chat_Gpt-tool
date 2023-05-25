n = int(input())
teams = {}

for i in range(n):
    match = input().split(';')

    for i in [0, 2]:
        if match[i] not in teams:
            teams[match[i]] = [0, 0, 0]

    if int(match[1]) > int(match[3]):
        teams[match[0]][0] += 1
        teams[match[2]][2] += 1
    elif int(match[1]) < int(match[3]):
        teams[match[0]][2] += 1
        teams[match[2]][0] += 1
    else:
        teams[match[0]][1] += 1
        teams[match[2]][1] += 1

for team, val in teams.items():
    print(f'{team}:{sum(val)}'
          f'{val[0]: 2}{val[1]: 2}{val[2]: 2}'
          f'{3 * val[0] + val[1]: 2}')
 