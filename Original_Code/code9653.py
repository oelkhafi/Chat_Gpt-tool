def one_game_two_command_table_res(goals1, goals2, cmd1_table, cmd2_table):
#   cmd_table = [command, games, wins, drawn, falls, points]
    cmd1_table[1] += 1
    cmd2_table[1] += 1
    if goals1 > goals2:  # победа первой
        cmd1_table[2] += 1  # первая команда плюс одна победа
        cmd2_table[4] += 1  # вторая команда плюс одно поражение
        cmd1_table[5] += 3
    elif goals1 < goals2:  # поражение первой
        cmd1_table[4] += 1  # первая команда плюс одно поражение
        cmd2_table[2] += 1  # вторая команда плюс одна победа
        cmd2_table[5] += 3
    else:  # ничья
        cmd1_table[3] += 1  # первая команда плюс одна ничья
        cmd2_table[3] += 1  # вторая команда плюс одна ничья
        cmd1_table[5] += 1
        cmd2_table[5] += 1

def command_table_in_tournament_table(command_name, tournament_table):
    for i in range(len(tournament_table)):
        if tournament_table[i][0] == command_name:
            return tournament_table[i]


n = int(input())
games_table = []
for i in range(0, n):
    st = input().strip().split(';')
    game = [x for x in st]
    for j in range(len(game)):
        if str.isdigit(game[j]):
            game[j] = int(game[j])
    games_table += [game]
#print(*games_table, sep='\n')
command_set = {x[0] for x in games_table} | {x[2] for x in games_table}
#print(command_set)
commands_count = len(command_set)
#print(commands_count)
tournament_table = [[x, 0, 0, 0, 0, 0] for x in command_set]
#print(*tournament_table, sep='\n')
for game in games_table:
    command1 = game[0]
    command2 = game[2]
    cmd1_table = command_table_in_tournament_table(game[0], tournament_table)
    cmd2_table = command_table_in_tournament_table(game[2], tournament_table)
    one_game_two_command_table_res(game[1], game[3], cmd1_table, cmd2_table)
for command in tournament_table:
    print(command[0] + ':' + str(command[1]), *command[2:]) 