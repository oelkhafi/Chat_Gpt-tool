import json

scheme = json.loads(input())
# scheme = [{""A"": []}, {""B"": [""A""]}, {""C"": [""A""]}, {""D"": [""B"", ""C""]}, {""V"": [""D""]}]

parent_and_children = {item['name']: [] for item in scheme}
# {'A': [], 'B': [], 'C': [], 'D': [], 'V': []}

for item in scheme:
    for parent in parent_and_children:
        if parent in item['parents']:
            parent_and_children[parent].append(item['name'])
# {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['V'], 'V': []}
# если класс есть в parents - его прямые дети добавляются в словарь

for item in parent_and_children:
    parent_and_children[item] = set(parent_and_children[item])
# {'A': {'C', 'B'}, 'B': {'D'}, 'C': {'D'}, 'D': {'V'}, 'V': set()}
# словари с детьми преобразуются в множества


# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for upcoming in graph[start] - visited:
        dfs(graph, upcoming, visited)
    return visited


# parent_and_children = {'A': {'C', 'B'}, 'B': {'D'}, 'C': {'D'}, 'D': {'V'}, 'V': set()}
# dfs(parent_and_children, 'A') = {'A', 'D', 'C', 'V', 'B'}
for item in sorted(parent_and_children.keys()):
    print(item, ':', len(dfs(parent_and_children, item)))
 