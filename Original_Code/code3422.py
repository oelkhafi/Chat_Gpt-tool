# put your python code here
def find_path(start, path):
    path.add(start)
    for node in graph[start]:
        if node not in path:
            find_path(node, path)

graph = {}
for i in range(int(input())):
    s = input().split()
    graph[s[0]] = s[2:] if len(s) > 1 else [s[0]]

for i in range(int(input())):
    s = input().split()
    path = set()
    find_path(s[1], path)
    print('Yes' if s[0] in path else 'No')



 