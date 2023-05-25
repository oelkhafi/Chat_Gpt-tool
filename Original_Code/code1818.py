n=int(input())
teams={}
for i in range(n):
    temp=input().split(';')
    if temp[0] in teams:
        teams[temp[0]][0]+=1
    else:
        teams[temp[0]]=[1, 0, 0, 0, 0]
    if temp[2] in teams:
        teams[temp[2]][0]+=1
    else:
        teams[temp[2]]=[1, 0, 0, 0, 0]
    if temp[1]==temp[3]:
        teams[temp[0]][2]+=1
        teams[temp[0]][4]+=1
        teams[temp[2]][2]+=1
        teams[temp[2]][4]+=1
    elif temp[1]>temp[3]:
        teams[temp[0]][1]+=1
        teams[temp[0]][4]+=3
        teams[temp[2]][3]+=1
    else:
        teams[temp[0]][3]+=1
        teams[temp[2]][4]+=3
        teams[temp[2]][1]+=1
for k, v in teams.items():
    print(k, ' '.join(list(map(str, v))), sep=':') 