# put your python code here
n, lst, d = int(input()), [], {}
for i in range(n):
    s = input().splitlines()
    for i in s:
        lst.append(i.split(';')) 
for i in range(n):
    for k in range(0,4,2):
        key = lst[i][k]
        if key in d:
            d[key][0] += 1
        else:    
            d[key] = list()
            d[key].append(1)
            d[key].append(0)
            d[key].append(0)
            d[key].append(0)
            d[key].append(0)
    if lst[i][1] > lst[i][3]:
        d[lst[i][0]][1] += 1
        d[lst[i][2]][3] += 1
        d[lst[i][0]][4] += 3
        d[lst[i][2]][4] += 0
    elif lst[i][1] < lst[i][3]:
        d[lst[i][0]][3] += 1
        d[lst[i][2]][1] += 1
        d[lst[i][0]][4] += 0
        d[lst[i][2]][4] += 3
    else:    
        d[lst[i][0]][2] += 1
        d[lst[i][2]][2] += 1
        d[lst[i][0]][4] += 1
        d[lst[i][2]][4] += 1
for a,b in d.items():
    print((a + ':'), *b, end = '\n')
 