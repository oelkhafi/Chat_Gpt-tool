n = int(input())
tabl = []
itog = {}
for i in range(n):
    igra = input().split(';')
    if igra[0] not in itog:
        itog[igra[0]] = [0]
    if igra[2] not in itog:
        itog[igra[2]] = [0]
    tabl += [igra]
for i in itog:
    for j in range(4):
        itog[i] += [0]
for i in range(n):
    #считаем кол-во игр
    if tabl[i][0] in itog:
        itog[tabl[i][0]][0] += 1
    if tabl[i][2] in itog:
        itog[tabl[i][2]][0] += 1
    #считаем Побед Ничьих Поражений и Всего_очков
    if tabl[i][1] > tabl[i][3]:
        itog[tabl[i][0]][1] += 1
        itog[tabl[i][0]][4] += 3
        itog[tabl[i][2]][3] += 1
    if tabl[i][1] == tabl[i][3]:
        itog[tabl[i][0]][2] += 1
        itog[tabl[i][0]][4] += 1
        itog[tabl[i][2]][2] += 1
        itog[tabl[i][2]][4] += 1
    if tabl[i][3] > tabl[i][1]:
        itog[tabl[i][2]][1] += 1
        itog[tabl[i][0]][3] += 1
        itog[tabl[i][2]][4] += 3
for key, value in itog.items():
    print(key, ':', ' '.join(str(num) for num in value), sep='') 