def sumMatrix(a,b):
    c = []
    for i in range(len(a)): c.append(a[i]+b[i])
    return c

teams = dict()

n = int(input())
for i in range(n):
    teamA,goalA,teamB,goalB = input().split(';')

    a = [1,0,0,0,0]
    b = [1,0,0,0,0]

    if goalA > goalB: 
        a[1] = 1 #количество побед
        a[4] = 3 #количество очков
        b[3] = 1 #количество поражений
    elif goalA < goalB: 
        b[1] = 1
        b[4] = 3
        a[3] = 1
    elif goalA == goalB:
        a[2],a[4],b[2],b[4] = 1,1,1,1
    if teamA in teams: teams[teamA] = sumMatrix(teams[teamA],a)
    else: teams[teamA] = a
    if teamB in teams: teams[teamB] = sumMatrix(teams[teamB],b)
    else: teams[teamB] = b

for team,points in teams.items():
    print(team + ':', points[0], points[1],points[2],points[3],points[4])
 