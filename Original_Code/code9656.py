from typing import Dict, Tuple

commands_str = [input() for x in range(int(input()))]
commands = {}
for string in commands_str:
    key = string.split()[0]
    val = int(string.split()[1])
    if key not in commands:
        commands[key] = val
    else:
        commands[key] += val
#print(commands)

def command_to_coordinate(commands : Dict[str, int], coordinate : Tuple[int, int]) \
        -> Tuple[int, int]:
    sev = 'север'
    yug = 'юг'
    vos = 'восток'
    zap = 'запад'
    last_coord = coordinate[0], coordinate[1]
    for key in commands:
        if key == sev:
            last_coord = last_coord[0], last_coord[1] + commands[sev]
        elif key == yug:
            last_coord = last_coord[0], last_coord[1] - commands[yug]
        elif key == vos:
            last_coord = last_coord[0] + commands[vos], last_coord[1]
        elif key == zap:
            last_coord = last_coord[0] - commands[zap], last_coord[1]
    return last_coord

last_coord = command_to_coordinate(commands, (0, 0))
print(*last_coord)

 