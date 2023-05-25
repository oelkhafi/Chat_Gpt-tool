x=int(input())
cl={}
for i in range(x):
    st=input().split()
    if len(st)==1:
        cl[st[0]]=[]
    else:
        for k in range(2, len(st)):
            if st[0] not in cl:
                cl[st[0]]=[st[k]]
            else:
                cl[st[0]].append(st[k])
for i in cl:
    for j in cl[i]:
        if j in cl:
            cl[i]+=cl[j]
x=int(input())
for i in range(x):
    st=input().split()
    if st[0]==st[1]:
        print('Yes')
    elif st[0] in cl[st[1]]:
        print('Yes')
    else:
        print('No')
 