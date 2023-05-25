n = int(input())

d = {}
for i in range(n):
    res = input().split(';')  # [team1, score1, team2, score2]
    
    team1  = res[0]
    score1 = res[1]
    team2  = res[2]
    score2 = res[3]
    
    # add team in dictionary if not exist
    # [games_num, wins, draws, looses, scores_num]
    if team1 not in d:
        d[team1] = [0, 0, 0, 0, 0] 
    if team2 not in d:
        d[team2] = [0, 0, 0, 0, 0]
    
    # change scores 
    games_num, wins, draws, looses, scores_num = 0, 1, 2, 3, 4
    if score1 > score2:
        res = d[team1]
        res[games_num] += 1 
        res[wins] += 1 
        res[scores_num] = res[wins] * 3 + res[draws]

        res = d[team2]
        res[games_num] += 1
        res[looses] += 1
    elif score1 < score2:
        res = d[team2]
        res[games_num] += 1 
        res[wins] += 1 
        res[scores_num] = res[wins] * 3 + res[draws]

        res = d[team1]
        res[games_num] += 1
        res[looses] += 1
    else:
        res = d[team1]
        res[games_num] += 1
        res[draws] += 1
        res[scores_num] = res[wins] * 3 + res[draws]

        res = d[team2]
        res[games_num] += 1
        res[draws] += 1
        res[scores_num] = res[wins] * 3 + res[draws]

for i, k in d.items():
    print(i + ':', end='')
    print(*k)
 