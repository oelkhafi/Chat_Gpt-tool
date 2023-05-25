# put your python code here
import json
dict, graph = {}, {}
js = json.loads(input())
  
# Собираем словарь вида { ""сын"" : [ ""родитель_1"", ""родитель_2"", ...] }    
for name_class in js:
    if name_class['name'] not in dict:
        dict[name_class['name']] = name_class['parents']
    else:
        dict[name_class['name']] += name_class['parents']

#print()
#print(dict)
# Перевернём словарь сделав его вида { ""родитель"" : [""сын_1"", ""сын_2"", ... ] }
for key, values in dict.items():
    if key not in graph:
        graph[key] = []
    for val in values:
        if val not in graph:
            graph[val] = [key]
        else:
            graph[val] += [key]

#print()
#print(graph)
# Соберём список всех вершин графа
vertex = []
for key, values in graph.items():
    vertex += [key, *values]
vertex = sorted(list(set(vertex)))
#print(sorted(list(set(vertex))))

# Запишем алгоритм поска в Глубину https://pimiento.github.io/python_graphs.html
def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

# Распакуем решение
for vr in vertex:
    print(vr, "":"", len(dfs(graph, '{}'.format(vr)))) 