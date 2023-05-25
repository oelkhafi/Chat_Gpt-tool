def enter_val(rep,what_do):#обработка количества запросов и что нужно сделать
    for step in range (rep):
        if what_do : ways.append([i for i in (input().split())]) # описание классов
        elif what_do == False :
            find(input())
def find (y): #обработка наследования
    quest.append(y)
    for step in range (len(quest)-1):
            finds(quest[step],y)
    if True in result: quests.append(y) #если хоть в одном ветвлении нашли предка
    result.clear()
def finds(find_y,y):
    if find_y==y: return result.append(True)
    for i in range (len(ways)):
            if y == ways[i][0]:
                if find_y in ways[i]: return result.append(True)
                elif len(ways[i])==1 :return result.append(False)
                else:
                    for j in range (2,len(ways[i])): finds(find_y,ways[i][j])
                    return result.append(False)
ways, result, quest, quests = [],[], [],[]
enter_val(int(input()),True) # число классов для описания наследования
enter_val(int(input()),False)# число запросов по наследованию
for i in quests:
    print(i) 