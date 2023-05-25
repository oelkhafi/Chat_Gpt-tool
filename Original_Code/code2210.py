# put your python code here
class Graph:
    def __init__(self):
        self.g = {}

    def add_node(self, node_name, parents):
        if node_name in self.g.keys():
            self.g[node_name].extend(parents)
        else:
            self.g[node_name] = parents
        for p in parents:
            if p not in self.g.keys(): self.add_node(p, [])

    def is_parent(self, parent, node_name, ans='No'):
        if parent == node_name or parent in self.g[node_name]:
            return ""Yes""
        else:
            for n in self.g[node_name]:
                if parent in self.g[n]:
                    return ""Yes""
                else:
                    ans = self.is_parent(parent, n)
                    if ans == 'Yes': return ans
        return ans

    def get_nodes(self):
        return self.g.keys()

    def read_data(self, data):
        node = [d.strip() for d in data.split(':')]
        parents = [p.strip() for p in node[1].split()] if len(node) > 1 else []
        self.add_node(node[0], parents)

g = Graph()
for i in range(int(input())): g.read_data(input())
exeptions = [input() for i in range(int(input()))]

nodes = g.get_nodes()
ans = {node: [] for node in nodes}
for parent in nodes:
    for child in nodes:
        res = g.is_parent(parent, child)
        if res == 'Yes':
            ans[parent].append(child)

for exeption in exeptions:
    if exeption in ans.keys():
        for child in ans[exeption]:
            if child != exeption and child in ans.keys(): del ans[child]
        del ans[exeption]
    else:
        print(exeption) 