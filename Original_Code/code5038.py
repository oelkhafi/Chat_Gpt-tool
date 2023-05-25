class Set:
    def __init__(self, counts):
        self.max_size = max(counts)
        self.ids = counts
        n = len(counts)

        self.parent = list(range(n))
        self.rank = [1] * n

    def _find(self, x, root=None):
        i = x
        while i != self.parent[i]:
            parent_i = self.parent[i]
            if root:
                self.parent[i] = root
            i = parent_i

        return i

    def find(self, x):
        return self._find(x, self._find(x))

    def union(self, x, y):
        x_idx = self.find(x)
        y_idx = self.find(y)

        root = x_idx
        if x_idx != y_idx:
            if self.rank[x_idx] > self.rank[y_idx]:
                self.parent[y_idx] = root
            else:
                root = y_idx
                self.parent[x_idx] = root
                if self.rank[x_idx] == self.rank[y_idx]:
                    self.rank[root] += 1

            self.ids[x_idx] = self.ids[y_idx] = self.ids[x_idx] + self.ids[y_idx]

        self.max_size = max(self.max_size, self.ids[root])
        return self.max_size

def union(tables, unions):
    unions_set = Set(tables)

    return [unions_set.union(*union) for union in unions]

def main():
    n, m = map(int, input().split())
    tables = list(map(int, input().split()))

    unions = []
    for _ in range(m):
        unions.append(tuple((int(v) - 1 for v in input().split())))

    union_sizes = union(tables, unions)
    print(*union_sizes, sep='\n')

if __name__ == '__main__':
    main() 