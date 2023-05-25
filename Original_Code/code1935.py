numberOfGames = int(input())
d = dict()
matchResult = []
def update_teams(d, team):
    if (team not in d):
        d[team] = [0, 0, 0, 0, 0]

def update_score(d, result):
    if(result[1] > result[3]):
        d[result[0]][0] += 1
        d[result[0]][1] += 1
        d[result[0]][4] += 3
        d[result[2]][0] += 1
        d[result[2]][3] += 1
    elif (result[1] == result[3]):
        d[result[0]][0] += 1
        d[result[0]][2] += 1
        d[result[0]][4] += 1
        d[result[2]][0] += 1
        d[result[2]][2] += 1
        d[result[2]][4] += 1
    else:
        d[result[2]][0] += 1
        d[result[2]][1] += 1
        d[result[2]][4] += 3
        d[result[0]][0] += 1
        d[result[0]][3] += 1

for i in range(numberOfGames):
    matchResult.append(input().split(';'))
    update_teams(d, matchResult[i][0])
    update_teams(d, matchResult[i][2])
    update_score(d, matchResult[i])

for key, values in d.items():
    print(key + ': ', values[0], values[1], values[2], values[3], values[4], end = '')
    print() 