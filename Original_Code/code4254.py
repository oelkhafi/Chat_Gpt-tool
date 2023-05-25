# put your python code here
def fill(i):
    if h[i]!=0:
        return h[i]
    if l[i]==-1:
        h[i] = 1
    else:
        h[i] = 1+fill(l[i])    
    return h[i]    


n = int(input())
l = [int(x) for x in input().split()]
h = [0]*n
for i in range(n):
    fill(i)
print(max(h))



 