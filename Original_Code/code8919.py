n=int(input())
d={}
for i in range(n):
    stroka=[str(i) for i in input().split(';')]
    if stroka[0] not in d:
        d[stroka[0]]=[0,0,0,0,0] 
    if stroka[2] not in d:
        d[stroka[2]]=[0,0,0,0,0]
    if int(stroka[1]) > int(stroka[3]):
        d[stroka[0]][0]+=1
        d[stroka[0]][1]+=1
        d[stroka[0]][4]+=3
        d[stroka[2]][0]+=1
        d[stroka[2]][3]+=1
    if int(stroka[1]) < int(stroka[3]):
        d[stroka[0]][0]+=1
        d[stroka[0]][3]+=1
        d[stroka[2]][0]+=1
        d[stroka[2]][1]+=1
        d[stroka[2]][4]+=3
    if int(stroka[1]) == int(stroka[3]):
        d[stroka[0]][0]+=1
        d[stroka[0]][2]+=1
        d[stroka[0]][4]+=1
        d[stroka[2]][0]+=1
        d[stroka[2]][2]+=1
        d[stroka[2]][4]+=1
for key in d.keys():
    toprint=str(key)+':'
    print(toprint,end='')
    s=d.get(key)
    for q in s:
        print(q,end=' ')
    print()


 