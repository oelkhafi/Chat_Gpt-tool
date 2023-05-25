n = int(input())
win, draw, defeat, points = {}, {}, {}, {}
for _ in range(n):
    values = input().split(';')
    teamA, scoreA, teamB, scoreB = values[0], int(values[1]), values[2], int(values[3])
    if scoreA < scoreB:
        tmp = scoreA
        scoreA = scoreB
        scoreB = tmp
        tmp = teamA
        teamA = teamB
        teamB = tmp    
    if scoreA == scoreB:
        draw[teamA] = draw.get(teamA, 0) + 1
        draw[teamB] = draw.get(teamB, 0) + 1
        points[teamA] = points.get(teamA, 0) + 1
        points[teamB] = points.get(teamB, 0) + 1
    else:
        win[teamA] = win.get(teamA, 0) + 1
        points[teamA] = points.get(teamA, 0) + 3
        defeat[teamB] = defeat.get(teamB, 0) + 1
        points[teamB] = points.get(teamB, 0)
for team in points.keys():
    print('%s:%d %d %d %d %d' % (team, win.get(team, 0) + draw.get(team, 0) + defeat.get(team, 0), 
                                 win.get(team, 0), draw.get(team, 0), defeat.get(team, 0), points[team])) 