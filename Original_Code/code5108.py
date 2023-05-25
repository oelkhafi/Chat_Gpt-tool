import sys

class Bstree():
    def __init__(self, nodes):
        self.nodes = nodes
    def val(self, node):
        return self.nodes[node][0]
    def left(self, node):
        return self.nodes[node][1]
    def right(self, node):
        return self.nodes[node][2]
    def check(self, node, _min, _max):
        if node == -1:
            return True
        if self.val(node) < _min or self.val(node) >= _max:
            return False
        else:
            return self.check(self.left(node), _min, self.val(node)) and self.check(self.right(node), self.val(node), _max)

def main():
    sys.setrecursionlimit(10 ** 5)
    count = int(input())
    if count == 0:
        print(""CORRECT"")
    else:
        tree = [tuple(map(int, input().split())) for i in range(count)] + [-1]
        bstree = Bstree(tree)
        print(bstree.check(0, -float(""inf""), float(""inf"")) and ""CORRECT"" or ""INCORRECT"")

if __name__ == ""__main__"":
    main()
 