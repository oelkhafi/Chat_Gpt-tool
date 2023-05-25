#1 Описание наследования классов
parents = {}
for i in range(int(input())):
    s = input().split()
    parents[s[0]] = s[2:] if len(s) > 1 else []
#2 Список исключений, записанных Антоном
e = [input() for i in range(int(input()))]
#3 Добавление потомкам всех предков
for key1, value1 in parents.items():
    for key2, value2 in parents.items():
        if key1 in value2:
            value2 += value1
#4 Добавление в parents предков без родителей
ancestors = [*parents.values()]
for i in range(len(ancestors)):
    for j in range(len(ancestors[i])):
        if ancestors[i][j] not in parents:
            parents[ancestors[i][j]] = []
#5 Имена исключений, которые можно удалить из кода
for i in range(len(e)):
    for j in range(len(parents[e[i]])):
        if parents[e[i]][j] in e:
            if e.index(parents[e[i]][j]) < e.index(e[i]):
                print(e[i])
                break 