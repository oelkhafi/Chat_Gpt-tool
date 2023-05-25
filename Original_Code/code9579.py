# put your python code here
n = int(input())
tableRes = {}
while n != 0:
    gameRes = input().split(';')
    if gameRes[1] > gameRes[3]:
        res1 = 3
        res2 = 0
    elif gameRes[1] == gameRes[3]:
        res1 = 1
        res2 = 1
    else:
        res1 = 0
        res2 = 3
    if gameRes[0] in tableRes and gameRes[2] not in tableRes:
        tableRes[gameRes[0]].append(res1)
        tableRes.update({gameRes[2]:[res2]})
    elif gameRes[0] not in tableRes and gameRes[2] in tableRes:
        tableRes[gameRes[2]].append(res2)
        tableRes.update({gameRes[0]:[res1]})
    elif gameRes[0] in tableRes and gameRes[2] in tableRes:
        tableRes[gameRes[0]].append(res1)
        tableRes[gameRes[2]].append(res2)
    else:
        tableRes.update({gameRes[0]:[res1], gameRes[2]:[res2]})
    n -= 1
for key in tableRes:
    count, win, draw, lose = 0, 0, 0, 0
    s = tableRes[key]
    for i in range(len(s)):
        count += s[i]
        if len(s) > 1:
            if s[i] == 3:
                win += 1
            elif s[i] == 1:
                draw += 1
            else:
                lose += 1
        elif len(s) == 1:
            if s[i] == 3:
                win += 1
            elif s[i] == 1:
                draw += 1
            else:
                lose += 1
    print(key + ':', len(s), win, draw, lose, count) 