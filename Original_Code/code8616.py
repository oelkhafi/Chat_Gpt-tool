n = int(input())
statistic = {'Games':0,'Win':0,'Draw':0,'Lose':0,'Score':0}
teams = dict()
for i in range(n): 
    in_data = input().split(';')
    if in_data[0] not in teams:
        teams[in_data[0]] = dict(statistic)
    if in_data[2] not in teams:
        teams[in_data[2]] = dict(statistic)
    teams[in_data[0]]['Games'] += 1
    teams[in_data[2]]['Games'] += 1
    if int(in_data[1]) > int(in_data[3]):
        teams[in_data[0]]['Win'] += 1
        teams[in_data[2]]['Lose'] += 1
        teams[in_data[0]]['Score'] += 3
    elif int(in_data[1]) < int(in_data[3]):
        teams[in_data[2]]['Win'] += 1
        teams[in_data[0]]['Lose'] += 1
        teams[in_data[2]]['Score'] += 3
    else:
        teams[in_data[2]]['Draw'] += 1
        teams[in_data[0]]['Draw'] += 1
        teams[in_data[2]]['Score'] += 1
        teams[in_data[0]]['Score'] += 1
for team, stat in teams.items():
    print(team + ':',end='')
    print(stat['Games'],stat['Win'],stat['Draw'],stat['Lose'],stat['Score']) 