class SimpleNode:
    def __init__(self):
        self.key = self.left = self.right = None

# in_order: left,parent,right
def in_order_seq(node):
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            yield node.key
            node = node.right

# pre_order: parent,left,right
def pre_order_seq(node):
    stack = []
    while node or stack:
        node = node or stack.pop()
        yield node.key
        if node.right:
            stack.append(node.right)
        node = node.left

# post_order: left,right,parent
def post_order_seq(node):
    stack = []
    while node or stack:
        if node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            node = node.left
            continue
        node = stack.pop()
        if stack and stack[-1] == node.right:
            stack[-1] = node
            node = node.right
        else:
            yield node.key
            node = None

def main():
    num_nodes = int(input())
    tree = [SimpleNode() for i in range(num_nodes)]
    for num in range(num_nodes):
        key, left, right = map(int, input().split())
        tree[num].key = key
        tree[num].left = None if left < 0 else tree[left]
        tree[num].right = None if right < 0 else tree[right]
    root = tree[0]
    print(*in_order_seq(root))
    print(*pre_order_seq(root))
    print(*post_order_seq(root))

main() 