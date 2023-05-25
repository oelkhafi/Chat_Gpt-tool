n = int(input())
tournament = {}
team = {'game': 0,
        'win': 0,
        'a_draw': 0,
        'lose': 0,
        'points': 0
        }
for game in range(n):
    count = 0
    team1, score1, team2, score2 = list(input().split(';'))
    if team1 in tournament:  # first team
        tournament[team1]['game'] += 1
    else:
        tournament[team1] = team.copy()
        tournament[team1]['game'] += 1
    if team2 in tournament:  # second team
        tournament[team2]['game'] += 1
    else:
        tournament[team2] = team.copy()
        tournament[team2]['game'] += 1
    if score2 != score1 > score2:  # points
        tournament[team1]['win'] += 1
        tournament[team2]['lose'] += 1
    elif score2 == score1:
        tournament[team1]['a_draw'] += 1
        tournament[team2]['a_draw'] += 1
    elif score1 != score2 > score1:
        tournament[team1]['lose'] += 1
        tournament[team2]['win'] += 1
    tournament[team1]['points'] = (tournament[team1]['win']) * 3 + (tournament[team1]['a_draw']) * 1
    tournament[team2]['points'] = (tournament[team2]['win']) * 3 + (tournament[team2]['a_draw']) * 1
for i in tournament:
    a = tournament[i].values()
    b = str(i) + ': '
    for j in a:
        b += str(j) + ' '
    print(b)
 