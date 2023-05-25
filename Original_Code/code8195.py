import sys

sys.setrecursionlimit(10 ** 5)


class SearchTree:
    def __init__(self, tree):
        self.tree = tree
        self.search_cache = {}

    def value(self, node):
        return self.tree[node][0]

    def left(self, node):
        return self.tree[node][1]

    def right(self, node):
        return self.tree[node][2]

    def check(self, node=0, min=-2 ** 32, max=2 ** 32):
        if node == -1:
            return True
        v = self.value(node)
        if v < min or v > max:
            return False
        return self.check(self.left(node), min, v - 1) and self.check(self.right(node), v + 1, max)


def process_lines(ar):
    tree = SearchTree([tuple(map(int, line.split())) for line in ar])

    return 'CORRECT' if len(tree.tree) == 0 or tree.check() else 'INCORRECT'

input()
print(process_lines(sys.stdin.readlines())) 