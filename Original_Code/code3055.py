def find_dots(otrezki):
    result = []
    count, i = 0, 0
    while count < (len(otrezki)):
        if otrezki[i][0] == None:
            i += 1
            continue
        else:
            point = otrezki[i][0]
        for j in range(len(otrezki)):
            if otrezki[j][0] != None:
                if i == j:
                    otrezki[j][0], otrezki[j][1] = None, None
                    count += 1
                else:
                    if otrezki[j][0] >= point >= otrezki[j][1]:
                        otrezki[j][0], otrezki[j][1] = None, None
                        count += 1
        result.append(point)
        i += 1
    return result

otrezki = []
for count in range(int(input())):
    a, b = map(int, input().split())
    if a > b: 
        a, b = b, a
    otrezki.append([b, a])
otrezki = sorted(otrezki)
res = find_dots(otrezki)
print(len(res))
print("" "".join(str(i) for i in res)) 