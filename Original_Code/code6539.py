import sys

w, n = map(int, next(sys.stdin).strip().split())
weights = list(map(int, next(sys.stdin).strip().split()))

for i,item in enumerate(weights):
    
    curr = [0 for j in range(w+1)]
    for j in range(w+1):
        if i == 0:
            if j >= item:
                curr[j] = item
        else:
            if j < item:
                curr[j] = prev[j]
            else:
                curr[j] = max(prev[j], item + prev[j-item])
        pass
    prev = curr
    pass
    
print(curr[-1]) 