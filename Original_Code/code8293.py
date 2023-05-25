ouf = {}
gms = int(input())
for i in range(gms):
    gms_lst = [i for i in input().split(';')]
    if gms_lst[0] not in ouf:
        ouf[gms_lst[0]] = [0, 0, 0, 0, 0]
    if gms_lst[2] not in ouf:
        ouf[gms_lst[2]] = [0, 0, 0, 0, 0]
    if gms_lst[0] in ouf:
        ouf[gms_lst[0]][0] += 1
        if gms_lst[1] > gms_lst[3]:
            ouf[gms_lst[0]][1] += 1
            ouf[gms_lst[2]][3] += 1
        elif gms_lst[1] == gms_lst[3]:
            ouf[gms_lst[0]][2] += 1
            ouf[gms_lst[2]][2] += 1
        else:
            ouf[gms_lst[2]][1] += 1
            ouf[gms_lst[0]][3] += 1
    if gms_lst[2] in ouf:
        ouf[gms_lst[2]][0] += 1
for key in ouf.keys():
    ouf[key][4] = ouf[key][1] * 3 + ouf[key][2]
    print(key, end=':')
    for value in ouf[key]:
        print(value, end=' ')
    print() 