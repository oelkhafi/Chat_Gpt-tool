# put your python code here
import sys
import json


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


data = sys.stdin.readline()
data = json.loads(data.strip())
g = Graph()
for d in data: g.add_node(d['name'], d['parents'])
nodes = g.get_nodes()
ans = {node: [] for node in nodes}
for parent in nodes:
    for child in nodes:
        res = g.is_parent(parent, child)
        if res == 'Yes':
            ans[parent].append(child)
for node in sorted(nodes): print('{} : {}'.format(node, len(ans[node]))) 