def football(n: int):
    stats = {}
    for i in range(n):
        string = input()
        line = [int(i) if i.isdigit() else i for i in string.split(';')]
        for j in range(0, len(line), 2):
            if line[j] not in stats:
                stats[line[j]] = [0, 0, 0, 0, 0]
        for j in range(1, 2):
            stats[line[j-1]][0] += 1
            stats[line[j+1]][0] += 1
            if line[j] > line[j+2]:
                stats[line[j-1]][1] += 1
                stats[line[j-1]][4] += 3
                stats[line[j+1]][3] += 1
            elif line[j] < line[j+2]:
                stats[line[j+1]][1] += 1
                stats[line[j+1]][4] += 3
                stats[line[j-1]][3] += 1
            else:
                stats[line[j-1]][2] += 1
                stats[line[j+1]][2] += 1
                stats[line[j-1]][4] += 1
                stats[line[j+1]][4] += 1
    for k, v in stats.items():
        print(k + ':', end = '')
        print(*v, sep = ' ')
football(int(input())) 