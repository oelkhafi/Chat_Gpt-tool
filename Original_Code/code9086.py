# Вводим предметы
n, w = map(int, input().split())
items = []
for i in range(n):
    ci, wi = map(int, input().split())
    k = ci / wi
    items.append([ci, wi, k])

# Надёжный шаг - взять предмет с самой дорогой стоимостью за единицу веса

# Но для начала сортировочка
items.sort(key=lambda x: x[2], reverse=True)

# Теперь основная часть
cnt = 0
summ = 0
for i in range(n):
    ci = items[i][0]
    wi = items[i][1]
    if cnt < w:
        if cnt + wi <= w:
            cnt += wi
            summ += ci
        else:
            summ += ci * (w - cnt) / wi
            cnt = w

print('%.3f' % summ)
 