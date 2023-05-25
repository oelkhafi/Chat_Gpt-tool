class Node:
    def __init__(self, value):
        self.value = self.sum = value
        self.left = self.right = self.parent = None

def update(node):
    if node is not None: 
        node.sum = node.value + (node.left.sum if node.left is not None else 0) + (node.right.sum if node.right is not None else 0)
        for child in [node.left,node.right]:
            if not child is None: 
                child.parent = node

def rotation(node):
    if node.parent is not None: 
        parent = node.parent
        grandparent = node.parent.parent
        if parent.left == node:
            node.right, parent.left = parent, node.right
        else:
            node.left, parent.right = parent, node.left
        node.parent, parent.parent = parent.parent, node
        update(parent)
        update(node)
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node

def splay(node):
    if node is not None: 
        while node.parent is not None:
            if node.parent.parent is None:
                rotation(node)
                break
            if ((node.parent.left == node and node.parent.parent.left == node.parent) 
                or (node.parent.right == node and node.parent.parent.right == node.parent)):
                rotation(node.parent)
                rotation(node)
            else:
                rotation(node)
                rotation(node)
        return node
    return None

def find(node, value):
    result = False
    while node is not None:
        if node.value == value:
            result = True
            break
        if node.value > value and  node.left is not None:
            node = node.left
            continue
        if node.value < value and  node.right is not None:
            node = node.right
            continue
        else: break
    node = splay(node)
    return  result, node

def split(node, value):
    if node is None:
        return None, None
    _, node = find(node, value)
    if node.value >= value: 
        left, node.left = node.left, None
        update(node)
        if left is not None:
            left.parent = None
        return left, node
    if node.value < value:
        right, node.right = node.right, None
        update(node)
        if right is not None:
            right.parent = None
        return node, right
    
def merge(left, right):
    if right == None:
        return left
    if left == None:
        return right
    _, right = find(right, left.value)
    right.left, left.parent = left, right
    update(right)
    return right

def insert(node, value):
    left, right = split(node, value)
    if right is not None and right.value == value:
        return merge(left, right)
    node = Node(value)   
    node.left, node.right = left, right
    update(node)
    return node

def delete(node, value):
    left, right = split(node, value)
    if right is not None and right.value == value:
        right = right.right
        if right is not None:
            right.parent = None
    return merge(left, right)
    
def summa(node, start, end):
    _sum = 0
    left, middle = split(node, start)
    middle, right = split(middle, end)
    if middle is not None:
        _sum = middle.sum
    if right is not None and right.value == end:
        _sum += end
    node = merge(left, merge(middle, right))
    return node, _sum

DIVISOR = 10 ** 9 + 1
last_result, tree = 0, None

def _hash(num, last_result):
    return (num + last_result) % DIVISOR

for i in range(int(input())):
    line = input()
    if line.startswith(""s""):
        start, end = map(int, line.split()[1:])
        tree, result = summa(tree, _hash(start, last_result), _hash(end, last_result))
        print(result)
        last_result = result % DIVISOR
    else:
        command, num = line.split()
        num = _hash(int(num), last_result)
        if command == ""+"":
            tree = insert(tree, num)
        elif command == ""-"":
            tree = delete(tree, num)
        else:
            result, tree = find(tree, num)
            print('Found' if result else 'Not found')
 