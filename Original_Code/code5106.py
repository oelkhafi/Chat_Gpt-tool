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
    def in_order(self, node=0):
        if node == -1: return []
        return self.in_order(self.left(node)) + [self.val(node), ] + self.in_order(self.right(node))
    def check(self, node):
        check_lst = self.in_order(0)
        for i in range(len(check_lst) - 1):
            if not check_lst[i] < check_lst[i + 1]:
                return False
        return True

def main():
    sys.setrecursionlimit(10 ** 5)
    count = int(input())
    if count == 0:
        print(""CORRECT"")
    else:
        tree = [tuple(map(int, input().split())) for i in range(count)] + [-1]
        bstree = Bstree(tree)
        print(bstree.check(0) and ""CORRECT"" or ""INCORRECT"")

if __name__ == ""__main__"":
    main()
 