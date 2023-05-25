# put your python code here
d={}
n=int(input())
for i in range(n):
    s=input().split(';')
    s[1]=int(s[1])
    s[3]=int(s[3])
    if s[0] not in d:
        d[s[0]]=[0, 0, 0, 0, 0]
        d[s[0]][0]+=1
        if s[1]>s[3]:
            d[s[0]][1]+=1 
            d[s[0]][4]+=3
        elif s[1]==s[3]:
            d[s[0]][2]+=1
            d[s[0]][4]+=1
        elif s[1]<s[3]:
            d[s[0]][3]+=1
    elif s[0] in d:
        d[s[0]][0]+=1
        if s[1]>s[3]:
            d[s[0]][1]+=1
            d[s[0]][4]+=3
        elif s[1]==s[3]:
            d[s[0]][2]+=1
            d[s[0]][4]+=1
        elif s[1]<s[3]:
            d[s[0]][3]+=1
    if s[2] not in d:
        d[s[2]]=[0, 0, 0, 0, 0]
        d[s[2]][0]+=1
        if s[3]>s[1]:
            d[s[2]][1]+=1
            d[s[2]][4]+=3
        elif s[3]==s[1]:
            d[s[2]][2]+=1
            d[s[2]][4]+=1
        elif s[3]<s[1]:
            d[s[2]][3]+=1
    elif s[2] in d:
        d[s[2]][0]+=1
        if s[3]>s[1]:
            d[s[2]][1]+=1
            d[s[2]][4]+=3
        elif s[3]==s[1]:
            d[s[2]][2]+=1
            d[s[2]][4]+=1
        elif s[3]<s[1]:
            d[s[2]][3]+=1
c=[]
for key, value in d.items():
    c.append(key)
    c.append(value)
i=0
while i<len(c):
    print(c[i]+':', end='')
    for x in c[i+1]:
        print(x,end=' ')
    print()
    i+=2 