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

    def pre_order(self, node=0):
        if node == -1: return []
        return [self.val(node), ] + self.pre_order(self.left(node)) + self.pre_order(self.right(node))

    def post_order(self, node=0):
        if node == -1: return []
        return self.post_order(self.left(node)) + self.post_order(self.right(node)) + [self.val(node), ]


def main():
    count = int(input())
    tree = [tuple(map(int, input().split())) for i in range(count)] + [-1]
    bstree = Bstree(tree)
    print(*bstree.in_order())
    print(*bstree.pre_order())
    print(*bstree.post_order())

if __name__ == ""__main__"":
    main()
 