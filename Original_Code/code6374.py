#1 Исходные данные
results, teams, goals, game_played, table = [],[],[],[],{}
#2 Ввод данных
games = int(input())                    # количество завершённых игр
for i in range(games):
    result = input().strip().split(';') # результат игры
    result[1] = int(result[1])          # забито 1-й командой
    result[3] = int(result[3])          # забито 2-й командой
    results.append(result)              # список результатов игр    
#3 Списки команд, голов 
for i in range(games):
    teams.append(results[i][0])        
    teams.append(results[i][2])
    goals.append(results[i][1])        
    goals.append(results[i][3])
team = sorted(list(set(teams)))         # список команд
#4 Шаблон сводной таблицы команд
table = {team[i]: [0]*5 for i in range(len(team))}
#5 Список количеств всего игр, сыгранных каждой командой
for i in range(len(team)):
    game_played.append(teams.count(team[i]))
    table[team[i]][0] = game_played[i]
#6 Заполнение таблицы
for i in range(games):
    if goals[2*i] > goals[2*i+1]:    # победа 1-й команды
        table[teams[2*i]][1] += 1       # количество побед 1-й команды
        table[teams[2*i+1]][3] += 1     # количество поражений 2-й команды
        table[teams[2*i]][4] += 3       # количество очков 1-й команды
    elif goals[2*i] < goals[2*i+1]:  # победа 2-й команды
        table[teams[2*i]][3] += 1       # количество поражений 1-й команды
        table[teams[2*i+1]][1] += 1     # количество побед 2-й команды
        table[teams[2*i+1]][4] += 3     # количество очков 2-й команды
    elif goals[2*i] == goals[2*i+1]: # ничья
        table[teams[2*i]][2] += 1       # количество ничьих 1-й команды
        table[teams[2*i+1]][2] += 1     # количество ничьих 2-й команды
        table[teams[2*i]][4] += 1       # количество очков 1-й команды
        table[teams[2*i+1]][4] += 1     # количество очков 2-й команды
#7 Вывод итоговой таблицы
for team, numbers in table.items():
    print(team+':', end = '')           # Команда:
    print(*numbers)                     # 15 6 6 3 24 