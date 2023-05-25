def find(i):
    if i!=parent[i]:
        parent[i]=find(parent[i])
    return parent[i]

def union(i,j):
    iid = find(i)
    jid = find(j)
    if iid == jid: 
        return
    if rank[iid]>rank[jid]:
        parent[jid]=iid
    else:
        parent[iid]=jid
        if rank[iid] == rank[jid]:
            rank[jid] += 1


n,d,e = [int(x) for x in input().split()]
if e==0:
    print(1)
else:
    parent = [x for x in range(0,n+1)]
    rank = [0]*(n+1)
    for i in range(d):
        a,b=[int(x) for x in input().split()]
        union(a,b)
    isOk = True
    for i in range(e):
        a,b=[int(x) for x in input().split()]
        if find(a)==find(b):
            isOk = False
            break
    if isOk:
        print(1)
    else:
        print(0)


 