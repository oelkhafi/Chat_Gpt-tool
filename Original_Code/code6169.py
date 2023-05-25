d = {}
stuff = input().split(', ')
ini_price = int(input())

for i in iter(stuff):
    d[i] = ini_price

names = input().split(', ')

summary = {}
for i in iter(input, 'Аукцион закончен!' ):
    i = i.split(' ')
    if i[0] not in names:
        continue
    else:
        item = ' '.join(i[1:-1])
        if int(i[-1]) > d[item]:
            d.update({item : int(i[-1])})
            summary.update({ item : (i[0] + ' ' + i[-1])})
for k in d.keys():
    if k in summary:
        print(k, summary[k])
    else:
        print(k, 'Предложений не было')

 