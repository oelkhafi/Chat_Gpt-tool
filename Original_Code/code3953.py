s=input().split() 
n=int(s[0]) 
m=int(s[1]) 
spisok = [[] for i in range(n)] 

for i in range(m): 
    a=([int(i) for i in input().split()]) 
    spisok[a[0]-1].append(a[1]) 
    spisok[a[1]-1].append(a[0])
    
for i in range(len(spisok)):
    for j in range(len(spisok[i])):
        spisok[i][j] = spisok[i][j]-1

visited = [False] * n
component = [-1] * n  # для каждой вершины храним номер её компоненты
num_components = 0

def dfs(v):
    component[v] = num_components
    visited[v] = True
    for w in spisok[v]:
        if visited[w] == False:
            dfs(w)

visited = [False] * n
for v in range(n):
    if not visited[v]:
        dfs(v)
        num_components += 1
        
print(num_components) 