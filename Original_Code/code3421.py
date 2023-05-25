# put your python code here
n = int(input())
graph = {}
for i in range(n):
    s = input().split()
    if len(s) > 1:
        graph[s[0]] = s[2:]
    else:
        graph[s[0]] = [s[0]]

def Parents(graph, start, end, path=[]):
    path += [start]
    if start == end:
        return path

    for i in graph.get(start):
        if i not in path:
            newpath = Parents(graph, i, end, path)
            if newpath: return newpath
    return None

m = int(input())
for i in range(m):
    s = input().split()
    if Parents(graph, s[1], s[0], path=[]):
        print('Yes')
    else:
        print('No')



 