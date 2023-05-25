s1=[input().split(' : ') for i in range(int(input()))]
s4=[input().split() for j in range(int(input()))]
s2={s1[i][0]:[] for i in range(len(s1))}
s3=[]
for j in range(len(s1)):
    if len(s1[j])>1:
        s2[s1[j][0]]=s1[j][1].split()
    else:
        s2[s1[j][0]]=[s1[j][0]]
for i in range(len(s2)):
    for key in s2:
        for jey in s2:
            if jey in s2[key]:
                for i in range(len(s2[jey])):
                    if s2[jey][i] not in s2[key]:
                        s2[key]+=[s2[jey][i]]
                    elif key not in s2[key]:
                        s2[key]+=[key]
for i in range(len(s4)):
    for j in range(len(s4)):
        if s4[i][0] in s2[s4[j][0]] and j>i and s4[j][0] not in s3:
            s3+=[s4[j][0]]
for i in range(len(s4)):
    for x in s3:
        if s4[i][0]==x:
            print(x)




 