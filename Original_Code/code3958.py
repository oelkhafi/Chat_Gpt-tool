n = int(input())
d = dict()

for i in range(n):
    matchs = input().split(';')
    if int(matchs[1]) > int(matchs[3]):
        if d.get(matchs[0]) == None:
            d[matchs[0]] = ['1','1','0','0','3']
        else:
            for i in range(len(d.get(matchs[0]))):
                d.get(matchs[0])[i] = int(d.get(matchs[0])[i]) + int(['1','1','0','0','3'][i])
        if d.get(matchs[2]) == None:
            d[matchs[2]] = ['1','0','0','1','0']
        else:
            for i in range(len(d.get(matchs[2]))):
                d.get(matchs[2])[i] = int(d.get(matchs[2])[i]) + int(['1','0','0','1','0'][i])

    elif int(matchs[1]) < int(matchs[3]):
        if d.get(matchs[0]) == None:
            d[matchs[0]] = ['1','0','0','1','0']
        else:
            for i in range(len(d.get(matchs[0]))):
                d.get(matchs[0])[i] = int(d.get(matchs[0])[i]) + int(['1','0','0','1','0'][i])
        if d.get(matchs[2]) == None:
            d[matchs[2]] = ['1','1','0','0','3']
        else:
            for i in range(len(d.get(matchs[2]))):
                d.get(matchs[2])[i] = int(d.get(matchs[2])[i]) + int(['1','1','0','0','3'][i])

    elif int(matchs[1]) == int(matchs[3]):
        if d.get(matchs[0]) == None:
            d[matchs[0]] = ['1','0','1','0','1']
        else:
            for i in range(len(d.get(matchs[0]))):
                d.get(matchs[0])[i] = int(d.get(matchs[0])[i]) + int(['1','0','1','0','1'][i])
        if d.get(matchs[2]) == None:
            d[matchs[2]] = ['1','0','1','0','1']
        else:
            for i in range(len(d.get(matchs[2]))):
                d.get(matchs[2])[i] = int(d.get(matchs[2])[i]) + int(['1','0','1','0','1'][i])
                
for i in d.keys():
    kl = []
    for j in d.get(i):
        kl.append(str(j))
    res = ' '.join(kl)
    print(i+':'+str(res)) 