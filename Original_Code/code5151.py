def move(position, command):
    direction, steps = command.split()
    offset_table = {
        'север': (0, int(steps)),
        'юг': (0, -int(steps)),
        'восток': (int(steps), 0),
        'запад': (-int(steps), 0)
    }
    return list(map(sum, zip(position, offset_table[direction])))


if __name__ == '__main__':
    position = (0, 0)
    for _ in range(int(input())):
        position = move(position, input())
    print(*position)





 