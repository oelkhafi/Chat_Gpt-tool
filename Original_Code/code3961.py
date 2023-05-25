cls = int(input())
dictionary, visited = dict(), dict()
for i in range(cls):
    str1 = input().split(' ')
    dictionary[str1[0]] = [i for i in str1[2:]]
    visited[str1[0]] = False
req = int(input())    
lst = []
#функция для поиска в глубину
def dfs(vertex):
    visited[vertex] = True
    for words in dictionary.get(vertex):
        lst.append(words)
        if visited[words] == False:
            dfs(words)
#цикл для считывания запросов по одному и вывод
for j in range(req): 
    for vertex in dictionary.keys():
        visited[vertex] = False
    str2 = input().split()
    dfs(str2[1])
    if (lst.count(str2[0]) > 0) or (str2[1] == str2[0]): print('Yes')
    else: print('No')
    lst.clear() 