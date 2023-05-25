# put your python code here
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


class BinTree:
    def __init__(self, ):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value <= node.key:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(node.right, value)

    def walk(self):
        self.path = []
        self.post_order(self.root)
        print(' '.join(map(str, self.path)))

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            self.path.append(node)


def run():
    _ = int(input())
    tree = BinTree()
    for value in input().split():
        tree.add(int(value))
    tree.walk()


if __name__ == '__main__':
    run()
 