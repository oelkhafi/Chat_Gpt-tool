def merge(a,b):
    global ans
    l1,l2 = len(a),len(b)
    merged,i,j = [0]*(l1+l2),0,0
    for i0 in range(l1+l2):
        if i<l1 and j<l2:
            if a[i] > b[j]:
                merged[i0] = b[j]
                j+=1
                ans+=len(a)-i
            else:
                merged[i0] = a[i]
                i+=1
        else:
            if i<l1:
                merged[i0] = a[i]
                i+=1
            else:
                merged[i0] = b[j]
                j+=1
    return merged
def mergesort(a):
    L = len(a)
    if L == 1: return a
    else:
        m = L//2
        return merge(mergesort(a[:m]),mergesort(a[m:]))
n = int(input())
a = list(map(int, input().split()))
ans = 0
mergesort(a)
print(ans) 