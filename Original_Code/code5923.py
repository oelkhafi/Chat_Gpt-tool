import time
l={i:[] for i in input().split(', ')}
a=[j for j in iter(input, '.')]

n=len(a)
for p in range(n-1):
    for k in range (p+1,n):
        t1=time.strptime(a[k].split('""')[2].split()[0],""%d.%m.%Y"")
        t2=time.strptime(a[p].split('""')[2].split()[0],""%d.%m.%Y"")
        if t1<t2:
            a[k],a[p]=a[p],a[k]
for j in a:
    action=j.split()[0]
    book='""'+j.split('""')[1]+'""'
    date1=j.split('""')[2].split()[0]
    if action==""Вернуть"":
        l[book].append([date1,action])
    if action==""Взять"":
        name=j.split('""')[2].split()[1][1:-1]
        l[book].append([date1,action,name])

for j in a:
    action=j.split()[0]
    book='""'+j.split('""')[1]+'""'
    date1=j.split('""')[2].split()[0]
    if action==""Взять"":
        name=j.split('""')[2].split()[1][1:-1]
        for i in range(len(l[book])):
            if date1 in l[book][i]:
                if i>0:
                    if l[book][i-1][1]=='Взять':
                        t1=time.strptime(l[book][i-1][0],""%d.%m.%Y"")
                        t2=time.strptime(l[book][i][0],""%d.%m.%Y"")
                        dt=t2.tm_yday-t1.tm_yday
                        print (f'Книга {book} отсутствует. Ее забрал(а) {l[book][i-1][2]}' if dt<30 else f'Книгу {book} забрал(а) {name}')
                    if l[book][i-1][1]=='Вернуть':
                        print (f'Книгу {book} забрал(а) {name}')                               
                if i==0:
                    print (f'Книгу {book} забрал(а) {name}')
                    



 