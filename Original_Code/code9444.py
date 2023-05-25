s1=[input().split(' : ') for i in range(int(input()))]
s4=[input().split() for j in range(int(input()))]
s2={s1[i][0]:[] for i in range(len(s1))}
for j in range(len(s1)):
    if len(s1[j])>1:
        s2[s1[j][0]]=s1[j][1].split()
    else:
        s2[s1[j][0]]=[s1[j][0]]
for i in range(len(s2)):
    for jey in s2:
        for key in s2:
            if key in s2[jey]:
                for i in range(len(s2[key])):
                    if s2[key][i] not in s2[jey]:
                        s2[jey]+=[s2[key][i]]
                    elif jey not in s2[jey]:
                        s2[jey]+=[jey]
for i in range(len(s4)):
    if s4[i][0] in s2[s4[i][1]]:
        print('Yes')
    else:
        print('No')




 