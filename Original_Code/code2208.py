class Graph:
    def __init__(self):
        self.g = {} 

    def add_node(self, node_name, parents):
        if node_name in self.g.keys():
            self.g[node_name].extend(parents)
        else:
            self.g[node_name] = parents
        for p in parents:
            if p not in self.g.keys():
                self.add_node(p, [])

    def is_parent(self, parent, node_name, ans = 'No'):        
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

    def read_data(self, data):
        node = [d.strip() for d in data.split(':')]
        parents = [p.strip() for p in node[1].split()] if len(node) > 1 else []
        self.add_node(node[0], parents)

    def read_question(self, data):        
        return self.is_parent(*[q.strip() for q in data.split()])

g = Graph()
for i in range(int(input())): g.read_data(input())
for i in range(int(input())): print(g.read_question(input())) 