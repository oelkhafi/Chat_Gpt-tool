num = int(input())
stand = {}
for i in range(num):
    team1, score1, team2, score2 = input().split(';')
    if team1 not in stand:
        stand[team1] = {'games': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'pts': 0}
    if team2 not in stand:
        stand[team2] = {'games': 0, 'wins': 0, 'draws': 0, 'loses': 0, 'pts': 0}
    if int(score1) > int(score2):
        stand[team1]['wins'] += 1
        stand[team2]['loses'] += 1
    elif int(score1) < int(score2):
        stand[team1]['loses'] += 1
        stand[team2]['wins'] += 1
    elif int(score1) == int(score2):
        stand[team1]['draws'] += 1
        stand[team2]['draws'] += 1
for item in stand:
    stand[item]['games'] = stand[item]['wins'] + stand[item]['draws'] + stand[item]['loses']
    stand[item]['pts'] = 3 * stand[item]['wins'] + stand[item]['draws']
    print(f""{item}:{stand[item]['games']} {stand[item]['wins']} {stand[item]['draws']} {stand[item]['loses']} {stand[item]['pts']}"")
 