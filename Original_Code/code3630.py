def addTeamData(teamName,data):
    if teamName in teams: 
        teams[teamName][0] += data[0]
        teams[teamName][1] += data[1]
        teams[teamName][2] += data[2]
        teams[teamName][3] += data[3]
        teams[teamName][4] += data[4]
    else: teams[teamName] = data
teams = dict()
n = int(input())
for i in range(n):
    teamA,goalA,teamB,goalB = input().split(';')
    if goalA > goalB: 
        addTeamData(teamA,[1,1,0,0,3])
        addTeamData(teamB,[1,0,0,1,0])
    elif goalA < goalB: 
        addTeamData(teamA,[1,0,0,1,0])
        addTeamData(teamB,[1,1,0,0,3])
    elif goalA == goalB:
        addTeamData(teamA,[1,0,1,0,1])
        addTeamData(teamB,[1,0,1,0,1])
for team,points in teams.items():
    print(team + ':', points[0], points[1],points[2],points[3],points[4]) 