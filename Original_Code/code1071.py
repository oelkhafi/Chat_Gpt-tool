win, loss, name, null, res = [], [], [], [], []
v_i, p, n, pr, it = 0, 0, 0, 0, 0
for i in range(int(input())):
    i = input().split(';')
    name.append(i[0])
    name.append(i[2])
    if i[1]>i[3]:
        win.append(i[0])
        loss.append(i[2])
    elif i[1]<i[3]:
        win.append(i[2])
        loss.append(i[0])
    elif i[1]==i[3]:
        null.append(i[2])
        null.append(i[0])
name.sort()
name1 = set(name)
for j in name1:
    if j in name:
        v_i = name.count(j)
    if j in win:
        p = win.count(j)
    if j in loss:
        pr =  loss.count(j)
    if j in null:
        n = null.count(j)
    it = p*3 + n*1 + pr*0
    res.append([j+':'+str(v_i), p, n, pr, it ])
    v_i, p, n, pr, it = 0, 0, 0, 0, 0
for i in res:
    print(*i, end='\n')





 