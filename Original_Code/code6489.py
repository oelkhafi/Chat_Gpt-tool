n = int(input())
champ = []
matches = []
for i in range(n):
    str = input().split(';')
    champ += [str]
    matches += [v for v in str[0:4:2]]
teams = set(matches)
dic = {}
for team in teams:
    dic[team] = [0,0,0,0,0]
    for t in matches:
        if t == team:
            dic[team][0] += 1 # Всего_игр
for team in champ:
    if team[1] == team[3]:
        dic[team[0]][4] += 1 # Всего_очков
        dic[team[2]][4] += 1 # Всего_очков
        dic[team[0]][2] += 1 # Ничьих
        dic[team[2]][2] += 1 # Ничьих       
    elif team[1] > team[3]:
        dic[team[0]][4] += 3 # Всего_очков
        dic[team[0]][1] += 1 # Побед
        dic[team[2]][3] += 1 # Поражений
    else:
        dic[team[2]][4] += 3 # Всего_очков
        dic[team[2]][1] += 1 # Побед
        dic[team[0]][3] += 1 # Поражений 
for team in dic:
    print('{0}:'.format(team), end='')
    print(*dic[team])
 