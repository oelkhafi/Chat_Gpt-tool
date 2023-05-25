n, m = [int(x) for x in input().split()]
size = [0] + [*map(int, input().split())]
root = [i for i in range(n + 1)]
current_max = max(size)
    
    
for i in range(m):
    root_d, root_s = [*map(int, input().split())]    
    
    # после этого в root_d -- корень дерева, в которое надо пихать
    while root_d != root[root_d]: root_d = root[root_d]
    
    # ищем корень той таблицы, которую надо влить в root_d 
    while root_s != root[root_s]: 
        root[root_s], root_s = root_d, root[root_s]
        
    if root_s != root_d: 
        size[root_d] += size[root_s]
        root[root_s] = root_d
        current_max = max(current_max, size[root_d])
 
    print(current_max) 