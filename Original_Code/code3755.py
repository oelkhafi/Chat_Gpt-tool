inp = [input().split(';') for _ in range(int(input()))]
table = {}

for i in range(len(inp)):

    command1, score1, command2, score2 = inp[i]
    commands = [command1, command2]

    for command in commands:
        if command not in table:
            table[command] = [0, 0, 0, 0, 0]

        table[command][0] += 1

    if score1 > score2:
        table[command1][1] += 1
        table[command2][3] += 1
    elif score1 == score2:
        table[command1][2] += 1
        table[command2][2] += 1
    else:
        table[command1][3] += 1
        table[command2][1] += 1

    for command in commands:
        table[command][4] = table[command][1] * 3 + table[command][2]

print('\n'.join((lambda t: [key + ':' + ' '.join([str(c) for c in t[key]]) for key in t])(table))) 