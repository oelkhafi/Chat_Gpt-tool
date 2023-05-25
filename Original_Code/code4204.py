# put your python code here

d = {}
games = [input().split(';') for i in range(int(input()))]
for game in games:
    team1 = game[0]
    if team1 not in d:
        d[team1] = [0, 0, 0]
    team2 = game[2]
    if team2 not in d:
        d[team2] = [0, 0, 0]
    if int(game[1]) > int(game[3]):
        d[team1][0] += 1
        d[team2][2] += 1
    if int(game[1]) < int(game[3]):
        d[team1][2] += 1
        d[team2][0] += 1
    if int(game[1]) == int(game[3]):
        d[team1][1] += 1
        d[team2][1] += 1
for key in d:
    print(key+':', sum(d[key]), *d[key], 3*d[key][0]+d[key][1])



 