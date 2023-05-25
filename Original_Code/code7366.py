n = int(input())
tab = {}
#                   0     1       2        3        4
# tab ={Команда : [Игр, Побед, Ничьих, Поражений, Очков]}
for i in range(n):
  result = input().split(';')
  #               0          1         2         3
  # result = [Команда 1 , голы(1), Команда 2, голы(2)]

  if result[1] > result[3]:
    if result[0] not in tab.keys(): tab[result[0]]=[0,0,0,0,0]
    tab[result[0]][0] += 1 # добавляем Команде 1 кол-во игр
    tab[result[0]][1] += 1 # добавляем Команде 1 кол-во побед
    tab[result[0]][4] += 3 # добавляем Команде 1 кол-во очков

    if result[2] not in tab.keys(): tab[result[2]]=[0,0,0,0,0]
    tab[result[2]][0] += 1 # добавляем Команде 2 кол-во игр
    tab[result[2]][3] += 1 # добавляем Команде 2 кол-во поражений
  
  elif result[1] < result[3]:
    if result[2] not in tab.keys(): tab[result[2]]=[0,0,0,0,0]
    tab[result[2]][0] += 1 # добавляем Команде 2 кол-во игр
    tab[result[2]][1] += 1 # добавляем Команде 2 кол-во побед
    tab[result[2]][4] += 3 # добавляем Команде 2 кол-во очков
    
    if result[0] not in tab.keys(): tab[result[0]]=[0,0,0,0,0]
    tab[result[0]][0] += 1 # добавляем Команде 1 кол-во игр
    tab[result[0]][3] += 1 # добавляем Команде 1 кол-во поражений
  
  else:
    if result[0] not in tab.keys(): tab[result[0]]=[0,0,0,0,0]
    tab[result[0]][0] += 1 # добавляем Команде 1 кол-во игр
    tab[result[0]][2] += 1 # добавляем Команде 1 кол-во ничьих
    tab[result[0]][4] += 1 # добавляем Команде 1 кол-во очков

    if result[2] not in tab.keys(): tab[result[2]]=[0,0,0,0,0]
    tab[result[2]][0] += 1 # добавляем Команде 2 кол-во игр
    tab[result[2]][2] += 1 # добавляем Команде 2 кол-во ничьих
    tab[result[2]][4] += 1 # добавляем Команде 2 кол-во очков
for i in tab.keys():
    print (i+"":"", end='')
    for j in tab[i]:
        print(j,'', end='')
    print() 