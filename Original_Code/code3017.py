res = list()
n = int(input())
for i in range(n):
    res.append(input().split("";""))
for i in range(len(res)):
    for j in range(4):
        if res[i][j].isdigit() == True:
            res[i][j] = int(res[i][j])

uniq = set()
for i in range(len(res)):
    for j in [0, 2]:
        uniq.add(res[i][j])
d = {}
for i in uniq:
    vsego_igr = 0
    pobed = 0
    nich = 0
    lose = 0
    vsego_och = 0
    for j in range(len(res)):
        for k in [0,2]:
            if i == res[j][k]:
                vsego_igr += res[j].count(i)
                m = max(res[j][1],res[j][3])
                if res[j][1] == res[j][3]:
                    nich += 1
                    vsego_och += 1
                elif res[j][k+1] == m:
                    pobed += 1
                    vsego_och += 3
                else: lose += 1 
    vsego_och = (pobed * 3 + nich * 1)
    d[i] = [vsego_igr, pobed, nich, lose, vsego_och]
for key, value in d.items():
    print(key, ':', ' '.join(str(i) for i in value), sep='')



 