n=int(input())
match_vs=[input().split(';') for i in range(n)] #ввод преобразовать в двумерный список

#получить список команд
teams=[]
for j in [[i[z] for z in range(len(i)) if z==0 or z==2] for i in match_vs]:
    teams+=j
teams_list=list(set(teams))

#получить словарь числа игр каждой команды
cnt_games ={}
for i in teams_list:
    cnt_games[i]=teams.count(i)

list_victory = [] #лист побед
list_trahere = [] #лист ничьих
list_cladem = []  #лист поражений

for i in match_vs:
    if int(i[1]) > int(i[3]):
        list_victory.append(i[0])
        list_cladem.append(i[2])
    elif int(i[1]) == int(i[3]):
        list_trahere.append(i[0])
        list_trahere.append(i[2])
    else:
        list_victory.append(i[2])
        list_cladem.append(i[0])

cnt_victory ={} #словарь число побед
cnt_trahere ={} #словарь число ничьих
cnt_cladem ={}  #словарь число поражений

score_victory = 3 #очки за победу
score_trahere = 1 #очки за ничью
score_cladem = 0  #очки за поражение
sum_score = {}    #всего очков
for i in teams_list:
    cnt_victory[i]= list_victory.count(i)
    cnt_trahere[i] = list_trahere.count(i)
    cnt_cladem[i] = list_cladem.count(i)
    sum_score[i] = (list_victory.count(i)*score_victory)+(list_trahere.count(i)*score_trahere)+(list_cladem.count(i)*score_cladem)

output={}
for i in teams_list:
    output[i] = cnt_games[i],cnt_victory[i],cnt_trahere[i],cnt_cladem[i],sum_score[i]
for key in  output:
    print(key,' '.join([ str(i) for i in output[key]]),sep=':') 