left = []
right = []
key = []
q = []

n = int(input());
if n == 0:
    print(""CORRECT"")
    exit()

parent = [-1] * n 
mins = [+2**31] * n
maxs = [-2**31] * n
    
for i in range(n):
    k, l, r = [*map(int, input().split())]
    key.append(k)
    left.append(l)
    right.append(r)
    if l != -1:
        parent[l] = i
    if r != -1: parent[r] = i
    if l == r == -1: q.append(i)
        
        
def check(q):
    while len(q) > 0:
        new_q = []
        for leave in q: 
            # для текущей вершины нужно проверить, выполняется ли для нее свойства
            # и обновить минимум и максимум соответствующие 
            maxs[leave] = max(maxs[leave], key[leave])
            mins[leave] = min(mins[leave], key[leave])
            
            if left[leave] != -1:
                if maxs[left[leave]] > key[leave]: return False
                maxs[leave] = max(maxs[leave], maxs[left[leave]])
                mins[leave] = min(mins[leave], mins[left[leave]])
            
            if right[leave] != -1:
                if mins[right[leave]] < key[leave]: return False
                maxs[leave] = max(maxs[leave], maxs[right[leave]])
                mins[leave] = min(mins[leave], mins[right[leave]])
            
            
            if parent[leave] !=-1 and parent[leave] not in new_q:
                new_q.append(parent[leave])
        q = new_q
    return True


print(""CORRECT"" if check(q) else ""INCORRECT"") 