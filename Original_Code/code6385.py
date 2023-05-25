#1 Список родителей
s, parents = [], {}
for i in range(int(input())):
    s.append(input().split())
    if s[i][0] not in parents:
        parents[s[i][0]] = s[i][2:]
    elif s[i][0] in parents:
        parents[s[i][0]] += s[i][2:]
#2 Список запросов
q = [input().split() for i in range(int(input()))]
#3 Добавление потомкам всех предков
for key1, value1 in parents.items():
    for key2, value2 in parents.items():
        if key1 in value2:
            value2 += value1
#4 Добавление предков без родителей
ancestors = [*parents.values()]
for i in range(len(ancestors)):
    for j in range(len(ancestors[i])):
        if ancestors[i][j] not in parents:
            parents[ancestors[i][j]] = []
#5 Ответы на запросы
for i in range(len(q)):
    if q[i][0] == q[i][1] or q[i][0] in parents[q[i][1]]:
        print('Yes')
    else:
        print('No') 