cnt_game = int(input())
dict_tables={}

for i in range (cnt_game):
    name1,goals1,name2,goals2= input().split(';')
    if name1 not in dict_tables:
        dict_tables[name1] = dict(games=0,win=0,draw=0,lose=0,point=0)
    if name2 not in dict_tables:
        dict_tables[name2] = dict(games=0,win=0,draw=0,lose=0,point=0)

    dict_tables[name1]['games'] += 1
    dict_tables[name2]['games'] += 1

    if int(goals1) > int(goals2):
        dict_tables[name1]['win'] +=1
        dict_tables[name1]['point'] +=3
        dict_tables[name2]['lose'] +=1
    elif int(goals1) < int(goals2):
        dict_tables[name2]['win'] += 1
        dict_tables[name2]['point'] += 3
        dict_tables[name1]['lose'] += 1
    elif int(goals1) == int(goals2):
        dict_tables[name2]['draw'] +=1
        dict_tables[name1]['draw'] +=1
        dict_tables[name2]['point'] +=1
        dict_tables[name1]['point'] += 1

for i in dict_tables.keys():
  print( i,':', end='',sep=('')) #два принта из за заморочки с двоеточием, что бы оно писалость именно так(с отступом от названия и прилипало к статам команды)
  print(dict_tables[i]['games'], dict_tables[i]['win'], dict_tables[i]['draw'], dict_tables[i]['lose'], dict_tables[i]['point'])

 