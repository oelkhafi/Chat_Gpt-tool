def get_winkey(goals1, goals2):
    if goals1 == goals2:
        return 'Ничьих'
    elif goals1 > goals2:
        return 'Побед'
    else:
        return 'Поражений'

def add_new_team(team):
    teams[team] = {'Всего_игр': 0, 'Побед': 0, 'Ничьих': 0, 'Поражений': 0, 'Всего_очков': 0}
    
def add_team_result(team, goals, winkey):
    if team not in teams:
        add_new_team(team)
    
    teams[team][winkey] += 1
    teams[team]['Всего_игр'] += 1
    teams[team]['Всего_очков'] += scoring[winkey]
    
def add_result(team1, goals1, team2, goals2):  
    add_team_result(team1, goals1, get_winkey(goals1, goals2)) 
    add_team_result(team2, goals2, get_winkey(goals2, goals1))

scoring, teams = {'Побед': 3, 'Ничьих': 1, 'Поражений': 0}, {}

a = int(input())
for i in range(a):
    set = input().split(';')
    add_result(set[0], int(set[1]), set[2], int(set[3]))
    
for team, results in teams.items():
    print(team+':'+ str(results['Всего_игр']), str(results['Побед']), 
                    str(results['Ничьих']), str(results['Поражений']), 
                    str(results['Всего_очков'])) 