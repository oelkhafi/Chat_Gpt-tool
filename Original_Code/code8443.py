n = int(input())
game_results = []
teams = set()
for i in range(n):  # ввожу данные и рисую двумерный список
    line = input().split(';')
    game_results += [line]
for i in range(n):  # делаю список команд без повторов
    teams.add(game_results[i][0])
    teams.add(game_results[i][2])
t_score = dict.fromkeys(teams, 0)  # сумма очков
t_win = dict.fromkeys(teams, 0)  # число побед
t_lose = dict.fromkeys(teams, 0)  # число поражений
t_draw = dict.fromkeys(teams, 0)  # число ничьих
t_played = dict.fromkeys(teams, 0)  # число игр
for i in range(n):
    if game_results[i][1] != game_results[i][3]:
        if game_results[i][1] > game_results[i][3]:  # выиграла первая команда
            t_score[game_results[i][0]] += 3
            t_win[game_results[i][0]] += 1
            t_lose[game_results[i][2]] += 1
            t_played[game_results[i][2]] += 1
            t_played[game_results[i][0]] += 1
        if game_results[i][3] > game_results[i][1]:  # выиграла вторая команда
            t_score[game_results[i][2]] += 3
            t_win[game_results[i][2]] += 1
            t_lose[game_results[i][0]] += 1
            t_played[game_results[i][2]] += 1
            t_played[game_results[i][0]] += 1
    else:  # ничья
        t_score[game_results[i][2]] += 1
        t_score[game_results[i][0]] += 1
        t_draw[game_results[i][2]] += 1
        t_draw[game_results[i][0]] += 1
        t_played[game_results[i][2]] += 1
        t_played[game_results[i][0]] += 1
for i in teams:  # печатаю результат
    team_played = str(i) + ':' + str(t_played[i])  # убираю пробел между названием и числом игр
    print(team_played, t_win[i], t_draw[i], t_lose[i], t_score[i])
 