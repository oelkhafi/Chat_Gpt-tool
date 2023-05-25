def frmt(n):
    print(""{:.2e}"".format(n))

transformations = {('mile', 'm'): 1609,
                   ('yard', 'm'): 0.9144,
                   ('foot', 'cm'): 30.48,
                   ('inch', 'cm'): 2.54,
                   ('km', 'm'): 1000,
                   ('cm', 'm'): 0.01,
                   ('mm', 'm'): 0.001,
                   }

def dfs_path(graph, start, goal, visited=set(), path = []):
    visited.add(start)
    if goal in graph[start]:
        path.extend([start, goal])
        return True
    else:
        for nod in graph[start]:
            if nod in visited: continue
            elif dfs_path(graph, nod, goal, visited, path):
                path.insert(0, start)
                return True
    return False

def make_graph():
    graph = {}
    for k in transformations:
        graph[k[0]] = graph.get(k[0], set()) | {k[1]}
        graph[k[1]] = graph.get(k[1], set()) | {k[0]}
    return graph

def main():
    graph = make_graph()
    (n, unitfrom, _, unitto) = input().split()
    n = float(n)
    if unitfrom == unitto: frmt(n)
    else:
        path = []
        dfs_path(graph, unitfrom, unitto, set(), path)
        mult = 1
        for i in range(len(path) - 1):
            if (path[i], path[i+1]) in transformations: mult *= transformations[(path[i], path[i+1])]
            else: mult /= transformations[(path[i+1], path[i])]
        frmt(mult*n)

if __name__ == ""__main__"": main() 