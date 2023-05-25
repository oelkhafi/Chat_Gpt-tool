a = [input().split(';') for i in range(int(input()))]
result = dict()
for i in range(len(a)):
        result[a[i][0]] = [0, 0, 0, 0, 0]
        result[a[i][2]] = [0, 0, 0, 0, 0]
for i in range(len(a)):   #победы, ничьи, поражения
    if a[i][1] > a[i][3]:
        result[a[i][0]][1] += 1
        result[a[i][2]][3] += 1
    elif a[i][1] == a[i][3]:
        result[a[i][0]][2] += 1
        result[a[i][2]][2] += 1
    else:
        result[a[i][2]][1] += 1
        result[a[i][0]][3] += 1
for key in result:   #  очки
    result[key][4] = (result[key][1]*3)+(result[key][2]*1)
for key in result:   #  количество сыгранных игр
    result[key][0] = result[key][1]+result[key][2]+result[key][3]
for key, value in result.items():
    print(key, end = ':'), print(*value)



 