graph = {}

def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if (start and end in graph):
    if start == end:
      return [path]
  if (start not in graph):
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpath = find_all_paths(graph, node, end, path)
      if newpath: 
        return newpath 
  if paths:
    return paths
          
def az(graph, start, end):
  x = find_all_paths(graph, start, end)
  if (x != None and x != []):
    return 'Yes'
  else:
    return 'No'

for i in range(int(input())):
  total = input()
  if (':' in total):
    el, parent = total.split(':')
    el = el.replace(' ', '')
    parent = parent.split()
    graph[el] = parent
  else:
    graph[total] = [total]
  # print(graph)

for i in range(int(input())):
  check = input().split()
  print(az(graph, check[1], check[0])) 