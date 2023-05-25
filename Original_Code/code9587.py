# put your python code here
classParent = {}                                                #Пустой словарь для хранения классов (графов)
def findParent(parent, child):                                  #Функция по поиску предок-наследник
    if child in classParent.keys():                             #Если ключ-наследник имеется в словаре, то: 
        if (parent == child) or (parent in classParent[child]): #Если наследник является сам себе предком или предок входит в сет                                                                     #наследника, где хранятся предки, то выводим Yes
            return True        
        elif parent not in classParent[child]:                  #Если предок не входит в сэт наследника
            child = [i for i in classParent[child]]             #Создаем список всех предков, которые теперь становятся наследниками                                                                 #для дальнейшего поиска связей
            if len(child) == 0:                                 #Если список наследников пуст, делаем вывод, что у наследника нет                                                                     #заданного по условию предка, значит ответ No
                return False
            else:
                for n in child:                                 #Если наследник 1 или более, то циклом перебираем по одному                                                                           #наследнику и..
                    nextDepth = findParent(parent, n)           #Запускаем рекурсивно функцию поиска наследник-предок и подставляем в                                                                 #нее на место наследника новое значение child                   
                    if nextDepth is True:                       #Если результатом работы функции будет True, 
                        return True                             #то заканчиваем перебирать наследников
                        break                                   #и останавливаемся
    else:
        return False                                            #Если не находим наследника в словаре, выдаем ответ No
        
n = int(input())                                                #Это количество вводов наследник-предок
for j in range(n):                                              
    classes = [str(i) for i in input().split()]                 #В список через цикл собираем все введенные значения
    if classes[0] not in classParent:                           #Проверка, если ключа-наследника еще нет, то
        if (len(classes)) == 1:                                 #Если введено одно значение
            classParent[classes[0]] = set()                     #Просто содаем ключ с пустым value в виде пустого set()
        else:
            classParent[classes[0]] = {classes[i] for i in range(2, len(classes))} #Если введено несколько значений, то создаем пару                                                                 #ключ-наследник: значение-предок/предки
    else:
        for c in range(2, len(classes)):                        #Циклом перебираем значения введенных предков (известно, что предки                                                                   #начинаюся со второго индекса от [2] и до конца длины списка classes)
            classParent[classes[0]].add(classes[c])             #Если же ключ есть, то добавляем в имеющийся ключ (мы знаем, что ключ                                                                 #всегда вводится первым, т.е. его индекс [0]) новые значения предков
q = int(input())                                                #Количество проверок предок-наследник
for j in range(q):
    searchClass = [str(i) for i in input().split()]             #Вводим стандартные запросы предок-наследник и складываем в список
    res = findParent(searchClass[0], searchClass[1])            #Запуск функции поиска предок-наследник
    if res is True:
        print('Yes')                                            #Вывод результата
    else:
        print(""No"") 