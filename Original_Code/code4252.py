# put your python code here
def getRes(w, i):
    if res[w][i] != -1:
        return res[w][i]
    if w == 0:
        res[w][i]=0
        return 0
    if i == 0:
        res[w][i]=0
        return 0
    if l[i-1]>w:
        res[w][i] = getRes(w,i-1)
        return res[w][i]
    res[w][i] = max(getRes(w-l[i-1],i-1)+l[i-1],getRes(w,i-1))
    return res[w][i]
        
w,n = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
res = [[-1 for x in range(n+1)] for y in range(w+1)]

print(getRes(w,n))



 