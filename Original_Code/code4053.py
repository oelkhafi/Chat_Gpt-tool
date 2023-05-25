# Команда:0 Всего_игр 1 Побед  2 Ничьих 3 Поражений  4 Всего_очков
n = int(input())
table = {}

for i in range(n):
    game = input().split(';') # ['team', 'goalsOneTeam', 'team2, 'goalsTwoTeam']
    team = game[0]
    team2 = game[2]
    # Если команды нет в таблице, добавляем команду и пустой список
    table.setdefault(team, [0,0,0,0,0])
    table.setdefault(team2, [0,0,0,0,0])
    # кол-во голов
    goalsOneTeam = game[1]
    goalsTwoTeam = game[3]
    
    # прибавляем кол-во игр
    table[team][0] +=1
    table[team2][0] +=1
    
    if goalsOneTeam > goalsTwoTeam:
        table[team][1] +=1 # победа
        table[team][4] +=3 # всего очков
        table[team2][3] +=1 # поражение
    elif goalsOneTeam < goalsTwoTeam:
        table[team2][1] +=1 # победа
        table[team2][4] +=3 # всего очков
        table[team][3] +=1 # поражение
        
    elif goalsOneTeam == goalsTwoTeam:
        table[team][2] +=1 # ничья
        table[team2][2] +=1 # ничья
        table[team][4] +=1 # всего очков
        table[team2][4] +=1 # всего очков
    
for k,v in table.items():
    print('{}:{}'.format(k, ' '.join(map(str,v))))
 