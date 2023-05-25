n=int(input())
com=[]
sl=dict()
for i in range(n):
    game=input().split(';')
    if game[0] not in com:
        com.append(game[0])
        sl[game[0]]=dict()
        sl[game[0]]['Игр']=0
        sl[game[0]]['Побед']=0
        sl[game[0]]['Ничьих'] = 0
        sl[game[0]]['Поражений'] = 0
        sl[game[0]]['Очков'] = 0
    if game[2] not in com:
        com.append(game[2])
        sl[game[2]] = dict()
        sl[game[2]] = dict()
        sl[game[2]]['Игр'] = 0
        sl[game[2]]['Побед'] = 0
        sl[game[2]]['Ничьих'] = 0
        sl[game[2]]['Поражений'] = 0
        sl[game[2]]['Очков'] = 0
    sl[game[0]]['Игр']+=1
    sl[game[2]]['Игр']+=1
    if game[1]>game[3]:
        sl[game[0]]['Побед']+=1
        sl[game[2]]['Поражений']+=1
        sl[game[0]]['Очков']+=3
    if game[1]<game[3]:
        sl[game[2]]['Побед']+=1
        sl[game[0]]['Поражений']+=1
        sl[game[2]]['Очков'] += 3
    if game[1]==game[3]:
        sl[game[0]]['Ничьих']+=1
        sl[game[2]]['Ничьих'] += 1
        sl[game[0]]['Очков'] += 1
        sl[game[2]]['Очков'] += 1
for key1 in sl.keys():
    print(key1,end=':')
    for value in sl[key1].values():
        print(value,end=' ')
    print() 