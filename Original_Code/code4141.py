play = int(input())
res = dict()
res_temp = dict()
match = [[input()] for i in range(play)]
for i in match:
    key1, value1, key2, value2 = i[0].split(';')
    value1 = int(value1)
    value2 = int(value2)
    res[key1] = {'play_k':0, 'win':0, 'par':0, 'los':0, 'score':0}
    res[key2] = {'play_k':0, 'win':0, 'par':0, 'los':0, 'score':0}
    res.update(res_temp)
    res[key1]['play_k'] = res[key1]['play_k'] + 1
    res[key2]['play_k'] = res[key2]['play_k'] + 1
    if value1 < value2:
        res[key2]['win'] = res[key2]['win'] + 1
        res[key1]['los'] = res[key1]['los'] + 1
        res[key2]['score'] = res[key2]['score'] + 3
    if value1 > value2:
        res[key1]['win'] = res[key1]['win'] + 1
        res[key1]['score'] = res[key1]['score'] + 3
        res[key2]['los'] = res[key2]['los'] + 1
    if value1 == value2:
        res[key1]['par'] = res[key1]['par'] + 1
        res[key2]['par'] = res[key2]['par'] + 1
        res[key1]['score'] = res[key1]['score'] + 1
        res[key2]['score'] = res[key2]['score'] + 1
    res_temp = res.copy()
for key in res.keys():
    print(key+':', end='')
    print(res[key]['play_k'], res[key]['win'], res[key]['par'], res[key]['los'], res[key]['score'] )
 