def shiftDown(i):
    maxIndex = i
    l = 2*i+1
    if l<n and arr[l]<arr[maxIndex]:
        maxIndex = l
    r = 2*i+2
    if r<n and arr[r]<arr[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        swaps.append((i,maxIndex))
        arr[i],arr[maxIndex] = arr[maxIndex],arr[i]        
        shiftDown(maxIndex)
        
n = int(input())
arr = [int(x) for x in input().split()]
swaps = []
for i in range(n//2,-1,-1):
    shiftDown(i)
print(len(swaps))
for pair in swaps:
    print(pair[0],pair[1])



 