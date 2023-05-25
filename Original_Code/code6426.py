def lsum(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c
    
d = dict()
n = int(input())
l = [input().split(';') for i in range(n)]

for i in range(n):
    if l[i][0] in d.keys():
        d[l[i][0]] = lsum(d[l[i][0]],[1,0,0,0,0])
    else:
        d[l[i][0]] = [1,0,0,0,0]

    if l[i][2] in d.keys():
        d[l[i][2]] = lsum(d[l[i][2]],[1,0,0,0,0])
    else:
        d[l[i][2]] = [1,0,0,0,0]

    if l[i][1] > l[i][3]:
        d[l[i][0]] = lsum(d[l[i][0]],[0,1,0,0,3])
        d[l[i][2]] = lsum(d[l[i][2]],[0,0,0,1,0])
    if l[i][1] == l[i][3]:
        d[l[i][0]] = lsum(d[l[i][0]],[0,0,1,0,1])
        d[l[i][2]] = lsum(d[l[i][2]],[0,0,1,0,1])
    if l[i][1] < l[i][3]:
        d[l[i][0]] = lsum(d[l[i][0]],[0,0,0,1,0])        
        d[l[i][2]] = lsum(d[l[i][2]],[0,1,0,0,3])
for j,i in d.items():
    print(j+':', end='')
    print(*i) 